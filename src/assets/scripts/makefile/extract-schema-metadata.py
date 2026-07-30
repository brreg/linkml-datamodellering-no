#!/usr/bin/env python3
"""
Ekstraher metadata frå LinkML-skjemafil.
Brukt av generate-readme-tables.sh for dynamisk README-generering.
"""

import sys
import re

def extract_description(schema_file):
    """Hent description-feltet frå YAML-skjema (einlinjes eller multiline)."""
    with open(schema_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Finn description-blokk (kan vere einlinjes eller multiline)
    # Multiline sluttar når vi finn eit nytt felt (linje som startar med bokstav + kolon)
    desc_pattern = r'^description:\s*(.+?)(?=\n[a-z_]+:)'
    desc_match = re.search(desc_pattern, content, re.MULTILINE | re.DOTALL)

    if not desc_match:
        return ""

    desc_raw = desc_match.group(1).strip()

    # Fjern >- eller > (multiline-markørar)
    desc_raw = re.sub(r'^(>-?|>)\s*', '', desc_raw)

    # Fjern innleiande whitespace frå kvar linje
    lines = desc_raw.split('\n')
    cleaned_lines = [line.strip() for line in lines]

    # Join til einlinjes tekst
    description = ' '.join(cleaned_lines).strip()

    return description

def extract_see_also(schema_file):
    """Hent første URI frå see_also-lista."""
    with open(schema_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Finn see_also-blokk
    see_also_pattern = r'^see_also:\s*\n\s*-\s+(https?://[^\s]+)'
    see_also_match = re.search(see_also_pattern, content, re.MULTILINE)

    if not see_also_match:
        return ""

    return see_also_match.group(1).strip()

def extract_title(schema_file):
    """Hent title-feltet frå YAML-skjema."""
    with open(schema_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Finn title-felt (einlinjes)
    title_pattern = r'^title:\s*(.+)$'
    title_match = re.search(title_pattern, content, re.MULTILINE)

    if not title_match:
        return ""

    return title_match.group(1).strip()

def extract_annotations_utgiver(schema_file):
    """Hent annotations.utgiver frå YAML-skjema."""
    with open(schema_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Finn annotations-blokk, deretter utgiver-felt
    # annotations:
    #   utgiver: https://data.norge.no/organizations/974760673
    anno_pattern = r'^annotations:\s*\n\s+utgiver:\s+(.+)$'
    anno_match = re.search(anno_pattern, content, re.MULTILINE)

    if not anno_match:
        return ""

    return anno_match.group(1).strip()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Bruk: extract-schema-metadata.py <schema-fil> <field>", file=sys.stderr)
        print("  field: 'description', 'see_also', 'title', 'annotations.utgiver'", file=sys.stderr)
        sys.exit(1)

    schema_file = sys.argv[1]
    field = sys.argv[2]

    if field == 'description':
        print(extract_description(schema_file))
    elif field == 'see_also':
        print(extract_see_also(schema_file))
    elif field == 'title':
        print(extract_title(schema_file))
    elif field == 'annotations.utgiver':
        print(extract_annotations_utgiver(schema_file))
    else:
        print(f"Ukjend felt: {field}", file=sys.stderr)
        sys.exit(1)
