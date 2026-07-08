#!/usr/bin/env python3
"""
Genererer Modellkatalog-instans (ModelDCAT-AP-NO) frå alle Informasjonsmodell-instansar.

Les alle metadata/modelldcat.yaml-filer i src/linkml/**/metadata/ og aggregerer
dei til ein Modellkatalog-instans i generated/modellkatalog.yaml.
"""

import sys
from pathlib import Path
import yaml
from typing import Dict, List


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
        f.write("# Samlar alle Informasjonsmodell-instansar frå src/linkml/**/metadata/modelldcat.yaml\n\n")
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


def discover_informasjonsmodell_files() -> List[Path]:
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


def generate_modellkatalog() -> Dict:
    """Generer Modellkatalog-instans frå alle Informasjonsmodell-instansar."""

    # 1. Finn alle Informasjonsmodell-instansar
    modelldcat_files = discover_informasjonsmodell_files()

    if not modelldcat_files:
        print("Warning: Ingen Informasjonsmodell-instansar funne i src/linkml/**/metadata/", file=sys.stderr)

    # 2. Last alle Informasjonsmodell-instansar
    informasjonsmodellar = []
    for file_path in modelldcat_files:
        try:
            modell = load_yaml(file_path)
            informasjonsmodellar.append(modell)
            print(f"✓ Inkludert: {file_path.relative_to(Path.cwd())}")
        except Exception as e:
            print(f"Warning: Kunne ikkje laste {file_path}: {e}", file=sys.stderr)

    # 3. Bygg Modellkatalog-instans
    modellkatalog = {
        'id': 'https://data.norge.no/modellkatalog',
        'tittel': generate_langstring(
            'Felles modellkatalog for LinkML-modellar',
            'Felles modellkatalog for LinkML-modellar'
        ),
        'beskrivelse': generate_langstring(
            'Samling av alle informasjonsmodellar i linkml-datamodellering-no-repoet.',
            'Samling av alle informasjonsmodellar i linkml-datamodellering-no-repoet.'
        ),
        'utgiver': 'https://data.norge.no/organizations/991825827',
        'kontaktpunkt': [
            'https://www.digdir.no/om-oss/kontakt-oss/887'
        ],
        'modell': informasjonsmodellar
    }

    return modellkatalog


def main():
    print("Genererer Modellkatalog-instans")

    # Generer
    modellkatalog = generate_modellkatalog()

    # Skriv til generated/modellkatalog.yaml
    output_path = Path.cwd() / 'generated' / 'modellkatalog.yaml'
    write_yaml(output_path, modellkatalog)

    print(f"✓ Generert: {output_path}")
    print(f"  Totalt {len(modellkatalog['modell'])} informasjonsmodellar")


if __name__ == '__main__':
    main()
