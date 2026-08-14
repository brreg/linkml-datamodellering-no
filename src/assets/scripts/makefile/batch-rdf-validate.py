#!/usr/bin/env python3
"""
Batch-valider FLEIRE RDF/Turtle-filer i éin prosess, i staden for éin
podman-kontainar per fil.

Bakgrunn: `assert_rdf_valid()` i tests/test_make.sh spann tidlegare opp EIN
NY podman-kontainar (full kontainar-oppstart + `import rdflib`, målt til
~2,5s) FOR KVART KALL — opptil 4 gonger per skjema (gen-rdf/gen-shacl/
gen-owl/convert-rdf sine output-filer), over 100 separate kontainar-
oppstartar for ei full testkøyring. Same rotårsak/løysing som
batch-generate.py m.fl.: amortiser importskatten over heile fillista i
staden for å betale han på nytt per fil. Sjå
specs/backlog/optimaliser-make-test-basert-pa-logginnsikt.md, Tiltak 1.

Køyrer sekvensielt ETTER dei andre Fase A-stega (gen-rdf/gen-shacl/
gen-owl/convert-rdf sine output-filer må vere ferdig skrivne FØR fillista
vert bygd) — sjå tests/test_make.sh sin run_phase_a_rdf_validity().

Bruk:
  python3 batch-rdf-validate.py --files-list <fil>

  files-list: éin filsti per linje.

Skriv `::error file=<filsti>::` til stderr for filer som ikkje er gyldig
RDF eller har ein tom graf (same attribueringsformat som
batch-generate.py/batch-lint.py/batch-convert.py) — grep-bart av
phase_a_check() i tests/test_make.sh. phase_a_check() sitt andre argument
er berre den eksakte matchestrengen etter `::error file=`, ikkje
nødvendigvis eit skjema — her vert han kalla med FILSTIEN (ikkje
skjemastien), sidan éin skjema kan ha fleire RDF-filer som treng
uavhengige resultat (rdf/shacl/owl/convert-rdf sjekkast separat av kvar
sin Fase B-testfunksjon).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def log_error(msg: str) -> None:
    print(f"[ERROR] {msg}", file=sys.stderr)


def log_info(msg: str) -> None:
    print(msg, file=sys.stderr)


def load_files(files_list: str) -> list[str]:
    return [line for line in Path(files_list).read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--files-list", required=True)
    args = parser.parse_args()

    import rdflib

    files = load_files(args.files_list)

    failed = 0
    for f in files:
        try:
            g = rdflib.Graph()
            g.parse(f)
            if len(g) == 0:
                log_error(f"::error file={f}::Graf er tom: {f}")
                failed += 1
            else:
                log_info(f"→ rdf-validity  {f} ({len(g)} tripler)")
        except Exception as exc:  # noqa: BLE001 — per-fil isolasjon, sjå batch-generate.py sitt tilsvarande mønster
            log_error(f"::error file={f}::rdf-validity feila for {f} — {exc}")
            failed += 1

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
