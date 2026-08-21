#!/usr/bin/env python3
"""
Finn klasser eller slots med liknande navn på tvers av LinkML-skjema.

Samanliknar berre navn definerte lokalt i kvart skjema sin classes:/slots:-
blokk (ikkje navn arva via imports) — elles ville importhierarkiet skapt
støy av "duplikat" som i røynda er éin delt definisjon.

For slots viser rapporten òg datatypen (`range:`) slik ho står skriven i
slot-definisjonen — nyttig for å vurdere om eit likskapsfunn er eit reelt
duplikat (same type) eller berre eit navnesamantreff (ulik type). Dette er
ei medvite forenkling: LinkML sin fulle arve-/default_range-logikk
(slot_usage-overstyring i klassar, skjemanivå-`default_range:` når
`range:` manglar) vert ikkje løyst — eit slot utan eksplisitt `range:` vert
vist som `(default)`. Full oppløysing ville kravd ein `SchemaView`-arvegraf
per skjema, som endrar skriptet sin ytingsprofil monaleg (i dag reint
`yaml.safe_load`, ingen LinkML-runtime).

For klassar viser rapporten tilsvarande slotnavna til kvar identifisert
klasse (frå `slots:`-lista og/eller `attributes:`-nøklane), slik at ein
visuelt kan vurdere om eit navnetreff òg er strukturelt likt. Lange lister
vert trunkerte til 12 slotnavn med eit «… (+N til)»-suffiks.

Ingen eksterne avhengigheiter utover pyyaml (tilgjengeleg i python-pytest-
containeren, jf. requirements-python-test.txt).
"""

import argparse
import sys
from difflib import SequenceMatcher
from pathlib import Path

import yaml

SCHEMA_DIR = Path("src/linkml")


def discover_schemas(domain: str | None = None) -> list[Path]:
    if domain:
        return sorted(SCHEMA_DIR.glob(f"{domain}/*/*-schema.yaml"))
    return sorted(SCHEMA_DIR.glob("*/*/*-schema.yaml"))


def schema_domain(path: Path) -> str:
    return path.relative_to(SCHEMA_DIR).parts[0]


def class_slot_names(defn: dict) -> list[str]:
    """Slotnavna ei klasse refererer, via slots: og/eller attributes:."""
    defn = defn or {}
    names = list(defn.get("slots") or [])
    names += list((defn.get("attributes") or {}).keys())
    return sorted(set(names))


def load_entries(path: Path, kind: str) -> list[tuple[str, str | list[str] | None]]:
    """Returnerer (navn, range) for slots, (navn, slotnavn-liste) for klassar."""
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        print(f"ÅTVARING: kunne ikkje parse {path}: {e}", file=sys.stderr)
        return []
    key = "classes" if kind == "class" else "slots"
    block = data.get(key) or {}
    if kind == "slot":
        return sorted((name, (defn or {}).get("range")) for name, defn in block.items())
    return sorted((name, class_slot_names(defn)) for name, defn in block.items())


def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def resolve_name(name: str, domain: str | None) -> Path:
    """Slår opp skjemastien for éin namngjeven modell (NAME=<modell>).

    DOMAIN + NAME saman slår opp direkte (som new-modell/remove-modell).
    NAME åleine søkjer på tvers av alle domene — feilar tydeleg dersom
    modellnamnet ikkje finst, eller finst i meir enn eitt domene."""
    if domain:
        path = SCHEMA_DIR / domain / name / f"{name}-schema.yaml"
        if not path.is_file():
            print(f"FEIL: fann ikkje {path}", file=sys.stderr)
            sys.exit(1)
        return path
    matches = sorted(SCHEMA_DIR.glob(f"*/{name}/{name}-schema.yaml"))
    if not matches:
        print(f"FEIL: fann ingen modell med namn '{name}' i {SCHEMA_DIR}", file=sys.stderr)
        sys.exit(1)
    if len(matches) > 1:
        found = ", ".join(str(m) for m in matches)
        print(
            f"FEIL: fann fleire modellar med namn '{name}': {found} — presiser med DOMAIN=",
            file=sys.stderr,
        )
        sys.exit(1)
    return matches[0]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kind", choices=["class", "slot"], required=True)
    parser.add_argument("--scope", choices=["domain", "all"], required=True)
    parser.add_argument("--domain", help="Avgrens til eitt domene (default: alle domene)")
    parser.add_argument(
        "--name",
        help=(
            "Avgrens til éin modell (NAME=<modell>) — samanliknar berre denne "
            "modellen sine klassar/slots mot resten av kandidatane innanfor "
            "scopet (same domene for --scope domain, heile repoet for --scope all)"
        ),
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.8,
        help="Fuzzy-likskapsterskel (0.0-1.0), default 0.8",
    )
    args = parser.parse_args()

    target_path = resolve_name(args.name, args.domain) if args.name else None

    schemas = discover_schemas(args.domain)
    if not schemas:
        where = f" for domene {args.domain}" if args.domain else ""
        print(f"FEIL: ingen skjema funne under {SCHEMA_DIR}{where}", file=sys.stderr)
        sys.exit(1)

    entries: list[tuple[str, str | list[str] | None, Path]] = []
    for schema in schemas:
        for name, extra in load_entries(schema, args.kind):
            entries.append((name, extra, schema))

    label = "klasser" if args.kind == "class" else "slots"
    name_label = "klassenavn" if args.kind == "class" else "slotnavn"
    scope_label = "same domene" if args.scope == "domain" else "alle domene"
    domain_label = f", domene {args.domain}" if args.domain else ""
    target_label = f"modell {schema_domain(target_path)}/{args.name}, " if target_path else ""
    print(
        f"# Liknande {name_label} ({target_label}{scope_label}{domain_label}, "
        f"terskel {args.threshold:.0%})\n"
    )

    if target_path:
        target_entries = [e for e in entries if e[2] == target_path]
        other_entries = [e for e in entries if e[2] != target_path]
        if not target_entries:
            print(f"ÅTVARING: fann ingen {label} i {target_path}", file=sys.stderr)
        pairs = ((a, b) for a in target_entries for b in other_entries)
    else:
        pairs = (
            (entries[i], entries[j])
            for i in range(len(entries))
            for j in range(i + 1, len(entries))
        )

    matches = []
    seen_pairs = set()
    for (name_a, extra_a, schema_a), (name_b, extra_b, schema_b) in pairs:
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
        matches.append((ratio, name_a, extra_a, schema_a, name_b, extra_b, schema_b))

    if not matches:
        print(f"Ingen liknande {name_label} funne ({len(entries)} {label} sjekka).")
        return

    matches.sort(key=lambda m: (-m[0], m[1], m[4]))

    def fmt_schema(path: Path) -> str:
        return path.parent.name

    def fmt_range(range_: str | None) -> str:
        return f"`{range_}`" if range_ else "(default)"

    def fmt_slots(names: list[str], limit: int = 12) -> str:
        if not names:
            return "(ingen)"
        shown = names[:limit]
        rest = len(names) - len(shown)
        text = ", ".join(f"`{n}`" for n in shown)
        return f"{text}, … (+{rest} til)" if rest > 0 else text

    if args.kind == "slot":
        print("| Likskap | Slot A | Type A | Skjema A | Slot B | Type B | Skjema B |")
        print("|---|---|---|---|---|---|---|")
        for ratio, name_a, range_a, schema_a, name_b, range_b, schema_b in matches:
            print(
                f"| {ratio:.0%} | `{name_a}` | {fmt_range(range_a)} | {fmt_schema(schema_a)} "
                f"| `{name_b}` | {fmt_range(range_b)} | {fmt_schema(schema_b)} |"
            )
    else:
        print("| Likskap | Klasse A | Slots A | Skjema A | Klasse B | Slots B | Skjema B |")
        print("|---|---|---|---|---|---|---|")
        for ratio, name_a, slots_a, schema_a, name_b, slots_b, schema_b in matches:
            print(
                f"| {ratio:.0%} | `{name_a}` | {fmt_slots(slots_a)} | {fmt_schema(schema_a)} "
                f"| `{name_b}` | {fmt_slots(slots_b)} | {fmt_schema(schema_b)} |"
            )

    print(f"\n**Totalt: {len(matches)} par funne av {len(entries)} {label}.**")


if __name__ == "__main__":
    main()
