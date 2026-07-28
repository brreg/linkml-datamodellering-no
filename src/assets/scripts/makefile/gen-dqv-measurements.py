#!/usr/bin/env python3
"""
Reknar ut DQV-kvalitetsmålingar (fullstendighet, aktualitet) for datafiler med
data_policy: felles-begrepskatalog eller felles-datakatalog, og skriv
dqv:hasQualityMeasurement-referansar attende til datafila.

Skriver attende med målretta tekstendringar (ikkje full YAML-dump), slik at
kommentarar og handskriven formatering i datafila er bevart.

Målingane får stabile id-ar (.../dqv/fullstendighet, .../dqv/aktualitet), så
gjentatte køyringar oppdaterer verdiane i staden for å hope opp duplikat.

Føresetnad: containeren (samlingar/modellkataloger) har akkurat éin oppføring
i datafila — målinga kan då knytast til den med tekstinnsetting.

Køyr frå repo-rota:
    python3 src/assets/scripts/gen-dqv-measurements.py [--dry-run]
"""
import argparse
import glob
import re
from datetime import date
from pathlib import Path

import yaml

METRIC_COMPLETENESS = "https://data.norge.no/vocabulary/quality-metric#qm-completeness-1004"
METRIC_CURRENTNESS = "https://data.norge.no/vocabulary/quality-metric#qm-currentness-1001"

# Per data_policy: korleis datafila er strukturert og kva som skal målast.
PROFILES = {
    "felles-begrepskatalog": {
        "items_key": "begrep",
        "required_field": "har_definisjon",
        "item_label": "begrep",
        "missing_label": "definisjon",
        "container_key": "samlingar",
        "date_field": None,
    },
    "felles-datakatalog": {
        "items_key": "informasjonsmodeller",
        "required_field": "lisens",
        "item_label": "informasjonsmodellar",
        "missing_label": "lisens",
        "container_key": "modellkataloger",
        "date_field": "endringsdato",
    },
}


def find_data_manifests(root="src/linkml"):
    """Finn alle datafil-manifest (build.yaml med data_policy, utan generators:)."""
    for path in sorted(glob.glob(f"{root}/*/*/data/*/build.yaml")):
        yield Path(path)


def load_yaml(path):
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def compute_completeness(items, required_field):
    total = len(items)
    missing = sum(1 for it in items if not it.get(required_field))
    rate = round(missing / total, 4) if total else 0.0
    return total, missing, rate


def compute_max_age_days(items, date_field, today):
    """Største antal dagar mellom today og date_field blant items. None viss ingen dato finst."""
    ages = []
    for it in items:
        raw = it.get(date_field)
        if not raw:
            continue
        try:
            d = date.fromisoformat(str(raw))
        except ValueError:
            continue
        ages.append((today - d).days)
    return max(ages) if ages else None


def find_top_level_block(text, key):
    """Finn (start, slutt) for ein toppnivåblokk 'key:\\n...' — slutt er rett før neste
    toppnivånøkkel (linje med 'identifikator:' utan innrykk) eller EOF. None viss
    nøkkelen ikkje finst. Linjer som startar med '-' (listeelement ved kol. 0, t.d.
    i flat-liste-stil) er ikkje ein ny toppnivånøkkel."""
    m = re.search(rf"^{re.escape(key)}:\n", text, re.MULTILINE)
    if not m:
        return None
    body_start = m.end()
    m2 = re.search(r"^[a-z_]+:", text[body_start:], re.MULTILINE)
    end = body_start + m2.start() if m2 else len(text)
    return m.start(), end


def detect_style(block_text):
    """Sample nøkkel- og listeinnrykk frå eit eksisterande multivalued felt i blokka.
    Returnerer (key_indent, list_indent) eller fallback ('  ', '  ') viss ikkje funne."""
    m = re.search(r"^(?P<key_indent>[ ]+)[a-z_]+:\n(?P<list_indent>[ ]+)- ", block_text, re.MULTILINE)
    if m:
        return m.group("key_indent"), m.group("list_indent")
    return "  ", "  "


def upsert_list_field(block_text, key_indent, field_name, values):
    """Sett inn eller oppdater 'key_indent + field_name:' + listeverdiar i blokka."""
    _, list_indent = detect_style(block_text)
    new_field = f"{key_indent}{field_name}:\n" + "".join(f"{list_indent}- {v}\n" for v in values)
    field_re = re.compile(
        rf"^{re.escape(key_indent)}{re.escape(field_name)}:\n(?:[ ]+- .*\n)*", re.MULTILINE
    )
    if field_re.search(block_text):
        return field_re.sub(new_field, block_text, count=1)
    return block_text + new_field


def render_entries(entries):
    """Render ei liste av målings-dict til YAML-tekst med toppnivå-stil (dash ved kol. 0)."""
    text = yaml.safe_dump(entries, allow_unicode=True, sort_keys=False, default_flow_style=False)
    return text


def process_datafile(manifest_path, profile, today, dry_run):
    data_dir = manifest_path.parent
    catalog = data_dir.name
    data_path = data_dir / f"{catalog}.yaml"
    if not data_path.is_file():
        return False

    data = load_yaml(data_path)
    items = data.get(profile["items_key"]) or []
    if not items:
        print(f"  HOPP OVER {data_path}: ingen '{profile['items_key']}'")
        return False

    containers = data.get(profile["container_key"]) or []
    if len(containers) != 1:
        print(
            f"  HOPP OVER {data_path}: '{profile['container_key']}' har "
            f"{len(containers)} oppføringar (krev akkurat 1 for trygg tekstinnsetting)"
        )
        return False
    base = (containers[0].get("id") or "").rstrip("/")
    if not base:
        print(f"  HOPP OVER {data_path}: '{profile['container_key']}'[0] har ingen id")
        return False

    existing_measurements = {m["id"]: m for m in (data.get("kvalitetsmaalingar") or []) if "id" in m}

    total, missing, rate = compute_completeness(items, profile["required_field"])
    completeness_id = f"{base}/dqv/fullstendighet"
    existing_measurements[completeness_id] = {
        "id": completeness_id,
        "er_kvalitetsmaaling_av": METRIC_COMPLETENESS,
        "har_numerisk_verdi": rate,
        "har_merknad": [
            f"{missing} av {total} {profile['item_label']} ({rate * 100:.1f} %) "
            f"manglar verdi for {profile['missing_label']}."
        ],
    }
    new_ids = [completeness_id]

    if profile["date_field"]:
        max_age = compute_max_age_days(items, profile["date_field"], today)
        if max_age is not None:
            currentness_id = f"{base}/dqv/aktualitet"
            existing_measurements[currentness_id] = {
                "id": currentness_id,
                "er_kvalitetsmaaling_av": METRIC_CURRENTNESS,
                "har_tekst_verdi": f"P{max_age}D",
                "har_merknad": [
                    f"Eldste {profile['date_field']} blant {profile['item_label']} er "
                    f"{max_age} dag(ar) gammal."
                ],
            }
            new_ids.append(currentness_id)

    text = data_path.read_text(encoding="utf-8")

    # 1) Sett inn/oppdater har_kvalitetsmaaling-referansen i container-oppføringa.
    container_block = find_top_level_block(text, profile["container_key"])
    if container_block is None:
        print(f"  HOPP OVER {data_path}: fann ikkje '{profile['container_key']}'-blokk i tekst")
        return False
    block_start, block_end = container_block
    block_text = text[block_start:block_end]
    key_indent, _ = detect_style(block_text)
    existing_refs_re = re.search(
        rf"^{re.escape(key_indent)}har_kvalitetsmaaling:\n(?:[ ]+- (.*)\n)*", block_text, re.MULTILINE
    )
    existing_refs = set()
    if existing_refs_re:
        existing_refs = set(re.findall(r"^[ ]+- (.*)$", existing_refs_re.group(0), re.MULTILINE))
    all_refs = sorted(existing_refs | set(new_ids))
    block_text = upsert_list_field(block_text, key_indent, "har_kvalitetsmaaling", all_refs)
    text = text[:block_start] + block_text + text[block_end:]

    # 2) Sett inn/oppdater toppnivå-blokka kvalitetsmaalingar:.
    new_section = "kvalitetsmaalingar:\n" + render_entries(list(existing_measurements.values()))
    top_block = find_top_level_block(text, "kvalitetsmaalingar")
    if top_block is not None:
        text = text[: top_block[0]] + new_section + text[top_block[1] :]
    else:
        if not text.endswith("\n"):
            text += "\n"
        text += new_section

    if not dry_run:
        data_path.write_text(text, encoding="utf-8")

    prefix = "[dry-run] " if dry_run else ""
    print(f"  {prefix}OPPDATERT: {data_path} ({', '.join(new_ids)})")
    return True


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Vis endringar utan å skrive til disk")
    args = parser.parse_args(argv)

    today = date.today()
    changed = 0
    for manifest_path in find_data_manifests():
        manifest = load_yaml(manifest_path)
        policy = manifest.get("data_policy")
        profile = PROFILES.get(policy)
        if not profile:
            continue
        if process_datafile(manifest_path, profile, today, args.dry_run):
            changed += 1

    print(f"\n{changed} datafil(er) oppdatert.")


if __name__ == "__main__":
    main()
