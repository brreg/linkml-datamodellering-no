#!/usr/bin/env python3
"""
Les rapportfilene frå analyse-similar-classes-domain,
analyse-similar-classes-all, analyse-similar-slots-domain,
analyse-similar-slots-all, analyse-similar-types-domain,
analyse-similar-types-all, analyse-iri-dereferering,
analyse-innhaldsforhandling, analyse-ap-no-gjenbruk og
analyse-modell-sammenhenger, trekker ut talet på funn/feil og talet sjekka
frå kvar rapport sine oppsummeringslinjer, og skriv ein konsolidert
sammendrag-tabell. Feilar aldri (informativ rapport) — manglande
rapportfiler eller uventa format gjev "?" i tabellen, ikkje ein feilkode.
Sjå .github/workflows/modell-analyse.yml for korleis rapporten vert brukt.

Ingen eksterne avhengigheiter utover stdlib.
"""

import re
import sys
from pathlib import Path

SIMILAR_ZERO = re.compile(r"Ingen \S+ over terskelen vart funne \((\d+) \S+ sjekka\)\.")
SIMILAR_FOUND = re.compile(r"\*\*Totalt: (\d+) par funne av (\d+) \S+\.\*\*")

IRI_TESTAR = re.compile(r"Testar (\d+) unike IRI-ar.*?frå \d+ skjema\.")
IRI_ALL_OK = re.compile(r"Alle IRI-ar let seg derefere\.")
IRI_FAILED = re.compile(r"\*\*(\d+) av (\d+) IRI-ar let seg ikkje derefere\.\*\*")

CN_ALL_OK = re.compile(r"Alle (\d+) innhaldsforhandlingstestar bestod\.")
CN_FAILED = re.compile(r"\*\*(\d+) av (\d+) innhaldsforhandlingstestar feila\.\*\*")

AVVIK_ZERO = re.compile(r"Ingen avvik over dei to sjekkane vart funne \((\d+) \S+ sjekka\)\.")
AVVIK_FOUND = re.compile(r"\*\*Totalt: (\d+) avvik funne av (\d+) \S+ sjekka\.\*\*")

# (etikett, rapportfil, parsefunksjon)
CHECKS = [
    ("Liknande klassenavn (same domene)", "similar-classes-domain-report.md", "similar"),
    ("Liknande klassenavn (alle domene)", "similar-classes-all-report.md", "similar"),
    ("Liknande slotnavn (same domene)", "similar-slots-domain-report.md", "similar"),
    ("Liknande slotnavn (alle domene)", "similar-slots-all-report.md", "similar"),
    ("Liknande typenavn (same domene)", "similar-types-domain-report.md", "similar"),
    ("Liknande typenavn (alle domene)", "similar-types-all-report.md", "similar"),
    ("IRI-dereferering", "iri-dereferering-report.md", "iri"),
    ("Innhaldsforhandling", "innhaldsforhandling-report.md", "content-negotiation"),
    ("AP-NO-gjenbruk (regel 14)", "ap-no-gjenbruk-report.md", "avvik"),
    ("Samanhengar mellom modellar (regel 12)", "modell-sammenhenger-report.md", "avvik"),
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


def parse_avvik(text: str) -> tuple[str, str]:
    m = AVVIK_FOUND.search(text)
    if m:
        return m.group(1), m.group(2)
    m = AVVIK_ZERO.search(text)
    if m:
        return "0", m.group(1)
    return "?", "?"


PARSERS = {
    "similar": parse_similar,
    "iri": parse_iri,
    "content-negotiation": parse_content_negotiation,
    "avvik": parse_avvik,
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
