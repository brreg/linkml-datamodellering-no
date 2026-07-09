#!/usr/bin/env python3
"""
Genererer Informasjonsmodell-instans (ModelDCAT-AP-NO) frå eit LinkML-skjema.

Les 6 kjelder:
1. schema.yaml (toppnivå + annotations)
2. build.yaml (heimeside, har_del)
3. CODEOWNERS.md YAML-frontmatter (kontaktpunkt)
4. Skjemaet sine lokale klasser (inneholder_modellelement)
5. Genererte artefaktar (finnes_i_format)
6. annotations.er_profil_av (MVP workaround for DX-PROF)

Skriv: metadata/modelldcat.yaml (samla datafil med Informasjonsmodell + Kontaktopplysning + Standard)
"""

import sys
import os
from pathlib import Path
import yaml
import glob
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
        f.write("# Generert av CI frå generate-informasjonsmodell.py — ikkje rediger manuelt\n")
        f.write("# Kjelder: schema.yaml, build.yaml, CODEOWNERS.md, lokale klasser, genererte artefaktar\n\n")
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)


def parse_codeowners(schema_path: Path) -> Optional[Dict]:
    """
    Parse CODEOWNERS.md YAML-frontmatter og finn kontaktpunkt-data for skjemaet.

    Matcher schema_path mot organizations[].path_patterns.

    Returnerer: Dict med contact_uri og name, eller None
    """
    # Finn repo-root frå current working directory
    repo_root = Path.cwd()
    codeowners_path = repo_root / "CODEOWNERS.md"

    if not codeowners_path.exists():
        print(f"Warning: CODEOWNERS.md ikkje funne på {codeowners_path}", file=sys.stderr)
        return None

    with open(codeowners_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse YAML-frontmatter (mellom ``` yaml og ```)
    if '```yaml' not in content:
        print("Warning: Ingen YAML-frontmatter i CODEOWNERS.md", file=sys.stderr)
        return None

    yaml_start = content.find('```yaml') + 7
    yaml_end = content.find('```', yaml_start)
    yaml_content = content[yaml_start:yaml_end].strip()

    codeowners_data = yaml.safe_load(yaml_content)

    # Finn organisasjon som matcher schema_path
    # Gjer schema_path relativ til repo_root
    schema_rel_path = str(schema_path.resolve().relative_to(repo_root))

    for org in codeowners_data.get('organizations', []):
        for pattern in org.get('path_patterns', []):
            # Enkel glob-match (kan utvidast til meir robust matching)
            pattern_prefix = pattern.replace('/**', '')
            if schema_rel_path.startswith(pattern_prefix):
                return {
                    'contact_uri': org.get('contact_uri'),
                    'name': org.get('name')
                }

    print(f"Warning: Ingen organisasjon i CODEOWNERS.md matcher {schema_rel_path}", file=sys.stderr)
    return None


def extract_local_classes(schema: Dict) -> List[str]:
    """
    Ekstraher URI-ar til lokale klasser (ikkje tree_root).

    URI-format: <default_prefix><ClassName>
    """
    default_prefix = schema.get('default_prefix', '')
    local_classes = []

    for class_name, class_def in schema.get('classes', {}).items():
        # Ekskluder tree_root-containerklassen
        if class_def.get('tree_root'):
            continue

        # Bruk class_uri dersom definert, ellers default_prefix + class_name
        class_uri = class_def.get('class_uri')
        if class_uri:
            # Ekspander prefix (enkel versjon - kan utvidast)
            if ':' in class_uri:
                prefix, local_name = class_uri.split(':', 1)
                prefix_uri = schema.get('prefixes', {}).get(prefix)
                if prefix_uri:
                    class_uri = prefix_uri + local_name
        else:
            class_uri = default_prefix + class_name

        local_classes.append(class_uri)

    return local_classes


def discover_artifacts(schema_path: Path) -> List[str]:
    """
    Finn alle format modellen er tilgjengeleg i:
    1. LinkML-skjemaet sjølv (kjeldekode i src/)
    2. Genererte artefaktar (i generated/)

    Base-URL: Henta frå git remote

    Obs: mkdocs-URL er IKKJE med her sidan den er i heimeside-feltet.
    """
    # schema_path: src/linkml/<domain>/<modell>/<modell>-schema.yaml
    schema_parts = schema_path.parts
    linkml_idx = schema_parts.index('linkml')
    domain = schema_parts[linkml_idx + 1]
    modell = schema_parts[linkml_idx + 2]

    repo_root = Path.cwd()
    base_url_prefix = get_github_raw_base_url()

    artifacts = []

    # 1. Legg til LinkML-skjemaet sjølv (kjeldekode)
    schema_abs_path = schema_path.resolve()
    schema_rel_path = schema_abs_path.relative_to(repo_root)
    artifacts.append(base_url_prefix + str(schema_rel_path))

    # 2. Legg til genererte artefaktar
    generated_dir = repo_root / 'generated' / domain / modell

    if not generated_dir.exists():
        print(f"Warning: Generated-katalog ikkje funne: {generated_dir}", file=sys.stderr)
        return artifacts  # Returner i det minste LinkML-skjemaet

    base_url_generated = base_url_prefix + f"generated/{domain}/{modell}/"

    # Inkluder relevante genererte artefaktar
    patterns = [
        '*-schema.ttl',
        '*-schema.json',
        '*-ontology.ttl',
        '*-shapes.ttl',
        '*.puml',
        '*-context.jsonld',
        '*.proto',
        '*-openapi.yaml'
    ]

    for pattern in patterns:
        for file_path in generated_dir.glob(pattern):
            artifacts.append(base_url_generated + file_path.name)

    return sorted(artifacts)


def generate_langstring(nb_value: str, nn_value: Optional[str] = None) -> Dict[str, str]:
    """
    Generer LangString-dict med nb og nn.

    Dersom nn_value er None, fall tilbake til nb_value.
    """
    return {
        'nb': nb_value,
        'nn': nn_value if nn_value else nb_value
    }


def generate_mkdocs_url(schema_path: Path) -> str:
    """
    Generer mkdocs-dokumentasjons-URL frå schema-path.

    Format: https://brreg.github.io/linkml-datamodellering-no/<domain>/<modell>/
    """
    schema_parts = schema_path.parts
    linkml_idx = schema_parts.index('linkml')
    domain = schema_parts[linkml_idx + 1]
    modell = schema_parts[linkml_idx + 2]

    return f"https://brreg.github.io/linkml-datamodellering-no/{domain}/{modell}/"


def get_github_raw_base_url() -> str:
    """
    Hent GitHub raw base-URL frå git remote.

    Fallback: brreg/linkml-datamodellering-no
    """
    import subprocess

    try:
        # Hent remote URL
        result = subprocess.run(
            ['git', 'remote', 'get-url', 'origin'],
            capture_output=True,
            text=True,
            check=True
        )
        remote_url = result.stdout.strip()

        # Parse owner/repo frå git@github.com:owner/repo.git eller https://github.com/owner/repo.git
        if remote_url.startswith('git@github.com:'):
            # git@github.com:owner/repo.git
            parts = remote_url.split(':')[1].replace('.git', '').split('/')
            owner = parts[0]
            repo = parts[1]
            return f"https://raw.githubusercontent.com/{owner}/{repo}/main/"
        elif remote_url.startswith('https://github.com/'):
            # https://github.com/owner/repo.git
            parts = remote_url.replace('https://github.com/', '').replace('.git', '').split('/')
            owner = parts[0]
            repo = parts[1]
            return f"https://raw.githubusercontent.com/{owner}/{repo}/main/"
    except:
        pass

    # Fallback
    return "https://raw.githubusercontent.com/brreg/linkml-datamodellering-no/main/"


def generate_kontaktopplysning(kontaktpunkt_data: Dict) -> Dict:
    """
    Generer Kontaktopplysning-instans frå CODEOWNERS-data.

    Returnerer ein dict med id, navn_vcard og har_kontaktside.
    """
    contact_uri = kontaktpunkt_data.get('contact_uri')
    name = kontaktpunkt_data.get('name')

    return {
        'id': contact_uri,
        'navn_vcard': generate_langstring(name),
        'har_kontaktside': contact_uri
    }


def generate_standard(external_spec_url: str, external_spec_label: str) -> Dict:
    """
    Generer Standard-instans frå build.yaml external_spec_*.

    Returnerer ein dict med id, tittel og har_referanse.
    """
    return {
        'id': external_spec_url,
        'tittel': generate_langstring(external_spec_label),
        'har_referanse': external_spec_url
    }


def generate_modelldcat_data(schema_path: Path) -> Dict:
    """
    Generer samla ModelDCAT-datafil med Informasjonsmodell, Kontaktopplysning og Standard.

    Returnerer: Dict med containerklasse og alle instansar inline.
    """

    # 1. Les schema.yaml
    schema = load_yaml(schema_path)

    # 2. Les build.yaml
    build_path = schema_path.parent / 'build.yaml'
    build_config = load_yaml(build_path) if build_path.exists() else {}

    # 3. Parse CODEOWNERS.md (kontaktpunkt-data)
    kontaktpunkt_data = parse_codeowners(schema_path)

    # 4. Ekstraher lokale klasser
    inneholder_modellelement = extract_local_classes(schema)

    # 5. Finn genererte artefaktar
    finnes_i_format = discover_artifacts(schema_path)

    # 6. Bygg Informasjonsmodell-instans
    annotations = schema.get('annotations', {})

    informasjonsmodell = {
        # Frå schema.yaml toppnivå
        'id': schema.get('id'),
        'tittel': generate_langstring(
            schema.get('title', ''),
            annotations.get('tittel_nn')
        ),
        'beskrivelse': generate_langstring(
            schema.get('description', ''),
            annotations.get('beskrivelse_nn')
        ),
        'versjonsnummer': schema.get('version'),
        'lisens': schema.get('license'),

        # Frå schema.yaml annotations
        'utgiver': annotations.get('utgiver'),
        'endringsdato': annotations.get('endringsdato'),
        'utgivelsesdato': annotations.get('utgivelsesdato'),
        'status': annotations.get('status'),
    }

    # Valgfrie felt frå annotations
    if 'tema' in annotations:
        informasjonsmodell['tema'] = annotations['tema']

    if 'dekningsomraade' in annotations:
        informasjonsmodell['dekningsomraade'] = annotations['dekningsomraade']

    if 'nokkelord' in annotations:
        informasjonsmodell['nokkelord'] = annotations['nokkelord']

    if 'er_profil_av' in annotations:
        informasjonsmodell['er_profil_av'] = annotations['er_profil_av']

    # heimeside → vår mkdocs-dokumentasjon
    informasjonsmodell['heimeside'] = generate_mkdocs_url(schema_path)

    # er_i_samsvar_med → referanse til Standard-instans (inline)
    standard_instans = None
    if 'external_spec_url' in build_config:
        external_spec_label = build_config.get('external_spec_label', schema.get('title', ''))
        standard_instans = generate_standard(build_config['external_spec_url'], external_spec_label)
        informasjonsmodell['er_i_samsvar_med'] = [standard_instans]

    # har_del → submodellar
    if 'submodels' in build_config:
        default_prefix = schema.get('default_prefix', schema.get('id', ''))
        if not default_prefix.endswith('/'):
            default_prefix += '/'
        informasjonsmodell['har_del'] = [default_prefix + sm for sm in build_config['submodels']]

    # kontaktpunkt → referanse til Kontaktopplysning-instans (inline)
    kontaktopplysning_instans = None
    if kontaktpunkt_data:
        kontaktopplysning_instans = generate_kontaktopplysning(kontaktpunkt_data)
        informasjonsmodell['kontaktpunkt'] = [kontaktopplysning_instans]

    # Frå lokale klasser
    if inneholder_modellelement:
        informasjonsmodell['inneholder_modellelement'] = inneholder_modellelement

    # Frå genererte artefaktar
    if finnes_i_format:
        informasjonsmodell['finnes_i_format'] = finnes_i_format

    # Fjern None-verdiar
    informasjonsmodell = {k: v for k, v in informasjonsmodell.items() if v is not None}

    # Returner berre Informasjonsmodell-instans (med inline Kontaktopplysning og Standard)
    return informasjonsmodell


def main():
    if len(sys.argv) != 2:
        print("Usage: generate-informasjonsmodell.py <schema.yaml>")
        sys.exit(1)

    schema_path = Path(sys.argv[1])

    if not schema_path.exists():
        print(f"Error: {schema_path} eksisterer ikkje")
        sys.exit(1)

    print(f"Genererer Informasjonsmodell-instans for {schema_path}")

    # Generer
    modelldcat_data = generate_modelldcat_data(schema_path)

    # Skriv til metadata/modelldcat.yaml
    output_path = schema_path.parent / 'metadata' / 'modelldcat.yaml'
    write_yaml(output_path, modelldcat_data)

    print(f"✓ Generert: {output_path}")


if __name__ == '__main__':
    main()
