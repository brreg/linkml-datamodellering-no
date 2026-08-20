#!/usr/bin/env python3
"""MCP-server for LinkML-skjemavalidering med konfigurerbar policy."""

import json
import re
import sys
import tempfile
import yaml
from pathlib import Path

# Heile repoet er montert read-only på /repo (sjå flatten-and-validate.bash),
# så det delte patch-modulet er tilgjengeleg utan å byggje det inn i imaget.
# Sjå src/assets/scripts/utils/linkml_relative_import_patch.py for grunngjeving.
sys.path.insert(0, "/repo/src/assets/scripts/utils")
try:
    import linkml_relative_import_patch
    linkml_relative_import_patch.apply()
except ImportError:
    sys.stderr.write(
        "ÅTVARING: fann ikkje linkml_relative_import_patch (/repo ikkje montert?) — "
        "versjonslåste importar med fleire nivå relative importar kan feile.\n"
    )


# ---------------------------------------------------------------------------
# Hjelpefunksjonar
# ---------------------------------------------------------------------------

def issue(severity: str, code: str, target: str, message: str) -> dict:
    return {"severity": severity, "code": code, "target": target, "message": message}


_POLICY_DIR = Path(__file__).parent / "policies"


def _merge_policies(parent: dict, child: dict) -> dict:
    merged = {}

    for key in ("version", "description"):
        val = child.get(key) or parent.get(key)
        if val is not None:
            merged[key] = val

    for key in ("required", "recommended"):
        merged[key] = {}
        for scope in ("schema", "class", "slot"):
            p = (parent.get(key) or {}).get(scope, [])
            c = (child.get(key) or {}).get(scope, [])
            merged[key][scope] = list(dict.fromkeys(p + c))

    p_must = (parent.get("common_classes") or {}).get("must_use", [])
    c_must = (child.get("common_classes") or {}).get("must_use", [])
    merged["common_classes"] = {"must_use": list(dict.fromkeys(p_must + c_must))}

    for key in ("checks", "fair_checks", "instance_checks"):
        p_checks = parent.get(key) or {}
        c_checks = child.get(key) or {}
        if p_checks or c_checks:
            merged[key] = {**p_checks, **c_checks}

    return merged


def load_policy(name: str = "bronze") -> dict:
    try:
        with open(_POLICY_DIR / f"{name}.yaml", encoding="utf-8") as f:
            policy = yaml.safe_load(f) or {}
    except FileNotFoundError:
        return {}

    parent_name = policy.get("extends")
    if parent_name:
        policy = _merge_policies(load_policy(parent_name), policy)

    return policy


def _is_base_policy(name: str) -> bool:
    """Returnerer True om policyen ikkje arvar frå ein annan (dvs. er rotpolicyen)."""
    try:
        with open(_POLICY_DIR / f"{name}.yaml", encoding="utf-8") as f:
            raw = yaml.safe_load(f) or {}
        return not bool(raw.get("extends"))
    except FileNotFoundError:
        return True


def send(obj: dict) -> None:
    sys.stdout.write(json.dumps(obj, ensure_ascii=False) + "\n")
    sys.stdout.flush()


# ---------------------------------------------------------------------------
# FAIR-sjekkar
# ---------------------------------------------------------------------------

def _all_slot_uris(schema) -> set:
    """Samlar alle slot_uri-verdiar frå globale slots og class-attributtar."""
    uris = set()
    for slot in (schema.slots or {}).values():
        if slot.slot_uri:
            uris.add(str(slot.slot_uri))
    for cls in (schema.classes or {}).values():
        for attr in (cls.attributes or {}).values():
            uri = getattr(attr, "slot_uri", None)
            if uri:
                uris.add(str(uri))
    return uris


def _fair_code(config: dict) -> str:
    p = config.get("principle")
    return ("fair_" + p.lower().replace(".", "")) if p else config.get("check", "check")


def _principle_prefix(config: dict) -> str:
    p = config.get("principle")
    return f"FAIR {p}: " if p else ""


def _check_schema_id_is_http_uri(sv, schema, config, issues):
    sid = str(schema.id or "")
    if not (sid.startswith("http://") or sid.startswith("https://")):
        issues.append(issue(
            config["severity"], _fair_code(config), "schema",
            f"{_principle_prefix(config)}schema.id er ikkje ein HTTP(S)-URI — persistent identifikator manglar",
        ))


def _check_schema_field_present(sv, schema, config, issues):
    field = config["field"]
    if not getattr(schema, field, None):
        issues.append(issue(
            config["severity"], _fair_code(config), "schema",
            f"{_principle_prefix(config)}schema.{field} manglar",
        ))


def _check_schema_has_annotation(sv, schema, config, issues):
    key = config["annotation"]
    allowed_values = config.get("allowed_values", [])
    value_pattern = config.get("value_pattern", "")
    ann = schema.annotations or {}
    raw = ann.get(key)
    value = str(raw.value if hasattr(raw, "value") else raw or "")
    code = f"schema_has_annotation_{key}"
    if not value:
        issues.append(issue(
            config["severity"], code, "schema",
            f"schema.annotations.{key} manglar",
        ))
        return
    if value_pattern and not re.match(value_pattern, value):
        issues.append(issue(
            config["severity"], code, "schema",
            f"schema.annotations.{key} '{value}' passar ikkje forventa format",
        ))
    elif allowed_values and value not in allowed_values:
        issues.append(issue(
            config["severity"], code, "schema",
            f"schema.annotations.{key} '{value}' er ikkje ein av: {', '.join(allowed_values)}",
        ))


def _check_default_prefix_is_https_uri(sv, schema, config, issues):
    dp = str(schema.default_prefix or "")
    if not (dp.startswith("https://") and dp.endswith("/")):
        issues.append(issue(
            config["severity"], "default_prefix_is_https_uri", "schema",
            f"schema.default_prefix '{dp}' er ikkje ein absolutt HTTPS-URI med avsluttande '/' "
            f"(t.d. https://data.norge.no/ngr/ngr-adresse/)",
        ))


def _check_class_names_pascal_case(sv, schema, config, issues):
    exclude = set(config.get("exclude_schemas", []))
    if (schema.name or "") in exclude:
        return
    for cname, cls in (schema.classes or {}).items():
        if cls.tree_root:
            continue
        if not cname[0].isupper():
            issues.append(issue(
                config["severity"], "class_names_pascal_case", f"class:{cname}",
                f"Klassenamn '{cname}' skal starte med stor forbokstav (PascalCase)",
            ))


def _check_slot_names_snake_case(sv, schema, config, issues):
    import re as _re
    exclude = set(config.get("exclude_schemas", []))
    if (schema.name or "") in exclude:
        return
    pattern = _re.compile(r'^[a-z][a-z0-9_]*$')
    for sname in (schema.slots or {}):
        if not pattern.match(sname):
            issues.append(issue(
                config["severity"], "slot_names_snake_case", f"slot:{sname}",
                f"Slotnamn '{sname}' er ikkje snake_case (berre a-z, 0-9, _)",
            ))


def _check_all_classes_have_class_uri(sv, schema, config, issues):
    for cname, cls in (schema.classes or {}).items():
        if cls.tree_root:
            continue
        if not cls.class_uri:
            issues.append(issue(
                config["severity"], _fair_code(config), f"class:{cname}",
                f"{_principle_prefix(config)}Klasse '{cname}' manglar class_uri (formal ressursbeskrivelse)",
            ))


def _check_all_slots_have_slot_uri(sv, schema, config, issues):
    for sname, slot in (schema.slots or {}).items():
        if not slot.slot_uri:
            issues.append(issue(
                config["severity"], _fair_code(config), f"slot:{sname}",
                f"{_principle_prefix(config)}Slot '{sname}' manglar slot_uri — formell RDF-semantikk er ikkje definert",
            ))


def _check_schema_declares_standard_prefix(sv, schema, config, issues):
    standard_prefixes = set(config.get("standard_prefixes", []))
    # sv.namespaces() slår berre saman prefiks frå schema_map, som ikkje er
    # fylt med importerte skjema før imports_closure() er kalla — utan dette
    # kallet ville sjekken berre sjå det lokale skjemaet sine eigne prefiks,
    # og feilaktig krevje at t.d. skos:/dct: vert deklarert lokalt sjølv om
    # dei alt kjem inn transitivt via eit importert AP-NO-skjema.
    sv.imports_closure()
    declared = set(sv.namespaces().keys())
    if not (declared & standard_prefixes):
        issues.append(issue(
            config["severity"], _fair_code(config), "schema",
            f"{_principle_prefix(config)}Ingen standard vokabularprefiks deklarert "
            f"({', '.join(sorted(standard_prefixes))})",
        ))


def _check_schema_has_slot_with_uri(sv, schema, config, issues):
    match_uris = set(config.get("match_any_uri", []))
    if not (_all_slot_uris(schema) & match_uris):
        curie_forms = sorted(u for u in match_uris if "://" not in u)
        issues.append(issue(
            config["severity"], _fair_code(config), "schema",
            f"{_principle_prefix(config)}Ingen slot med {' / '.join(curie_forms)} funnen",
        ))


def _has_identifier_slot(sv, class_name: str) -> bool:
    """Returnerer True om klassen (eigen eller arva) har ein slot med identifier: true."""
    visited: set = set()
    queue = [class_name]
    while queue:
        cname = queue.pop()
        if cname in visited:
            continue
        visited.add(cname)
        cls = sv.get_class(cname)
        if cls is None:
            continue
        for slot_name in (cls.slots or []):
            slot = sv.get_slot(slot_name)
            if slot and slot.identifier:
                return True
            usage = (cls.slot_usage or {}).get(slot_name)
            if usage and usage.identifier:
                return True
        for attr in (cls.attributes or {}).values():
            if attr.identifier:
                return True
        if cls.is_a:
            queue.append(cls.is_a)
        for mixin in (cls.mixins or []):
            queue.append(mixin)
    return False


def _check_all_classes_have_identifier(sv, schema, config, issues):
    code = "all_classes_have_identifier"
    for cname, cls in (schema.classes or {}).items():
        if cls.tree_root:
            continue
        if not _has_identifier_slot(sv, cname):
            issues.append(issue(
                config["severity"], code, f"class:{cname}",
                f"Klasse '{cname}' manglar global identifikator (slot med identifier: true)",
            ))


def _check_no_inlined_on_primitive_range(sv, schema, config, issues):
    """`inlined`/`inlined_as_list` har berre effekt når `range` er ein klasse.
    Sett på ein primitiv/type-range (string, integer, LangString osv.) vert
    nøkkelen stille ignorert av alle generatorane — daud konfigurasjon som
    ser ut som han gjer noko, men ikkje gjer det."""
    code = "no_inlined_on_primitive_range"

    def _check(inlined, inlined_as_list, range_name, target):
        if not (inlined or inlined_as_list) or not range_name:
            return
        if sv.get_class(range_name) is not None:
            return
        issues.append(issue(
            config["severity"], code, target,
            f"'{target}' har inlined/inlined_as_list sett, men range '{range_name}' "
            "er ikkje ein klasse — nøkkelen har ingen effekt",
        ))

    for sname, slot in (schema.slots or {}).items():
        _check(slot.inlined, slot.inlined_as_list, slot.range, f"slot:{sname}")

    for cname, cls in (schema.classes or {}).items():
        for aname, attr in (cls.attributes or {}).items():
            _check(attr.inlined, attr.inlined_as_list, attr.range,
                   f"class:{cname} → attribute:{aname}")
        for usage_name, usage in (cls.slot_usage or {}).items():
            base_slot = sv.get_slot(usage_name)
            range_name = usage.range or (base_slot.range if base_slot else None)
            _check(usage.inlined, usage.inlined_as_list, range_name,
                   f"class:{cname} → slot:{usage_name}")


def _check_all_classes_have_concept_ref(sv, schema, config, issues):
    catalog_uri = config.get("concept_catalog_uri",
                             "https://concept-catalog.fellesdatakatalog.digdir.no/collections")
    code = "all_classes_have_concept_ref"
    accepted_prefix = catalog_uri.rstrip("/") + "/"
    for cname, cls in (schema.classes or {}).items():
        if cls.tree_root:
            continue
        ann = cls.annotations or {}
        begrep = ann.get("begrepsidentifikator")
        begrep_val = str(begrep.value if hasattr(begrep, "value") else begrep or "")
        if begrep_val.startswith(accepted_prefix):
            continue
        issues.append(issue(
            config["severity"], code, f"class:{cname}",
            f"Klasse '{cname}' manglar annotations.begrepsidentifikator som peikar på begrep i {catalog_uri}",
        ))


def _collect_class_slot_uris(sv, class_name: str) -> set:
    """Samlar alle slot_uri-verdiar for ein klasse, inkludert arva slots."""
    uris: set = set()
    visited: set = set()
    queue = [class_name]
    while queue:
        cname = queue.pop()
        if cname in visited:
            continue
        visited.add(cname)
        cls = sv.get_class(cname)
        if cls is None:
            continue
        for sname in (cls.slots or []):
            slot = sv.get_slot(sname)
            if slot and slot.slot_uri:
                uris.add(str(slot.slot_uri))
        for attr in (cls.attributes or {}).values():
            if attr.slot_uri:
                uris.add(str(attr.slot_uri))
        if cls.is_a:
            queue.append(cls.is_a)
        for mixin in (cls.mixins or []):
            queue.append(mixin)
    return uris


def _check_class_has_slot_with_uri(sv, schema, config, issues):
    cname = config["class"]
    required_uri = config["slot_uri"]
    own_class_names = set(schema.classes.keys()) if schema.classes else set()
    if cname not in own_class_names:
        return
    if required_uri not in _collect_class_slot_uris(sv, cname):
        severity = config["severity"]
        code = "class_missing_required_slot" if severity == "error" else "class_missing_recommended_slot"
        issues.append(issue(
            severity, code, f"class:{cname}",
            f"Klasse '{cname}' manglar slot med {required_uri}",
        ))


def _check_container_has_class(sv, schema, config, issues):
    container_cls = container_name = None
    for cname, cls in (schema.classes or {}).items():
        if cls.tree_root:
            container_cls = cls
            container_name = cname
            break

    if container_cls is None:
        if not any(i["code"] == "no_container_class" for i in issues):
            issues.append(issue(
                "error", "no_container_class", "schema",
                "Ingen tree_root-klasse funnen — kan ikkje sjekke container-klasse-krav",
            ))
        return

    target_class = config["class"]
    container_ranges = {
        str(attr.range)
        for attr in (container_cls.attributes or {}).values()
        if attr.range
    }
    for slot_name in (container_cls.slots or []):
        slot = sv.get_slot(slot_name)
        if slot and slot.range:
            container_ranges.add(str(slot.range))
    if target_class not in container_ranges:
        severity = config["severity"]
        code = "container_missing_required_class" if severity == "error" else "container_missing_recommended_class"
        issues.append(issue(
            severity, code, f"class:{container_name}",
            f"Container '{container_name}' manglar attributt med range '{target_class}'",
        ))


def _check_schema_imports(sv, schema, config, issues):
    must_import = config["must_import"]
    # Direct check: works when schema is not pre-merged
    found = any(must_import in imp for imp in (schema.imports or []))
    if not found:
        # Merged schemas lose the imports list — use a characteristic class as proxy
        char_class = config.get("characteristic_class")
        if char_class and sv.get_class(char_class) is not None:
            found = True
    if not found:
        issues.append(issue(
            config["severity"], "missing_required_import", "schema",
            f"Skjemaet importerer ikkje '{must_import}'",
        ))


def _check_merged_class_has_slot_with_uri(sv, schema, config, issues):
    cname = config["class"]
    required_uri = config["slot_uri"]
    if sv.get_class(cname) is None:
        return
    if required_uri not in _collect_class_slot_uris(sv, cname):
        severity = config["severity"]
        code = "class_missing_required_slot" if severity == "error" \
               else "class_missing_recommended_slot"
        issues.append(issue(
            severity, code, f"class:{cname}",
            f"Klasse '{cname}' manglar slot med {required_uri}",
        ))


def _check_class_count(sv, schema, config, issues):
    max_classes = config.get("max_classes", 50)
    non_root = [
        cname for cname, cls in (schema.classes or {}).items()
        if not cls.tree_root
    ]
    count = len(non_root)
    if count > max_classes:
        issues.append(issue(
            config["severity"], "class_count_exceeds_limit", "schema",
            f"Skjemaet har {count} klasser (maks anbefalt: {max_classes}). "
            f"Vurder å dele opp i fleire skjema (Digdir-regel 6: Modularitet).",
        ))


def _check_merged_class_has_any_slot_with_uri(sv, schema, config, issues):
    cname = config["class"]
    slot_uris = config["slot_uris"]
    if sv.get_class(cname) is None:
        return
    found = _collect_class_slot_uris(sv, cname)
    if not any(uri in found for uri in slot_uris):
        severity = config["severity"]
        code = "class_missing_required_slot" if severity == "error" \
               else "class_missing_recommended_slot"
        issues.append(issue(
            severity, code, f"class:{cname}",
            f"Klasse '{cname}' manglar minst éin slot med URI frå: "
            f"{', '.join(slot_uris)}",
        ))


def _check_controlled_vocabulary_annotations(sv, schema, config, issues):
    """
    Sjekk at slots med kontrollerte vokabular har korrekte annotations.

    Bronze-nivå: Sjekk at slots med gyldige_verdier har vokabular_krav,
    og at SKAL/BØR/KAN i description matcher vokabular_krav.
    """
    def get_annotation_value(annot, key):
        """Hent verdien frå ein Annotation-objekt eller dict."""
        raw = annot.get(key)
        if not raw:
            return None
        return str(raw.value if hasattr(raw, "value") else raw)

    for slot_name, slot in sv.all_slots().items():
        annot = slot.annotations or {}
        gyldige_verdier = get_annotation_value(annot, "gyldige_verdier")

        if not gyldige_verdier:
            continue

        # Sjekk at vokabular_krav finst
        vokabular_krav = get_annotation_value(annot, "vokabular_krav")
        if not vokabular_krav:
            issues.append(issue(
                config["severity"], "slot_missing_vokabular_krav", f"slot:{slot_name}",
                f"Slot '{slot_name}' har annotations.gyldige_verdier men manglar "
                f"annotations.vokabular_krav (skal|bør|kan)",
            ))
            continue

        # Sjekk at vokabular_krav har gyldig verdi
        if vokabular_krav not in ("skal", "bør", "kan"):
            issues.append(issue(
                config["severity"], "slot_invalid_vokabular_krav", f"slot:{slot_name}",
                f"Slot '{slot_name}' har ugyldig vokabular_krav='{vokabular_krav}' "
                f"(gyldige: skal, bør, kan)",
            ))
            continue

        # Sjekk at description matcher vokabular_krav
        desc = slot.description or ""
        skal_match = "SKAL" if vokabular_krav == "skal" else None
        bor_match = "BØR" if vokabular_krav == "bør" else None
        kan_match = "KAN" if vokabular_krav == "kan" else None

        expected = skal_match or bor_match or kan_match
        if expected and expected not in desc:
            issues.append(issue(
                config["severity"], "slot_description_mismatch", f"slot:{slot_name}",
                f"Slot '{slot_name}' har vokabular_krav='{vokabular_krav}' men "
                f"description inneheld ikkje '{expected}'",
            ))


def _check_slot_has_range_and_multivalued(sv, schema, config, issues):
    """
    Sjekkar at ein slot på ein bestemt klasse har forventa range og multivalued-status.

    Brukt for å verifiere at skjemaet er rigga for tospråkverdiar (t.d. LangString
    med multivalued: true), sjølv om instansvalidering ikkje kan sjekke faktisk
    tospråkdekning i YAML-format.
    """
    class_name = config["class"]
    slot_uri = config["slot_uri"]
    expected_range = config.get("expected_range")
    expected_multivalued = config.get("expected_multivalued")

    cls = sv.get_class(class_name)
    if not cls:
        return

    # Finn slot med matchande slot_uri (transitivt via import)
    target_slot = None
    for slot_name in (cls.slots or []):
        slot = sv.get_slot(slot_name)
        if slot and (slot.slot_uri or "") == slot_uri:
            target_slot = slot
            break

    if not target_slot:
        # Sloten finst ikkje — annan sjekk (`merged_class_has_slot_with_uri`)
        # vil fange dette opp, så me returnerer utan å rapportere her
        return

    # Sjekk range
    if expected_range and target_slot.range != expected_range:
        issues.append(issue(
            config["severity"],
            "slot_range_mismatch",
            f"class:{class_name} → slot:{slot_uri}",
            f"Slot har range '{target_slot.range}' (forventa: '{expected_range}')",
        ))

    # Sjekk multivalued
    if expected_multivalued is not None:
        actual_multivalued = target_slot.multivalued or False
        if actual_multivalued != expected_multivalued:
            issues.append(issue(
                config["severity"],
                "slot_multivalued_mismatch",
                f"class:{class_name} → slot:{slot_uri}",
                f"Slot har multivalued={actual_multivalued} (forventa: {expected_multivalued})",
            ))


_CHECK_HANDLERS = {
    "schema_id_is_http_uri":           _check_schema_id_is_http_uri,
    "schema_field_present":            _check_schema_field_present,
    "schema_has_annotation":           _check_schema_has_annotation,
    "default_prefix_is_https_uri":     _check_default_prefix_is_https_uri,
    "class_names_pascal_case":         _check_class_names_pascal_case,
    "slot_names_snake_case":           _check_slot_names_snake_case,
    "all_classes_have_class_uri":      _check_all_classes_have_class_uri,
    "all_slots_have_slot_uri":         _check_all_slots_have_slot_uri,
    "schema_declares_standard_prefix": _check_schema_declares_standard_prefix,
    "schema_has_slot_with_uri":        _check_schema_has_slot_with_uri,
    "all_classes_have_identifier":     _check_all_classes_have_identifier,
    "no_inlined_on_primitive_range":   _check_no_inlined_on_primitive_range,
    "all_classes_have_concept_ref":    _check_all_classes_have_concept_ref,
    "class_has_slot_with_uri":            _check_class_has_slot_with_uri,
    "container_has_class":                _check_container_has_class,
    "schema_imports":                     _check_schema_imports,
    "merged_class_has_slot_with_uri":     _check_merged_class_has_slot_with_uri,
    "merged_class_has_any_slot_with_uri": _check_merged_class_has_any_slot_with_uri,
    "class_count":                        _check_class_count,
    "controlled_vocabulary_annotations":  _check_controlled_vocabulary_annotations,
    "slot_has_range_and_multivalued":     _check_slot_has_range_and_multivalued,
}


def _check_instance_slot_uri_pattern(sv, schema, instance, config, issues):
    slot_uri_target = config["slot_uri"]
    pattern = re.compile(config["pattern"])
    known_values = config.get("known_values", [])

    target_slots = {
        name
        for name, s in sv.all_slots().items()
        if (s.slot_uri or "") == slot_uri_target
    }

    def walk(obj, path=""):
        if isinstance(obj, dict):
            for key, val in obj.items():
                new_path = f"{path}.{key}" if path else key
                if key in target_slots:
                    values = val if isinstance(val, list) else [val]
                    for v in values:
                        if not isinstance(v, str):
                            continue
                        loc = f"instance:{new_path}"
                        if not pattern.match(v):
                            issues.append(issue(
                                config["severity"],
                                "instance_slot_invalid_uri_pattern",
                                loc,
                                f"'{v}' passar ikkje mønsteret {config['pattern']} "
                                f"for {slot_uri_target}",
                            ))
                        elif known_values and v not in known_values:
                            issues.append(issue(
                                config["severity"],
                                "instance_slot_unknown_value",
                                loc,
                                f"'{v}' er ikkje i lista over kjente utgivarar: "
                                f"{', '.join(known_values)}",
                            ))
                walk(val, new_path)
        elif isinstance(obj, list):
            for idx, item in enumerate(obj):
                walk(item, f"{path}[{idx}]")

    walk(instance)


def _check_instance_begrep_definisjon_language_coverage(sv, schema, instance, config, issues):
    relasjon_slot_uri = config["relasjon_slot_uri"]
    krev_spraak = config.get("krev_spraak", [])
    suffix_pattern = re.compile(config.get("id_suffiks_pattern", r"-([a-z]{2})$"))

    target_slots = {
        name
        for name, s in sv.all_slots().items()
        if (s.slot_uri or "") == relasjon_slot_uri
    }

    def walk(obj, path=""):
        if isinstance(obj, dict):
            for key, val in obj.items():
                new_path = f"{path}.{key}" if path else key
                if key in target_slots and isinstance(val, list):
                    langs_found = set()
                    for v in val:
                        if not isinstance(v, str):
                            continue
                        m = suffix_pattern.search(v)
                        if m:
                            langs_found.add(m.group(1))
                    missing = [lang for lang in krev_spraak if lang not in langs_found]
                    if missing:
                        begrep_id = obj.get("id", "?")
                        issues.append(issue(
                            config["severity"],
                            "instance_begrep_missing_language_definisjon",
                            f"instance:{path}" if path else "instance",
                            f"Begrep '{begrep_id}' manglar Definisjon med språk-suffiks for: "
                            f"{', '.join(missing)} (tospråkskravet, basert på ID-suffikskonvensjonen)",
                        ))
                walk(val, new_path)
        elif isinstance(obj, list):
            for idx, item in enumerate(obj):
                walk(item, f"{path}[{idx}]")

    walk(instance)


def _check_instance_controlled_vocabulary_pattern(sv, schema, instance, config, issues):
    """
    Validerer at instansverdiar for slots med vokabular_pattern matcher regex-mønsteret.

    Silver-nivå: Åtvaring dersom verdiar ikkje matcher pattern.
    Gold-nivå: Feil dersom verdiar ikkje matcher pattern.
    """
    def get_annotation_value(annot, key):
        """Hent verdien frå ein Annotation-objekt eller dict."""
        raw = annot.get(key)
        if not raw:
            return None
        return str(raw.value if hasattr(raw, "value") else raw)

    def walk(obj, path=""):
        if isinstance(obj, dict):
            for key, val in obj.items():
                new_path = f"{path}.{key}" if path else key
                slot = sv.all_slots().get(key)
                if not slot:
                    walk(val, new_path)
                    continue

                annot = slot.annotations or {}
                vokabular_pattern = get_annotation_value(annot, "vokabular_pattern")
                vokabular_krav = get_annotation_value(annot, "vokabular_krav")
                gyldige_verdier = get_annotation_value(annot, "gyldige_verdier")

                if not vokabular_pattern:
                    walk(val, new_path)
                    continue

                pattern = re.compile(vokabular_pattern)
                values = val if isinstance(val, list) else [val]

                for v in values:
                    if not isinstance(v, str):
                        continue

                    loc = f"instance:{new_path}"

                    # Sjekk pattern
                    if not pattern.match(v):
                        # Alvorlegheit avheng av vokabular_krav
                        if vokabular_krav == "skal":
                            severity = "error"
                        elif vokabular_krav == "bør":
                            severity = "warning"
                        else:  # kan
                            severity = "info"

                        issues.append(issue(
                            severity,
                            "instance_slot_invalid_vocabulary_pattern",
                            loc,
                            f"'{v}' passar ikkje vokabular_pattern {vokabular_pattern} "
                            f"for slot '{key}' (vokabular_krav: {vokabular_krav})",
                        ))

                    # Sjekk domene (gyldige_verdier)
                    if gyldige_verdier and not v.startswith(gyldige_verdier):
                        severity = config["severity"]
                        if vokabular_krav == "skal":
                            severity = "error"
                        elif vokabular_krav == "bør":
                            severity = "warning"

                        issues.append(issue(
                            severity,
                            "instance_slot_invalid_vocabulary_domain",
                            loc,
                            f"'{v}' er ikkje frå vokabular-domenet {gyldige_verdier} "
                            f"for slot '{key}' (vokabular_krav: {vokabular_krav})",
                        ))

                walk(val, new_path)
        elif isinstance(obj, list):
            for idx, item in enumerate(obj):
                walk(item, f"{path}[{idx}]")

    walk(instance)


_INSTANCE_CHECK_HANDLERS = {
    "instance_slot_uri_pattern": _check_instance_slot_uri_pattern,
    "instance_begrep_definisjon_language_coverage": _check_instance_begrep_definisjon_language_coverage,
    "instance_controlled_vocabulary_pattern": _check_instance_controlled_vocabulary_pattern,
}


def _run_instance_checks(sv, schema, instance, policy, issues):
    for config in (policy.get("instance_checks") or {}).values():
        handler = _INSTANCE_CHECK_HANDLERS.get(config.get("check"))
        if handler:
            handler(sv, schema, instance, config, issues)


def _run_checks(sv, schema, policy: dict, issues: list) -> None:
    for key in ("checks", "fair_checks"):
        for config in policy.get(key, {}).values():
            handler = _CHECK_HANDLERS.get(config.get("check"))
            if handler:
                handler(sv, schema, config, issues)


# ---------------------------------------------------------------------------
# Validering
# ---------------------------------------------------------------------------

def validate_schema(schema_text: str | None = None, policy_name: str = "bronze",
                     instance_text: str | None = None, schema_path: str | None = None) -> dict:
    """
    Validerer eit LinkML-skjema. Gjev anten `schema_text` (rå YAML, skriven til
    ein mellombels fil) eller `schema_path` (sti til ei skjemafil som alt
    finst på disk, t.d. inne i eit montert repo) — aldri begge.

    `schema_path` let SchemaView løyse relative imports naturleg mot
    filsystemet, utan behov for førehandsutflating via `gen-linkml
    --mergeimports` (sjå specs/backlog/effektiviser-mcp-linkml-validator-
    koyretid.md, Tiltak 2). `schema_text` er framleis støtta for kallarar
    som ikkje har eit montert repo tilgjengeleg (t.d. ein ekstern MCP-klient
    som berre har skjemainnhaldet i minnet).
    """
    if schema_path is None and schema_text is None:
        return {
            "valid": False, "errorCount": 1, "warningCount": 0,
            "issues": [issue("error", "parse_error", "schema",
                              "Anten schemaText eller schemaPath må oppgjevast")],
        }

    policy = load_policy(policy_name)
    base = _is_base_policy(policy_name)
    issues = []

    tmp_dir_ctx = None
    if schema_path is None:
        tmp_dir_ctx = tempfile.TemporaryDirectory()
        schema_path = str(Path(tmp_dir_ctx.name) / "schema.yaml")
        Path(schema_path).write_text(schema_text, encoding="utf-8")

    try:
        # 1) Parse — gir parse-feil som error
        try:
            from linkml_runtime.utils.schemaview import SchemaView
            sv = SchemaView(schema_path)
        except Exception as exc:
            return {
                "valid": False,
                "errorCount": 1,
                "warningCount": 0,
                "issues": [issue("error", "parse_error", "schema", str(exc))],
            }

        # 2) LinkML linter — berre for basispolicyen (ingen extends).
        # Silver og gold arvar bronse; lint er allereie køyrt på bronsenivå.
        if base:
            try:
                from linkml.linter.linter import Linter
                linter = Linter()
                for problem in linter.lint(schema_path, validate_schema=True):
                    level = getattr(problem.level, "value", str(problem.level)).lower()
                    rule = getattr(problem, "rule_name", None) or "linkml_lint"
                    target = str(getattr(problem, "source", None) or "schema")
                    issues.append(issue(level, rule, target, str(problem.message)))
            except Exception as exc:
                issues.append(issue("error", "linter_error", "schema", str(exc)))

        schema = sv.schema

        # 3) Instansvalidering — køyrer for alle policyer om instans er gjeven.
        # Gjenbruk sv.schema (alt bygd, med imports løyste) i staden for å
        # sende schema_path vidare til lm_validate(): linkml sin eigen
        # sti-baserte import-oppløysing bruker CWD/objektnamn som base i
        # staden for skjemafila sin eigen katalog, og reknar difor ut feil
        # absolutt sti for relative importar (verifisert empirisk — feilar
        # med t.d. "/ap-no/..." i staden for "/repo/src/linkml/ap-no/...").
        # target_class er alt kjent frå sv.schema her, så validate_instance()
        # slepp òg å parse skjemaet på nytt berre for å finne tree_root-klassen.
        if instance_text is not None:
            target_class = next(
                (cname for cname, cls in (schema.classes or {}).items() if cls.tree_root), None)
            inst_result = validate_instance(
                schema_text, instance_text, target_class=target_class, schema_obj=schema)
            issues.extend(inst_result["issues"])

        # 4) Policy-felt-sjekkar
        def _check(obj, obj_label: str, required_fields: list, recommended_fields: list):
            for field in required_fields:
                if not getattr(obj, field, None):
                    issues.append(issue(
                        "error", "missing_required_metadata", obj_label,
                        f"Manglar obligatorisk metadata: {field}",
                    ))
            for field in recommended_fields:
                if not getattr(obj, field, None):
                    issues.append(issue(
                        "warning", "missing_recommended_metadata", obj_label,
                        f"Manglar anbefalt metadata: {field}",
                    ))

        _check(
            schema,
            f"schema:{schema.name or 'ukjent'}",
            policy.get("required", {}).get("schema", []),
            policy.get("recommended", {}).get("schema", []),
        )
        for cname, cls in (schema.classes or {}).items():
            _check(
                cls, f"class:{cname}",
                policy.get("required", {}).get("class", []),
                policy.get("recommended", {}).get("class", []),
            )
        for sname, slot in (schema.slots or {}).items():
            _check(
                slot, f"slot:{sname}",
                policy.get("required", {}).get("slot", []),
                policy.get("recommended", {}).get("slot", []),
            )

        # Påkravde fellesklasser
        must_use = policy.get("common_classes", {}).get("must_use", [])
        all_class_names = set(sv.all_classes().keys())
        for cc in must_use:
            if cc not in all_class_names:
                issues.append(issue(
                    "error", "missing_common_class", f"class:{cc}",
                    f"Påkravd fellesklasse manglar: {cc}",
                ))

        # 5) Policy-spesifikke struktursjekkar (checks + fair_checks)
        _run_checks(sv, schema, policy, issues)

        # 6) Instans-spesifikke policy-sjekkar (instance_checks)
        if instance_text is not None:
            parsed_instance = yaml.safe_load(instance_text)
            _run_instance_checks(sv, schema, parsed_instance, policy, issues)
    finally:
        if tmp_dir_ctx is not None:
            tmp_dir_ctx.cleanup()

    errors = [i for i in issues if i["severity"] == "error"]
    warnings = [i for i in issues if i["severity"] == "warning"]
    return {
        "valid": len(errors) == 0,
        "errorCount": len(errors),
        "warningCount": len(warnings),
        "issues": issues,
    }


# ---------------------------------------------------------------------------
# Instansvalidering — tilsvarar `linkml validate --schema <schema> <instance>`
# ---------------------------------------------------------------------------

def validate_instance(schema_text: str | None, instance_text: str, target_class: str | None = None,
                       schema_obj=None, schema_path: str | None = None) -> dict:
    """
    Gjev skjema anten som `schema_text` (rå YAML, vert parsa til ein dict),
    `schema_obj` (eit alt bygd `SchemaDefinition`, typisk `sv.schema` frå
    ein eksisterande SchemaView) eller `schema_path` (sti til ei skjemafil
    som alt finst på disk, t.d. inne i eit montert repo) — berre éitt av dei
    tre skal gjevast.

    `schema_path` let SchemaView løyse relative imports naturleg mot
    filsystemet, same grunngjeving som `validate_schema()` sin tilsvarande
    parameter (sjå specs/backlog/effektiviser-mcp-linkml-validator-
    koyretid.md, Tiltak 2, og specs/backlog/batch-validate-lint-test-per-
    skjema.md, Tiltak 3 Kategori C).

    Merk: å sende ein rå skjemasti til `linkml.validator.validate()` er
    **ikkje** trygt — verifisert empirisk at biblioteket då reknar ut feil
    absolutt sti for relative importar (brukar CWD/objektnamn som base i
    staden for skjemafila sin eigen katalog). `schema_path` løyser difor
    imports sjølv via `SchemaView` og sender det ferdig oppløyste
    `SchemaDefinition`-objektet vidare, akkurat som `schema_obj`.
    """
    issues = []

    try:
        instance = yaml.safe_load(instance_text)
    except Exception as exc:
        return {
            "valid": False,
            "errorCount": 1,
            "warningCount": 0,
            "issues": [issue("error", "parse_error", "instance", str(exc))],
        }

    schema_for_validate: object
    if schema_obj is not None:
        schema_for_validate = schema_obj
    elif schema_path is not None:
        try:
            from linkml_runtime.utils.schemaview import SchemaView
            sv = SchemaView(schema_path)
        except Exception as exc:
            return {
                "valid": False,
                "errorCount": 1,
                "warningCount": 0,
                "issues": [issue("error", "parse_error", "schema", str(exc))],
            }
        schema_for_validate = sv.schema
        if not target_class:
            target_class = next(
                (cname for cname, cls in (sv.schema.classes or {}).items() if cls.tree_root), None)
    else:
        try:
            schema_dict = yaml.safe_load(schema_text)
        except Exception as exc:
            return {
                "valid": False,
                "errorCount": 1,
                "warningCount": 0,
                "issues": [issue("error", "parse_error", "schema", str(exc))],
            }
        schema_for_validate = schema_dict
        if not target_class:
            for cname, cls_def in (schema_dict.get("classes") or {}).items():
                if isinstance(cls_def, dict) and cls_def.get("tree_root"):
                    target_class = cname
                    break

    try:
        from linkml.validator import validate as lm_validate
        from linkml.validator.report import Severity
        report = lm_validate(instance, schema_for_validate, target_class=target_class)
        _severity_map = {
            Severity.FATAL: "error",
            Severity.ERROR: "error",
            Severity.WARN:  "warning",
            Severity.INFO:  "info",
        }
        for result in report.results:
            sev = _severity_map.get(result.severity, "error")
            target = result.instantiates or "instance"
            if result.instance_index is not None:
                target = f"{target}[{result.instance_index}]"
            issues.append(issue(sev, result.type or "validation_error", target, result.message))
    except Exception as exc:
        issues.append(issue("error", "validation_error", "instance", str(exc)))

    errors   = [i for i in issues if i["severity"] == "error"]
    warnings = [i for i in issues if i["severity"] == "warning"]
    return {
        "valid":        len(errors) == 0,
        "errorCount":   len(errors),
        "warningCount": len(warnings),
        "issues":       issues,
    }


# ---------------------------------------------------------------------------
# MCP-protokoll
# ---------------------------------------------------------------------------

TOOL_DEF = {
    "name": "validate_linkml_schema",
    "description": (
        "Validerer eit LinkML-skjema i rekkjefølgja: (1) lint skjema, "
        "(2) valider instans mot skjema (om instanceText er gjeven), "
        "(3) valider mot policy-reglar. "
        "Medaljongnivå: 'bronze' (basis), 'silver' (bronze + AP-NO), 'gold' (silver + FAIR)."
    ),
    "inputSchema": {
        "type": "object",
        "properties": {
            "schemaText": {
                "type": "string",
                "description": (
                    "LinkML-skjema i YAML-format. Bruk schemaPath i staden dersom skjemaet "
                    "har relative imports og filsystemet er montert i kontainaren — SchemaView "
                    "løyser då imports naturleg, utan førehandsutflating. Anten schemaText "
                    "eller schemaPath må oppgjevast, aldri begge."
                ),
            },
            "schemaPath": {
                "type": "string",
                "description": (
                    "Sti til ei skjemafil som alt finst på disk i kontainaren "
                    "(t.d. /repo/src/linkml/<domain>/<modell>/<modell>-schema.yaml). "
                    "Brukast i staden for schemaText når heile repoet er montert inn."
                ),
            },
            "policy": {
                "type": "string",
                "description": "Policy-namn (default: 'bronze'). Tilgjengelege: 'bronze', 'silver', 'gold'.",
                "default": "bronze",
            },
            "instanceText": {
                "type": "string",
                "description": (
                    "Eksempeldata i YAML-format (valfri). "
                    "Vert validert mot skjemaet etter linting og før policy-sjekkar. "
                    "Tilsvarar `linkml validate --schema <schema> <instans>`."
                ),
            },
        },
    },
}

TOOL_DEF_INSTANCE = {
    "name": "validate_linkml_instance",
    "description": (
        "Validerer eit datasett (instans) mot eit LinkML-skjema. "
        "Tilsvarar `linkml validate --schema <schema> <instance>`. "
        "Finn tree_root-klassen automatisk dersom targetClass ikkje er oppgjeven."
    ),
    "inputSchema": {
        "type": "object",
        "required": ["instanceText"],
        "properties": {
            "schemaText": {
                "type": "string",
                "description": (
                    "LinkML-skjema i YAML-format. Bruk schemaPath i staden dersom skjemaet "
                    "har relative imports og filsystemet er montert i kontainaren — SchemaView "
                    "løyser då importar naturleg mot filsystemet. Anten schemaText eller "
                    "schemaPath må oppgjevast, aldri begge."
                ),
            },
            "schemaPath": {
                "type": "string",
                "description": "Sti til ei skjemafil som alt finst i kontainaren (t.d. eit montert repo).",
            },
            "instanceText": {
                "type": "string",
                "description": "Datasett/instans i YAML-format.",
            },
            "targetClass": {
                "type": "string",
                "description": "Målklasse for validering. Valfri — tree_root-klassen nyttast som standard.",
            },
        },
    },
}


def handle(msg: dict) -> dict | None:
    method = msg.get("method", "")
    msg_id = msg.get("id")

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "mcp-linkml-validator", "version": "1.0.0"},
            },
        }

    if method == "initialized":
        return None  # notifikasjon — ingen respons

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {"tools": [TOOL_DEF, TOOL_DEF_INSTANCE]},
        }

    if method == "tools/call":
        tool_name = msg.get("params", {}).get("name")
        arguments = msg.get("params", {}).get("arguments", {})

        if tool_name == "validate_linkml_schema":
            policy_name = arguments.get("policy", "bronze")
            instance_text = arguments.get("instanceText") or None
            schema_path = arguments.get("schemaPath") or None
            schema_text = arguments.get("schemaText") or None
            result = validate_schema(schema_text, policy_name, instance_text, schema_path=schema_path)
            return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "content": [
                        {"type": "text", "text": json.dumps(result, ensure_ascii=False, indent=2)}
                    ]
                },
            }

        if tool_name == "validate_linkml_instance":
            instance_schema_text = arguments.get("schemaText") or None
            instance_schema_path = arguments.get("schemaPath") or None
            if instance_schema_text is None and instance_schema_path is None:
                result = {
                    "valid": False, "errorCount": 1, "warningCount": 0,
                    "issues": [issue("error", "parse_error", "schema",
                                      "Anten schemaText eller schemaPath må oppgjevast")],
                }
            else:
                result = validate_instance(
                    instance_schema_text,
                    arguments.get("instanceText", ""),
                    arguments.get("targetClass") or None,
                    schema_path=instance_schema_path,
                )
            return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "content": [
                        {"type": "text", "text": json.dumps(result, ensure_ascii=False, indent=2)}
                    ]
                },
            }

        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": {"code": -32602, "message": f"Ukjent verktøy: {tool_name}"},
        }

    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "error": {"code": -32601, "message": f"Metode ikkje funnen: {method}"},
    }


def main():
    for raw in sys.stdin:
        raw = raw.strip()
        if not raw:
            continue
        try:
            msg = json.loads(raw)
        except json.JSONDecodeError as exc:
            send({"jsonrpc": "2.0", "id": None,
                  "error": {"code": -32700, "message": f"Parse-feil: {exc}"}})
            continue

        try:
            response = handle(msg)
        except Exception as exc:
            # Ein uventa feil i handteringa av éin melding skal ikkje ta ned
            # resten av stdin-straumen — kritisk når fleire valideringskall
            # vert batcha inn i éin serverprosess (sjå batch-flatten-and-
            # validate.py), sidan éin ubehandla exception elles ville drepe
            # heile prosessen og miste resultatet for alle attverande jobbar.
            response = {"jsonrpc": "2.0", "id": msg.get("id"),
                        "error": {"code": -32000, "message": f"Uventa feil: {exc}"}}
        if response is not None:
            send(response)


if __name__ == "__main__":
    main()
