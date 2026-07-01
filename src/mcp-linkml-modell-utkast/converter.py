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

def _deep_merge(base: dict, override: dict) -> dict:
    """Slår saman to dicts; override-verdiar vinn. Nøsta dicts vert slått saman rekursivt."""
    result = dict(base)
    for k, v in override.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = _deep_merge(result[k], v)
        else:
            result[k] = v
    return result


def load_profile(name: str) -> dict:
    """Lastar ein namngitt profil frå profiles/-katalogen. Handterer 'extends:'-arv."""
    profile_dir = Path(__file__).parent / "profiles"
    with open(profile_dir / f"{name}.yaml", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    parent_name = data.pop("extends", None)
    if parent_name:
        parent = load_profile(parent_name)
        data = _deep_merge(parent, data)
    return data


# ---------------------------------------------------------------------------
# Interne hjelpefunksjonar
# ---------------------------------------------------------------------------

def _to_plural(name: str, suffix: str = "er") -> str:
    """Lagar container-slot-namn: lowercase første bokstav + suffiks.

    Bindestrekar vert erstatta med understrek for å gje gyldige attributtnamn.
    Døme (suffix='er'): 'Person' → 'personers', 'Ting' → 'tinger'.
    Dette er ein enkel heuristikk som gjev akseptable utkast-namn.
    """
    if not name:
        return name
    safe = name.replace("-", "_")
    return safe[0].lower() + safe[1:] + suffix


def _transliterate(name: str) -> str:
    """Translittererer særnorske bokstavar til ASCII (æ→ae, ø→oe, å→aa)."""
    return (
        name
        .replace("æ", "ae").replace("Æ", "Ae")
        .replace("ø", "oe").replace("Ø", "Oe")
        .replace("å", "aa").replace("Å", "Aa")
    )


def _sanitize_slot_name(name: str) -> str:
    """Gjer slotnamnet til ein gyldig identifikator: erstatter - med _."""
    return name.replace("-", "_")


def _sanitize_identifier(name: str) -> str:
    """Gjer eit $defs-nøkkelnamn til ein gyldig LinkML/Python-identifikator.

    Translittererer særnorske bokstavar og erstattar bindestrek med understrek.
    Døme: 'E-postadresse' → 'E_postadresse'
    """
    return _transliterate(name).replace("-", "_")


def _to_pascal_case(name: str) -> str:
    """Konverterer kebab-case/snake_case til PascalCase.

    t.d. 'bvr-innfelles' → 'BvrInnfelles', 'generated' → 'Generated'
    """
    parts = name.replace("_", "-").split("-")
    return "".join(p.capitalize() for p in parts if p)


def _resolve_ref(ref: str) -> str:
    """Hentar klassenamnet frå ein lokal JSON Schema $ref.

    '#/$defs/Foo' → 'Foo', '#/$defs/E-postadresse' → 'E_postadresse'
    """
    return _sanitize_identifier(ref.split("/")[-1])


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


_FORMAT_TO_XSD: dict[str, tuple[str, str]] = {
    "date":      ("xsd:date",     "str"),
    "date-time": ("xsd:dateTime", "str"),
    "uri":       ("xsd:anyURI",   "str"),
    "time":      ("xsd:time",     "str"),
}

_JSON_TYPE_TO_XSD: dict[str, tuple[str, str]] = {
    "string":  ("xsd:string",  "str"),
    "integer": ("xsd:integer", "int"),
    "number":  ("xsd:float",   "float"),
}


def _collect_types(json_schema: dict) -> dict:
    """Samlar primitive $defs frå JSON Schema som LinkML types:.

    Ein def vert behandla som type viss:
    - type er 'string', 'integer' eller 'number'
    - ingen 'properties' (ville gjort han til ein klasse)
    - ingen 'enum' (vil verte handtert som LinkML enum av Tiltak 2)
    """
    types_out: dict = {}

    for defs_key in ("$defs", "definitions"):
        for name, defn in (json_schema.get(defs_key) or {}).items():
            json_type = defn.get("type", "")
            if "properties" in defn or "enum" in defn:
                continue
            if json_type not in _JSON_TYPE_TO_XSD:
                continue

            fmt = defn.get("format")
            uri, base = _FORMAT_TO_XSD.get(fmt, _JSON_TYPE_TO_XSD[json_type]) if fmt else _JSON_TYPE_TO_XSD[json_type]

            type_entry: dict = {"uri": uri, "base": base}
            type_entry["description"] = defn.get("description") or "TODO: beskriv typen"
            if pattern := defn.get("pattern"):
                type_entry["pattern"] = pattern

            types_out[_sanitize_identifier(name)] = type_entry

    return types_out


def _collect_enums(json_schema: dict) -> dict:
    """Samlar $defs med enum-liste frå JSON Schema som LinkML enums:.

    Ein def vert behandla som enum viss han har ein 'enum'-nøkkel,
    uavhengig av om 'type' er sett.
    """
    enums_out: dict = {}

    for defs_key in ("$defs", "definitions"):
        for name, defn in (json_schema.get(defs_key) or {}).items():
            enum_values = defn.get("enum")
            if not enum_values:
                continue

            enum_entry: dict = {}
            enum_entry["description"] = defn.get("description") or "TODO: beskriv enumet"
            enum_entry["permissible_values"] = {str(v): {} for v in enum_values}

            enums_out[_sanitize_identifier(name)] = enum_entry

    return enums_out


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
                classes[_sanitize_identifier(name)] = {
                    "properties": dict(defn.get("properties") or {}),
                    "required":   set(defn.get("required") or []),
                    "description": defn.get("description") or "",
                }

    if not classes and ("properties" in json_schema or json_schema.get("type") == "object"):
        classes[_sanitize_identifier(schema_name)] = {
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
    schema_uri  = schema_id.rstrip("/") + "/"
    prefix_name = schema_id.rstrip("/").split("/")[-1].replace("-", "_")
    prefixes: dict = {"linkml": std_prefixes.get("linkml", "https://w3id.org/linkml/")}
    prefixes[prefix_name] = schema_uri
    for k, v in std_prefixes.items():
        if k != "linkml":
            prefixes[k] = v

    # ── Skjema-topp ──────────────────────────────────────────────────────────
    schema: dict = {"id": schema_id, "name": schema_name}
    schema["title"] = schema_title or f"TODO: tittel for {schema_name}"
    schema["description"] = (
        json_schema.get("description")
        or f"Generert modell for '{schema_name}'."
    )
    schema["version"] = "0.1.0"
    schema["license"] = "https://creativecommons.org/licenses/by/4.0/"

    # ── Silver-annotasjonar frå profil ────────────────────────────────────────
    profile_annotations = profile.get("schema_annotations")
    if profile_annotations:
        schema["annotations"] = dict(profile_annotations)

    schema["prefixes"]       = prefixes
    schema["default_prefix"] = schema_uri  # absolutt HTTPS-URI med avsluttande /

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

    add_id              = gen.get("add_id_slot", True)
    add_begrep_annotation = gen.get("add_begrep_annotation", True)
    begrep_base_uri     = gen.get("begrep_base_uri", "https://concept-catalog.fellesdatakatalog.digdir.no/collections/TODO/concepts/")
    req_subset   = subsets_cfg.get("required_maps_to", "Obligatorisk")
    def_subset   = subsets_cfg.get("non_required_default", "Anbefalt")

    # ── Globale slots (med kollisjonsdeteksjon) ───────────────────────────────
    global_slots: dict = {}

    for cls_data in classes_data.values():
        for prop_name, prop_def in cls_data["properties"].items():
            if prop_name == "id":
                continue
            slot_name = _sanitize_slot_name(prop_name)
            attrs     = _resolve_type(prop_def, profile, warnings)
            new_range = attrs.get("range", "string")

            if slot_name in global_slots:
                existing_range = global_slots[slot_name].get("range", "string")
                existing_multivalued = global_slots[slot_name].get("multivalued", False)
                new_multivalued = attrs.get("multivalued", False)

                # Sjekk om range er ein primitiv LinkML-type eller ein klasse-referanse
                primitive_types = {"string", "integer", "float", "boolean", "uriorcurie", "date", "datetime"}
                existing_is_primitive = existing_range in primitive_types
                new_is_primitive = new_range in primitive_types

                if existing_range != new_range:
                    # Velg den mest spesifikke/informative definisjonen:
                    # 1. Prioriter multivalued (array) over single-value
                    # 2. Prioriter primitive typar over klasse-referansar (meir spesifikt)
                    should_replace = False
                    reason = ""

                    if new_multivalued and not existing_multivalued:
                        should_replace = True
                        reason = f"(multivalued)"
                    elif new_is_primitive and not existing_is_primitive:
                        should_replace = True
                        reason = f"(primitiv type)"
                    elif not new_is_primitive and existing_is_primitive:
                        # Behold primitiv type
                        should_replace = False

                    if should_replace:
                        warnings.append(
                            f"Slot '{slot_name}' har ulik type i fleire klasser "
                            f"('{existing_range}' vs '{new_range}' {reason}) — bruker '{new_range}' {reason}"
                        )
                        slot_entry: dict = {}
                        slot_entry["description"] = prop_def.get("description") or "TODO: beskriv eigenskapen"
                        slot_entry["slot_uri"] = f"{prefix_name}:{_transliterate(slot_name)}"
                        if new_range:
                            slot_entry["range"] = new_range
                        if new_multivalued:
                            slot_entry["multivalued"] = True
                        global_slots[slot_name] = slot_entry
                    else:
                        # Behold eksisterande definisjon
                        warnings.append(
                            f"Slot '{slot_name}' har ulik type i fleire klasser "
                            f"('{existing_range}' vs '{new_range}') — bruker '{existing_range}'"
                        )
            else:
                slot_entry: dict = {}
                slot_entry["description"] = prop_def.get("description") or "TODO: beskriv eigenskapen"
                slot_entry["slot_uri"] = f"{prefix_name}:{_transliterate(slot_name)}"
                if new_range:
                    slot_entry["range"] = new_range
                if attrs.get("multivalued"):
                    slot_entry["multivalued"] = True
                global_slots[slot_name] = slot_entry

    # ── Bygg klasse-oppføringane ──────────────────────────────────────────────
    classes_out: dict = {}

    for cls_name, cls_data in classes_data.items():
        props    = cls_data["properties"]
        required = cls_data["required"]
        desc     = cls_data["description"]

        entry: dict = {}
        entry["description"] = desc or "TODO: beskriv klassen"
        entry["class_uri"] = f"{prefix_name}:{_transliterate(cls_name)}"
        if add_begrep_annotation:
            entry["annotations"] = {"begrepsidentifikator": f"{begrep_base_uri}TODO"}

        slot_names = (["id"] if add_id else []) + [_sanitize_slot_name(n) for n in props if n != "id"]
        if slot_names:
            entry["slots"] = slot_names

        slot_usage: dict = {}
        for prop_name in props:
            if prop_name == "id":
                continue
            slot_name = _sanitize_slot_name(prop_name)
            su: dict = {}
            if prop_name in required:
                su["required"]   = True
                su["in_subset"]  = [req_subset]
            else:
                su["in_subset"]  = [def_subset]
            slot_usage[slot_name] = su
        if slot_usage:
            entry["slot_usage"] = slot_usage

        classes_out[cls_name] = entry

    # ── Containerklasse ───────────────────────────────────────────────────────
    add_container  = gen.get("add_container_class", True)
    container_name = gen.get("container_class_name") or f"{_to_pascal_case(schema_name)}Container"
    suffix         = gen.get("container_slot_suffix", "er")

    if add_container and classes_data:
        attrs_dict: dict = {}
        for cls_name in classes_data:
            slot_key = _to_plural(cls_name, suffix)
            attrs_dict[slot_key] = {
                "description":    "TODO: beskriv eigenskapen",
                "range":          cls_name,
                "multivalued":    True,
                "inlined":        True,
                "inlined_as_list": True,
            }
        classes_out[container_name] = {
            "description": "TODO: beskriv containerklassen",
            "tree_root":   True,
            "attributes":  attrs_dict,
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

    # ── Typar og enums (primitive $defs) ─────────────────────────────────────
    types_out = _collect_types(json_schema)
    enums_out = _collect_enums(json_schema)

    # ── Samle alt og serialiser ───────────────────────────────────────────────
    if types_out:
        schema["types"] = types_out
    if enums_out:
        schema["enums"] = enums_out
    schema["classes"] = classes_out
    schema["slots"]   = slots_out

    yaml_str = yaml.dump(
        schema,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    )

    header = (
        "# Generert av mcp-linkml-generator — dette er eit utkast.\n"
        f"# Prefiks '{prefix_name}:' er ein placeholder — erstatt med ekte vokabular-URIar.\n"
        "# 'TODO'-felt må fyllast inn manuelt.\n\n"
    )
    return header + yaml_str, warnings
