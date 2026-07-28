#!/usr/bin/env python3
"""
gen-modelldcat-elements.py

Genererer ModelDCAT-AP-NO-modellelement (Objekttype, Attributt, Assosiasjon,
Kodeliste, Kodeelement, delte Enkeltype-instansar) frå LinkML-skjemastruktur
via SchemaView, og skriv dei inn i riktig org sin modellkatalog-datafil.
Set 'inneholder_modellelement' på tilhøyrande Informasjonsmodell-oppføring.

Mapping LinkML → ModelDCAT (sjå spec for full grunngjeving):
  - konkret, ikkje-abstrakt/mixin/tree_root-klasse                 -> Objekttype
  - slot med primitiv/innebygd range                               -> Attributt (har_enkel_type)
  - slot med range = lokal enum                                    -> Attributt (har_verdi_fra)
  - slot med range = annan klasse, ikkje inlined                   -> Assosiasjon (refererer_til)
  - slot med range = annan klasse, inlined                         -> Attributt (inneholder_objekttype)
  - enum (lokalt definert)                                         -> Kodeliste + Kodeelement pr. verdi

Containerattributtane er konkret-typa (objekttyper, attributter, assosiasjoner,
kodelister, kodeelementer, enkeltyper) — IKKJE éin delt polymorf liste. Sjå
specs/bugs/polymorphic-inlined-list-yaml-loader.md (BUG-8): polymorf
inlined_as_list krasjar linkml-convert/RDF-generering.

Idempotent: identifiserer tidlegare genererte element via stabilt ID-skjema
(under <catalog_base>/<skjemanavn>/...) og erstattar (ikkje duplikat) ved ny
køyring. Delte Enkeltype-instansar (under <catalog_base>/types/...) er org-
globale og blir aldri fjerna, berre lagt til ved behov.

Føresetnad: krev linkml-pakken (SchemaView) — køyr via $(LINKML_RUN), ikkje
$(PYTHON_RUN).

Køyr frå repo-rota:
    python3 src/assets/scripts/gen-modelldcat-elements.py [--org ALIAS] [--dry-run]
"""
import argparse
import importlib.util
import os
import sys

import yaml
from linkml_runtime.utils.schemaview import SchemaView

# Gjenbruk org-/skjemaoppslagslogikk frå update-modellkatalog.py (DRY-prinsippet i CLAUDE.md).
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "update_modellkatalog", os.path.join(_SCRIPT_DIR, "update-modellkatalog.py")
)
update_modellkatalog = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(update_modellkatalog)

CODEOWNERS_PATH = update_modellkatalog.CODEOWNERS_PATH
load_org_registry = update_modellkatalog.load_org_registry
load_release_manifest = update_modellkatalog.load_release_manifest
load_annotated_schemas = update_modellkatalog.load_annotated_schemas
group_schemas_by_org = update_modellkatalog.group_schemas_by_org
find_catalog_data = update_modellkatalog.find_catalog_data
entry_name = update_modellkatalog.entry_name

GENERATED_LIST_KEYS = ["objekttyper", "attributter", "assosiasjoner", "kodelister", "kodeelementer"]

_TRANSLITERATION = str.maketrans({
    "æ": "ae", "Æ": "Ae",
    "ø": "oe", "Ø": "Oe",
    "å": "aa", "Å": "Aa",
})


def transliterate_uri_segment(value):
    """Translittererer særnorske bokstavar i ein URI-lokaldel, jf. CLAUDE.md sin
    identifikatorkonvensjon — permissible_values (t.d. enum-koden 'OPPLØST') er
    fritekst, ikke garantert URI-trygge, og kan inneholde slike bokstavar."""
    return str(value).translate(_TRANSLITERATION)


def as_langstring_list(value):
    """str() sikrar at linkml sine NamedElement-subklassar av str (ClassDefinitionName,
    SlotDefinitionName, EnumDefinitionName) blir vanlege Python-strenger — elles
    feiler yaml.dump med ein userialiserbar !!python/object/new-tag."""
    return [str(value)] if value else None


def class_local_name(class_def):
    return class_def.name


def is_concrete_domain_class(class_def):
    return not class_def.abstract and not class_def.mixin and not class_def.tree_root


def resolve_external_class_ref(sv, range_name):
    """URI for ei klasse definert i eit importert skjema (ikkje generert lokalt)."""
    return sv.get_uri(range_name, expand=True)


def build_objekttype(catalog_base, schema_name, class_def):
    objekttype_id = f"{catalog_base}/{schema_name}/{class_local_name(class_def)}"
    entry = {"id": objekttype_id}
    tittel = as_langstring_list(class_def.title or class_def.name)
    if tittel:
        entry["tittel"] = tittel
    beskrivelse = as_langstring_list(class_def.description)
    if beskrivelse:
        entry["beskrivelse"] = beskrivelse
    return objekttype_id, entry


def build_kodeliste(catalog_base, schema_name, enum_name, enum_def):
    kodeliste_id = f"{catalog_base}/{schema_name}/{enum_name}"
    entry = {"id": kodeliste_id}
    entry["tittel"] = as_langstring_list(enum_def.title or enum_name) or [str(enum_name)]
    beskrivelse = as_langstring_list(enum_def.description)
    if beskrivelse:
        entry["beskrivelse"] = beskrivelse
    kodeelementer = []
    for value, pv in (enum_def.permissible_values or {}).items():
        kodeelement_id = f"{kodeliste_id}/{transliterate_uri_segment(value)}"
        kel = {
            "id": kodeelement_id,
            "i_kodeliste": [kodeliste_id],
            "kode": str(value),
        }
        descr = getattr(pv, "description", None) if pv else None
        if descr:
            kel["anbefalt_kodetekst"] = [str(descr)]
            kel["definisjon"] = [str(descr)]
        else:
            kel["anbefalt_kodetekst"] = [str(value)]
        kodeelementer.append(kel)
    return kodeliste_id, entry, kodeelementer


def get_or_create_enkeltype(catalog_base, type_name, enkeltyper_by_id):
    enkeltype_id = f"{catalog_base}/types/{type_name}"
    if enkeltype_id not in enkeltyper_by_id:
        enkeltyper_by_id[enkeltype_id] = {
            "id": enkeltype_id,
            "tittel": [str(type_name)],
        }
    return enkeltype_id


def build_egenskaper_for_class(sv, catalog_base, schema_name, class_def, objekttype_id,
                                local_class_names, local_enum_names, enkeltyper_by_id):
    """Returnerer (attributt_entries, assosiasjon_entries, egenskap_ids) for éi klasse."""
    attributter = []
    assosiasjoner = []
    egenskap_ids = []

    for slot in sv.class_induced_slots(class_def.name):
        if slot.identifier:
            continue
        egenskap_id = f"{objekttype_id}/{slot.name}"
        base_entry = {"id": egenskap_id}
        tittel = as_langstring_list(slot.title or slot.name)
        if tittel:
            base_entry["tittel"] = tittel
        beskrivelse = as_langstring_list(slot.description)
        if beskrivelse:
            base_entry["beskrivelse"] = beskrivelse
        base_entry["nedre_multiplisitet"] = 1 if slot.required else 0
        base_entry["oevre_multiplisitet"] = "*" if slot.multivalued else "1"

        range_name = slot.range or sv.schema.default_range
        range_class = sv.get_class(range_name, strict=False)
        range_enum = None if range_class else sv.get_enum(range_name, strict=False)

        if range_class is not None:
            # Berre klasser som faktisk fekk ein Objekttype (lokal, konkret) kan
            # refereres internt — abstrakte/mixin-klasser (lokale eller importerte)
            # har ingen Objekttype-id og må derfor alltid løyses via skjema-URI-en.
            if range_name in local_class_names and is_concrete_domain_class(range_class):
                target_id = f"{catalog_base}/{schema_name}/{range_name}"
            else:
                target_id = resolve_external_class_ref(sv, range_name)
            if slot.inlined or slot.inlined_as_list:
                # Faktisk nøsta innhald -> Attributt.inneholder_objekttype
                base_entry["inneholder_objekttype"] = [target_id]
                attributter.append(base_entry)
            else:
                # Referanse via URI -> Assosiasjon.refererer_til
                base_entry["refererer_til"] = target_id
                assosiasjoner.append(base_entry)
        elif range_enum is not None and range_name in local_enum_names:
            # Kodeliste for lokale enum er allereie bygd i build_for_schema — same ID-skjema.
            kodeliste_id = f"{catalog_base}/{schema_name}/{range_name}"
            base_entry["har_verdi_fra"] = [kodeliste_id]
            attributter.append(base_entry)
        else:
            # Primitiv/innebygd type (eller ekstern enum, behandla som primitiv) -> Attributt.har_enkel_type
            type_key = range_name if range_enum is None else "string"
            enkeltype_id = get_or_create_enkeltype(catalog_base, type_key, enkeltyper_by_id)
            base_entry["har_enkel_type"] = [enkeltype_id]
            attributter.append(base_entry)

        egenskap_ids.append(egenskap_id)

    return attributter, assosiasjoner, egenskap_ids


def build_for_schema(sv, catalog_base, schema_name):
    """Bygg alle modellelement for eitt skjema. Returnerer dict med lister + objekttype-ids."""
    local_classes = sv.all_classes(imports=False)
    local_enums = sv.all_enums(imports=False)
    local_class_names = set(local_classes)
    local_enum_names = set(local_enums)

    objekttyper = []
    attributter = []
    assosiasjoner = []
    kodelister = []
    kodeelementer = []
    enkeltyper_by_id = {}
    objekttype_ids = []

    for enum_name, enum_def in local_enums.items():
        _kodeliste_id, kl_entry, kel_entries = build_kodeliste(catalog_base, schema_name, enum_name, enum_def)
        kodelister.append(kl_entry)
        kodeelementer.extend(kel_entries)

    for class_name, class_def in local_classes.items():
        if not is_concrete_domain_class(class_def):
            continue
        objekttype_id, ot_entry = build_objekttype(catalog_base, schema_name, class_def)
        attrs, assocs, egenskap_ids = build_egenskaper_for_class(
            sv, catalog_base, schema_name, class_def, objekttype_id,
            local_class_names, local_enum_names, enkeltyper_by_id,
        )
        if egenskap_ids:
            ot_entry["har_egenskap"] = egenskap_ids
        objekttyper.append(ot_entry)
        objekttype_ids.append(objekttype_id)
        attributter.extend(attrs)
        assosiasjoner.extend(assocs)

    return {
        "objekttyper": objekttyper,
        "attributter": attributter,
        "assosiasjoner": assosiasjoner,
        "kodelister": kodelister,
        "kodeelementer": kodeelementer,
        "enkeltyper": list(enkeltyper_by_id.values()),
        "objekttype_ids": objekttype_ids,
    }


def replace_schema_scoped(existing_list, catalog_base, schema_name, new_entries):
    """Fjern alle eksisterande element under <catalog_base>/<schema_name>/... for DENNE
    skjema-køyringa, og legg til dei nyleg genererte."""
    prefix = f"{catalog_base}/{schema_name}/"
    kept = [e for e in existing_list if not (e.get("id") or "").startswith(prefix)]
    return kept + new_entries


def merge_enkeltyper(existing_list, new_entries):
    by_id = {e["id"]: e for e in existing_list if "id" in e}
    for e in new_entries:
        by_id[e["id"]] = e
    return list(by_id.values())


def process_org_schemas(org, schemas, dry_run):
    catalog_path, exists = find_catalog_data(org)
    if not exists:
        print(f"  ÅTVARSLE: Katalogdatafil ikkje funne: {catalog_path}")
        return

    with open(catalog_path, encoding="utf-8") as fh:
        catalog = yaml.safe_load(fh) or {}

    catalog_base = ""
    if catalog.get("modellkataloger"):
        catalog_base = catalog["modellkataloger"][0].get("id", "").rstrip("/")
    if not catalog_base:
        print(f"  HOPP OVER {catalog_path}: fann ikkje modellkataloger[0].id")
        return

    entries = catalog.get("informasjonsmodeller") or []
    entry_by_name = {entry_name(e): e for e in entries}

    for key in GENERATED_LIST_KEYS + ["enkeltyper"]:
        catalog.setdefault(key, [])

    processed = []
    for schema in schemas:
        schema_name = schema["name"]
        if not schema_name:
            continue
        sv = SchemaView(schema["path"])
        result = build_for_schema(sv, catalog_base, schema_name)

        for key in GENERATED_LIST_KEYS:
            catalog[key] = replace_schema_scoped(catalog[key], catalog_base, schema_name, result[key])
        catalog["enkeltyper"] = merge_enkeltyper(catalog["enkeltyper"], result["enkeltyper"])

        if schema_name in entry_by_name:
            entry_by_name[schema_name]["inneholder_modellelement"] = result["objekttype_ids"]

        processed.append((schema_name, result))
        print(
            f"  {schema_name}: {len(result['objekttyper'])} objekttyper, "
            f"{len(result['attributter'])} attributter, {len(result['assosiasjoner'])} assosiasjoner, "
            f"{len(result['kodelister'])} kodelister, {len(result['kodeelementer'])} kodeelementer, "
            f"{len(result['enkeltyper'])} nye enkeltyper"
        )

    catalog["informasjonsmodeller"] = entries

    if not dry_run and processed:
        with open(catalog_path, "w", encoding="utf-8") as fh:
            yaml.dump(catalog, fh, allow_unicode=True, sort_keys=False, default_flow_style=False)
        print(f"  Skreiv {catalog_path}")
    elif dry_run and processed:
        print("  (--dry-run: ingen filer endra)")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codeowners", default=CODEOWNERS_PATH, help="Sti til CODEOWNERS.md")
    parser.add_argument("--org", default=None, help="Køyr berre for éin org (alias)")
    parser.add_argument("--dry-run", action="store_true", help="Vis endringar utan å skrive til disk")
    args = parser.parse_args(argv)

    if not os.path.isfile(args.codeowners):
        print(f"FEIL: Fann ikkje {args.codeowners}", file=sys.stderr)
        sys.exit(1)

    org_registry = load_org_registry(args.codeowners)
    if not org_registry:
        print("FEIL: Ingen organisasjonar funne i CODEOWNERS.md-frontmatter.", file=sys.stderr)
        sys.exit(1)

    schemas = load_annotated_schemas(release_manifest=load_release_manifest())
    grouped, _unknown = group_schemas_by_org(schemas, org_registry)

    orgs_to_process = [
        org for uri, org in org_registry.items()
        if args.org is None or org["alias"] == args.org
    ]

    for org in orgs_to_process:
        org_schemas = grouped.get(org["org_uri"], [])
        print(f"--- {org['name']} ({org['alias']}) — {len(org_schemas)} skjema ---")
        if not org_schemas:
            print("  Ingen skjema med matchande annotations.utgiver.")
            print()
            continue
        process_org_schemas(org, org_schemas, args.dry_run)
        print()


if __name__ == "__main__":
    main()
