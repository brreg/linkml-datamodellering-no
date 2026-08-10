#!/usr/bin/env python3
"""
Batch-generer dei ikkje-linkml PYTHON_RUN-generatorane (docgen-examples,
openapi, asyncapi-generering, informasjonsmodell-instans) for FLEIRE skjema
i éin prosess, i staden for éin podman-kontainar per skjema.

Bakgrunn: sjølv om desse scripta ikkje importerer linkml/linkml_runtime (og
difor ikkje ber ~5,4 s import-skatt, jf. spec «Funn»-avsnittet), betaler
kvar av dei ~2,6 s podman/Python-kontainar-oppstart PER SKJEMA PER SCRIPT.
Sjå specs/backlog/effektiviser-generate-workflow-koyretid.md (Tiltak 3).

Kvart av dei fire underliggjande scripta (gen-docgen-examples.py,
gen-openapi.py, gen-asyncapi.py, generate-informasjonsmodell.py) er
UENDRA i denne endringa (framleis brukbare frittståande, éin-skjema-om-
gongen, jf. sine eigne main()-funksjonar) — dette skriptet importerer
berre dei reine funksjonane deira og løkkar over N skjema i same prosess.

`asyncapi validate` (Node.js-CLI i eige ASYNCAPI_IMAGE) er MEDVITE IKKJE
batcha her — berre 1 skjema i heile repoet har `asyncapi: true` i dag,
så det finst ingenting å batche (jf. "Ikkje eit tiltak: gen-xsd" i
same spec for identisk grunngjeving). `openapi-spec-validator` ER batcha
(same python-pytest-image som generering, ingen ekstra kontainar).

Bruk:
  python3 batch-generate-instances.py --generator <kind> -- schema1.yaml schema2.yaml ...
  python3 batch-generate-instances.py --generator convert --jobs-tsv <fil>

  <kind>: docgen-examples | openapi | asyncapi | informasjonsmodell
        | erdiagram-filter | plantuml-filter | convert

`erdiagram-filter`/`plantuml-filter` er Fase B for gen-erdiagram/
gen-plantuml (Fase A, rå-generering, er batcha i batch-generate.py) —
filtrerer alt genererte `-raw`/`-unfiltered`-mellomfiler, importerer
`filter_erdiagram.py`/`filter_plantuml.py` sine reine `process_file()`-
funksjonar. `convert` batchar `linkml-convert` (eksempel → RDF/Turtle) via
ei jobb-TSV frå `convert-examples.sh` (schema/example/out-triplar,
handterer m.a. `tests/fixtures/`-overstyring — IKKJE duplisert her).
Sjå specs/backlog/effektiviser-generate-workflow-koyretid.md (Tiltak 4).
"""

from __future__ import annotations

import argparse
import contextlib
import importlib.util
import io
import os
import re
import sys
import time
from pathlib import Path

LOGLVL = os.environ.get("LOGLVL", "INFO")
CLR_STEP = os.environ.get("CLR_STEP", "")
CLR_OK = os.environ.get("CLR_OK", "")
CLR_RST = os.environ.get("CLR_RST", "")
GEN_DIR = os.environ.get("GEN_DIR", "generated")
SCRIPT_DIR = Path(__file__).resolve().parent


def log(msg: str) -> None:
    print(msg, file=sys.stderr)


def log_debug(msg: str) -> None:
    if LOGLVL == "DEBUG":
        log(f"[DEBUG] {msg}")


def log_info(msg: str) -> None:
    if LOGLVL != "ERROR":
        log(msg)


def log_error(msg: str) -> None:
    log(f"[ERROR] {msg}")


def fmt_elapsed(seconds: float) -> str:
    ms = int(seconds * 1000)
    return f"{ms // 1000}.{ms % 1000 // 10:02d}s"


def _import_from_path(module_name: str, file_name: str):
    """Importer eit script med bindestrek-i-namnet (t.d. gen-openapi.py) som modul.
    Registrerer modulen i sys.modules FØR exec_module() — obligatorisk for
    at @dataclass (brukt av batch-generate.py) skal fungere, sidan
    dataclasses sin interne typeoppløysing slår opp sys.modules[cls.__module__]."""
    spec = importlib.util.spec_from_file_location(module_name, SCRIPT_DIR / file_name)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def schema_domain_name(schema: str) -> tuple[str, str]:
    domain = schema.split("/")[2]
    name = re.sub(r"-schema$", "", Path(schema).stem)
    return domain, name


def read_build_yaml_flag(schema: str, flag: str) -> bool:
    manifest = Path(schema).parent / "build.yaml"
    if not manifest.is_file():
        return False
    text = manifest.read_text(encoding="utf-8")
    return re.search(rf"^  {re.escape(flag)}: true$", text, re.MULTILINE) is not None


def filter_enabled(schemas: list[str], flag: str | None, generator: str) -> list[str]:
    """Skjema utan build.yaml eller utan `<flag>: true` vert hoppa over (ikkje feil)."""
    if flag is None:
        return list(schemas)
    enabled = [s for s in schemas if read_build_yaml_flag(s, flag)]
    names = ", ".join(schema_domain_name(s)[1] for s in enabled)
    names_display = f"{CLR_OK}{names}{CLR_RST}" if names else "(ingen)"
    log_debug(f"{generator} ({flag}: true) — køyrer: {names_display}")
    return enabled


def run_erdiagram_filter(schemas: list[str]) -> int:
    """Fase B for gen-erdiagram: filtrer $name-erdiagram-unfiltered.md (skrive
    av awk-steget mellom batch-generate.py sin "erdiagram"-kind og dette
    steget, jf. spec Tiltak 4) til den endelege $name-erdiagram.md."""
    schemas = filter_enabled(schemas, "erdiagram", "erdiagram-filter")
    mod = _import_from_path("filter_erdiagram", "filter_erdiagram.py")
    failed = 0
    for s in schemas:
        domain, name = schema_domain_name(s)
        unfiltered = Path(GEN_DIR) / domain / name / f"{name}-erdiagram-unfiltered.md"
        out = Path(GEN_DIR) / domain / name / f"{name}-erdiagram.md"
        if not unfiltered.is_file():
            log_error(f"ÅTVARING: {unfiltered} finst ikkje — hoppar over erdiagram-filter for {domain}/{name}")
            continue
        t0 = time.time()
        try:
            out.write_text(mod.process_file(Path(s), unfiltered), encoding="utf-8")
        except Exception as exc:  # noqa: BLE001 — per-skjema isolasjon
            log_error(f"::error file={s}::erdiagram-filter feila for {domain}/{name} ({fmt_elapsed(time.time() - t0)}) — {exc}")
            failed += 1
            continue
        log_info(f"{CLR_STEP}→ erdiagram-filter  {domain}/{name}{CLR_RST} ({fmt_elapsed(time.time() - t0)})")
    return failed


def run_plantuml_filter(schemas: list[str]) -> int:
    """Fase B for gen-plantuml: filtrer $name-raw.puml (skrive av
    batch-generate.py sin "plantuml"-kind) til $name-filtered.puml og
    $name.puml (full) — 2 modus per skjema, jf. spec Tiltak 4."""
    schemas = filter_enabled(schemas, "plantuml", "plantuml-filter")
    mod = _import_from_path("filter_plantuml", "filter_plantuml.py")
    failed = 0
    for s in schemas:
        domain, name = schema_domain_name(s)
        diagrams_dir = Path(GEN_DIR) / domain / name / "diagrams"
        raw = diagrams_dir / f"{name}-raw.puml"
        if not raw.is_file():
            log_error(f"ÅTVARING: {raw} finst ikkje — hoppar over plantuml-filter for {domain}/{name}")
            continue
        t0 = time.time()
        try:
            # process_file() returnerer utan avsluttande linjeskift (som
            # print() i CLI-en la til) — legg det til her for byte-identisk
            # output.
            (diagrams_dir / f"{name}-filtered.puml").write_text(mod.process_file(Path(s), raw, "filtered") + "\n", encoding="utf-8")
            (diagrams_dir / f"{name}.puml").write_text(mod.process_file(Path(s), raw, "full") + "\n", encoding="utf-8")
        except Exception as exc:  # noqa: BLE001 — per-skjema isolasjon
            log_error(f"::error file={s}::plantuml-filter feila for {domain}/{name} ({fmt_elapsed(time.time() - t0)}) — {exc}")
            failed += 1
            continue
        log_info(f"{CLR_STEP}→ plantuml-filter  {domain}/{name}{CLR_RST} ({fmt_elapsed(time.time() - t0)})")
    return failed


def run_convert(jobs_tsv: str) -> int:
    """Batchar linkml-convert (eksempel → RDF/Turtle) for jobbane i jobs_tsv
    (schema\\texample\\tout per linje, produsert av convert-examples.sh sin
    eksisterande discovery/filtreringslogikk — IKKJE duplisert her, sidan
    ho m.a. handterer tests/fixtures/-overstyring). Same Click-drivne
    in-process-mønster som batch-generate.py (linkml.converter.cli:cli
    skriv sjølv til --output, ikkje stdout)."""
    batch_generate = _import_from_path("batch_generate", "batch-generate.py")
    converter_mod = importlib.import_module("linkml.converter.cli")
    cli_cmd = converter_mod.cli
    failed = 0
    lines = [line for line in Path(jobs_tsv).read_text(encoding="utf-8").splitlines() if line.strip()]
    for line in lines:
        schema, example, out = line.split("\t")
        parts = Path(out).parts  # generated/<domain>/<name>/<fil>.ttl
        domain, name = parts[1], parts[2]
        t0 = time.time()
        try:
            Path(out).parent.mkdir(parents=True, exist_ok=True)
            batch_generate.run_click(
                cli_cmd,
                ["--schema", schema, "--output-format", "ttl", "--no-validate", "--output", out, example],
            )
        except Exception as exc:  # noqa: BLE001 — per-skjema isolasjon
            log_error(f"::error file={schema}::linkml-convert feila for {domain}/{name} ({fmt_elapsed(time.time() - t0)}) — {exc}")
            failed += 1
            continue
        log_info(f"{CLR_STEP}→ linkml-convert  {example}{CLR_RST} ({fmt_elapsed(time.time() - t0)})")
    return failed


def run_docgen_examples(schemas: list[str]) -> int:
    schemas = filter_enabled(schemas, "docs", "docgen-examples")
    mod = _import_from_path("gen_docgen_examples", "gen-docgen-examples.py")
    failed = 0
    for s in schemas:
        domain, name = schema_domain_name(s)
        example = Path("src/linkml") / domain / name / "examples" / f"{name}-eksempel.yaml"
        out_dir = Path(GEN_DIR) / domain / name / "docgen-examples"
        t0 = time.time()
        try:
            mod.process_schema(Path(s), example, out_dir)
        except Exception as exc:  # noqa: BLE001 — per-skjema isolasjon
            log_error(f"::error file={s}::docgen-examples feila for {domain}/{name} ({fmt_elapsed(time.time() - t0)}) — {exc}")
            failed += 1
            continue
        log_info(f"{CLR_STEP}→ docgen-examples  {domain}/{name}{CLR_RST} ({fmt_elapsed(time.time() - t0)})")
    return failed


def run_informasjonsmodell(schemas: list[str]) -> int:
    mod = _import_from_path("generate_informasjonsmodell", "generate-informasjonsmodell.py")
    failed = 0
    for s in schemas:
        domain, name = schema_domain_name(s)
        schema_path = Path(s)
        t0 = time.time()
        try:
            data = mod.generate_modelldcat_data(schema_path)
            output_path = schema_path.parent / "metadata" / f"{name}-manifest.yaml"
            mod.write_yaml(
                output_path, data,
                generated_by="generate-informasjonsmodell.py",
                note="Kjelder: schema.yaml, build.yaml, CODEOWNERS.md, lokale klasser, genererte artefakter",
            )
        except Exception as exc:  # noqa: BLE001 — per-skjema isolasjon
            log_error(f"::error file={s}::gen-informasjonsmodell-instance feila for {domain}/{name} ({fmt_elapsed(time.time() - t0)}) — {exc}")
            failed += 1
            continue
        log_info(f"{CLR_STEP}→ gen-informasjonsmodell-instance  {domain}/{name}{CLR_RST} ({fmt_elapsed(time.time() - t0)})")
    return failed


def run_openapi(schemas: list[str]) -> int:
    schemas = filter_enabled(schemas, "openapi", "gen-openapi")
    gen_mod = _import_from_path("gen_openapi", "gen-openapi.py")
    validator_mod = importlib.import_module("openapi_spec_validator.__main__")
    failed = 0
    for s in schemas:
        domain, name = schema_domain_name(s)
        json_schema = Path(GEN_DIR) / domain / name / f"{name}-schema.json"
        out = Path(GEN_DIR) / domain / name / f"{name}-openapi.yaml"
        if not json_schema.is_file():
            log_error(f"ÅTVARING: {json_schema} finst ikkje — hoppar over gen-openapi for {domain}/{name}")
            continue
        t0 = time.time()
        try:
            doc = gen_mod.build_openapi(json_schema, s)
            import yaml as _yaml
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(_yaml.dump(doc, allow_unicode=True, default_flow_style=False, sort_keys=False), encoding="utf-8")
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                try:
                    validator_mod.main([str(out)])
                except SystemExit as exc:
                    if exc.code not in (0, None):
                        raise RuntimeError(f"openapi-spec-validator: {buf.getvalue().strip()}") from None
        except Exception as exc:  # noqa: BLE001 — per-skjema isolasjon
            log_error(f"::error file={s}::gen-openapi feila for {domain}/{name} ({fmt_elapsed(time.time() - t0)}) — {exc}")
            failed += 1
            continue
        log_info(f"{CLR_STEP}→ gen-openapi  {domain}/{name}{CLR_RST} ({fmt_elapsed(time.time() - t0)})")
    return failed


def run_asyncapi(schemas: list[str]) -> int:
    """Batchar berre generering (build_asyncapi) — IKKJE `asyncapi validate`,
    sjå moduldocstring for grunngjeving."""
    schemas = filter_enabled(schemas, "asyncapi", "gen-asyncapi")
    gen_mod = _import_from_path("gen_asyncapi", "gen-asyncapi.py")
    failed = 0
    for s in schemas:
        domain, name = schema_domain_name(s)
        json_schema = Path(GEN_DIR) / domain / name / f"{name}-schema.json"
        out = Path(GEN_DIR) / domain / name / f"{name}-asyncapi.yaml"
        if not json_schema.is_file():
            log_error(f"ÅTVARING: {json_schema} finst ikkje — hoppar over gen-asyncapi for {domain}/{name}")
            continue
        t0 = time.time()
        try:
            doc = gen_mod.build_asyncapi(json_schema, s)
            import yaml as _yaml
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(_yaml.dump(doc, allow_unicode=True, default_flow_style=False, sort_keys=False), encoding="utf-8")
        except Exception as exc:  # noqa: BLE001 — per-skjema isolasjon
            log_error(f"::error file={s}::gen-asyncapi feila for {domain}/{name} ({fmt_elapsed(time.time() - t0)}) — {exc}")
            failed += 1
            continue
        log_info(f"{CLR_STEP}→ gen-asyncapi  {domain}/{name}{CLR_RST} ({fmt_elapsed(time.time() - t0)})")
    return failed


RUNNERS = {
    "docgen-examples": run_docgen_examples,
    "informasjonsmodell": run_informasjonsmodell,
    "openapi": run_openapi,
    "asyncapi": run_asyncapi,
    "erdiagram-filter": run_erdiagram_filter,
    "plantuml-filter": run_plantuml_filter,
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--generator", required=True, choices=sorted([*RUNNERS, "convert"]))
    parser.add_argument("--jobs-tsv", help="TSV-fil (schema\\texample\\tout per linje) — berre for --generator convert")
    parser.add_argument("schemas", nargs="*")
    args = parser.parse_args()

    if args.generator == "convert":
        if not args.jobs_tsv:
            parser.error("--generator convert krev --jobs-tsv")
        failed = run_convert(args.jobs_tsv)
    else:
        failed = RUNNERS[args.generator](args.schemas)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
