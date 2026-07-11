#!/usr/bin/env python3
"""
Samlar alle begrep frå begrepssamlingar og genererer begrepskatalog per organisasjon.

For kvar organisasjon:
 1. Finn alle begrepssamlingar med aggregation.organization = <org-nr>
 2. Samle alle begrep-YAML-filer frå begrepssamling-<namn>/begrep/*.yaml
 3. Generer aggregert begrepskatalog.yaml i begrepskatalog/<org>-begrepskatalog/data/<org>-begrepskatalog/

Køyrast av CI før generatorfasen.
"""

import sys
from pathlib import Path
import yaml
from typing import Dict, List
from collections import defaultdict


def load_yaml(file_path: Path) -> Dict:
    """Last YAML-fil."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def write_yaml(file_path: Path, data: Dict):
    """Skriv YAML-fil."""
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        # Legg til header-kommentar
        f.write("# Generert av CI frå collect-concepts.py — ikkje rediger manuelt\n")
        f.write(f"# Samlar alle begrep frå begrepssamlingane til organisasjon\n\n")
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)


def find_begrepssamlingar(src_dir: Path) -> List[Path]:
    """Finn alle begrepssamlingar med build.yaml."""
    return sorted(src_dir.glob("*/begrepssamling-*/build.yaml"))


def collect_begrep_from_samling(samling_dir: Path) -> List[Dict]:
    """Samle alle begrep frå ei begrepssamling."""
    begrep_dir = samling_dir / "begrep"

    if not begrep_dir.exists():
        return []

    begrep_list = []
    for begrep_file in sorted(begrep_dir.glob("*.yaml")):
        try:
            begrep = load_yaml(begrep_file)
            begrep_list.append(begrep)
        except Exception as e:
            print(f"[WARNING] Kunne ikkje lese {begrep_file}: {e}", file=sys.stderr)

    return begrep_list


def generate_begrepskatalog(org_nr: str, catalog_name: str, begrepssamlingar: List[Path], output_dir: Path):
    """Generer begrepskatalog.yaml for ein organisasjon."""
    print(f"[INFO] Genererer {catalog_name}.yaml for organisasjon {org_nr}")

    catalog_dir = output_dir / catalog_name / "data" / catalog_name
    catalog_file = catalog_dir / f"{catalog_name}.yaml"

    # Samle alle begrep frå alle begrepssamlingane
    all_begrep = []
    for samling_dir in begrepssamlingar:
        samling_name = samling_dir.parent.name
        print(f"[INFO]   Samlar begrep frå {samling_name}")
        begrep_list = collect_begrep_from_samling(samling_dir.parent)
        all_begrep.extend(begrep_list)

    # Skriv til fil
    data = {"begrep": all_begrep}
    write_yaml(catalog_file, data)

    print(f"[INFO] ✓ Genererte {catalog_file} med {len(all_begrep)} begrep")


def main():
    """Hovudlogikk."""
    repo_root = Path.cwd()
    src_dir = repo_root / "src/linkml"
    begrepskatalog_dir = src_dir / "begrepskatalog"

    print("[INFO] Startar aggregering av begrep til begrepskatalogar")

    # Finn alle begrepssamlingar og grupper per organisasjon
    org_samlings: Dict[str, Dict] = defaultdict(lambda: {"catalog_name": None, "samlings": []})

    for build_file in find_begrepssamlingar(src_dir):
        try:
            build_data = load_yaml(build_file)
            aggregation = build_data.get("aggregation", {})

            org_nr = aggregation.get("organization")
            catalog_name = aggregation.get("catalog_name")

            if not org_nr or not catalog_name:
                print(f"[WARNING] Hoppar over {build_file.parent} — manglar aggregation.organization eller aggregation.catalog_name", file=sys.stderr)
                continue

            # Legg til i org_samlings
            org_samlings[org_nr]["catalog_name"] = catalog_name
            org_samlings[org_nr]["samlings"].append(build_file)

        except Exception as e:
            print(f"[WARNING] Kunne ikkje lese {build_file}: {e}", file=sys.stderr)

    # Generer begrepskatalog per organisasjon
    for org_nr, org_data in org_samlings.items():
        catalog_name = org_data["catalog_name"]
        samlings = org_data["samlings"]

        generate_begrepskatalog(org_nr, catalog_name, samlings, begrepskatalog_dir)

    print("[INFO] ✓ Ferdig med aggregering av begrepskatalogar")


if __name__ == "__main__":
    main()
