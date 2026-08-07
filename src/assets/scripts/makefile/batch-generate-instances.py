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

  <kind>: docgen-examples | openapi | asyncapi | informasjonsmodell
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
    return f"{int(seconds)}.{int(seconds * 10) % 10}s"


def _import_from_path(module_name: str, file_name: str):
    """Importer eit script med bindestrek-i-namnet (t.d. gen-openapi.py) som modul."""
    spec = importlib.util.spec_from_file_location(module_name, SCRIPT_DIR / file_name)
    module = importlib.util.module_from_spec(spec)
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
    """Same filtreringssemantikk som run-parallel-gen.sh sin --flag: skjema
    utan build.yaml eller utan `<flag>: true` vert hoppa over (ikkje feil)."""
    if flag is None:
        return list(schemas)
    enabled, skipped = [], []
    for s in schemas:
        (enabled if read_build_yaml_flag(s, flag) else skipped).append(s)
    if skipped:
        names = ", ".join("/".join(schema_domain_name(s)) for s in skipped)
        log_debug(f"{generator}: hoppar over ({flag}: false): {names}")
    return enabled


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
                note="Kjelder: schema.yaml, build.yaml, CODEOWNERS.md, lokale klasser, genererte artefaktar",
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
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--generator", required=True, choices=sorted(RUNNERS))
    parser.add_argument("schemas", nargs="+")
    args = parser.parse_args()

    failed = RUNNERS[args.generator](args.schemas)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
