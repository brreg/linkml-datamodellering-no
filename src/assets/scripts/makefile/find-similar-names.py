#!/usr/bin/env python3
"""
Finn klasser eller slots med liknande namn på tvers av LinkML-skjema.

Samanliknar berre namn definerte lokalt i kvart skjema sin classes:/slots:-
blokk (ikkje namn arva via imports) — elles ville importhierarkiet skapt
støy av "duplikat" som i røynda er éin delt definisjon.

Ingen eksterne avhengigheiter utover pyyaml (tilgjengeleg i python-pytest-
containeren, jf. requirements-python-test.txt).
"""

import argparse
import sys
from difflib import SequenceMatcher
from pathlib import Path

import yaml

SCHEMA_DIR = Path("src/linkml")


def discover_schemas() -> list[Path]:
    return sorted(SCHEMA_DIR.glob("*/*/*-schema.yaml"))


def schema_domain(path: Path) -> str:
    return path.relative_to(SCHEMA_DIR).parts[0]


def load_names(path: Path, kind: str) -> list[str]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        print(f"ÅTVARING: kunne ikkje parse {path}: {e}", file=sys.stderr)
        return []
    key = "classes" if kind == "class" else "slots"
    return sorted((data.get(key) or {}).keys())


def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kind", choices=["class", "slot"], required=True)
    parser.add_argument("--scope", choices=["domain", "all"], required=True)
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.8,
        help="Fuzzy-likskapsterskel (0.0-1.0), default 0.8",
    )
    args = parser.parse_args()

    schemas = discover_schemas()
    if not schemas:
        print(f"FEIL: ingen skjema funne under {SCHEMA_DIR}", file=sys.stderr)
        sys.exit(1)

    entries: list[tuple[str, Path]] = []
    for schema in schemas:
        for name in load_names(schema, args.kind):
            entries.append((name, schema))

    label = "klasser" if args.kind == "class" else "slots"
    scope_label = "same domene" if args.scope == "domain" else "alle domene"
    print(f"# Liknande {label}namn ({scope_label}, terskel {args.threshold:.0%})\n")

    matches = []
    seen_pairs = set()
    for i, (name_a, schema_a) in enumerate(entries):
        for name_b, schema_b in entries[i + 1 :]:
            if schema_a == schema_b:
                continue
            if args.scope == "domain" and schema_domain(schema_a) != schema_domain(schema_b):
                continue
            ratio = similarity(name_a, name_b)
            if ratio < args.threshold:
                continue
            pair_key = tuple(sorted([f"{schema_a}:{name_a}", f"{schema_b}:{name_b}"]))
            if pair_key in seen_pairs:
                continue
            seen_pairs.add(pair_key)
            matches.append((ratio, name_a, schema_a, name_b, schema_b))

    if not matches:
        print(f"Ingen {label} over terskelen vart funne ({len(entries)} {label} sjekka).")
        return

    matches.sort(key=lambda m: (-m[0], m[1], m[3]))

    print("| Likskap | Namn A | Skjema A | Namn B | Skjema B |")
    print("|---|---|---|---|---|")
    for ratio, name_a, schema_a, name_b, schema_b in matches:
        print(f"| {ratio:.0%} | `{name_a}` | {schema_a} | `{name_b}` | {schema_b} |")

    print(f"\n**Totalt: {len(matches)} par funne blant {len(entries)} {label}.**")


if __name__ == "__main__":
    main()
