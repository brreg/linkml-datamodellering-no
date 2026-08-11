#!/usr/bin/env python3
"""Samla YAML-lesing for mkdocs/publish.sh sin Steg 1.5/Steg 2.

Erstattar opptil ~211 separate `podman run`-kall (eitt per skjema/manifest-
felt, sjå specs/backlog/reduser-podman-kall-docs-publish.md) med EIN
containerprosess som les alle build.yaml/*-schema.yaml/CODEOWNERS.md éin
gong kvar.

Input (stdin): éi linje per skjema som skal dokumenterast, felt skilt med
\x1f (unit separator):
    domain\x1fschema\x1fschema_file_path\x1fmanifest_path
`schema_file_path`/`manifest_path` er tomme strengar dersom fila ikkje
finst (same semantikk som `[ -n "$schema_file" ]`-vaktene i bash-koden
dette scriptet erstattar).

Output (stdout): tre seksjonar, skilde med `### SUBMODELS` / `### SCHEMAS`
/ `### ORGS`-linjer, felt skilt med \x1f. Bash-sida les seksjonane inn i
associative arrays — same mønster som SCHEMA_NAME_TO_DOMAIN_SERIALIZED
o.l. i publish.sh, ikkje JSON (unngår ei ny jq-avhengigheit på hosten).
"""
import os
import re
import sys

import yaml

REPO_ROOT = "/work"
US = "\x1f"


def read_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f) or {}


def read_manifest(manifest_path):
    """Same fallback-semantikk som load_manifest_cache() i metadata_parsers.sh."""
    policy, url, label = "bronze", "", ""
    if not manifest_path:
        return policy, url, label
    try:
        d = read_yaml(manifest_path)
    except Exception as e:
        print(f"ÅTVARING: kunne ikkje lese {manifest_path} — bruker default-verdiar ({e})", file=sys.stderr)
        return policy, url, label
    return (
        str(d.get("validation_policy", "bronze")),
        str(d.get("external_spec_url", "")),
        str(d.get("external_spec_label", "")),
    )


def detect_quickstart(schema):
    """Same logikk som heredocen i kom_i_gang.sh: finn container-klasse,
    representativ eksempel-klasse (Obligatorisk > Anbefalt > første ikkje-
    container-klasse > containerklassen sjølv), og eit snake_case
    variabelnamn."""
    classes = schema.get("classes", {}) or {}

    container_class = None
    for cls_name, cls_def in classes.items():
        if isinstance(cls_def, dict) and cls_def.get("tree_root"):
            container_class = cls_name
            break

    def first_match(subset):
        for cls_name, cls_def in classes.items():
            if not isinstance(cls_def, dict) or cls_name == container_class:
                continue
            if subset in (cls_def.get("in_subset") or []):
                return cls_name
        return None

    example_class = first_match("Obligatorisk") or first_match("Anbefalt")
    if not example_class:
        for cls_name, cls_def in classes.items():
            if not isinstance(cls_def, dict) or cls_name == container_class:
                continue
            if not cls_def.get("abstract"):
                example_class = cls_name
                break
    if not example_class:
        example_class = container_class or "Container"

    example_var = re.sub("([a-z0-9])([A-Z])", r"\1_\2", example_class).lower()
    return example_class, example_var


def read_schema_file(schema_file_path):
    """version/title/description/example_class/example_var/quickstart_policy
    — tom streng på manglande felt/fil, same som dei einskilde call-sites
    sine fallback-tomme-strengar før (bash-sida legg på sine eigne
    fallback-verdiar etterpå, uendra).

    quickstart_policy vert lese frå build.yaml i SAME katalog som
    schema-fila ligg i (ikkje frå den konstruerte
    src/linkml/<domain>/<schema>/build.yaml-stien) — dette matchar
    kom_i_gang.sh sin heredoc-logikk før denne refaktoreringa. For
    delmodell-skjema (t.d. dqv-core, som ligg i dqv-ap-no/ sin katalog)
    gjev dette **ikkje** same verdi som `policy`-feltet (som brukar den
    konstruerte, ofte ikkje-eksisterande <schema>/build.yaml-stien og difor
    fell tilbake til 'bronze') — dette er ein pre-eksisterande, uendra
    inkonsistens i genererte sider, ikkje ein ny bug. Sjå
    specs/backlog/reduser-podman-kall-docs-publish.md."""
    if not schema_file_path:
        return "", "", "", "", "", "bronze"
    try:
        d = read_yaml(schema_file_path)
    except Exception as e:
        print(f"ÅTVARING: kunne ikkje lese {schema_file_path} ({e})", file=sys.stderr)
        return "", "", "", "", "", "bronze"

    version = str(d.get("version", "") or "")
    title = str(d.get("title", d.get("name", "")) or "")
    description = str(d.get("description", "") or "")
    description_first_sentence = description.split(".")[0] if description else ""
    example_class, example_var = detect_quickstart(d)

    quickstart_policy = "bronze"
    build_file = os.path.join(os.path.dirname(schema_file_path), "build.yaml")
    if os.path.exists(build_file):
        try:
            build_config = read_yaml(build_file)
        except Exception as e:
            print(f"ÅTVARING: kunne ikkje lese {build_file} for quickstart-policy ({e})", file=sys.stderr)
            build_config = {}
        quickstart_policy = str(build_config.get("validation_policy", "bronze"))

    return version, title, description_first_sentence, example_class, example_var, quickstart_policy


def path_pattern_to_regex(pattern):
    placeholder = "__DOUBLESTAR__"
    regex_pattern = pattern.replace("**", placeholder).replace("*", "[^/]*").replace(placeholder, ".*")
    regex_pattern = re.sub(r"/\.\*$", r"(/.*)?", regex_pattern)
    return regex_pattern


def match_codeowners(orgs, schema_path, schema):
    """Same to-stegs matching som generate_contact_info() i kontakt.sh:
    fyrst catalog_slug == schema, deretter path_patterns mot schema_path."""
    for org in orgs:
        if org.get("catalog_slug", "") == schema:
            return org.get("name", ""), org.get("org_uri", ""), org.get("contact_uri", "")
    for org in orgs:
        for pattern in org.get("path_patterns", []) or []:
            if re.search(path_pattern_to_regex(pattern), schema_path):
                return org.get("name", ""), org.get("org_uri", ""), org.get("contact_uri", "")
    return "", "", ""


def load_codeowners_orgs(codeowners_path):
    try:
        with open(codeowners_path) as f:
            content = f.read()
    except FileNotFoundError:
        return []
    match = re.search(r"^```yaml\n(.*?)\n```", content, re.MULTILINE | re.DOTALL)
    if not match:
        return []
    data = yaml.safe_load(match.group(1)) or {}
    return data.get("organizations", []) or []


def collect_submodels():
    """Gjenskaper Steg 1.5-løkka i publish.sh: gå gjennom ALLE build.yaml
    under src/linkml/ (skjema- OG datafil-manifest), nøkla på
    katalognamnet (basename), same nøkkel som bash sin
    `schema=$(basename "$schema_dir")`."""
    import subprocess

    result = subprocess.run(
        ["find", f"{REPO_ROOT}/src/linkml", "-name", "build.yaml"],
        capture_output=True, text=True, check=True,
    )
    entries = []
    for manifest_path in result.stdout.splitlines():
        if not manifest_path:
            continue
        schema_key = manifest_path.rsplit("/", 2)[-2]
        try:
            d = read_yaml(manifest_path)
        except Exception as e:
            print(f"ÅTVARING: kunne ikkje lese submodels frå {manifest_path} — hoppar over ({e})", file=sys.stderr)
            continue
        submodels = d.get("submodels", []) or []
        if submodels:
            entries.append((schema_key, ",".join(submodels)))
    return entries


def main():
    orgs = load_codeowners_orgs(f"{REPO_ROOT}/CODEOWNERS.md")

    print("### SUBMODELS")
    for schema_key, submodels_csv in collect_submodels():
        print(US.join([schema_key, submodels_csv]))

    print("### SCHEMAS")
    for line in sys.stdin:
        line = line.rstrip("\n")
        if not line:
            continue
        domain, schema, schema_file_path, manifest_path = line.split(US)
        policy, ext_url, ext_label = read_manifest(manifest_path)
        version, title, desc, example_class, example_var, quickstart_policy = read_schema_file(schema_file_path)
        schema_path = f"src/linkml/{domain}/{schema}"
        co_name, co_org_uri, co_contact_uri = match_codeowners(orgs, schema_path, schema)
        print(US.join([
            f"{domain}/{schema}", policy, ext_url, ext_label,
            version, title, desc, example_class, example_var, quickstart_policy,
            co_name, co_org_uri, co_contact_uri,
        ]))

    print("### ORGS")
    for org in orgs:
        print(US.join([org.get("org_uri", ""), org.get("name", "")]))


if __name__ == "__main__":
    main()
