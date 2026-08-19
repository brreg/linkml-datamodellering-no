#!/usr/bin/env python3
"""
Les dei fem rapportfilene frå analyse-similar-classes-domain,
analyse-similar-classes-all, analyse-similar-slots-domain,
analyse-similar-slots-all og analyse-iri-resolution, trekker ut talet på
funn/feil og talet sjekka frå kvar rapport sine oppsummeringslinjer, og
skriv ein konsolidert sammendrag-tabell. Feilar aldri (informativ rapport)
— manglande rapportfiler eller uventa format gjev "?" i tabellen, ikkje
ein feilkode. Sjå .github/workflows/modell-analyse.yml for korleis
rapporten vert brukt.

Ingen eksterne avhengigheiter utover stdlib.
"""

import re
import sys
from pathlib import Path

SIMILAR_ZERO = re.compile(r"Ingen \S+ over terskelen vart funne \((\d+) \S+ sjekka\)\.")
SIMILAR_FOUND = re.compile(r"\*\*Totalt: (\d+) par funne av (\d+) \S+\.\*\*")

IRI_TESTAR = re.compile(r"Testar (\d+) unike IRI-ar.*?frå \d+ skjema\.")
IRI_ALL_OK = re.compile(r"Alle IRI-ar resolverte\.")
IRI_FAILED = re.compile(r"\*\*(\d+) av (\d+) IRI-ar resolverte ikkje\.\*\*")

CN_ALL_OK = re.compile(r"Alle (\d+) innhaldsforhandlingstestar bestod\.")
CN_FAILED = re.compile(r"\*\*(\d+) av (\d+) innhaldsforhandlingstestar feila\.\*\*")

# (etikett, rapportfil, parsefunksjon)
CHECKS = [
    ("Liknande klassenavn (same domene)", "similar-classes-domain-report.md", "similar"),
    ("Liknande klassenavn (alle domene)", "similar-classes-all-report.md", "similar"),
    ("Liknande slotnavn (same domene)", "similar-slots-domain-report.md", "similar"),
    ("Liknande slotnavn (alle domene)", "similar-slots-all-report.md", "similar"),
    ("IRI-resolusjon", "iri-resolution-report.md", "iri"),
    ("Innhaldsforhandling", "iri-resolution-report.md", "content-negotiation"),
]


def parse_similar(text: str) -> tuple[str, str]:
    m = SIMILAR_FOUND.search(text)
    if m:
        return m.group(1), m.group(2)
    m = SIMILAR_ZERO.search(text)
    if m:
        return "0", m.group(1)
    return "?", "?"


def parse_iri(text: str) -> tuple[str, str]:
    m = IRI_FAILED.search(text)
    if m:
        return m.group(1), m.group(2)
    if IRI_ALL_OK.search(text):
        m = IRI_TESTAR.search(text)
        return "0", m.group(1) if m else "?"
    return "?", "?"


def parse_content_negotiation(text: str) -> tuple[str, str]:
    m = CN_FAILED.search(text)
    if m:
        return m.group(1), m.group(2)
    m = CN_ALL_OK.search(text)
    if m:
        return "0", m.group(1)
    return "?", "?"


PARSERS = {
    "similar": parse_similar,
    "iri": parse_iri,
    "content-negotiation": parse_content_negotiation,
}


def main() -> None:
    print("# Sammendrag: modell-analyse\n")
    print("| Sjekk | Funn/feil | Sjekka totalt |")
    print("|---|---|---|")
    for label, filename, kind in CHECKS:
        path = Path(filename)
        if not path.exists():
            print(f"| {label} | ? | (rapportfil {filename} finst ikkje) |")
            print(f"ÅTVARING: {filename} finst ikkje — hoppar over {label}", file=sys.stderr)
            continue
        text = path.read_text(encoding="utf-8")
        found, total = PARSERS[kind](text)
        print(f"| {label} | {found} | {total} |")


if __name__ == "__main__":
    main()
