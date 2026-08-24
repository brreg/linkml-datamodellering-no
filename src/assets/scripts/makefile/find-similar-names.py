#!/usr/bin/env python3
"""
Finn klasser, slots eller typar (types:) med liknande navn på tvers av
LinkML-skjema.

Samanliknar berre navn definerte lokalt i kvart skjema sin
classes:/slots:/types:-blokk (ikkje navn arva via imports) — elles ville
importhierarkiet skapt støy av "duplikat" som i røynda er éin delt
definisjon.

For slots viser rapporten òg datatypen (`range:`) slik ho står skriven i
slot-definisjonen — nyttig for å vurdere om eit likskapsfunn er eit reelt
duplikat (same type) eller berre eit navnesamantreff (ulik type). Dette er
ei medvite forenkling: LinkML sin fulle arve-/default_range-logikk
(slot_usage-overstyring i klasser, skjemanivå-`default_range:` når
`range:` manglar) vert ikkje løyst — eit slot utan eksplisitt `range:` vert
vist som `(default)`. Full oppløysing ville kravd ein `SchemaView`-arvegraf
per skjema, som endrar skriptet sin ytingsprofil monaleg (i dag reint
`yaml.safe_load`, ingen LinkML-runtime).

For typar (`--kind types`) viser rapporten tilsvarande `base:` (grunntypen
scalar-typen er avleidd frå, t.d. `str`) — den strukturelle analogen til
`range:` på eit slot.

For klasser viser rapporten tilsvarande slotnavna til kvar identifisert
klasse (frå `slots:`-lista og/eller `attributes:`-nøklane), slik at ein
visuelt kan vurdere om eit navnetreff òg er strukturelt likt. Lange lister
vert trunkerte til 12 slotnavn med eit «… (+N til)»-suffiks.

Ingen eksterne avhengigheiter utover pyyaml (tilgjengeleg i python-pytest-
containeren, jf. requirements-python-test.txt).

To bruksmåtar:

1. Enkelt-rapport, stdout (uendra sidan scriptet vart innført — brukt av
   `make analyse-similar-*-domain`/`-all` og `modell-analyse.yml`):
     python3 find-similar-names.py --kind class --scope domain [--domain D] [--name N]

2. Batch, fil-skriving (sjå
   specs/backlog/effektiviser-modellanalyse-koyretid.md): i dag les/parsar
   scriptet ALLE skjema i scopet på nytt (`yaml.safe_load`) for KVART
   `--name`-filtrerte kall — for eit domene med N skjema og 3 kindar gjev
   det O(3N²) yaml-parsingar for å produsere 3N rapportfiler. Batch-modus
   lastar kvart skjema **éin gong** per kind, gjer dei same O(N²)
   parsamanlikningane (billeg — reine in-memory SequenceMatcher-kall på
   korte strenger, ikkje disk-I/O), og skriv éi fil per skjema:
     python3 find-similar-names.py --domain <domene> --out-dir <sti>       # per-skjema domain-rapportar
     python3 find-similar-names.py --out-dir <sti>                        # eitt kombinert --scope all-sett

   Filnavn/katalogstruktur matchar det dei tilsvarande enkelt-rapport-
   kalla alt produserer i dag (`<out-dir>/<domene>/<skjema>/model-analyse/
   similar-<kind>-domain-report.md` for domene-modus,
   `<out-dir>/similar-<kind>-all-report.md` for scope all-modus), slik at
   `generate-modellanalyse-md.py`/`mkdocs/publish.sh` ikkje treng endrast.
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
    """Returnerer (navn, range) for slots, (navn, base) for typar,
    (navn, slotnavn-liste) for klasser."""
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        print(f"ÅTVARING: kunne ikkje parse {path}: {e}", file=sys.stderr)
        return []
    key = {"class": "classes", "slot": "slots", "types": "types"}[kind]
    block = data.get(key) or {}
    if kind == "class":
        return sorted((name, class_slot_names(defn)) for name, defn in block.items())
    field = "range" if kind == "slot" else "base"
    return sorted((name, (defn or {}).get(field)) for name, defn in block.items())


def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


KIND_TO_FILE_STEM = {"class": "classes", "slot": "slots", "types": "types"}


def compute_matches(
    entries: list[tuple[str, str | list[str] | None, Path]],
    scope: str,
    threshold: float,
    target_path: Path | None = None,
) -> list[tuple]:
    """Kjernematchinga — same logikk som var inline i main() (line 152-179
    før denne refaktoreringa). Delt av stdout-modus og batch-modus."""
    if target_path:
        target_entries = [e for e in entries if e[2] == target_path]
        other_entries = [e for e in entries if e[2] != target_path]
        pairs = ((a, b) for a in target_entries for b in other_entries)
    else:
        pairs = (
            (entries[i], entries[j]) for i in range(len(entries)) for j in range(i + 1, len(entries))
        )

    matches = []
    seen_pairs = set()
    for (name_a, extra_a, schema_a), (name_b, extra_b, schema_b) in pairs:
        if schema_a == schema_b:
            continue
        if scope == "domain" and schema_domain(schema_a) != schema_domain(schema_b):
            continue
        ratio = similarity(name_a, name_b)
        if ratio < threshold:
            continue
        pair_key = tuple(sorted([f"{schema_a}:{name_a}", f"{schema_b}:{name_b}"]))
        if pair_key in seen_pairs:
            continue
        seen_pairs.add(pair_key)
        matches.append((ratio, name_a, extra_a, schema_a, name_b, extra_b, schema_b))

    matches.sort(key=lambda m: (-m[0], m[1], m[4]))
    return matches


def _fmt_schema(path: Path) -> str:
    return path.parent.name


def _fmt_range(range_: str | None) -> str:
    return f"`{range_}`" if range_ else "(default)"


def _fmt_slots(names: list[str], limit: int = 12) -> str:
    if not names:
        return "(ingen)"
    shown = names[:limit]
    rest = len(names) - len(shown)
    text = ", ".join(f"`{n}`" for n in shown)
    return f"{text}, … (+{rest} til)" if rest > 0 else text


def build_report(
    kind: str,
    scope: str,
    threshold: float,
    entries: list[tuple[str, str | list[str] | None, Path]],
    matches: list[tuple],
    target_label: str = "",
    domain_label: str = "",
) -> str:
    """Formaterer rapportteksten — same output som main() sine print()-kall
    før denne refaktoreringa (verifisert byte-for-byte, sjå spec «Utført»).
    Returnerer teksten UTAN avsluttande linjeskift (som print() ville lagt
    til) — kallar legg til det sjølv (print(), eller '+ \"\\n\"' ved
    filskriving)."""
    label = {"class": "klasser", "slot": "slots", "types": "typer"}[kind]
    name_label = {"class": "klassenavn", "slot": "slotnavn", "types": "typenavn"}[kind]
    scope_label = "same domene" if scope == "domain" else "alle domene"

    lines = [
        f"# Liknande {name_label} ({target_label}{scope_label}{domain_label}, "
        f"terskel {threshold:.0%})",
        "",
    ]

    if not matches:
        lines.append(f"Ingen liknande {name_label} funne ({len(entries)} {label} sjekka).")
        return "\n".join(lines)

    if kind in ("slot", "types"):
        col_a, col_b = ("Slot", "Type") if kind == "slot" else ("Type", "Grunntype")
        lines.append(f"| Likskap | {col_a} A | {col_b} A | Skjema A | {col_a} B | {col_b} B | Skjema B |")
        lines.append("|---|---|---|---|---|---|---|")
        for ratio, name_a, range_a, schema_a, name_b, range_b, schema_b in matches:
            lines.append(
                f"| {ratio:.0%} | `{name_a}` | {_fmt_range(range_a)} | {_fmt_schema(schema_a)} "
                f"| `{name_b}` | {_fmt_range(range_b)} | {_fmt_schema(schema_b)} |"
            )
    else:
        lines.append("| Likskap | Klasse A | Slots A | Skjema A | Klasse B | Slots B | Skjema B |")
        lines.append("|---|---|---|---|---|---|---|")
        for ratio, name_a, slots_a, schema_a, name_b, slots_b, schema_b in matches:
            lines.append(
                f"| {ratio:.0%} | `{name_a}` | {_fmt_slots(slots_a)} | {_fmt_schema(schema_a)} "
                f"| `{name_b}` | {_fmt_slots(slots_b)} | {_fmt_schema(schema_b)} |"
            )

    lines.append(f"\n**Totalt: {len(matches)} par funne av {len(entries)} {label}.**")
    return "\n".join(lines)


def write_domain_reports(domain: str, base_dir: Path, threshold: float) -> None:
    """Batch-modus: skriv similar-<kind>-domain-report.md for alle skjema
    i domenet, éin YAML-innlasting per skjema per kind (ikkje éin per
    skjema × kind-KOMBINASJON som dagens per-skjema CLI-kall)."""
    schemas = discover_schemas(domain)
    if not schemas:
        print(f"ÅTVARING: fann ingen skjema for domene '{domain}'", file=sys.stderr)
        return

    for kind in ("class", "slot", "types"):
        entries = [(name, extra, schema) for schema in schemas for name, extra in load_entries(schema, kind)]
        for schema in schemas:
            schema_name = schema.parent.name
            matches = compute_matches(entries, "domain", threshold, target_path=schema)
            target_label = f"modell {domain}/{schema_name}, "
            domain_label = f", domene {domain}"
            report = build_report(kind, "domain", threshold, entries, matches, target_label, domain_label)
            out_dir = base_dir / domain / schema_name / "model-analyse"
            out_dir.mkdir(parents=True, exist_ok=True)
            filename = f"similar-{KIND_TO_FILE_STEM[kind]}-domain-report.md"
            (out_dir / filename).write_text(report + "\n", encoding="utf-8")
        print(f"  ✓ {domain}: similar-{KIND_TO_FILE_STEM[kind]}-domain-report.md skrive for {len(schemas)} skjema")


def write_all_reports(base_dir: Path, threshold: float) -> None:
    """Batch-modus: skriv dei tre kombinerte similar-<kind>-all-report.md
    (--scope all, ingen domene-/navnefilter) i éin prosess i staden for
    tre separate kontainarkall."""
    schemas = discover_schemas(None)
    base_dir.mkdir(parents=True, exist_ok=True)
    for kind in ("class", "slot", "types"):
        entries = [(name, extra, schema) for schema in schemas for name, extra in load_entries(schema, kind)]
        matches = compute_matches(entries, "all", threshold)
        report = build_report(kind, "all", threshold, entries, matches)
        filename = f"similar-{KIND_TO_FILE_STEM[kind]}-all-report.md"
        (base_dir / filename).write_text(report + "\n", encoding="utf-8")
        print(f"  ✓ similar-{KIND_TO_FILE_STEM[kind]}-all-report.md skrive ({len(schemas)} skjema)")


def resolve_name(name: str, domain: str | None) -> Path:
    """Slår opp skjemastien for éin navngjeven modell (NAME=<modell>).

    DOMAIN + NAME saman slår opp direkte (som new-modell/remove-modell).
    NAME åleine søkjer på tvers av alle domene — feilar tydeleg dersom
    modellnavnet ikkje finst, eller finst i meir enn eitt domene."""
    if domain:
        path = SCHEMA_DIR / domain / name / f"{name}-schema.yaml"
        if not path.is_file():
            print(f"FEIL: fann ikkje {path}", file=sys.stderr)
            sys.exit(1)
        return path
    matches = sorted(SCHEMA_DIR.glob(f"*/{name}/{name}-schema.yaml"))
    if not matches:
        print(f"FEIL: fann ingen modell med navn '{name}' i {SCHEMA_DIR}", file=sys.stderr)
        sys.exit(1)
    if len(matches) > 1:
        found = ", ".join(str(m) for m in matches)
        print(
            f"FEIL: fann fleire modellar med navn '{name}': {found} — presiser med DOMAIN=",
            file=sys.stderr,
        )
        sys.exit(1)
    return matches[0]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kind", choices=["class", "slot", "types"])
    parser.add_argument("--scope", choices=["domain", "all"])
    parser.add_argument("--domain", help="Avgrens til eitt domene (default: alle domene)")
    parser.add_argument(
        "--name",
        help=(
            "Avgrens til éin modell (NAME=<modell>) — samanliknar berre denne "
            "modellen sine klasser/slots/typar mot resten av kandidatane innanfor "
            "scopet (same domene for --scope domain, heile repoet for --scope all)"
        ),
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.8,
        help="Fuzzy-likskapsterskel (0.0-1.0), default 0.8",
    )
    parser.add_argument(
        "--out-dir",
        help=(
            "Batch-modus (sjå moduldocstring): skriv rapportar til fil i staden for "
            "stdout. Kombinert med --domain: éi fil per skjema i domenet (--scope domain, "
            "alle tre kindar). Åleine (ingen --domain): dei tre kombinerte --scope all-"
            "rapportane. Kan ikkje kombinerast med --kind/--scope/--name."
        ),
    )
    args = parser.parse_args()

    if args.out_dir:
        if args.kind or args.scope or args.name:
            parser.error("--out-dir (batch-modus) kan ikkje kombinerast med --kind/--scope/--name")
        if args.domain:
            write_domain_reports(args.domain, Path(args.out_dir), args.threshold)
        else:
            write_all_reports(Path(args.out_dir), args.threshold)
        return

    if not args.kind or not args.scope:
        parser.error("krev anten --out-dir [--domain ...] (batch), eller --kind og --scope (stdout)")

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

    label = {"class": "klasser", "slot": "slots", "types": "typer"}[args.kind]
    domain_label = f", domene {args.domain}" if args.domain else ""
    target_label = f"modell {schema_domain(target_path)}/{args.name}, " if target_path else ""

    if target_path:
        target_entries = [e for e in entries if e[2] == target_path]
        if not target_entries:
            print(f"ÅTVARING: fann ingen {label} i {target_path}", file=sys.stderr)

    matches = compute_matches(entries, args.scope, args.threshold, target_path=target_path)
    print(build_report(args.kind, args.scope, args.threshold, entries, matches, target_label, domain_label))


if __name__ == "__main__":
    main()
