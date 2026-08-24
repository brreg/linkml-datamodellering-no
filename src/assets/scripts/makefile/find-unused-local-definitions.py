#!/usr/bin/env python3
"""
Finn lokalt definerte slots, enums, types eller subsets som ALDRI vert
brukt av ein lokal klasse i same skjema, eller lokale klassar som er
heilt isolerte (ingen referansar til/frå nokon annan lokal klasse).

Bakgrunn: sjå specs/backlog/modellanalyse-ubrukte-lokale-definisjonar.md.
Denne "brukt lokalt vs. definert lokalt"-sjekken vart tidlegare rekna ut
*inline*, rad for rad, i Usage-kolonna i
src/assets/templates/docgen/index.md.jinja2 sine Slots/Enumerations/
Types/Subsets-tabellar. Sjekken er flytta hit som ein eigen
modellanalyse-jobb (etter mønster av find-similar-names.py) slik at
tabellane kan reindyrkast til berre å dokumentere kva som finst, medan
"er dette verdt å følgje opp"-vurderinga samlast under
## Modellanalyse-overskrifta i staden.

For --kind slot/enum/type/subset er algoritmen ein direkte port av
Jinja-malen sin eksisterande is_used-logikk (ikkje ei ny tolking) — sjå
dei fire *_is_used()-funksjonane under, som kvar viser til den
tilsvarande linja i index.md.jinja2 dei erstattar.

--kind class er ein heilt ny, femte analyse (ikkje ein port — Classes-
tabellen har ingen Usage-kolonne i dag): finn lokale klassar som ikkje er
reelt integrerte i modellgrafen (via slot-/attributtrange, eller
is_a/mixins) til noka anna lokal klasse. Containerklassen (tree_root)
reknast alltid som tilkopla resten (ho er modellen sitt inngangspunkt) og
vert difor aldri sjølv rapportert som isolert — men i motsetnad til andre
klassar tel IKKJE containeren sine EIGNE referansar til andre lokale
klassar som reell tilkopling for måla. To kategoriar vert difor skilde:

- **Heilt isolert** — ingen tilkopling i det heile, ikkje eingong via
  containerklassen.
- **Kun tilkopla via containerklassen** — containeren refererer klassen
  (ho er eit registrert inngangspunkt), men ho har elles ingen tilkopling
  til/frå noka anna lokal klasse. Fangar klassar som er registrerte som
  container-attributt, men aldri faktisk vovne inn i resten av
  modellgrafen (t.d. eit ufullstendig scaffold eller feilplassert
  attributt).

Ei klasse med minst éi REELL (ikkje-container) tilkopling — anten
utgåande til, eller innkomande frå, ei anna lokal klasse — vert aldri
flagga, sjølv om ho i tillegg er referert av containeren.

Krev SchemaView (og dermed induced_slot()-arveoppløysing) — bruk
LINKML_RUN, ikkje PYTHON_RUN (jf. check-import-duplicates.py).

To bruksmåtar:

1. Enkelt-sjekk, stdout (uendra sidan spec-en dette scriptet vart innført
   i — brukt av `make analyse-ubrukte-*`/`analyse-isolerte-klasser`):
     python3 find-unused-local-definitions.py --kind slot --schema <sti>

2. Batch, fil-skriving (sjå
   specs/backlog/effektiviser-modellanalyse-koyretid.md): bygg **eitt**
   SchemaView per skjema og skriv alle fem kind-rapportane i éin
   Python-prosess i staden for fem separate podman-kontainarar (kvar med
   sin eigen ~0,9 s linkml_runtime-importskatt) — det er denne 5×
   redundante import+SchemaView-kostnaden per skjema som gjorde
   modellanalyse-steget til det klart tyngste steget i generate.yml:
     python3 find-unused-local-definitions.py --domain <domene> --out-dir <sti>

   Diskoverer alle skjema i domenet
   (`src/linkml/<domene>/*/*-schema.yaml`), skriv
   `<out-dir>/<domene>/<skjema>/model-analyse/<rapportnavn>.md` per
   skjema — same filnavn og katalogstruktur som steg 1 sine fem separate
   kall produserte, slik at `generate-modellanalyse-md.py`/
   `mkdocs/publish.sh` ikkje treng endrast. Eitt skjema som feilar (t.d.
   ugyldig import) stoppar ikkje resten av domenet — feilen vert logga
   (`::warning::`) og løkka held fram, same prinsipp som
   `check-import-duplicates.py`/`batch-lint.py`.

Exit-kode: alltid 0 — informativ rapport, ikkje ein valideringspolicy
(same prinsipp som find-similar-names.py).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Sjå src/assets/scripts/utils/linkml_relative_import_patch.py — fiksar ein
# upstream-bug i import-oppløysing for versjonslåste (raw.githubusercontent.com)
# importar, brukt av alle batch-script i denne katalogen.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "utils"))
import linkml_relative_import_patch  # noqa: E402

linkml_relative_import_patch.apply()

KIND_LABELS = {
    "slot": "slots",
    "enum": "enums",
    "type": "typar",
    "subset": "subsets",
    "class": "klassar",
}

# Rapportfilnavn — MÅ matche det .github/workflows/generate.yml (og
# generate-modellanalyse-md.py sin REPORTS-liste) forventar under
# generated/<domene>/<skjema>/model-analyse/.
KIND_TO_REPORT_FILENAME = {
    "slot": "ubrukte-slots-report.md",
    "enum": "ubrukte-enums-report.md",
    "type": "ubrukte-types-report.md",
    "subset": "ubrukte-subsets-report.md",
    "class": "isolerte-klasser-report.md",
}

ALL_KINDS = ("slot", "enum", "type", "subset", "class")


def log_error(msg: str) -> None:
    print(f"[ERROR] {msg}", file=sys.stderr)


def local_classes(sv, include_root: bool = True) -> list:
    """Klassar (ClassDefinition) definerte lokalt i sv.schema sjølv.

    Portar filteret schemaview.all_classes() + c_origin == schema.id frå
    index.md.jinja2 (t.d. line 161-164 for slots)."""
    result = []
    for class_name in sv.all_classes():
        c = sv.get_class(class_name)
        if not c:
            continue
        origin = c.from_schema if c.from_schema else sv.schema.id
        if origin != sv.schema.id:
            continue
        if not include_root and c.tree_root:
            continue
        result.append(c)
    return result


def slot_is_used(slot_name: str, classes: list) -> bool:
    """Port av index.md.jinja2 line 160-172/186-198/212-224."""
    return any(slot_name in (c.slots or []) for c in classes)


def enum_is_used(sv, enum_name: str, classes: list) -> bool:
    """Port av index.md.jinja2 line 275-305 (to grener, OR-a saman)."""
    for local_slot_name in (sv.schema.slots or {}).keys():
        s = sv.get_slot(local_slot_name)
        if s and s.range == enum_name and slot_is_used(local_slot_name, classes):
            return True
    for c in classes:
        for slot_name in c.slots or []:
            induced = sv.induced_slot(slot_name, c.name)
            if induced and induced.range == enum_name:
                return True
    return False


def type_is_used(sv, type_name: str, classes: list) -> bool:
    """Port av index.md.jinja2 line 376-401 (to grener, OR-a saman,
    same struktur som enum_is_used)."""
    for local_slot_name in (sv.schema.slots or {}).keys():
        s = sv.get_slot(local_slot_name)
        if s and s.range == type_name and slot_is_used(local_slot_name, classes):
            return True
    for c in classes:
        for slot_name in c.slots or []:
            induced = sv.induced_slot(slot_name, c.name)
            if induced and induced.range == type_name:
                return True
    return False


def subset_is_used(subset_name: str, classes: list) -> bool:
    """Port av index.md.jinja2 line 452-474."""
    for c in classes:
        if subset_name in (c.in_subset or []):
            return True
        for slot_usage in (c.slot_usage or {}).values():
            if subset_name in (slot_usage.in_subset or []):
                return True
    return False


def find_unused(sv, kind: str) -> list[tuple[str, str]]:
    """Returnerer [(navn, skildring), ...] for lokalt DEFINERTE navn av
    denne kinden som ikkje er brukt av nokon lokal (ikkje-root) klasse."""
    classes = local_classes(sv, include_root=False)
    if kind == "slot":
        local_names = (sv.schema.slots or {}).keys()
        used = lambda name: slot_is_used(name, classes)  # noqa: E731
        get = sv.get_slot
    elif kind == "enum":
        local_names = (sv.schema.enums or {}).keys()
        used = lambda name: enum_is_used(sv, name, classes)  # noqa: E731
        get = sv.get_enum
    elif kind == "type":
        local_names = (sv.schema.types or {}).keys()
        used = lambda name: type_is_used(sv, name, classes)  # noqa: E731
        get = sv.get_type
    elif kind == "subset":
        local_names = (sv.schema.subsets or {}).keys()
        used = lambda name: subset_is_used(name, classes)  # noqa: E731
        get = sv.get_subset
    else:
        raise ValueError(f"ukjend kind: {kind}")

    unused = []
    for name in sorted(local_names):
        if used(name):
            continue
        obj = get(name)
        description = (obj.description or "").strip() if obj else ""
        unused.append((name, description))
    return unused


def class_connections(sv, c) -> set[str]:
    """Navna på alle andre lokale klassar denne klassa er tilkopla til,
    via slot-/attributtrange (begge retningar via induced_slot) eller
    is_a/mixins."""
    local_names = {lc.name for lc in local_classes(sv, include_root=True)}
    connected: set[str] = set()

    for slot in sv.class_induced_slots(c.name):
        if slot.range in local_names and slot.range != c.name:
            connected.add(slot.range)

    if c.is_a and c.is_a in local_names:
        connected.add(c.is_a)
    for mixin in c.mixins or []:
        if mixin in local_names:
            connected.add(mixin)

    return connected


REASON_ISOLATED = "Heilt isolert"
REASON_CONTAINER_ONLY = "Kun tilkopla via containerklassen"


def find_isolated_classes(sv) -> list[tuple[str, str, str]]:
    """Finn lokale klassar (utanom containerklassen) som ikkje har NOKA
    REELL tilkopling til noka anna lokal klasse. Ein klasse vert rekna som
    reelt tilkopla dersom ho anten sjølv koplar seg til ei anna lokal
    klasse, eller ei anna IKKJE-container lokal klasse koplar seg til
    henne. Containerklassen sine EIGNE utgåande koplingar tel ikkje som
    reell tilkopling for måla — dei sporsast separat (`container_targets`)
    for å skilje "heilt isolert" frå "kun tilkopla via containerklassen"."""
    all_local = local_classes(sv, include_root=True)
    container = next((c for c in all_local if c.tree_root), None)
    container_targets = class_connections(sv, container) if container else set()

    connected_names: set[str] = set()
    for c in all_local:
        if c.tree_root:
            continue  # containeren sine eigne mål tel ikkje som reell tilkopling
        targets = class_connections(sv, c)
        if targets:
            connected_names.add(c.name)
            connected_names.update(targets)

    isolated = []
    for c in all_local:
        if c.tree_root:
            continue
        if c.name in connected_names:
            continue
        description = (c.description or "").strip()
        reason = REASON_CONTAINER_ONLY if c.name in container_targets else REASON_ISOLATED
        isolated.append((c.name, description, reason))
    return sorted(isolated)


def compute_items_and_total(sv, kind: str) -> tuple[list[tuple], int]:
    """(items, total) for éin kind — delt av stdout-modus og batch-modus."""
    if kind == "class":
        return find_isolated_classes(sv), len(local_classes(sv, include_root=True))
    items = find_unused(sv, kind)
    local_names = {
        "slot": sv.schema.slots or {},
        "enum": sv.schema.enums or {},
        "type": sv.schema.types or {},
        "subset": sv.schema.subsets or {},
    }[kind]
    return items, len(local_names)


def format_report(kind: str, schema_path: str, items: list[tuple], total: int) -> str:
    label = KIND_LABELS[kind]
    if kind == "class":
        title = f"# Isolerte lokale klassar ({schema_path})"
        empty_msg = f"Ingen isolerte lokale klassar funne ({total} lokale klassar sjekka)."
        col_a = "Klasse"
    else:
        title = f"# Ubrukte lokale {label} ({schema_path})"
        empty_msg = f"Ingen ubrukte lokale {label} funne ({total} sjekka)."
        col_a = {"slot": "Slot", "enum": "Enum", "type": "Type", "subset": "Subset"}[kind]

    lines = [title, ""]

    if not items:
        lines.append(empty_msg)
        return "\n".join(lines)

    if kind == "class":
        lines.append(f"| {col_a} | Grunn | Skildring |")
        lines.append("|---|---|---|")
        for name, description, reason in items:
            lines.append(f"| `{name}` | {reason} | {description or '(inga skildring)'} |")
        n_container_only = sum(1 for _, _, reason in items if reason == REASON_CONTAINER_ONLY)
        n_isolated = len(items) - n_container_only
        lines.append(
            f"\n**Totalt: {len(items)} isolerte/underintegrerte klassar av {total} "
            f"lokale klassar** ({n_isolated} heilt isolert, "
            f"{n_container_only} kun tilkopla via containerklassen)."
        )
    else:
        lines.append(f"| {col_a} | Skildring |")
        lines.append("|---|---|")
        for name, description in items:
            lines.append(f"| `{name}` | {description or '(inga skildring)'} |")
        lines.append(f"\n**Totalt: {len(items)} ubrukte lokale {label} av {total} sjekka.**")

    return "\n".join(lines)


def process_schema_all_kinds(schema_path: Path, out_dir: Path) -> bool:
    """Byggjer eitt SchemaView for schema_path og skriv alle fem
    kind-rapportane til out_dir. Returnerer False (loggar sjølv) viss
    skjemaet ikkje kunne lastast — kallar avgjer sjølv om det skal stoppe
    resten av ein batch eller halde fram."""
    try:
        from linkml_runtime import SchemaView

        sv = SchemaView(str(schema_path))
    except Exception as exc:  # noqa: BLE001 — same isolasjonsprinsipp som check-import-duplicates.py
        log_error(f"klarte ikkje laste {schema_path} med SchemaView — {exc}")
        return False

    out_dir.mkdir(parents=True, exist_ok=True)
    for kind in ALL_KINDS:
        items, total = compute_items_and_total(sv, kind)
        report = format_report(kind, str(schema_path), items, total)
        (out_dir / KIND_TO_REPORT_FILENAME[kind]).write_text(report + "\n", encoding="utf-8")
    return True


def process_domain(domain: str, base_dir: Path) -> None:
    """Diskoverer alle skjema i domenet og skriv model-analyse/-rapportar
    for kvart, i éin Python-prosess (éin linkml_runtime-import totalt, i
    staden for éin per skjema × kind)."""
    schemas = sorted(Path("src/linkml").glob(f"{domain}/*/*-schema.yaml"))
    if not schemas:
        print(f"ÅTVARING: fann ingen skjema for domene '{domain}'", file=sys.stderr)
        return

    for schema_path in schemas:
        schema_name = schema_path.parent.name
        out_dir = base_dir / domain / schema_name / "model-analyse"
        if process_schema_all_kinds(schema_path, out_dir):
            print(f"  ✓ {schema_name}: {len(ALL_KINDS)} lokal-modellanalyse-rapportar skrivne")
        else:
            print(f"::warning::lokal modellanalyse feila for {schema_name}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kind", choices=list(ALL_KINDS), help="Stdout-modus: éin kind for eitt skjema")
    parser.add_argument("--schema", help="Stdout-modus: sti til <modell>-schema.yaml")
    parser.add_argument("--domain", help="Batch-modus: skriv rapportar for alle skjema i domenet")
    parser.add_argument("--out-dir", help="Batch-modus: rot-katalog rapportane vert skrivne under")
    args = parser.parse_args()

    if args.domain:
        if not args.out_dir:
            parser.error("--domain krev --out-dir")
        if args.kind or args.schema:
            parser.error("--domain kan ikkje kombinerast med --kind/--schema")
        process_domain(args.domain, Path(args.out_dir))
        return 0

    if not args.kind or not args.schema:
        parser.error("krev anten --domain --out-dir, eller --kind --schema")

    schema_path = Path(args.schema)
    if not schema_path.is_file():
        log_error(f"fann ikkje {schema_path}")
        return 1

    try:
        from linkml_runtime import SchemaView

        sv = SchemaView(str(schema_path))
    except Exception as exc:  # noqa: BLE001 — same isolasjonsprinsipp som check-import-duplicates.py
        log_error(f"klarte ikkje laste {schema_path} med SchemaView — {exc}")
        return 1

    items, total = compute_items_and_total(sv, args.kind)
    print(format_report(args.kind, args.schema, items, total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
