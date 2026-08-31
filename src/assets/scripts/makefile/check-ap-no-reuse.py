#!/usr/bin/env python3
"""
Sjekk gjenbruk av common-ap-no-schema (Digdir-regel 14: Gjenbruk).

To sjekkar, begge baserte på LinkML sitt eige `imports:`-felt (rå YAML,
ingen SchemaView/LinkML-runtime nødvendig):

1. Alle skjema under `ap-no/*` (unnateke common-ap-no-schema sjølv) skal
   importere common-ap-no-schema, direkte eller transitivt — jf. PRINCIPLES.md
   § 3 og CLAUDE.md: AP-NO-profilane skal importere common-ap-no-schema.
2. Skjema UTANFOR `ap-no/*` skal ikkje importere common-ap-no-schema
   DIREKTE — dei skal importere ein AP-NO-profil (t.d. dcat-ap-no-schema)
   i staden, som igjen importerer common-ap-no-schema. Direkte import forbi
   profilane bryt pull/lenking-prinsippet i PRINCIPLES.md § 3.

Rapporterer berre avvik (jf. specs/backlog/utvid-dekningsgrad-regel-5-12-14-15.md,
«Avklaringar» punkt 3) — skjema som alt følgjer mønsteret, vert ikkje lista.

Ingen eksterne avhengigheiter utover pyyaml.

Bruk:
    python3 check-ap-no-reuse.py
"""

import sys
from pathlib import Path

import yaml

SCHEMA_DIR = Path("src/linkml")
COMMON_AP_NO_KEY = "ap-no/common-ap-no"


def discover_schemas() -> list[Path]:
    return sorted(SCHEMA_DIR.glob("*/*/*-schema.yaml"))


def schema_key(path: Path) -> str:
    """'domain/model' — same nøkkelform som discover_schemas() sitt glob-mønster."""
    parts = path.relative_to(SCHEMA_DIR).parts
    return f"{parts[0]}/{parts[1]}"


def normalize_import(raw: str, schema_dir: Path) -> str | None:
    """Normaliser eitt imports:-element til ein 'domain/model'-nøkkel, eller
    None for linkml:types og andre ikkje-domeneskjema-importar."""
    raw = raw.strip()
    if raw.startswith("linkml:"):
        return None
    if raw.startswith("http://") or raw.startswith("https://"):
        # Versjonslåst import via raw.githubusercontent.com — trekk ut stien
        # etter src/linkml/ (sjå t.d. enhetsregisteret-*-schema.yaml).
        marker = "/src/linkml/"
        idx = raw.find(marker)
        if idx == -1:
            return None
        parts = raw[idx + len(marker):].split("/")
        return f"{parts[0]}/{parts[1]}" if len(parts) >= 2 else None
    resolved = (schema_dir / raw).resolve()
    try:
        rel = resolved.relative_to(SCHEMA_DIR.resolve())
    except ValueError:
        return None
    parts = rel.parts
    return f"{parts[0]}/{parts[1]}" if len(parts) >= 2 else None


def load_direct_imports(path: Path) -> list[str]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        print(f"ÅTVARING: kunne ikkje parse {path}: {e}", file=sys.stderr)
        return []
    raw_imports = data.get("imports") or []
    normalized = (normalize_import(imp, path.parent) for imp in raw_imports)
    return sorted({n for n in normalized if n})


def build_import_graph(schemas: list[Path]) -> dict[str, set[str]]:
    graph: dict[str, set[str]] = {}
    for path in schemas:
        graph[schema_key(path)] = set(load_direct_imports(path))
    return graph


def transitive_closure(key: str, graph: dict[str, set[str]]) -> set[str]:
    visited: set[str] = set()
    queue = list(graph.get(key, ()))
    while queue:
        current = queue.pop()
        if current in visited:
            continue
        visited.add(current)
        queue.extend(graph.get(current, ()))
    return visited


def find_missing_common_ap_no(graph: dict[str, set[str]]) -> list[str]:
    missing = []
    for key in sorted(graph):
        if not key.startswith("ap-no/") or key == COMMON_AP_NO_KEY:
            continue
        if COMMON_AP_NO_KEY not in transitive_closure(key, graph):
            missing.append(key)
    return missing


def find_direct_import_outside_ap_no(graph: dict[str, set[str]]) -> list[str]:
    drift = []
    for key in sorted(graph):
        if key.startswith("ap-no/"):
            continue
        if COMMON_AP_NO_KEY in graph.get(key, ()):
            drift.append(key)
    return drift


def build_report(missing: list[str], drift: list[str], total_schemas: int) -> str:
    lines = ["# Gjenbruk av common-ap-no-schema (Digdir-regel 14)", ""]
    total_avvik = len(missing) + len(drift)
    if total_avvik:
        lines.append(f"**Totalt: {total_avvik} avvik funne av {total_schemas} skjema sjekka.**")
    else:
        lines.append(f"Ingen avvik over dei to sjekkane vart funne ({total_schemas} skjema sjekka).")
    lines.append("")

    lines.append("## AP-NO-skjema som ikkje importerer common-ap-no-schema")
    lines.append("")
    if missing:
        lines.append("| Skjema |")
        lines.append("|---|")
        for key in missing:
            lines.append(f"| `{key}` |")
    else:
        lines.append(
            "Ingen avvik funne — alle ap-no/*-skjema (unnateke common-ap-no sjølv) "
            "importerer common-ap-no-schema, direkte eller transitivt."
        )
    lines.append("")

    lines.append("## Skjema utanfor ap-no/* som importerer common-ap-no-schema direkte")
    lines.append("")
    if drift:
        lines.append(
            "Desse bør importere ein AP-NO-profil (t.d. dcat-ap-no-schema) i staden "
            "for å importere common-ap-no-schema direkte (PRINCIPLES.md § 3):"
        )
        lines.append("")
        lines.append("| Skjema |")
        lines.append("|---|")
        for key in drift:
            lines.append(f"| `{key}` |")
    else:
        lines.append(
            "Ingen avvik funne — ingen skjema utanfor ap-no/* importerer "
            "common-ap-no-schema direkte."
        )
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    schemas = discover_schemas()
    graph = build_import_graph(schemas)
    missing = find_missing_common_ap_no(graph)
    drift = find_direct_import_outside_ap_no(graph)
    total_schemas = len(graph) - (1 if COMMON_AP_NO_KEY in graph else 0)
    print(build_report(missing, drift, total_schemas))


if __name__ == "__main__":
    main()
