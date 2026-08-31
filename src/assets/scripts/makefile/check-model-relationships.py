#!/usr/bin/env python3
"""
Sjekk samanhengar mellom modellar (Digdir-regel 12: Sammenhenger mellom modeller).

Kryssrefererer to uavhengige kjelder:

1. **Strukturell importgraf** — LinkML sitt eige `imports:`-felt per skjema
   under `src/linkml/*/*/*-schema.yaml` (rå YAML, same tilnærming som
   check-ap-no-reuse.py).
2. **Dokumentert katalogrelasjon** — `Informasjonsmodell`-instansar i
   modellkatalog-datafilene (`src/linkml/modellkatalog/*/data/*/*.yaml`),
   som kan populere `har_del`, `er_i_samsvar_med`, `er_profil_av`,
   `erstatter` og `er_erstattet_av` (definerte i modelldcat-katalog-schema.yaml).

To sjekkar:

A) Eit skjema som strukturelt importerer eit anna domeneskjema, men der
   den tilhøyrande Informasjonsmodell-instansen (om ho finst i ein katalog)
   ikkje har nokon har_del/er_i_samsvar_med/er_profil_av-verdi som peikar
   mot det importerte skjemaet — eit dokumentasjonsgap mellom kode og katalog.
B) erstatter/er_erstattet_av-par som ikkje er gjensidige.

Rapporterer berre avvik (jf. specs/backlog/utvid-dekningsgrad-regel-5-12-14-15.md,
«Avklaringar» punkt 3).

Ingen eksterne avhengigheiter utover pyyaml.

Bruk:
    python3 check-model-relationships.py
"""

import sys
from pathlib import Path

import yaml

SCHEMA_DIR = Path("src/linkml")
MODELLKATALOG_DIR = SCHEMA_DIR / "modellkatalog"
RELATIONSHIP_FIELDS = ("har_del", "er_i_samsvar_med", "er_profil_av")


def discover_schemas() -> list[Path]:
    return sorted(SCHEMA_DIR.glob("*/*/*-schema.yaml"))


def schema_key(path: Path) -> str:
    parts = path.relative_to(SCHEMA_DIR).parts
    return f"{parts[0]}/{parts[1]}"


def model_name(key: str) -> str:
    return key.split("/", 1)[1]


def normalize_import(raw: str, schema_dir: Path) -> str | None:
    raw = raw.strip()
    if raw.startswith("linkml:"):
        return None
    if raw.startswith("http://") or raw.startswith("https://"):
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


def load_direct_imports(path: Path) -> set[str]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        print(f"ÅTVARING: kunne ikkje parse {path}: {e}", file=sys.stderr)
        return set()
    raw_imports = data.get("imports") or []
    normalized = (normalize_import(imp, path.parent) for imp in raw_imports)
    return {n for n in normalized if n}


def build_import_graph(schemas: list[Path]) -> dict[str, set[str]]:
    return {schema_key(p): load_direct_imports(p) for p in schemas}


def url_slug(url: str) -> str:
    """Siste sti-segment av ein modellkatalog-URI — brukt til å matche
    Informasjonsmodell-instansar mot skjema-modellnavn."""
    return str(url).rstrip("/").rsplit("/", 1)[-1]


def as_list(value) -> list:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def discover_modellkatalog_files() -> list[Path]:
    if not MODELLKATALOG_DIR.is_dir():
        return []
    return sorted(MODELLKATALOG_DIR.glob("*/data/*/*.yaml"))


def load_informasjonsmodeller(files: list[Path]) -> dict[str, dict]:
    """Nøkkel: modellnavn-slug (siste sti-segment av id). Verdi: rådata for
    Informasjonsmodell-instansen, pluss kva fil ho vart funnen i."""
    result: dict[str, dict] = {}
    for path in files:
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as e:
            print(f"ÅTVARING: kunne ikkje parse {path}: {e}", file=sys.stderr)
            continue
        for entry in data.get("informasjonsmodeller") or []:
            entry_id = entry.get("id")
            if not entry_id:
                continue
            slug = url_slug(entry_id)
            result[slug] = {**entry, "_source": path}
    return result


def find_undocumented_dependencies(
    graph: dict[str, set[str]], informasjonsmodeller: dict[str, dict]
) -> list[tuple[str, str]]:
    """(importerande skjema, importert skjema) der importen ikkje er
    dokumentert via har_del/er_i_samsvar_med/er_profil_av på den
    importerande sida sin Informasjonsmodell-instans."""
    gaps = []
    for key, imports in sorted(graph.items()):
        own_name = model_name(key)
        own_entry = informasjonsmodeller.get(own_name)
        if own_entry is None:
            continue  # skjemaet er ikkje katalogisert enno — utanfor scope
        documented_targets = set()
        for field in RELATIONSHIP_FIELDS:
            for target in as_list(own_entry.get(field)):
                documented_targets.add(url_slug(target))
        for imported_key in sorted(imports):
            imported_name = model_name(imported_key)
            if imported_name not in informasjonsmodeller:
                continue  # målet er heller ikkje katalogisert — utanfor scope
            if imported_name not in documented_targets:
                gaps.append((key, imported_key))
    return gaps


def find_asymmetric_erstatter(informasjonsmodeller: dict[str, dict]) -> list[tuple[str, str]]:
    """(A, B) der A seier erstatter: B, men B manglar er_erstattet_av: A."""
    asymmetric = []
    for name, entry in sorted(informasjonsmodeller.items()):
        for target in as_list(entry.get("erstatter")):
            target_slug = url_slug(target)
            target_entry = informasjonsmodeller.get(target_slug)
            if target_entry is None:
                continue
            er_erstattet_av = {url_slug(v) for v in as_list(target_entry.get("er_erstattet_av"))}
            if name not in er_erstattet_av:
                asymmetric.append((name, target_slug))
    return asymmetric


def count_considered_dependencies(
    graph: dict[str, set[str]], informasjonsmodeller: dict[str, dict]
) -> int:
    """Talet på (importerande, importert)-par der begge sider er
    katalogiserte — nemnaren for udokumenterte-avhengigheiter-sjekken."""
    total = 0
    for key, imports in graph.items():
        if model_name(key) not in informasjonsmodeller:
            continue
        for imported_key in imports:
            if model_name(imported_key) in informasjonsmodeller:
                total += 1
    return total


def count_erstatter_pairs(informasjonsmodeller: dict[str, dict]) -> int:
    total = 0
    for entry in informasjonsmodeller.values():
        for target in as_list(entry.get("erstatter")):
            if url_slug(target) in informasjonsmodeller:
                total += 1
    return total


def build_report(
    gaps: list[tuple[str, str]], asymmetric: list[tuple[str, str]], total_checked: int
) -> str:
    lines = ["# Samanhengar mellom modellar (Digdir-regel 12)", ""]
    total_avvik = len(gaps) + len(asymmetric)
    if total_avvik:
        lines.append(f"**Totalt: {total_avvik} avvik funne av {total_checked} avhengigheiter sjekka.**")
    else:
        lines.append(f"Ingen avvik over dei to sjekkane vart funne ({total_checked} avhengigheiter sjekka).")
    lines.append("")

    lines.append("## Udokumenterte strukturelle avhengigheiter")
    lines.append("")
    if gaps:
        lines.append(
            "Skjema som importerer eit anna domeneskjema strukturelt, men der "
            "Informasjonsmodell-instansen manglar har_del/er_i_samsvar_med/"
            "er_profil_av som peikar mot det:"
        )
        lines.append("")
        lines.append("| Importerande skjema | Importert skjema (udokumentert) |")
        lines.append("|---|---|")
        for key, imported_key in gaps:
            lines.append(f"| `{key}` | `{imported_key}` |")
    else:
        lines.append(
            "Ingen avvik funne — alle katalogiserte skjema med strukturelle "
            "avhengigheiter til andre katalogiserte skjema dokumenterer det."
        )
    lines.append("")

    lines.append("## Asymmetriske erstatter/er_erstattet_av-par")
    lines.append("")
    if asymmetric:
        lines.append("| A (erstatter B) | B (manglar er_erstattet_av: A) |")
        lines.append("|---|---|")
        for a, b in asymmetric:
            lines.append(f"| `{a}` | `{b}` |")
    else:
        lines.append("Ingen avvik funne.")
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    schemas = discover_schemas()
    graph = build_import_graph(schemas)
    katalog_files = discover_modellkatalog_files()
    informasjonsmodeller = load_informasjonsmodeller(katalog_files)
    gaps = find_undocumented_dependencies(graph, informasjonsmodeller)
    asymmetric = find_asymmetric_erstatter(informasjonsmodeller)
    total_checked = count_considered_dependencies(graph, informasjonsmodeller) \
        + count_erstatter_pairs(informasjonsmodeller)
    print(build_report(gaps, asymmetric, total_checked))


if __name__ == "__main__":
    main()
