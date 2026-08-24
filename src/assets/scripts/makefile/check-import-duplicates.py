#!/usr/bin/env python3
"""
Sjekk at ingen skjema definerer eit topnivå-slot/klasse/type/enum/subset som
kolliderer med eit element frå importkjeda (same navn, ulikt kjeldeskjema).

Bakgrunn: sjå specs/done/oreg-scaffold-generering-feiler.md og
specs/backlog/new-modell-dublettsjekk-mot-imports.md. Seks nye oreg-skjema
definerte lokale slots/klassar (t.d. `beskrivelse`, `versjon`,
`Kontaktopplysning`) med same navn som eit element alt importert via
dcat-ap-no-schema/common-ap-no-schema. LinkML sitt import-hierarki mergar
IKKJE slike par til éitt element — dei kolliderer, og feilen dukkar først opp
djupt inne i python/proto/graphql/jsonld-context/plantuml-generatorane med
den kryptiske meldinga "Conflicting URIs (<skjema-a>, <skjema-b>) for item:
<navn>", lenge etter at nokon kunne retta problemet enkelt.

Denne sjekken bruker `linkml.utils.schemaloader.SchemaLoader` direkte — same
mekanisme desse generatorane alt bruker internt for å slå saman importkjeda
(`uses_schemaloader = True`-generatorfamilien) — i staden for å
reimplementere import-oppløysing for hand. Kollisjonsfeilen kjem frå
`linkml.utils.mergeutils.merge_dicts()`:

    if k in target and source[k].from_schema != target[k].from_schema:
        raise ValueError(f"Conflicting URIs ({source[k].from_schema}, "
                          f"{target[k].from_schema}) for item: {k}")

— eit reint navne-basert sjekk (same navn frå to ulike skjema-kjelder), ikkje
ei samanlikning av faktiske slot_uri/class_uri-verdiar. Å kalle
SchemaLoader(...).resolve() sjølv gjev difor 100 % åtferdsparitet med feilen
sjekken skal fange, dekkjer types:/enums:/subsets: i tillegg til
slots:/classes: heilt gratis, og krev ingen eiga reimplementering av LinkML
sin CURIE-/prefiks-oppløysingsalgoritme.

Bruk:
  python3 check-import-duplicates.py schema1.yaml schema2.yaml ...

Exit-kode: 0 = ingen kollisjonar funne, 1 = minst éin kollisjon (eller eit
skjema som ikkje kunne lastast av annan grunn).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Sjå src/assets/scripts/utils/linkml_relative_import_patch.py — fiksar ein
# upstream-bug i import-oppløysing for versjonslåste (raw.githubusercontent.com)
# importar, brukt av alle batch-script i denne katalogen.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "utils"))
import linkml_relative_import_patch  # noqa: E402

linkml_relative_import_patch.apply()

_CONFLICT_RE = re.compile(r"^Conflicting URIs \((.+), (.+)\) for item: (.+)$")


def log_error(msg: str) -> None:
    print(f"[ERROR] {msg}", file=sys.stderr)


def check_schema(schema_path: str) -> bool:
    """Returnerer True dersom skjemaet ikkje har importkollisjonar."""
    from linkml.utils.schemaloader import SchemaLoader

    try:
        SchemaLoader(schema_path, mergeimports=True).resolve()
    except ValueError as exc:
        match = _CONFLICT_RE.match(str(exc))
        if match:
            schema_a, schema_b, name = match.groups()
            log_error(
                f"::error file={schema_path}::dublett-navn '{name}' finst i to skjema i "
                f"importkjeda ({schema_a} og {schema_b}) — gi det lokale elementet eit meir "
                f"spesifikt navn (t.d. prefiks med modellnavnet, jf. "
                f"<modell>_kontaktinformasjon-mønsteret i oreg-skjema)"
            )
        else:
            log_error(f"::error file={schema_path}::check-import-duplicates feila for {schema_path} — {exc}")
        return False
    except Exception as exc:  # noqa: BLE001 — per-skjema isolasjon, sjå batch-lint.py sitt tilsvarande mønster
        log_error(
            f"::error file={schema_path}::check-import-duplicates kunne ikkje analysere "
            f"{schema_path} — {exc}"
        )
        return False
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("schemas", nargs="+", help="Skjema-stiar (repo-relative) som skal sjekkast")
    args = parser.parse_args()

    failed = False
    for schema in args.schemas:
        if not check_schema(schema):
            failed = True

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
