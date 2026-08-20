#!/usr/bin/env python3
"""
Batch-konverter FLEIRE linkml-convert-kall i éin prosess, i staden for éin
podman-kontainar per kall. Batchar convert-instance-rdf og roundtrip-json/roundtrip-
ttl sine underliggande linkml-convert-kall (opptil 8 per skjema) frå
tests/test_make.sh.

Bakgrunn: import av linkml/linkml_runtime (~5,4 s) vert betalt på nytt for
kvar einaste podman-kontainar (same rotårsak som batch-generate.py).

Kallar dei underliggjande linkml-primitiva DIREKTE (`SchemaView`,
`PythonGenerator(...).compile_module()`, `get_loader`/`get_dumper`,
`infer_root_class`) i staden for å gå via `linkml.converter.cli:cli` sin
Click-callback (slik dette skriptet gjorde tidlegare, sjå
specs/done/evaluer-batching-resterande-kommandoar.md). Grunngjeving: kvart
CLI-kall gjer `PythonGenerator(schema).compile_module()` (kodegenerering +
rå `compile()`+`exec()`) HEILT PÅ NYTT, sjølv når FLEIRE jobbrader på rad
brukar SAME skjema — verifisert at INGEN caching finst i linkml/
linkml_runtime for dette (`inspect.getsource()` av `compile_python()`), og
målt til ~3,3s per kall (mot ~0,01s for `SchemaView(schema)` — under 1%
av kostnaden). For roundtrip-json (3 jobbrader per skjema) og
roundtrip-ttl (4 jobbrader per skjema) vart `compile_module()` betalt 3-4
gonger per skjema i staden for éin. Dette skriptet cachar difor BERRE
`python_module` (reint funksjonelt, stateless kodegenererings-resultat)
PER UNIKT SKJEMA i `module_cache` og gjenbruker han på tvers av jobbrader.

`SchemaView` vert construert PÅ NYTT for KVAR jobbrad, IKKJE cacha —
verifisert empirisk at gjenbruk av éin delt `SchemaView`-instans på tvers
av jobbrader for same skjema INTRODUSERER FEIL (ei ekte regresjonskjelde,
ikkje berre teoretisk risiko): eit roundtrip-ttl-kall for
`brreg-modellkatalog`/`novari-modellkatalog` (som passerer i dag) feila
med `Modellkatalog.__init__() got an unexpected keyword argument
'tittel_literal'` og ei "Inconsistent URI to class map"-åtvaring når
`sv` vart delt mellom RDFLibDumper (skriv b.ttl) og RDFLibLoader (les
b.ttl → c.yaml) sine kall — tydeleg teikn på at RDFLib-lastar/dumpar-laget
mutrerer/cache-tilstand PÅ schemaview-objektet på ein måte som ikkje er
trygg å dele mellom uavhengige kall. Sidan `SchemaView`-konstruksjon uansett
er neglisjerbart billig samanlikna med `compile_module()`, er det ikkje
noko å vinne på å cache han — berre risiko. Sjå
specs/backlog/optimaliser-make-test-basert-pa-logginnsikt.md, Tiltak 2.

Reimplementasjonen er MED VILJE avgrensa til nøyaktig dei kodestigane
`cli.callback` tek for argv-forma dette skriptet alltid byggjer
(`--schema <s> --output-format <f> --no-validate --output <o> <input>`,
sjå `_run_phase_a_convert_batch()`/`run_phase_a_convert_rdf()`/
`run_phase_a_roundtrip_json()`/`run_phase_a_roundtrip_ttl()` i
tests/test_make.sh — INGEN kallar nokon gong `--module`, `--target-class`,
`--prefix`, `--context`, `--infer`, `--validate` eller XSV-relaterte flagg
for dette skriptet). Kjeldekoden til `cli.callback` vart lesen fullt ut via
`inspect.getsource()` for å stadfeste kva forgreiningar som faktisk kan
nåast med denne argv-forma, FØR reimplementasjonen vart skriven — sjå
spec-fila for detaljar. Dersom kallarane i tests/test_make.sh nokon gong
tek i bruk fleire flagg, må reimplementasjonen her utvidast tilsvarande.

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

    from linkml.generators.pythongen import PythonGenerator
    from linkml.utils import datautils
    from linkml.utils.datautils import _get_format, get_dumper, get_loader, infer_root_class
    from linkml_runtime.utils.schemaview import SchemaView

    jobs = load_jobs(args.jobs_tsv)

    # python_module (compilert Python-datamodell) per unikt skjema — sjå
    # toppkommentaren for grunngjeving. SchemaView vert IKKJE cacha (usikker
    # å dele mellom kall, sjå toppkommentaren).
    module_cache: dict[str, object] = {}

    def get_python_module(schema: str):
        cached = module_cache.get(schema)
        if cached is None:
            cached = PythonGenerator(schema).compile_module()
            module_cache[schema] = cached
        return cached

    failed = 0
    for schema, input_, output_format, output in jobs:
        Path(output).parent.mkdir(parents=True, exist_ok=True)
        try:
            python_module = get_python_module(schema)
            sv = SchemaView(schema)
            target_class = infer_root_class(sv)
            if target_class is None:
                raise Exception("target class not specified and could not be inferred")
            py_target_class = python_module.__dict__[target_class]

            input_format = _get_format(input_, None)
            loader = get_loader(input_format)
            inargs = {}
            if datautils._is_rdf_format(input_format):
                inargs["schemaview"] = sv
                inargs["fmt"] = input_format
            obj = loader.load(source=input_, target_class=py_target_class, **inargs)

            # --no-validate vert alltid sendt av kallarane i test_make.sh —
            # ingen valideringssteg her, jf. cli.callback sin `if validate:`.

            resolved_output_format = _get_format(output, output_format, default="json")
            outargs = {}
            if resolved_output_format in ("rdf", "ttl"):
                outargs["schemaview"] = sv
            dumper = get_dumper(resolved_output_format)
            dumper.dump(obj, output, **outargs)

            log_info(f"→ convert  {input_} → {output}")
        except Exception as exc:  # noqa: BLE001 — per-jobb isolasjon, sjå batch-generate.py sitt tilsvarande mønster
            log_error(f"::error file={schema}::convert feila ({input_} → {output}) — {exc}")
            failed += 1

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
