#!/usr/bin/env python3
"""
Samlar alle begrep frå begrepssamlingar og genererer begrepskatalog per organisasjon.

For kvar organisasjon:
 1. Finn alle begrepssamlingar med aggregation.organization = <org-nr> (frå build.yaml eller CODEOWNERS.md)
 2. Samle alle begrep-YAML-filer frå begrepssamling-<namn>/begrep/*.yaml
 3. Generer aggregert begrepskatalog.yaml i begrepskatalog/<org>-begrepskatalog/data/<org>-begrepskatalog/

Fallback-orden for aggregation-metadata:
 1. Eksplisitt aggregation-blokk i build.yaml
 2. Auto-deteksjon frå CODEOWNERS.md basert på path-matching
 3. Feil/warning dersom ingen av dei to finn eigar-org

Køyrast av CI før generatorfasen.
"""

import sys
from pathlib import Path
from typing import Dict, List, Optional
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "src" / "assets" / "scripts"))
from utils.yaml_io import load_yaml, write_yaml  # noqa: E402
from utils.codeowners import load_codeowners, find_owner_org  # noqa: E402


def get_aggregation_metadata(begrepssamling_dir: Path, orgs: List[Dict]) -> Optional[Dict]:
    """
    Hent aggregation-metadata frå build.yaml, eller frå CODEOWNERS.md som fallback.

    Returns:
        Dict med 'organization' og 'catalog_name', eller None dersom ikkje funne
    """
    build_yaml = begrepssamling_dir / "build.yaml"
    if not build_yaml.exists():
        return None

    build_data = load_yaml(build_yaml)

    # Dersom aggregation-blokka finst, bruk den
    if "aggregation" in build_data and build_data["aggregation"]:
        return build_data["aggregation"]

    # Elles: finn organisasjon frå CODEOWNERS.md
    # Konverter til relativ sti frå repo-root
    repo_root = Path.cwd()
    try:
        relative_path = begrepssamling_dir.relative_to(repo_root)
    except ValueError:
        # begrepssamling_dir er ikkje under repo_root
        return None

    owner_org = find_owner_org(relative_path, orgs)
    if not owner_org:
        print(f"[WARNING] Kan ikkje finne eigar-org for {relative_path} i CODEOWNERS.md", file=sys.stderr)
        return None

    # Ekstraher organisasjonsnummer frå org_uri
    org_uri = owner_org.get("org_uri", "")
    org_number = org_uri.split("/")[-1] if org_uri else None

    # Utlei begrepskatalog_slug frå catalog_slug
    catalog_slug = owner_org.get("catalog_slug", "")
    begrepskatalog_slug = catalog_slug.replace("-modellkatalog", "-begrepskatalog") if catalog_slug else None

    if not org_number or not begrepskatalog_slug:
        print(f"[WARNING] Ugyldig org_uri eller catalog_slug for {owner_org.get('alias')}", file=sys.stderr)
        return None

    print(f"[INFO] Auto-detektert {relative_path} → org {org_number} ({owner_org.get('name')}), katalog {begrepskatalog_slug}")

    return {
        "organization": org_number,
        "catalog_name": begrepskatalog_slug,
    }


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
    write_yaml(
        catalog_file, data,
        generated_by=Path(__file__).name,
        note="Samlar alle begrep frå begrepssamlingane til organisasjon",
    )

    print(f"[INFO] ✓ Genererte {catalog_file} med {len(all_begrep)} begrep")


def main():
    """Hovudlogikk."""
    repo_root = Path.cwd()
    src_dir = repo_root / "src/linkml"
    begrepskatalog_dir = src_dir / "begrepskatalog"

    print("[INFO] Startar aggregering av begrep til begrepskatalogar")

    # Last CODEOWNERS.md for auto-deteksjon
    orgs = load_codeowners(repo_root)
    if orgs:
        print(f"[INFO] Lasta {len(orgs)} organisasjonar frå CODEOWNERS.md")

    # Finn alle begrepssamlingar og grupper per organisasjon
    org_samlings: Dict[str, Dict] = defaultdict(lambda: {"catalog_name": None, "samlings": []})

    for build_file in find_begrepssamlingar(src_dir):
        try:
            # Hent aggregation-metadata (frå build.yaml eller CODEOWNERS.md)
            aggregation = get_aggregation_metadata(build_file.parent, orgs)

            if not aggregation:
                print(f"[WARNING] Hoppar over {build_file.parent} — manglar aggregation-metadata", file=sys.stderr)
                continue

            org_nr = aggregation.get("organization")
            catalog_name = aggregation.get("catalog_name")

            if not org_nr or not catalog_name:
                print(f"[WARNING] Hoppar over {build_file.parent} — ugyldig aggregation-metadata", file=sys.stderr)
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
