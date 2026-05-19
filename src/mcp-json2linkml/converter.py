#!/usr/bin/env python3
"""JSON Schema → LinkML-konvertering.

Offentleg API:
  load_profile(name)                          → dict
  convert(json_schema, profile, ...)          → (yaml_str, warnings)
"""

import yaml
from pathlib import Path


# ---------------------------------------------------------------------------
# Profil
# ---------------------------------------------------------------------------

def load_profile(name: str) -> dict:
    """Lastar ein namngitt profil frå profiles/-katalogen."""
    profile_dir = Path(__file__).parent / "profiles"
    with open(profile_dir / f"{name}.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


# ---------------------------------------------------------------------------
# Interne hjelpefunksjonar
# ---------------------------------------------------------------------------

def _to_plural(name: str, suffix: str = "er") -> str:
    """Lagar container-slot-namn: lowercase første bokstav + suffiks.

    Døme (suffix='er'): 'Person' → 'personers', 'Ting' → 'tinger'.
    Dette er ein enkel heuristikk som gjev akseptable utkast-namn.
    """
    if not name:
        return name
    return name[0].lower() + name[1:] + suffix


def _resolve_ref(ref: str) -> str:
    """Hentar klassenamnet frå ein lokal JSON Schema $ref.

    '#/$defs/Foo' → 'Foo'
    """
    return ref.split("/")[-1]


def _resolve_type(prop: dict, profile: dict, warnings: list) -> dict:
    """Omset ein JSON Schema-eigeskap til LinkML slot-attributtar.

    Returnerer ein dict med t.d. {'range': 'string', 'multivalued': True}.
    """
    type_map = profile.get("type_mapping") or {}
    fmt_map  = profile.get("format_mapping") or {}

    # anyOf: nullable-mønster — filtrer bort null-typen
    if "anyOf" in prop:
        non_null = [s for s in prop["anyOf"] if s.get("type") != "null"]
        if len(non_null) == 1:
            return _resolve_type(non_null[0], profile, warnings)
        if len(non_null) > 1:
            warnings.append(
                "anyOf med fleire ikkje-null-typar er ikkje støtta — bruker range: string"
            )
        return {"range": "string"}

    # oneOf / allOf — ikkje støtta i v1
    for kw in ("oneOf", "allOf"):
        if kw in prop:
            warnings.append(f"{kw} er ikkje støtta i v1 — bruker range: string")
            return {"range": "string"}

    # $ref
    if "$ref" in prop:
        ref = prop["$ref"]
        if not ref.startswith("#"):
            warnings.append(f"Ekstern $ref '{ref}' er ikkje støtta — bruker range: string")
            return {"range": "string"}
        return {"range": _resolve_ref(ref)}

    # array
    if prop.get("type") == "array":
        result: dict = {"multivalued": True}
        items = prop.get("items") or {}
        if items:
            result.update(_resolve_type(items, profile, warnings))
        return result

    # null — ingen range
    if prop.get("type") == "null":
        return {}

    # format overrider type
    fmt = prop.get("format")
    if fmt and fmt in fmt_map:
        return {"range": fmt_map[fmt]}

    # grunntype
    json_type = prop.get("type", "string")
    return {"range": type_map.get(json_type, "string")}


def _collect_classes(json_schema: dict, schema_name: str) -> dict:
    """Samlar klassedefinisjonar frå JSON Schema.

    Returnerer:
      { klassnamn: {"properties": {...}, "required": set, "description": str} }

    Strategi:
    - Les frå '$defs' / 'definitions' — berre object-definisjonar
    - Om ingen $defs finst: bruk rot-properties som éin klasse kalla schema_name
    """
    classes: dict = {}

    for defs_key in ("$defs", "definitions"):
        for name, defn in (json_schema.get(defs_key) or {}).items():
            if defn.get("type") == "object" or "properties" in defn:
                classes[name] = {
                    "properties": dict(defn.get("properties") or {}),
                    "required":   set(defn.get("required") or []),
                    "description": defn.get("description") or "",
                }

    if not classes and ("properties" in json_schema or json_schema.get("type") == "object"):
        classes[schema_name] = {
            "properties": dict(json_schema.get("properties") or {}),
            "required":   set(json_schema.get("required") or []),
            "description": json_schema.get("description") or "",
        }

    return classes


# ---------------------------------------------------------------------------
# Hovudfunksjon
# ---------------------------------------------------------------------------

def convert(
    json_schema: dict,
    profile: dict,
    schema_id: str,
    schema_name: str,
    schema_title: str = "",
) -> tuple[str, list[str]]:
    """Konverterer eit JSON Schema til eit LinkML-skjema (YAML-streng).

    Returnerer (linkml_yaml_str, warnings).
    """
    warnings: list[str] = []
    gen         = profile.get("generation") or {}
    subsets_cfg = profile.get("subsets") or {}
    std_prefixes = profile.get("standard_prefixes") or {}

    # ── Prefiks ──────────────────────────────────────────────────────────────
    ex_uri = schema_id.rstrip("/") + "/"
    prefixes: dict = {"linkml": std_prefixes.get("linkml", "https://w3id.org/linkml/")}
    prefixes["ex"] = ex_uri
    for k, v in std_prefixes.items():
        if k != "linkml":
            prefixes[k] = v

    # ── Skjema-topp ──────────────────────────────────────────────────────────
    schema: dict = {"id": schema_id, "name": schema_name}
    if schema_title:
        schema["title"] = schema_title
    schema["description"] = (
        json_schema.get("description")
        or f"Generert frå JSON Schema '{schema_name}'."
    )
    schema["prefixes"]      = prefixes
    schema["default_prefix"] = "ex"

    defaults = profile.get("schema_defaults") or {}
    schema["default_range"] = defaults.get("default_range", "string")
    schema["imports"]       = list(defaults.get("imports") or ["linkml:types"])

    # ── Subsets ──────────────────────────────────────────────────────────────
    schema["subsets"] = {
        "Obligatorisk": {"description": "Obligatoriske eigenskapar."},
        "Anbefalt":     {"description": "Anbefalte eigenskapar."},
        "Valgfri":      {"description": "Valfrie eigenskapar."},
    }

    # ── Samle klasseinformasjon ───────────────────────────────────────────────
    classes_data = _collect_classes(json_schema, schema_name)

    add_id       = gen.get("add_id_slot", True)
    add_see_also = gen.get("add_see_also_stub", True)
    see_also_base = gen.get("see_also_base_uri", "https://data.norge.no/concepts/")
    req_subset   = subsets_cfg.get("required_maps_to", "Obligatorisk")
    def_subset   = subsets_cfg.get("non_required_default", "Anbefalt")

    # ── Globale slots (med kollisjonsdeteksjon) ───────────────────────────────
    global_slots: dict = {}

    for cls_data in classes_data.values():
        for prop_name, prop_def in cls_data["properties"].items():
            if prop_name == "id":
                continue
            attrs    = _resolve_type(prop_def, profile, warnings)
            new_range = attrs.get("range", "string")

            if prop_name in global_slots:
                existing_range = global_slots[prop_name].get("range", "string")
                if existing_range != new_range:
                    warnings.append(
                        f"Slot '{prop_name}' har ulik type i fleire klasser "
                        f"('{existing_range}' vs '{new_range}') — bruker '{existing_range}'"
                    )
            else:
                slot_entry: dict = {}
                desc = prop_def.get("description") or ""
                if desc:
                    slot_entry["description"] = desc
                slot_entry["slot_uri"] = f"ex:{prop_name}"
                if new_range:
                    slot_entry["range"] = new_range
                if attrs.get("multivalued"):
                    slot_entry["multivalued"] = True
                global_slots[prop_name] = slot_entry

    # ── Bygg klasse-oppføringane ──────────────────────────────────────────────
    classes_out: dict = {}

    for cls_name, cls_data in classes_data.items():
        props    = cls_data["properties"]
        required = cls_data["required"]
        desc     = cls_data["description"]

        entry: dict = {}
        if desc:
            entry["description"] = desc
        entry["class_uri"] = f"ex:{cls_name}"
        if add_see_also:
            entry["see_also"] = [f"{see_also_base}TODO"]

        slot_names = (["id"] if add_id else []) + [n for n in props if n != "id"]
        if slot_names:
            entry["slots"] = slot_names

        slot_usage: dict = {}
        for prop_name in props:
            if prop_name == "id":
                continue
            su: dict = {}
            if prop_name in required:
                su["required"]   = True
                su["in_subset"]  = [req_subset]
            else:
                su["in_subset"]  = [def_subset]
            slot_usage[prop_name] = su
        if slot_usage:
            entry["slot_usage"] = slot_usage

        classes_out[cls_name] = entry

    # ── Containerklasse ───────────────────────────────────────────────────────
    add_container  = gen.get("add_container_class", True)
    container_name = gen.get("container_class_name", "Containerklasse")
    suffix         = gen.get("container_slot_suffix", "er")

    if add_container and classes_data:
        attrs_dict: dict = {}
        for cls_name in classes_data:
            slot_key = _to_plural(cls_name, suffix)
            attrs_dict[slot_key] = {
                "range":          cls_name,
                "multivalued":    True,
                "inlined":        True,
                "inlined_as_list": True,
            }
        classes_out[container_name] = {
            "tree_root":  True,
            "attributes": attrs_dict,
        }

    # ── Slots-seksjon ─────────────────────────────────────────────────────────
    slots_out: dict = {}
    if add_id:
        slots_out["id"] = {
            "description": "Unik URI-identifikator for ressursen.",
            "identifier":  True,
            "range":       "uriorcurie",
        }
    slots_out.update(global_slots)

    # ── Samle alt og serialiser ───────────────────────────────────────────────
    schema["classes"] = classes_out
    schema["slots"]   = slots_out

    yaml_str = yaml.dump(
        schema,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    )

    header = (
        "# Generert av mcp-json2linkml — dette er eit utkast.\n"
        "# Prefiks 'ex:' er ein placeholder — erstatt med ekte vokabular-URIar.\n"
        "# 'see_also: TODO' må erstattast med reelle begrepsreferansar.\n\n"
    )
    return header + yaml_str, warnings
