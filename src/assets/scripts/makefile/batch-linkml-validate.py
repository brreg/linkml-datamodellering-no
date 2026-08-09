#!/usr/bin/env python3
"""
Batch-valider FLEIRE (skjema, instans)-par via `linkml.validator.validate()`
direkte i éin prosess, i staden for éin podman-kontainar per `linkml
validate`-CLI-kall.

Bakgrunn: `linkml.validator.cli:cli` (bak `linkml validate`) kallar
`sys.exit()` i kroppen (ulikt `linkml.converter.cli:cli`) og kan difor
IKKJE gjenbrukast via `run_click()`-mønsteret batch-generate.py/
batch-convert.py brukar. I staden nyttar dette skriptet
`linkml.validator.validate()` direkte — same funksjon mcp-linkml-validator
sin server.py alt brukar internt (sjå `validate_instance()` i server.py,
og grunngjevinga i specs/backlog/effektiviser-mcp-linkml-validator-
koyretid.md): send eit alt oppløyst `SchemaView(schema_path).schema`-
objekt, ALDRI ein rå skjemasti eller instans-filsti, sidan
`linkml.validator.validate()` elles anten reknar ut feil absolutt sti for
relative importar (skjemaet) eller behandlar filstinamnet sjølv som
instansdata (instansen — verifisert empirisk, `validate()` krev eit alt
parsa objekt, ikkje ein filsti-streng). `target_class` treng ikkje
oppgjevast eksplisitt — `validate()` finn `tree_root`-klassen automatisk
når han er `None`.

Sjå specs/backlog/batch-validate-lint-test-per-skjema.md, Tiltak 3
Kategori D.

Bruk:
  python3 batch-linkml-validate.py --jobs-tsv <fil>

  jobs.tsv: éi jobb per linje, tab-separert:
    attribueringsnøkkel<TAB>skjema-å-validere-mot<TAB>instansfil

  Nøkkelen og skjemaet er normalt like, men skil seg for skjema som vert
  validerte mot ein test-fixture i staden for det ekte skjemaet (t.d.
  AP-NO-profilar utan tree_root) — nøkkelen er alltid det ORIGINALE
  skjemaet, slik phase_a_check() i tests/test_make.sh kan slå det opp med
  same sti som testen sjølv kjenner skjemaet under.

Skriv `::error file=<nøkkel>::` til stderr for feila jobbar (same
attribueringsformat som batch-generate.py/batch-lint.py/batch-convert.py).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def log_error(msg: str) -> None:
    print(f"[ERROR] {msg}", file=sys.stderr)


def log_info(msg: str) -> None:
    print(msg, file=sys.stderr)


def load_jobs(jobs_tsv: str) -> list[tuple[str, str, str]]:
    jobs = []
    for line in Path(jobs_tsv).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        key, schema, instance = line.split("\t")
        jobs.append((key, schema, instance))
    return jobs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jobs-tsv", required=True)
    args = parser.parse_args()

    import yaml
    from linkml.validator import validate as lm_validate
    from linkml_runtime.utils.schemaview import SchemaView

    jobs = load_jobs(args.jobs_tsv)

    failed = 0
    for key, schema, instance in jobs:
        try:
            sv = SchemaView(schema)
            instance_obj = yaml.safe_load(Path(instance).read_text(encoding="utf-8"))
            report = lm_validate(instance_obj, sv.schema)
            if report.results:
                messages = "; ".join(str(r.message) for r in report.results[:3])
                log_error(f"::error file={key}::linkml-validate feila for {key} "
                          f"({len(report.results)} problem) — {messages}")
                failed += 1
            else:
                log_info(f"→ linkml-validate  {key}")
        except Exception as exc:  # noqa: BLE001 — per-jobb isolasjon, sjå batch-generate.py sitt tilsvarande mønster
            log_error(f"::error file={key}::linkml-validate feila for {key} — {exc}")
            failed += 1

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
