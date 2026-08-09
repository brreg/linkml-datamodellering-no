#!/usr/bin/env python3
"""
Batch-lint FLEIRE skjema i éin prosess, i staden for éin podman-kontainar
per skjema.

Bakgrunn: same rotårsak som batch-generate.py — import av linkml/
linkml_runtime (~5,4 s) vert betalt på nytt for kvar einaste podman-
kontainar. `linkml lint` sin eigen CLI-kommando (linkml.linter.cli.main)
kallar `sys.exit()` direkte i funksjonskroppen, så han kan IKKJE gjenbrukast
via same `run_click()`-mønster som batch-generate.py (ein `SystemExit` etter
første skjema ville drepe heile batchen). I staden nyttar dette skriptet
`Linter`- og `TerminalFormatter`-klassane direkte — same klassar CLI-en
sjølv byggjer på — og let éin `Linter`-instans og éin formatter-sesjon dekkje
alle skjema, nøyaktig slik CLI-en alt gjer når `SCHEMA`-argumentet er ein
katalog (sjå `get_yaml_files()` i linkml.linter.cli).

Funne biverknad av denne omlegginga: det gamle `make lint`-målet kjeda
CLI-kall med `&&` — sidan CLI-en returnerer exit-kode 1 for skjema med berre
åtvaringar (ikkje berre feil), stoppa `make lint` (utan SCHEMA=) i praksis
alltid etter det FØRSTE skjemaet med minst éi åtvaring, og linta difor aldri
resten av skjema-lista. Dette skriptet prosesserer alle skjema uavhengig av
kvarandre (som batch-generate.py sitt per-skjema try/except), og rapporterer
difor eit fullstendig bilete — sjå spec «Utført» for detaljar.

Bruk:
  python3 batch-lint.py --config <sti-til-config.yaml> -- schema1.yaml schema2.yaml ...

Exit-kode (same semantikk som linkml sin eigen CLI, summert over alle
skjema): 0 = ingen problem, 1 = berre åtvaringar, 2 = minst éin feil (eller
eit skjema som ikkje kunne prosesserast i det heile, t.d. ugyldig YAML).
"""

from __future__ import annotations

import argparse
import sys

import yaml


def log_error(msg: str) -> None:
    print(f"[ERROR] {msg}", file=sys.stderr)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("schemas", nargs="+")
    args = parser.parse_args()

    from linkml.linter.config.datamodel.config import RuleLevel
    from linkml.linter.formatters import TerminalFormatter
    from linkml.linter.linter import Linter

    with open(args.config, encoding="utf-8") as f:
        config = yaml.safe_load(f)

    linter = Linter(config=config)
    formatter = TerminalFormatter(sys.stdout, verbose=False)

    error_count = 0
    warning_count = 0
    schema_failed = False

    formatter.start_report()
    for schema in args.schemas:
        formatter.start_schema(schema)
        try:
            for problem in linter.lint(schema):
                if str(problem.level) is RuleLevel.error.text:
                    error_count += 1
                elif str(problem.level) is RuleLevel.warning.text:
                    warning_count += 1
                formatter.handle_problem(problem)
        except Exception as exc:  # noqa: BLE001 — per-skjema isolasjon, sjå batch-generate.py sitt tilsvarande mønster
            log_error(f"::error file={schema}::lint feila for {schema} — {exc}")
            schema_failed = True
        formatter.end_schema()
    formatter.end_report()

    if error_count > 0 or schema_failed:
        return 2
    if warning_count > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
