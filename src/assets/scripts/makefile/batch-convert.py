#!/usr/bin/env python3
"""
Batch-konverter FLEIRE linkml-convert-kall i éin prosess, i staden for éin
podman-kontainar per kall. Batchar convert-rdf og roundtrip-json/roundtrip-
ttl sine underliggande linkml-convert-kall (opptil 8 per skjema) frå
tests/test_make.sh.

Bakgrunn: import av linkml/linkml_runtime (~5,4 s) vert betalt på nytt for
kvar einaste podman-kontainar (same rotårsak som batch-generate.py).
`linkml.converter.cli:cli` (bak `linkml-convert`) er, ulikt
`linkml.linter.cli.main`/`linkml.validator.cli.cli`, ein rein Click-
kommando UTAN `sys.exit()` i kroppen (kastar exceptions i staden) —
verifisert direkte med `inspect.getsource()`. Kompatibel med same
`run_click()`-mønster som batch-generate.py brukar for dei linkml-baserte
generatorane. Sjå specs/backlog/batch-validate-lint-test-per-skjema.md,
Tiltak 3 Kategori D.

Jobbane er heterogene (ulik schema/input/output-format/output per jobb,
ulikt Kategori A/B sine faste generator-typar med berre `schema` som
argument) — same mønster som batch-flatten-and-validate.py sin
`--jobs-tsv` brukar for heterogene MCP-valideringsjobbar.

Jobbar for same skjema (t.d. dei 3-4 stega i eit roundtrip-kall) må stå i
rett rekkjefølgje i TSV-fila når eit steg sin `input` er eit tidlegare
steg sin `output` — scriptet prosesserer jobbane strengt sekvensielt (éin
prosess, ingen parallellitet internt), så skrive-før-les-avhengigheiter
mellom jobbar for same skjema er trygge så lenge kallaren listar dei i rett
rekkjefølgje. Jobbar for ULIKE skjema kan stå i vilkårleg rekkjefølgje seg
imellom.

Bruk:
  python3 batch-convert.py --jobs-tsv <fil>

  jobs.tsv: éi jobb per linje, tab-separert:
    schema<TAB>input<TAB>output-format<TAB>output

Skriv `::error file=<schema>::` til stderr for feila jobbar (same
attribueringsformat som batch-generate.py/batch-lint.py) — grep-bart av
`phase_a_check()` i tests/test_make.sh.
"""

from __future__ import annotations

import argparse
import contextlib
import io
import sys
from pathlib import Path

# Sjå src/assets/scripts/utils/linkml_relative_import_patch.py — fiksar ein
# upstream-bug i SchemaView.imports_closure() for versjonslåste importar.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "utils"))
import linkml_relative_import_patch
linkml_relative_import_patch.apply()


def log_error(msg: str) -> None:
    print(f"[ERROR] {msg}", file=sys.stderr)


def log_info(msg: str) -> None:
    print(msg, file=sys.stderr)


def run_click(cli_cmd, argv: list[str]) -> None:
    ctx = cli_cmd.make_context(cli_cmd.name, list(argv))
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf), ctx:
        cli_cmd.invoke(ctx)


def load_jobs(jobs_tsv: str) -> list[tuple[str, str, str, str]]:
    jobs = []
    for line in Path(jobs_tsv).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        schema, input_, output_format, output = line.split("\t")
        jobs.append((schema, input_, output_format, output))
    return jobs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jobs-tsv", required=True)
    args = parser.parse_args()

    from linkml.converter.cli import cli as convert_cli

    jobs = load_jobs(args.jobs_tsv)

    failed = 0
    for schema, input_, output_format, output in jobs:
        Path(output).parent.mkdir(parents=True, exist_ok=True)
        argv = ["--schema", schema, "--output-format", output_format,
                "--no-validate", "--output", output, input_]
        try:
            run_click(convert_cli, argv)
            log_info(f"→ convert  {input_} → {output}")
        except Exception as exc:  # noqa: BLE001 — per-jobb isolasjon, sjå batch-generate.py sitt tilsvarande mønster
            log_error(f"::error file={schema}::convert feila ({input_} → {output}) — {exc}")
            failed += 1

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
