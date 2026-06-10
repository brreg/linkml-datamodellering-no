"""
update-modellkatalog.py

Les silver-annotasjonar frå alle skjema og oppdater Informasjonsmodell-innslag
i ein modellkatalog-datafil.

Oppdaterte felt (henta frå annotations.*):
  utgiver, endringsdato, utgivelsesdato, status

Ikkje-oppdaterte felt (manuelt vedlikehaldne):
  tittel, beskrivelse, tema, lisens, kontaktpunkt, m.m.

Kjøyr frå repo-rota:
    python3 src/assets/scripts/update-modellkatalog.py [--catalog PATH] [--dry-run]
"""
import argparse
import glob
import os
import sys

import yaml

DEFAULT_CATALOG = (
    "src/linkml/modellkatalog/brreg-modellkatalog/"
    "data/brreg-modellkatalog/brreg-modellkatalog.yaml"
)

ANNOTATION_FIELD_MAP = [
    ("utgiver",        "utgiver"),
    ("endringsdato",   "endringsdato"),
    ("utgivelsesdato", "utgivelsesdato"),
    ("status",         "status"),
]


def load_annotated_schemas(root="src/linkml"):
    schemas = []
    for path in sorted(glob.glob(f"{root}/*/*/*.yaml")):
        if not path.endswith("-schema.yaml"):
            continue
        with open(path) as fh:
            data = yaml.safe_load(fh)
        if not data:
            continue
        anns = data.get("annotations") or {}
        if not anns.get("utgiver"):
            continue
        schemas.append(
            {
                "path": path,
                "name": data.get("name"),
                "title": data.get("title"),
                "description": data.get("description"),
                "schema_id": data.get("id"),
                "annotations": anns,
            }
        )
    return schemas


def entry_name(entry):
    """Derive a short name from the catalog entry id (last path segment)."""
    return (entry.get("id") or "").rstrip("/").split("/")[-1]


def update_entry(entry, schema):
    """Apply annotation fields to an existing catalog entry. Returns True if changed."""
    anns = schema["annotations"]
    changed = False
    for ann_key, entry_key in ANNOTATION_FIELD_MAP:
        val = anns.get(ann_key)
        if val is not None and entry.get(entry_key) != val:
            entry[entry_key] = val
            changed = True
    return changed


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", default=DEFAULT_CATALOG, help="Sti til katalogdatafila")
    parser.add_argument("--dry-run", action="store_true", help="Vis endringar utan å skrive til disk")
    args = parser.parse_args(argv)

    if not os.path.isfile(args.catalog):
        print(f"FEIL: Fann ikkje katalogfil: {args.catalog}", file=sys.stderr)
        sys.exit(1)

    schemas = load_annotated_schemas()
    if not schemas:
        print("Ingen skjema med annotations.utgiver funne.")
        return

    with open(args.catalog) as fh:
        catalog = yaml.safe_load(fh) or {}

    entries = catalog.get("informasjonsmodeller") or []
    entry_by_name = {entry_name(e): e for e in entries}

    updated_names = []
    unmatched = []

    for schema in schemas:
        name = schema["name"]
        if not name:
            continue
        if name in entry_by_name:
            if update_entry(entry_by_name[name], schema):
                updated_names.append(name)
        else:
            unmatched.append(schema)

    if updated_names:
        print("Oppdaterte innslag:")
        for n in updated_names:
            print(f"  {n}")
    else:
        print("Ingen eksisterande innslag hadde utdaterte annotasjonar.")

    if unmatched:
        print("\nSkjema med annotasjonar som ikkje er i katalogen (legg til manuelt):")
        for s in unmatched:
            print(f"  {s['name']} ({s['path']})")

    if not args.dry_run and updated_names:
        with open(args.catalog, "w", encoding="utf-8") as fh:
            yaml.dump(
                catalog,
                fh,
                allow_unicode=True,
                sort_keys=False,
                default_flow_style=False,
            )
        print(f"\nSkreiv oppdatert katalog til {args.catalog}")
    elif args.dry_run and updated_names:
        print("\n(--dry-run: ingen filer endra)")


if __name__ == "__main__":
    main()
