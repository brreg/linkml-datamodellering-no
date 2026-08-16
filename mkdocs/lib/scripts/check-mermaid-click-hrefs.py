#!/usr/bin/env python3
"""
Evaluerer alle mermaid `click <Namn> href "..."`-direktiv i den publiserte
mkdocs-portalen (klasse-/slot-sider). Portal-interne hrefar vert stadfesta
mot sitemap.xml (case-sensitivt, som på GitHub Pages); absolutte eksterne
hrefar (t.d. XSD-typedefinisjonar hos w3.org, sjå BUG-13/
bugs/mermaid-link-ekstern-uri-prefiks.md) vert i staden stadfesta med eit
direkte HTTP-oppslag mot målet, sidan dei aldri kan finnast i vår eigen
sitemap.

Bakgrunn: mkdocs sin eigen lenkje-validator ser berre rendra <a href>-element,
ikkje rå tekst inni fenced code-blokker — mermaid click-hrefs er difor
usynlege for `validation.links` i mkdocs.yml. Sjå
specs/backlog/mermaid-klikkbare-lenker-404.md.

Bruk: python3 check-mermaid-click-hrefs.py <site_url> [--concurrency N] [--report PATH]

Alle HTTP-oppslag (sidehenting og eksterne HEAD-sjekkar) brukar automatisk
eksponentiell backoff med jitter ved 429/5xx-svar eller nettverksfeil (opptil
MAX_RETRIES forsøk), og respekterer ein evt. Retry-After-header frå
429-svaret — sjå specs/backlog/mermaid-click-href-429-retry.md.
"""

import argparse
import html
import random
import re
import sys
import threading
import time
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, urlopen

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src" / "assets" / "scripts"))
from utils.error_handler import log_error  # noqa: E402

SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
MERMAID_BLOCK_RE = re.compile(r'<pre class="mermaid">(.*?)</pre>', re.S)
CLICK_RE = re.compile(r'click\s+(\S+)\s+href\s+"([^"]*)"')
TIMEOUT_S = 15

# Retry/backoff-konfigurasjon (429/5xx-handtering, sjå
# specs/backlog/mermaid-click-href-429-retry.md).
MAX_RETRIES = 5
RETRY_BASE_DELAY_S = 1.0
RETRY_MAX_DELAY_S = 30.0
RETRYABLE_STATUS = {429, 500, 502, 503, 504}

# Cache for eksterne URL-oppslag (BUG-13) — same eksterne URL (t.d. ein
# XSD-typeanker) kan opptre i click-hrefar på svært mange sider, og bør
# berre sjekkast éin gong per køyring.
_EXTERNAL_LINK_CACHE: dict[str, bool] = {}
_EXTERNAL_LINK_LOCK = threading.Lock()


def _parse_retry_after(header_value: str | None) -> float | None:
    """Tolk ein Retry-After-header (sekund eller HTTP-dato-format).

    Returnerer None dersom header manglar eller ikkje kan tolkast.
    """
    if not header_value:
        return None
    header_value = header_value.strip()
    try:
        return max(0.0, float(header_value))
    except ValueError:
        pass
    try:
        retry_at = parsedate_to_datetime(header_value)
    except (TypeError, ValueError):
        return None
    if retry_at is None:
        return None
    if retry_at.tzinfo is None:
        retry_at = retry_at.replace(tzinfo=timezone.utc)
    return max(0.0, (retry_at - datetime.now(timezone.utc)).total_seconds())


def _retry_delay(attempt: int, retry_after: float | None) -> float:
    """Ventetid før neste forsøk: Retry-After når gyldig, elles eksponentiell
    backoff (basis * 2^(attempt-1)) pluss jitter, avgrensa til RETRY_MAX_DELAY_S.
    """
    if retry_after is not None:
        return min(retry_after, RETRY_MAX_DELAY_S)
    backoff = RETRY_BASE_DELAY_S * (2 ** (attempt - 1))
    jitter = random.uniform(0, RETRY_BASE_DELAY_S)
    return min(backoff + jitter, RETRY_MAX_DELAY_S)


def _urlopen_with_retry(req_or_url, *, timeout: float = TIMEOUT_S):
    """urlopen() med eksponentiell backoff + jitter ved 429/5xx/nettverksfeil.

    Respekterer ein evt. Retry-After-header frå 429-svaret. Kastar siste feil
    vidare umiddelbart dersom han ikkje er retryable (t.d. 404), eller etter
    MAX_RETRIES forsøk. Feilen som til slutt vert kasta, får eit
    `.retry_attempts`-attributt som fortel kor mange forsøk som vart gjort.
    """
    last_exc: Exception
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            return urlopen(req_or_url, timeout=timeout)  # noqa: S310 — kjende, faste URL-ar
        except HTTPError as exc:
            retryable = exc.code in RETRYABLE_STATUS
            retry_after = _parse_retry_after(exc.headers.get("Retry-After")) if exc.headers else None
            last_exc = exc
        except (URLError, TimeoutError, OSError) as exc:
            retryable = True
            retry_after = None
            last_exc = exc
        last_exc.retry_attempts = attempt
        if not retryable or attempt == MAX_RETRIES:
            raise last_exc
        time.sleep(_retry_delay(attempt, retry_after))
    raise last_exc  # pragma: no cover — løkka raiser eller returnerer alltid før dette punktet


def normalize(url: str) -> str:
    """Normaliser URL for mengd-medlemskapssjekk: berre path, med avsluttande /."""
    path = urlsplit(url).path
    if not path.endswith("/"):
        path += "/"
    return path


def fetch(url: str) -> str:
    with _urlopen_with_retry(url) as resp:
        return resp.read().decode("utf-8", errors="replace")


def check_external_url(url: str) -> bool:
    """Stadfest at ei ekstern absolutt URL faktisk resolverer (HTTP HEAD).

    Nytta for hrefar som peikar utanfor vår eigen portal (t.d. XSD-typar,
    BUG-13) — desse kan aldri finnast i vår eigen sitemap.xml, så dei må
    verifiserast direkte mot målserveren i staden.
    """
    with _EXTERNAL_LINK_LOCK:
        cached = _EXTERNAL_LINK_CACHE.get(url)
    if cached is not None:
        return cached
    ok = True
    try:
        req = Request(url, method="HEAD")  # noqa: S310 — kjende eksterne vokabular-URL-ar
        with _urlopen_with_retry(req) as resp:
            ok = 200 <= resp.status < 400
    except (URLError, TimeoutError, OSError):
        ok = False
    with _EXTERNAL_LINK_LOCK:
        _EXTERNAL_LINK_CACHE[url] = ok
    return ok


def load_sitemap_urls(site_url: str) -> set[str]:
    sitemap_url = urljoin(site_url.rstrip("/") + "/", "sitemap.xml")
    try:
        body = fetch(sitemap_url)
    except (URLError, TimeoutError, OSError):
        log_error({"step": "load_sitemap_urls", "sitemap_url": sitemap_url})
    try:
        root = ET.fromstring(body)
    except ET.ParseError:
        log_error({"step": "parse_sitemap", "sitemap_url": sitemap_url})
    urls = {
        loc.text.strip()
        for loc in root.iter(f"{SITEMAP_NS}loc")
        if loc.text
    }
    if not urls:
        print(f"FEIL: fann ingen <loc>-element i {sitemap_url}", file=sys.stderr)
        sys.exit(1)
    return urls


def check_page(url: str, known_paths: set[str], site_netloc: str) -> tuple[str, list[dict]]:
    """Hent éi side, evaluer click-hrefs. Returnerer (url, [funn])."""
    findings = []
    try:
        body = fetch(url)
    except (URLError, TimeoutError, OSError) as exc:
        attempts = getattr(exc, "retry_attempts", 1)
        status = (
            f"HENTING FEILA ETTER {attempts} FORSØK: {exc}"
            if attempts > 1
            else f"HENTING FEILA: {exc}"
        )
        findings.append({
            "name": None,
            "href": None,
            "status": status,
        })
        return url, findings

    block_match = MERMAID_BLOCK_RE.search(body)
    if not block_match:
        return url, findings

    block = html.unescape(block_match.group(1))
    for click_match in CLICK_RE.finditer(block):
        name, href = click_match.group(1), click_match.group(2)
        resolved = urljoin(url, href)
        if urlsplit(resolved).netloc != site_netloc:
            # Absolutt ekstern URL (t.d. XSD-typedefinisjon, BUG-13) — kan
            # aldri finnast i vår eigen sitemap, valider mot målserveren.
            if not check_external_url(resolved):
                findings.append({"name": name, "href": href, "status": "EKSTERN LENKJE FEILA"})
            continue
        if normalize(resolved) not in known_paths:
            findings.append({"name": name, "href": href, "status": "IKKJE FUNNE"})
    return url, findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site_url", help="Bas-URL til publisert portal, t.d. https://brreg.github.io/linkml-datamodellering-no")
    parser.add_argument("--concurrency", type=int, default=5)
    parser.add_argument("--report", type=Path, default=None, help="Skriv markdown-rapport til denne fila")
    args = parser.parse_args()

    all_urls = load_sitemap_urls(args.site_url)
    known_paths = {normalize(u) for u in all_urls}
    class_pages = sorted(u for u in all_urls if "/klasser/" in u)
    site_netloc = urlsplit(args.site_url).netloc

    print(f"Fann {len(all_urls)} sider i sitemap.xml, {len(class_pages)} klasse-/slot-sider å sjekke.")

    rows: list[tuple[str, str, str, str]] = []
    total_click_hrefs = 0
    broken = 0

    with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        futures = {pool.submit(check_page, url, known_paths, site_netloc): url for url in class_pages}
        for future in as_completed(futures):
            url, findings = future.result()
            for f in findings:
                total_click_hrefs += 0 if f["name"] is None else 1
                broken += 1
                rows.append((url, f["name"] or "-", f["href"] or "-", f["status"]))
                print(f"::error file={url}::click-href broten ({f['name']}): {f['status']} — {f['href']}")

    print(f"\nTotalt sjekka: {len(class_pages)} sider. Broten funn: {broken}.")

    if args.report:
        with args.report.open("w", encoding="utf-8") as fh:
            fh.write("| Side | Click-namn | Href | Status |\n")
            fh.write("|---|---|---|---|\n")
            for url, name, href, status in rows:
                fh.write(f"| {url} | {name} | {href} | {status} |\n")
            fh.write(f"\n**Totalt: {len(class_pages)} sider sjekka, {broken} broten click-href(s) funne.**\n")

    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
