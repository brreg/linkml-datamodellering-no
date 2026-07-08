#!/usr/bin/env python3
"""
Genererer per-org Modellkatalog-instansar frå alle metadata/modelldcat.yaml-filer.

Les alle Informasjonsmodell-instansar, grupper dei etter utgiver (frå CODEOWNERS.md),
og generer éi katalogfil per organisasjon i src/linkml/modellkatalog/<org>/data/<org>/<org>.yaml.

Dette scriptet erstatter update-modellkatalog.py ved å generere komplette katalogfiler
i staden for berre oppdatere eksisterande felt.
"""

import sys
from pathlib import Path
import yaml
from typing import Dict, List, Optional


def load_yaml(file_path: Path) -> Dict:
    """Last YAML-fil."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def write_yaml(file_path: Path, data: Dict):
    """Skriv YAML-fil."""
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        # Legg til header-kommentar
        f.write("# Generert av CI frå generate-modellkatalog.py — ikkje rediger manuelt\n")
        f.write("# Samlar alle Informasjonsmodell-instansar per organisasjon frå metadata/modelldcat.yaml\n\n")
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)


def generate_langstring(nb_value: str, nn_value: str = None) -> Dict[str, str]:
    """
    Generer LangString-dict med nb og nn.

    Dersom nn_value er None, fall tilbake til nb_value.
    """
    return {
        'nb': nb_value,
        'nn': nn_value if nn_value else nb_value
    }


def load_codeowners() -> Dict:
    """
    Les CODEOWNERS.md YAML-frontmatter.

    Returnerer: Dict med org_uri som nøkkel, org-data som verdi.
    """
    repo_root = Path.cwd()
    codeowners_path = repo_root / "CODEOWNERS.md"

    if not codeowners_path.exists():
        print(f"Error: CODEOWNERS.md ikkje funne på {codeowners_path}", file=sys.stderr)
        return {}

    with open(codeowners_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse YAML-frontmatter (mellom ``` yaml og ```)
    if '```yaml' not in content:
        print("Error: CODEOWNERS.md manglar YAML-frontmatter", file=sys.stderr)
        return {}

    yaml_start = content.find('```yaml') + 7
    yaml_end = content.find('```', yaml_start)

    if yaml_end == -1:
        print("Error: Ugyldig YAML-frontmatter i CODEOWNERS.md", file=sys.stderr)
        return {}

    yaml_content = content[yaml_start:yaml_end].strip()
    codeowners_data = yaml.safe_load(yaml_content)

    # Bygg dict med org_uri som nøkkel
    org_registry = {}
    for org in codeowners_data.get('organizations', []):
        org_uri = org.get('org_uri')
        if org_uri:
            org_registry[org_uri] = org

    return org_registry


def discover_modelldcat_files() -> List[Path]:
    """
    Finn alle metadata/modelldcat.yaml-filer i src/linkml/**/metadata/.

    Returnerer sortert liste (alfabetisk etter domain/modell-path).
    """
    repo_root = Path.cwd()
    src_linkml = repo_root / 'src' / 'linkml'

    if not src_linkml.exists():
        print(f"Warning: src/linkml/ katalog ikkje funne på {src_linkml}", file=sys.stderr)
        return []

    # Finn alle metadata/modelldcat.yaml-filer
    modelldcat_files = sorted(src_linkml.glob('**/metadata/modelldcat.yaml'))

    return modelldcat_files


def convert_to_org_uri(standard_uri: str, org_catalog_base: str) -> str:
    """
    Konverter standard URI (https://data.norge.no/...) til org-spesifikk URI.

    Eksempel:
        https://data.norge.no/ngr/ngr-virksomhet
        → https://brreg.no/modellkatalogar/brreg-modellkatalog/ngr-virksomhet
    """
    # Ekstraher siste segment (modellnamn)
    modell_name = standard_uri.rstrip('/').split('/')[-1]
    return f"{org_catalog_base}/{modell_name}"


def convert_informasjonsmodell_to_org_format(modell: Dict, org: Dict) -> Dict:
    """
    Konverter Informasjonsmodell-instans frå standard format til org-spesifikk format.

    Endringar:
    - id: https://data.norge.no/... → https://<org-domene>/modellkatalogar/<catalog_slug>/...
    - Legg til identifikator_literal (same som id)
    - Legg til informasjonsmodellidentifikator (heimeside)
    - Legg til type_concept: LogicalDataModel
    - Konverter tittel/beskrivelse frå LangString {nb, nn} til liste [string]
    - Behald kontaktpunkt, er_i_samsvar_med, inneholder_modellelement som dei er
    """
    catalog_slug = org.get('catalog_slug')
    org_domain = org.get('org_uri', 'https://example.org').replace('https://', '').replace('http://', '')
    catalog_base = f"https://{org_domain}/modellkatalogar/{catalog_slug}"

    # Konverter standard URI til org-spesifikk URI
    original_id = modell.get('id', '')
    new_id = convert_to_org_uri(original_id, catalog_base)

    # Bygg org-formatert Informasjonsmodell
    org_modell = {
        'id': new_id,
        'tittel': [modell.get('tittel', {}).get('nb', '')],  # LangString → liste
        'beskrivelse': [modell.get('beskrivelse', {}).get('nb', '')],  # LangString → liste
    }

    # Valgfrie felt
    if 'relatert_begrep' in modell:
        org_modell['relatert_begrep'] = modell['relatert_begrep']

    org_modell['utgiver'] = modell.get('utgiver')
    org_modell['identifikator_literal'] = new_id
    org_modell['informasjonsmodellidentifikator'] = modell.get('heimeside')

    # Kontaktpunkt — ekstraher URI frå inline-instans dersom det er dict
    kontaktpunkt = modell.get('kontaktpunkt', [])
    if kontaktpunkt:
        if isinstance(kontaktpunkt[0], dict):
            org_modell['kontaktpunkt'] = [kp.get('id') for kp in kontaktpunkt if kp.get('id')]
        else:
            org_modell['kontaktpunkt'] = kontaktpunkt

    # Tema
    if 'tema' in modell:
        org_modell['tema'] = modell['tema']

    # Lisens
    if 'lisens' in modell:
        org_modell['lisens'] = modell['lisens']

    # Status
    if 'status' in modell:
        org_modell['status'] = modell['status']

    # Datoar
    if 'utgivelsesdato' in modell:
        org_modell['utgivelsesdato'] = modell['utgivelsesdato']
    if 'endringsdato' in modell:
        org_modell['endringsdato'] = modell['endringsdato']

    # Versjonsnummer
    if 'versjonsnummer' in modell:
        org_modell['versjonsnummer'] = modell['versjonsnummer']

    # Type (alltid LogicalDataModel for LinkML-skjema)
    org_modell['type_concept'] = 'https://data.norge.no/vocabulary/modelldcatno#LogicalDataModel'

    # Modellelement — konverter URI-ar til org-spesifikke
    if 'inneholder_modellelement' in modell:
        # Ekstraher klassenamn frå URI og konverter til org-format
        modellelement = []
        for element_uri in modell['inneholder_modellelement']:
            class_name = element_uri.rstrip('/').split('/')[-1]
            org_element_uri = f"{new_id}/{class_name}"
            modellelement.append(org_element_uri)
        org_modell['inneholder_modellelement'] = modellelement

    return org_modell


def generate_modellkatalog_for_org(org: Dict, informasjonsmodeller: List[Dict]) -> Dict:
    """
    Generer Modellkatalog-instans for éin organisasjon.

    Returnerer: Dict med 'modellkataloger' og 'informasjonsmodeller'.
    """
    catalog_slug = org.get('catalog_slug')
    org_name = org.get('name')
    org_uri = org.get('org_uri')
    contact_uri = org.get('contact_uri')

    org_domain = org_uri.replace('https://', '').replace('http://', '')
    catalog_id = f"https://{org_domain}/modellkatalogar/{catalog_slug}"

    # Konverter alle Informasjonsmodell-instansar til org-format
    org_informasjonsmodeller = []
    modell_ids = []
    for modell in informasjonsmodeller:
        org_modell = convert_informasjonsmodell_to_org_format(modell, org)
        org_informasjonsmodeller.append(org_modell)
        modell_ids.append(org_modell['id'])

    # Bygg Modellkatalog-metadata
    modellkatalog = {
        'id': catalog_id,
        'tittel': [f"{org_name} - Modellkatalog"],
        'beskrivelse': [f"Informasjonsmodellar frå {org_name} i LinkML-format, tilgjengeleg som SHACL, JSON Schema, OWL og RDF/Turtle."],
        'identifikator_literal': catalog_id,
        'utgiver': org_uri,
        'kontaktpunkt': [contact_uri] if contact_uri else [],
        'har_del': modell_ids,
        'modell': modell_ids,
        'spraak': ['http://publications.europa.eu/resource/authority/language/NOB'],
        'lisens': 'http://publications.europa.eu/resource/authority/licence/CC_BY_4_0',
    }

    # Returner samla struktur
    return {
        'modellkataloger': [modellkatalog],
        'informasjonsmodeller': org_informasjonsmodeller
    }


def main():
    print("Genererer per-org Modellkatalog-instansar")

    # 1. Last CODEOWNERS.md
    org_registry = load_codeowners()
    if not org_registry:
        print("Error: Ingen organisasjonar funne i CODEOWNERS.md", file=sys.stderr)
        sys.exit(1)

    print(f"✓ Lasta {len(org_registry)} organisasjonar frå CODEOWNERS.md")

    # 2. Finn alle Informasjonsmodell-instansar
    modelldcat_files = discover_modelldcat_files()
    if not modelldcat_files:
        print("Warning: Ingen Informasjonsmodell-instansar funne", file=sys.stderr)
        sys.exit(0)

    print(f"✓ Fann {len(modelldcat_files)} metadata/modelldcat.yaml-filer")

    # 3. Last alle Informasjonsmodell-instansar og grupper etter utgiver
    org_models = {org_uri: [] for org_uri in org_registry}

    for file_path in modelldcat_files:
        try:
            modell = load_yaml(file_path)
            utgiver = modell.get('utgiver')

            if not utgiver:
                print(f"Warning: {file_path} manglar 'utgiver', hoppar over", file=sys.stderr)
                continue

            if utgiver in org_registry:
                org_models[utgiver].append(modell)
            else:
                print(f"Warning: {file_path} har utgiver {utgiver} som ikkje finst i CODEOWNERS.md", file=sys.stderr)

        except Exception as e:
            print(f"Warning: Kunne ikkje laste {file_path}: {e}", file=sys.stderr)

    # 4. Generer per-org katalogfiler
    generated_count = 0
    for org_uri, org in org_registry.items():
        modeller = org_models.get(org_uri, [])
        if not modeller:
            print(f"  Hoppar over {org.get('name')} (ingen modellar)")
            continue

        catalog_slug = org.get('catalog_slug')
        if not catalog_slug:
            print(f"Warning: {org.get('name')} manglar 'catalog_slug', hoppar over", file=sys.stderr)
            continue

        # Generer katalog
        katalog_data = generate_modellkatalog_for_org(org, modeller)

        # Skriv til fil
        output_path = Path(f"src/linkml/modellkatalog/{catalog_slug}/data/{catalog_slug}/{catalog_slug}.yaml")
        write_yaml(output_path, katalog_data)

        print(f"✓ Generert: {output_path} ({len(modeller)} modellar)")
        generated_count += 1

    print(f"\n✓ Totalt {generated_count} organisasjonskatalogar generert")


if __name__ == '__main__':
    main()
