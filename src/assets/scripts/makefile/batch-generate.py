#!/usr/bin/env python3
"""
Batch-generer LinkML-artefakter (SHACL, OWL, Python, JSON Schema, RDF,
Protobuf, JSON-LD-context, skjema-validering/merge) for FLEIRE skjema i éin
prosess, i staden for éin podman-kontainar per skjema.

Bakgrunn: import av linkml/linkml_runtime tek ~5,4 s og vert betalt på nytt
for kvar einaste podman-kontainar (sjå
specs/backlog/effektiviser-generate-workflow-koyretid.md, «Funn»). gen-shacl/
gen-owl m.fl. er LinkML sine EIGNE CLI-verktøy (Click-kommandoar frå
`linkml`-pakken, ikkje kode dette repoet eig) — det finst difor ingen
ferdig stdin-løkke å batche mot (i motsetnad til mcp-linkml-validator sin
server.py, sjå batch-flatten-and-validate.py). I staden kallar dette
skriptet Click-kommandoen sitt eige `make_context()`/`invoke()` direkte i
prosessen, éin gong per skjema, med same argv som CLI-et ville fått.

Dette gjev IDENTISK oppførsel til den ekte CLI-en (same
flagg-standardverdiar, same argument-parsing, same cli()-funksjonskropp —
t.d. owlgen sin skjulte `metadata_profiles`-standardverdi og pythongen sin
`--validate`-spesialhandtering) UTAN å måtte handoversette kvart
click.option til eit generator-kwarg sjølv. Verifisert empirisk
(graph-isomorfi mot ekte CLI-subprosess-output) før denne batch-arkitekturen
vart tatt i bruk.

NB — kjend, IKKJE-relatert non-determinisme: SHACL/OWL/RDF-generatorane i
linkml sjølve kan produsere ulik blanknode-/eigenskapsrekkjefølgje (og i
sjeldne tilfelle ulikt `sh:ignoredProperties`-nærvær) mellom to køyringar av
SAME, uendra CLI-kommando — verifisert ved å køyre
`gen-shacl --exclude-imports` to gonger på same skjema utan denne batchen
involvert i det heile. Dette er ein eigenskap ved linkml/rdflib sin bruk av
hash-baserte set/dict internt, ikkje noko denne batch-arkitekturen innfører
eller forverrar. Byte-for-byte-diff er difor ikkje eit gyldig
identitetskriterium for desse tre generatorane — bruk graf-isomorfi.

Bruk:
  python3 batch-generate.py --generator <kind> -- schema1.yaml schema2.yaml ...

  <kind>: merge | jsonld-context | shacl | python | json-schema | owl | rdf | proto
        | graphql | erdiagram | plantuml | doc

`erdiagram`/`plantuml`/`doc` batchar berre RÅ-genereringssteget (Fase A) —
`erdiagram`/`plantuml` sine filter-etterhandsamingar (Fase B) er batcha
separat i batch-generate-instances.py, sidan dei ikkje er linkml-Python-
API-kall. `doc` skriv sjølv til ein katalog (via `-d`, `DocGenerator`) i
staden for å returnere éin streng — handtert via `extra_argv_fn`/`post_fn`
på `GeneratorSpec`, verifisert (spike) å produsere identisk katalog-
innhald mot CLI-subprosess, sjå
specs/backlog/effektiviser-generate-workflow-koyretid.md (Tiltak 4).
"""

from __future__ import annotations

import argparse
import contextlib
import importlib
import io
import os
import re
import shlex
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

import yaml

# Sjå src/assets/scripts/utils/linkml_relative_import_patch.py — fiksar ein
# upstream-bug i SchemaView.imports_closure() for versjonslåste importar.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "utils"))
import linkml_relative_import_patch
linkml_relative_import_patch.apply()

LOGLVL = os.environ.get("LOGLVL", "INFO")
CLR_STEP = os.environ.get("CLR_STEP", "")
CLR_OK = os.environ.get("CLR_OK", "")
CLR_RST = os.environ.get("CLR_RST", "")
GEN_DIR = os.environ.get("GEN_DIR", "generated")


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


@dataclass
class GeneratorSpec:
    module: str  # linkml.generators.<module>
    out_suffix: str | None = None  # None => diskarder run_click()-returverdien (validering, eller kommandoen skreiv sjølv via eige katalog-/filargument)
    flag: str | None = None  # build.yaml generators.<flag> — None => alltid aktivert
    extra_flags_field: str | None = None  # build.yaml generators.<felt> (sitatert streng), override
    default_extra_argv: list[str] = field(default_factory=list)
    extra_argv_fn: Callable[[str, str], list[str]] | None = None  # (domain, name) -> ekstra argv (kan ha biverknader, t.d. mkdir)
    post_fn: Callable[[str, str], None] | None = None  # (domain, name) -> None, køyrt etter vellukka run_click()
    out_subdir: str = ""  # t.d. "diagrams" for plantuml — tomt betyr $GEN_DIR/<domain>/<name>/ direkte
    skip_if_versioned_import: bool = False  # sjå schema_has_versioned_import() — BUG-17
    parallel: bool = False  # køyr per-skjema-lykka i eit ProcessPoolExecutor — sjå _generate_one()


def _doc_extra_argv(domain: str, name: str) -> list[str]:
    outdir = Path(GEN_DIR) / domain / name
    (outdir / "docgen-examples").mkdir(parents=True, exist_ok=True)
    (outdir / "docs").mkdir(parents=True, exist_ok=True)
    return [
        "--template-directory", "src/assets/templates/docgen",
        "--no-mergeimports", "--no-render-imports", "--no-hierarchical-class-view",
        "--diagram-type", "mermaid_class_diagram",
        "--example-directory", str(outdir / "docgen-examples"),
        "-d", str(outdir / "docs"),
    ]


def _doc_post(domain: str, name: str) -> None:
    """Same opprydding som sed -i "/Container/d" — fjern Container-referansar frå index.md."""
    index_path = Path(GEN_DIR) / domain / name / "docs" / "index.md"
    if not index_path.is_file():
        return
    lines = [line for line in index_path.read_text(encoding="utf-8").splitlines(keepends=True) if "Container" not in line]
    index_path.write_text("".join(lines), encoding="utf-8")


REGISTRY: dict[str, GeneratorSpec] = {
    "merge": GeneratorSpec(module="linkml.generators.linkmlgen"),
    "jsonld-context": GeneratorSpec(
        module="linkml.generators.jsonldcontextgen", out_suffix="context.jsonld", flag="jsonld_context"
    ),
    "shacl": GeneratorSpec(
        module="linkml.generators.shaclgen", out_suffix="shapes.ttl", flag="shacl", extra_flags_field="shacl_flags"
    ),
    "python": GeneratorSpec(module="linkml.generators.pythongen", out_suffix="model.py", flag="python"),
    "json-schema": GeneratorSpec(
        module="linkml.generators.jsonschemagen", out_suffix="schema.json", flag="json_schema"
    ),
    "owl": GeneratorSpec(
        module="linkml.generators.owlgen",
        out_suffix="ontology.ttl",
        flag="owl",
        extra_flags_field="owl_flags",
        default_extra_argv=[
            "--skip-vacuous-local-range-axioms",
            "--skip-vacuous-min-zero-cardinality-axioms",
            "--consolidate-cardinality-axioms",
        ],
    ),
    "rdf": GeneratorSpec(
        module="linkml.generators.rdfgen",
        out_suffix="schema.ttl",
        flag="rdf",
        skip_if_versioned_import=True,
        parallel=True,
    ),
    "proto": GeneratorSpec(module="linkml.generators.protogen", out_suffix="schema.proto", flag="protobuf"),
    "graphql": GeneratorSpec(module="linkml.generators.graphqlgen", out_suffix="schema.graphql", flag="graphql"),
    "erdiagram": GeneratorSpec(
        module="linkml.generators.erdiagramgen",
        out_suffix="erdiagram-raw.md",
        flag="erdiagram",
        default_extra_argv=["--no-mergeimports"],
    ),
    "plantuml": GeneratorSpec(
        module="linkml.generators.plantumlgen", out_suffix="raw.puml", flag="plantuml", out_subdir="diagrams"
    ),
    "doc": GeneratorSpec(
        module="linkml.generators.docgen",
        out_suffix=None,  # DocGenerator skriv sjølv til katalogen via -d, ikkje stdout
        flag="docs",
        extra_argv_fn=_doc_extra_argv,
        post_fn=_doc_post,
        parallel=True,
    ),
}


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


def read_build_yaml_extra_flags(schema: str, field_name: str) -> str:
    manifest = Path(schema).parent / "build.yaml"
    if not manifest.is_file():
        return ""
    text = manifest.read_text(encoding="utf-8")
    m = re.search(rf'^  {re.escape(field_name)}: *"(.*)"$', text, re.MULTILINE)
    return m.group(1) if m else ""


def schema_has_versioned_import(schema: str) -> bool:
    """True dersom skjemaet sin imports:-liste inneheld eit versjonslåst URL-import.

    RDFGenerator/JSONLDGenerator kan ikkje handtere slike importar — sjå
    bugs/gen-rdf-manglar-stotte-for-versjonslaste-importar.md (BUG-17).
    """
    schema_dict = yaml.safe_load(Path(schema).read_text(encoding="utf-8")) or {}
    return any("://" in str(imp) for imp in schema_dict.get("imports") or [])


def run_click(cli_cmd, argv: list[str]) -> str:
    ctx = cli_cmd.make_context(cli_cmd.name, list(argv))
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf), ctx:
        cli_cmd.invoke(ctx)
    return buf.getvalue()


def fmt_elapsed(seconds: float) -> str:
    ms = int(seconds * 1000)
    return f"{ms // 1000}.{ms % 1000 // 10:02d}s"


def _build_argv(s: str, domain: str, name: str, spec: GeneratorSpec) -> list[str]:
    argv = [s]
    if spec.extra_flags_field:
        extra = read_build_yaml_extra_flags(s, spec.extra_flags_field)
        argv += shlex.split(extra) if extra else list(spec.default_extra_argv)
    elif spec.default_extra_argv:
        argv += list(spec.default_extra_argv)
    if spec.extra_argv_fn:
        argv += spec.extra_argv_fn(domain, name)
    return argv


# Sett i main() FØR ProcessPoolExecutor vert oppretta (berre for
# spec.parallel=True-generatorar, t.d. doc/rdf — sjå GeneratorSpec.parallel).
# Linux sin standard multiprocessing-startmetode er "fork": worker-prosessar
# er ein copy-on-write-kopi av foreldreprosessen sitt minne på forke-
# tidspunktet, så denne modul-globalen er alt sett i kvar worker utan at
# sjølve Click Command-objektet (som ikkje er triviellt pickle-bart) nokon
# gong må sendast over IPC-køen. Berre task-tuplane (str/list/GeneratorSpec
# — alle pickle-bare) vert sendt til pool.map().
_CLI_CMD = None


def _generate_one(task: tuple[str, str, str, str, list[str], GeneratorSpec]) -> tuple[str, bool, str]:
    """Generer output for éitt skjema. Køyrer anten direkte (sekvensiell
    sti) eller i eit ProcessPoolExecutor-worker-prosess (spec.parallel=True)
    — sjå main(). Returnerer (schema, ok, loggmelding); kastar aldri, for
    trygg bruk med pool.map().
    """
    generator_name, s, domain, name, argv, spec = task
    t0 = time.time()
    try:
        output = run_click(_CLI_CMD, argv)
        if spec.out_suffix:
            outdir = Path(GEN_DIR) / domain / name / spec.out_subdir
            outdir.mkdir(parents=True, exist_ok=True)
            (outdir / f"{name}-{spec.out_suffix}").write_text(output, encoding="utf-8")
        if spec.post_fn:
            spec.post_fn(domain, name)
    except Exception as exc:  # noqa: BLE001 — per-skjema isolasjon, sjå spec Tiltak 1 steg 6
        elapsed = time.time() - t0
        return (s, False, f"::error file={s}::{generator_name} feila for {domain}/{name} ({fmt_elapsed(elapsed)}) — {exc}")
    elapsed = time.time() - t0
    return (s, True, f"{CLR_STEP}→ {generator_name}  {domain}/{name}{CLR_RST} ({fmt_elapsed(elapsed)})")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--generator", required=True, choices=sorted(REGISTRY))
    parser.add_argument("schemas", nargs="+")
    args = parser.parse_args()

    spec = REGISTRY[args.generator]

    enabled: list[str] = [
        s for s in args.schemas if spec.flag is None or read_build_yaml_flag(s, spec.flag)
    ]

    if spec.skip_if_versioned_import:
        skipped_versioned = [s for s in enabled if schema_has_versioned_import(s)]
        enabled = [s for s in enabled if s not in skipped_versioned]
        for s in skipped_versioned:
            domain, name = schema_domain_name(s)
            log_info(
                f"HOPPAR OVER {args.generator} for {domain}/{name} — versjonslåst URL-import, "
                "sjå bugs/gen-rdf-manglar-stotte-for-versjonslaste-importar.md (BUG-17)"
            )

    flag_desc = f" ({spec.flag}: true)" if spec.flag else ""
    names = ", ".join(schema_domain_name(s)[1] for s in enabled)
    names_display = f"{CLR_OK}{names}{CLR_RST}" if names else "(ingen)"
    log_debug(f"{args.generator}{flag_desc} — køyrer: {names_display}")

    if not enabled:
        return 0

    module = importlib.import_module(spec.module)
    global _CLI_CMD
    _CLI_CMD = module.cli

    tasks = []
    for s in enabled:
        domain, name = schema_domain_name(s)
        argv = _build_argv(s, domain, name, spec)
        tasks.append((args.generator, s, domain, name, argv, spec))

    failed = 0
    if spec.parallel and len(tasks) > 1:
        # Sjå GeneratorSpec.parallel — per-skjema-arbeidet er CPU-bunde og
        # uavhengig på tvers av skjema (ingen deler mutable tilstand), så
        # det skalerer over fleire kjernar via eit ProcessPoolExecutor i
        # staden for éin sekvensiell, éin-tråda lykke. Talet på workers er
        # avgrensa (standard 6) sidan kvar ekstra worker har eiga
        # fork-/schedulerings-kostnad — venta nær metningspunktet gjeve dei
        # målte per-skjema-tidene (sjå specs/done/paralleliser-fase-a-test-make.md,
        # Del 2). pool.map() bevarer rekkjefølgja frå `tasks` i resultat-
        # straumen (uavhengig av fullføringsrekkjefølgje), så loggutskrifta
        # under held seg til same, føreseielege skjema-rekkjefølgje som den
        # sekvensielle stien.
        max_workers = min(len(tasks), int(os.environ.get("BATCH_GENERATE_WORKERS", "6")))
        with ProcessPoolExecutor(max_workers=max_workers) as pool:
            for s, ok, message in pool.map(_generate_one, tasks):
                if ok:
                    log_info(message)
                else:
                    log_error(message)
                    failed += 1
    else:
        for task in tasks:
            s, ok, message = _generate_one(task)
            if ok:
                log_info(message)
            else:
                log_error(message)
                failed += 1

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
