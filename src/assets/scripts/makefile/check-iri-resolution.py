#!/usr/bin/env python3
"""
Testar HTTP-resolusjon for IRI-ane i kvart skjema sitt id, default_prefix og
prefixes-blokk. Loggar IRI-ar som ikkje resolverer saman med kva skjema som
refererer dei. Testar i tillegg innhaldsforhandling (content negotiation) for
IRI-ar repoet sjølv eig (id/default_prefix): om Accept: text/turtle gir RDF
Turtle, og om Accept-Language: nb/en gir høvesvis norsk bokmål- og engelsk
representasjon (jf. avvik 4 i
specs/backlog/avvik-peikarar-til-offentlege-ressursar.md). Feilar aldri
(informativ rapport, ikkje blokkerande sjekk) — sjå
.github/workflows/modell-analyse.yml for korleis rapporten vert brukt.

Innhaldsforhandlingstestane er avgrensa til id/default_prefix — ikkje
prefixes til tredjeparts vokabular (dct:, xsd:, foaf: osv.) — sidan repoet
ikkje kan fikse innhaldsforhandling hjå eksterne vokabular-utgivarar.
class_uri/slot_uri/see_also/begrepsidentifikator er også utelatne frå heile
scriptet — desse peikar ofte til eigne, enno upubliserte ressursar og er
ikkje meint å opnast direkte i nettlesar.

Ingen eksterne avhengigheiter utover pyyaml + stdlib urllib.
"""

import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

import yaml

SCHEMA_DIR = Path("src/linkml")
TIMEOUT = 10
USER_AGENT = "linkml-datamodellering-no-iri-check/1.0"

# IRI-mønster som er stadfesta, avgjorde tilfelle av ikkje-resolvbare
# identifikator-URI-ar — same mønster og grunngjeving som dei tilsvarande
# .github/lychee.toml-eksklusjonane, delt her for å unngå at denne rapporten
# re-flaggar spørsmål som alt er granska og avslutta:
# - schema.fintlabs.no: portvakt-verna FINT-API-namnerom, aldri offentleg
#   tilgjengeleg (specs/done/lenkjesjekk-fint-schema-fintlabs-no.md)
# - data.norge.no/vocabulary/ngr-*: NGR-vokabularnamnerom, stadfesta at det
#   ikkje er meint å vere resolvbart (specs/done/lenkjesjekk-ngr-vocabulary-namespace.md)
# - example.org/*.example.org: RFC 2606-plasshaldardomene brukt medvite i
#   referansemodellar og malskjema (specs/done/lenkje-og-mermaid-sjekk.md)
KNOWN_UNRESOLVABLE_PATTERNS = [
    re.compile(r"^https://schema\.fintlabs\.no/"),
    re.compile(r"^https://data\.norge\.no/vocabulary/ngr-"),
    re.compile(r"^https?://(www\.)?example\.(com|org|net)"),
    re.compile(r"^https?://[^/]*\.example\.org"),
]


def is_known_unresolvable(iri: str) -> bool:
    return any(p.match(iri) for p in KNOWN_UNRESOLVABLE_PATTERNS)


def discover_schemas() -> list[Path]:
    return sorted(SCHEMA_DIR.glob("*/*/*-schema.yaml"))


def load_schema(path: Path) -> dict:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        print(f"ÅTVARING: kunne ikkje parse {path}: {e}", file=sys.stderr)
        return {}


def collect_iris(data: dict) -> list[str]:
    iris = []
    if data.get("id"):
        iris.append(data["id"])
    if data.get("default_prefix"):
        iris.append(data["default_prefix"])
    for uri in (data.get("prefixes") or {}).values():
        if isinstance(uri, str):
            iris.append(uri)
    return iris


def collect_own_iris(data: dict) -> list[str]:
    return [iri for iri in (data.get("id"), data.get("default_prefix")) if iri]


def _open(url: str, method: str, headers: dict | None = None):
    all_headers = {"User-Agent": USER_AGENT, **(headers or {})}
    req = urllib.request.Request(url, method=method, headers=all_headers)
    return urllib.request.urlopen(req, timeout=TIMEOUT)


def check_iri(iri: str) -> tuple[bool, str]:
    url = urllib.parse.urldefrag(iri)[0]
    if not url.lower().startswith(("http://", "https://")):
        return False, "ikkje ein http(s)-URI"
    try:
        with _open(url, "HEAD") as resp:
            return True, str(resp.status)
    except urllib.error.HTTPError as e:
        if e.code != 405:
            return False, f"HTTP {e.code}"
    except Exception as e:
        return False, str(e)

    # HEAD ikkje støtta (405) — prøv GET
    try:
        with _open(url, "GET") as resp:
            return True, str(resp.status)
    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}"
    except Exception as e:
        return False, str(e)


def check_turtle(iri: str) -> tuple[bool, str]:
    """Følgjer redirects (urllib vidarefører Accept-headeren til redirect-
    target) og sjekkar om sluttresponsen sin Content-Type inneheld "turtle"."""
    url = urllib.parse.urldefrag(iri)[0]
    try:
        with _open(url, "GET", {"Accept": "text/turtle"}) as resp:
            content_type = resp.headers.get("Content-Type", "")
            if "turtle" in content_type.lower():
                return True, content_type
            return False, f"Content-Type: {content_type or '(manglar)'}"
    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}"
    except Exception as e:
        return False, str(e)


def check_language(iri: str, lang: str) -> tuple[bool, str]:
    """Følgjer redirects (urllib vidarefører Accept-Language-headeren til
    redirect-target) og sjekkar om sluttresponsen sin Content-Language
    startar med det forventa språkkoden."""
    url = urllib.parse.urldefrag(iri)[0]
    try:
        with _open(url, "GET", {"Accept-Language": lang}) as resp:
            content_language = resp.headers.get("Content-Language", "")
            if content_language.lower().startswith(lang.lower()):
                return True, content_language
            return False, f"Content-Language: {content_language or '(manglar)'}"
    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}"
    except Exception as e:
        return False, str(e)


def print_resolution_report(schemas: list[Path], schema_data: dict[Path, dict]) -> None:
    referrers: dict[str, list[str]] = defaultdict(list)
    for schema in schemas:
        for iri in collect_iris(schema_data[schema]):
            referrers[iri].append(str(schema))

    testable = {iri: refs for iri, refs in referrers.items() if not is_known_unresolvable(iri)}
    skipped = len(referrers) - len(testable)

    print("# IRI-resolusjonssjekk\n")
    print(f"Testar {len(testable)} unike IRI-ar (id/default_prefix/prefixes) frå {len(schemas)} skjema.")
    if skipped:
        print(
            f"({skipped} kjende, ikkje-resolvbare identifikator-URI-ar utelatne — "
            "sjå KNOWN_UNRESOLVABLE_PATTERNS i check-iri-resolution.py.)"
        )
    print()

    failures = []
    for iri in sorted(testable):
        ok, detail = check_iri(iri)
        if not ok:
            failures.append((iri, detail))

    if not failures:
        print("Alle IRI-ar resolverte.\n")
        return

    print("| IRI | Feil | Referert av |")
    print("|---|---|---|")
    for iri, detail in failures:
        schemas_str = ", ".join(sorted(set(testable[iri])))
        print(f"| {iri} | {detail} | {schemas_str} |")

    print(f"\n**{len(failures)} av {len(testable)} IRI-ar resolverte ikkje.**\n")


def print_content_negotiation_report(schemas: list[Path], schema_data: dict[Path, dict]) -> None:
    referrers: dict[str, list[str]] = defaultdict(list)
    for schema in schemas:
        for iri in collect_own_iris(schema_data[schema]):
            referrers[iri].append(str(schema))

    print("## Innhaldsforhandling\n")
    print(
        f"Testar om repoet sine eigne IRI-ar (`id`/`default_prefix`, {len(referrers)} "
        f"unike IRI-ar) støttar innhaldsforhandling:\n"
    )
    print("- `Accept: text/turtle` → skal gi RDF Turtle-representasjonen (`Content-Type` inneheld \"turtle\")")
    print('- `Accept-Language: nb` → skal gi norsk bokmål-representasjonen (`Content-Language` startar med "nb")')
    print('- `Accept-Language: en` → skal gi engelsk representasjonen (`Content-Language` startar med "en")\n')

    checks = [
        ("Accept: text/turtle", check_turtle, None),
        ("Accept-Language: nb", check_language, "nb"),
        ("Accept-Language: en", check_language, "en"),
    ]

    failures = []
    total = 0
    for iri in sorted(referrers):
        for label, check_fn, arg in checks:
            total += 1
            ok, detail = check_fn(iri, arg) if arg is not None else check_fn(iri)
            if not ok:
                failures.append((iri, label, detail))

    if not failures:
        print(f"Alle {total} innhaldsforhandlingstestar bestod.")
        return

    print("| IRI | Test | Resultat | Referert av |")
    print("|---|---|---|---|")
    for iri, label, detail in failures:
        schemas_str = ", ".join(sorted(set(referrers[iri])))
        print(f"| {iri} | {label} | {detail} | {schemas_str} |")

    print(f"\n**{len(failures)} av {total} innhaldsforhandlingstestar feila.**")
    if len(failures) == total:
        print(
            "\nAlle IRI-ar på data.norge.no manglar i dag innhaldsforhandling for heile "
            "domenet (kjent, dokumentert infrastrukturgap — ikkje eit per-skjema-avvik). "
            "Sjå specs/done/iri-resolusjon-innhaldsforhandling.md."
        )


def main() -> None:
    schemas = discover_schemas()
    if not schemas:
        print(f"FEIL: ingen skjema funne under {SCHEMA_DIR}", file=sys.stderr)
        sys.exit(1)

    schema_data = {schema: load_schema(schema) for schema in schemas}

    print_resolution_report(schemas, schema_data)
    print_content_negotiation_report(schemas, schema_data)


if __name__ == "__main__":
    main()
