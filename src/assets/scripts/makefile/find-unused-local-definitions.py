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
tabellen har ingen Usage-kolonne i dag): finn lokale klassar som er
isolerte, dvs. ikkje har NOKA tilkopling (via slot-/attributtrange, eller
is_a/mixins) til noka anna lokal klasse. Containerklassen (tree_root)
reknast alltid som tilkopla resten (ho er modellen sitt inngangspunkt) og
vert difor aldri sjølv rapportert som isolert, men referansane hennar til
andre lokale klassar tel som reell tilkopling for målklassane.

Krev SchemaView (og dermed induced_slot()-arveoppløysing) — bruk
LINKML_RUN, ikkje PYTHON_RUN (jf. check-import-duplicates.py).

Bruk:
  python3 find-unused-local-definitions.py --kind slot --schema <sti>
  python3 find-unused-local-definitions.py --kind class --schema <sti>

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
    """Returnerer [(namn, skildring), ...] for lokalt DEFINERTE namn av
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
    """Namna på alle andre lokale klassar denne klassa er tilkopla til,
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


def find_isolated_classes(sv) -> list[tuple[str, str]]:
    """Finn lokale klassar (utanom containerklassen) som ikkje har NOKA
    tilkopling til noka anna lokal klasse. Ein klasse vert rekna som
    tilkopla dersom ho anten sjølv koplar seg til ei anna lokal klasse,
    eller ei anna lokal klasse (inkl. containeren) koplar seg til henne."""
    all_local = local_classes(sv, include_root=True)
    connected_names: set[str] = set()

    for c in all_local:
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
        isolated.append((c.name, description))
    return sorted(isolated)


def render_report(kind: str, schema_path: str, items: list[tuple[str, str]], total: int) -> None:
    label = KIND_LABELS[kind]
    if kind == "class":
        title = f"# Isolerte lokale klassar ({schema_path})"
        empty_msg = f"Ingen isolerte lokale klassar funne ({total} lokale klassar sjekka)."
        col_a = "Klasse"
    else:
        title = f"# Ubrukte lokale {label} ({schema_path})"
        empty_msg = f"Ingen ubrukte lokale {label} funne ({total} sjekka)."
        col_a = {"slot": "Slot", "enum": "Enum", "type": "Type", "subset": "Subset"}[kind]

    print(f"{title}\n")

    if not items:
        print(empty_msg)
        return

    print(f"| {col_a} | Skildring |")
    print("|---|---|")
    for name, description in items:
        print(f"| `{name}` | {description or '(inga skildring)'} |")

    if kind == "class":
        print(f"\n**Totalt: {len(items)} isolerte klassar av {total} lokale klassar.**")
    else:
        print(f"\n**Totalt: {len(items)} ubrukte lokale {label} av {total} sjekka.**")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kind", choices=["slot", "enum", "type", "subset", "class"], required=True)
    parser.add_argument("--schema", required=True, help="Sti til <modell>-schema.yaml")
    args = parser.parse_args()

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

    if args.kind == "class":
        items = find_isolated_classes(sv)
        total = len(local_classes(sv, include_root=True))
    else:
        items = find_unused(sv, args.kind)
        local_names = {
            "slot": sv.schema.slots or {},
            "enum": sv.schema.enums or {},
            "type": sv.schema.types or {},
            "subset": sv.schema.subsets or {},
        }[args.kind]
        total = len(local_names)

    render_report(args.kind, args.schema, items, total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
