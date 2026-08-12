#!/usr/bin/env python3
"""
Evaluerer alle mermaid `click <Namn> href "..."`-direktiv i den publiserte
mkdocs-portalen (klasse-/slot-sider) og stadfestar at kvar href peikar til
ei side som faktisk finst i sitemap.xml (case-sensitivt, som på GitHub Pages).

Bakgrunn: mkdocs sin eigen lenkje-validator ser berre rendra <a href>-element,
ikkje rå tekst inni fenced code-blokker — mermaid click-hrefs er difor
usynlege for `validation.links` i mkdocs.yml. Sjå
specs/backlog/mermaid-klikkbare-lenker-404.md.

Bruk: python3 check-mermaid-click-hrefs.py <site_url> [--concurrency N] [--report PATH]
"""

import argparse
import html
import re
import sys
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.error import URLError
from urllib.parse import urljoin, urlsplit
from urllib.request import urlopen

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src" / "assets" / "scripts"))
from utils.error_handler import log_error  # noqa: E402

SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
MERMAID_BLOCK_RE = re.compile(r'<pre class="mermaid">(.*?)</pre>', re.S)
CLICK_RE = re.compile(r'click\s+(\S+)\s+href\s+"([^"]*)"')
TIMEOUT_S = 15


def normalize(url: str) -> str:
    """Normaliser URL for mengd-medlemskapssjekk: berre path, med avsluttande /."""
    path = urlsplit(url).path
    if not path.endswith("/"):
        path += "/"
    return path


def fetch(url: str) -> str:
    with urlopen(url, timeout=TIMEOUT_S) as resp:  # noqa: S310 — kjende, faste GitHub Pages-URLar
        return resp.read().decode("utf-8", errors="replace")


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


def check_page(url: str, known_paths: set[str]) -> tuple[str, list[dict]]:
    """Hent éi side, evaluer click-hrefs. Returnerer (url, [funn])."""
    findings = []
    try:
        body = fetch(url)
    except (URLError, TimeoutError, OSError) as exc:
        findings.append({
            "name": None,
            "href": None,
            "status": f"HENTING FEILA: {exc}",
        })
        return url, findings

    block_match = MERMAID_BLOCK_RE.search(body)
    if not block_match:
        return url, findings

    block = html.unescape(block_match.group(1))
    for click_match in CLICK_RE.finditer(block):
        name, href = click_match.group(1), click_match.group(2)
        resolved = normalize(urljoin(url, href))
        if resolved not in known_paths:
            findings.append({"name": name, "href": href, "status": "IKKJE FUNNE"})
    return url, findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site_url", help="Bas-URL til publisert portal, t.d. https://brreg.github.io/linkml-datamodellering-no")
    parser.add_argument("--concurrency", type=int, default=10)
    parser.add_argument("--report", type=Path, default=None, help="Skriv markdown-rapport til denne fila")
    args = parser.parse_args()

    all_urls = load_sitemap_urls(args.site_url)
    known_paths = {normalize(u) for u in all_urls}
    class_pages = sorted(u for u in all_urls if "/klasser/" in u)

    print(f"Fann {len(all_urls)} sider i sitemap.xml, {len(class_pages)} klasse-/slot-sider å sjekke.")

    rows: list[tuple[str, str, str, str]] = []
    total_click_hrefs = 0
    broken = 0

    with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        futures = {pool.submit(check_page, url, known_paths): url for url in class_pages}
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
