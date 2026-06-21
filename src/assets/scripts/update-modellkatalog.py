"""
update-modellkatalog.py

Les silver-annotasjonar frå alle skjema og oppdaterer Informasjonsmodell-innslag
i per-org modellkatalogar. Eigarskapsregisteret vert lese frå CODEOWNERS.md.

Oppdaterte felt (henta frå annotations.* og schema.version):
  utgiver, endringsdato, utgivelsesdato, status, versjonsnummer

Ikkje-oppdaterte felt (manuelt vedlikehaldne):
  tittel, beskrivelse, tema, lisens, kontaktpunkt, m.m.
  (For nye skjema vert det oppretta ein stub med TODO-verdiar for desse.)

Køyr frå repo-rota:
    python3 src/assets/scripts/update-modellkatalog.py [--codeowners PATH] [--org ALIAS] [--dry-run]
"""
import argparse
import glob
import os
import sys

import yaml

CODEOWNERS_PATH = "CODEOWNERS.md"
CATALOG_DATA_TEMPLATE = "src/linkml/modellkatalog/{slug}/data/{slug}/{slug}.yaml"
PORTAL_BASE = "https://brreg.github.io/linkml-datamodellering-no"
RELEASE_MANIFEST_PATH = ".release-please-manifest.json"

# modellkatalog er outputdomenet (sjølvreferanse), begrepskatalog er SKOS-AP-NO
# (ein annan artefakttype enn Informasjonsmodell), referanse er ikkje-produksjon.
EXCLUDED_DOMAINS = {"referanse", "modellkatalog", "begrepskatalog"}

ANNOTATION_FIELD_MAP = [
    ("utgiver",        "utgiver"),
    ("endringsdato",   "endringsdato"),
    ("utgivelsesdato", "utgivelsesdato"),
    ("status",         "status"),
]


def load_org_registry(codeowners_path=CODEOWNERS_PATH):
    """Parse YAML frontmatter from CODEOWNERS.md. Returns dict keyed on org_uri."""
    with open(codeowners_path, encoding="utf-8") as fh:
        content = fh.read()
    if not content.startswith("---"):
        return {}
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}
    data = yaml.safe_load(parts[1]) or {}
    orgs = data.get("organizations", [])
    return {org["org_uri"]: org for org in orgs}


def load_release_manifest(path=RELEASE_MANIFEST_PATH):
    """Load .release-please-manifest.json. Returns dict keyed on package path."""
    if not os.path.isfile(path):
        return {}
    import json
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def load_annotated_schemas(root="src/linkml", release_manifest=None):
    """Load all schemas with annotations.utgiver.

    versjonsnummer kjem frå .release-please-manifest.json (nøkkel: skjemaet sin
    katalogsti), sidan schema.version vist seg å vere upålitelig — release-please
    sin extra-files-mekanisme oppdaterer ikkje alltid version-feltet i YAML-fila
    direkte. Fallback til schema.version berre for skjema som ikkje er
    release-please-pakkar (t.d. common-ap-no, xkos-ap-no).
    """
    release_manifest = release_manifest or {}
    schemas = []
    for path in sorted(glob.glob(f"{root}/*/*/*.yaml")):
        if not path.endswith("-schema.yaml"):
            continue
        with open(path, encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        if not data:
            continue
        parts = path.split("/")
        domain = parts[2] if len(parts) >= 3 else "unknown"
        if domain in EXCLUDED_DOMAINS:
            continue
        anns = data.get("annotations") or {}
        if not anns.get("utgiver"):
            continue
        package_path = os.path.dirname(path)
        version = release_manifest.get(package_path, data.get("version"))
        schemas.append({
            "path": path,
            "name": data.get("name"),
            "title": data.get("title"),
            "description": data.get("description"),
            "schema_id": data.get("id"),
            "domain": domain,
            "annotations": anns,
            "version": version,
        })
    return schemas


def group_schemas_by_org(schemas, org_registry):
    """Group schemas by annotations.utgiver. Returns (grouped_dict, unknown_list)."""
    grouped = {org_uri: [] for org_uri in org_registry}
    unknown = []
    for schema in schemas:
        org_uri = schema["annotations"].get("utgiver")
        if org_uri in org_registry:
            grouped[org_uri].append(schema)
        else:
            unknown.append(schema)
    return grouped, unknown


def find_catalog_data(org):
    """Resolve catalog data file path for org. Returns (path, exists)."""
    slug = org["catalog_slug"]
    path = CATALOG_DATA_TEMPLATE.format(slug=slug)
    return path, os.path.isfile(path)


def entry_name(entry):
    """Derive schema name from catalog entry id (last path segment)."""
    return (entry.get("id") or "").rstrip("/").split("/")[-1]


def update_entry(entry, schema):
    """Update annotation fields in existing entry. Returns True if changed."""
    anns = schema["annotations"]
    changed = False
    for ann_key, entry_key in ANNOTATION_FIELD_MAP:
        val = anns.get(ann_key)
        if val is not None and entry.get(entry_key) != val:
            entry[entry_key] = val
            changed = True
    version = schema.get("version")
    if version is not None and entry.get("versjonsnummer") != version:
        entry["versjonsnummer"] = version
        changed = True
    return changed


def make_stub(schema, org, catalog_base):
    """Create a new minimal catalog entry for a schema not yet in the catalog."""
    name = schema["name"] or "unknown"
    entry_id = f"{catalog_base}/{name}" if catalog_base else f"TODO/{name}"
    portal_url = f"{PORTAL_BASE}/{schema['domain']}/{name}/"
    stub = {
        "id": entry_id,
        "tittel": [schema["title"] or f"TODO: tittel for {name}"],
        "beskrivelse": [schema["description"] or f"TODO: beskriv {name}"],
        "utgiver": schema["annotations"].get("utgiver"),
        "identifikator_literal": entry_id,
        "informasjonsmodellidentifikator": portal_url,
        "kontaktpunkt": [org.get("contact_uri", "TODO")],
        "tema": ["TODO"],
        "lisens": "TODO",
    }
    for ann_key, entry_key in ANNOTATION_FIELD_MAP:
        val = schema["annotations"].get(ann_key)
        if val:
            stub[entry_key] = val
    if schema.get("version") is not None:
        stub["versjonsnummer"] = schema["version"]
    return stub


def process_org(org, schemas, dry_run):
    """Process one org: update existing entries, report new schemas as unmatched."""
    catalog_path, exists = find_catalog_data(org)
    if not exists:
        print(f"  ÅTVARSLE: Katalogdatafil ikkje funne: {catalog_path}")
        print(f"  Køyr: make new-org-catalog ORG={org['alias']}  for å opprette katalogen.")
        return

    with open(catalog_path, encoding="utf-8") as fh:
        catalog = yaml.safe_load(fh) or {}

    entries = catalog.get("informasjonsmodeller") or []
    entry_by_name = {entry_name(e): e for e in entries}

    catalog_base = ""
    if catalog.get("modellkataloger"):
        catalog_base = catalog["modellkataloger"][0].get("id", "").rstrip("/")

    updated_names = []
    added_names = []

    for schema in schemas:
        name = schema["name"]
        if not name:
            continue
        if name in entry_by_name:
            if update_entry(entry_by_name[name], schema):
                updated_names.append(name)
        else:
            stub = make_stub(schema, org, catalog_base)
            entries.append(stub)
            entry_by_name[name] = stub
            added_names.append(name)
            if catalog.get("modellkataloger"):
                modellkatalog = catalog["modellkataloger"][0]
                modellkatalog.setdefault("har_del", []).append(stub["id"])
                modellkatalog.setdefault("modell", []).append(stub["id"])

    if updated_names:
        print(f"  Oppdaterte: {', '.join(updated_names)}")
    if added_names:
        print(f"  Lagt til som nye stubs (treng manuell utfylling av TODO-felt): {', '.join(added_names)}")
    if not updated_names and not added_names:
        print("  Ingen endringar.")

    catalog["informasjonsmodeller"] = entries

    if not dry_run and (updated_names or added_names):
        with open(catalog_path, "w", encoding="utf-8") as fh:
            yaml.dump(
                catalog,
                fh,
                allow_unicode=True,
                sort_keys=False,
                default_flow_style=False,
            )
        print(f"  Skreiv {catalog_path}")
    elif dry_run and (updated_names or added_names):
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
    if not schemas:
        print("Ingen skjema med annotations.utgiver funne.")
        return

    grouped, unknown = group_schemas_by_org(schemas, org_registry)

    if unknown:
        print("Åtvarsel — skjema med utgiver som ikkje er i CODEOWNERS.md:")
        for s in unknown:
            print(f"  {s['name']} ({s['path']}) — utgiver: {s['annotations'].get('utgiver')}")
        print()

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
        process_org(org, org_schemas, args.dry_run)
        print()


if __name__ == "__main__":
    main()
