# Per-skjema per-artefakt i generate-workflow — plan

## Bakgrunn

`generate.yml` har i dag éin jobb per domene som køyrer alle generatorar sekvensielt.
Med `generate.yaml` per skjema veit vi no eksplisitt kva artefaktar kvart enkelt skjema
skal produsere. Det opnar for å køyre éin jobb per artefakt per skjema — finare
parallellisering, finare cache-granularitet og ingen ubrukte steg.

---

## Ny arkitektur

```
ensure-images ──┐
                ├──► generate [matrix: schema × artefakt]   ← éin jobb per (skjema, artefakt)
setup ──────────┘    (~190 jobbar totalt, under GH-grensa på 256)
                          │
                     publish (samlar alle artefaktar → Pages)
```

Kvar matrise-jobb:
1. Lastar inn container-image
2. Kallar det relevante composite action (`gen-shapes`, `gen-rdf`, osv.) med `schema`-input
3. Lastar opp genererte filer som GitHub Actions-artefakt

---

## Steg 1 — Nye Makefile-mål for enkeltskjema

Eksisterande `domain-gen-*`-mål opererer på alle skjema i eit domene.
Det trengst tilsvarande `schema-gen-*`-mål for eitt enkelt skjema.

Legg til etter `domain-gen-plantuml`-blokken i Makefile:

```makefile
# ---------------------------------------------------------------------------
# Per-skjema-mål for CI — krev SCHEMA=<sti-til-skjema>
# Eksempel: make schema-gen-shapes SCHEMA=src/linkml/fint/fint-administrasjon/fint-administrasjon-schema.yaml
# ---------------------------------------------------------------------------

schema-gen-linkml:
	@echo "$(CLR_STEP)→ gen-linkml  $(SCHEMA)$(CLR_RST)"
	$(LINKML_RUN) gen-linkml $(SCHEMA) > /dev/null

schema-gen-context:
	$(call run_gen,$(SCHEMA),gen-jsonld-context,context.jsonld)

schema-gen-shapes:
	$(call run_gen_shacl,$(SCHEMA))

schema-gen-python:
	$(call run_gen,$(SCHEMA),gen-python,model.py)

schema-gen-json-schema:
	$(call run_gen,$(SCHEMA),gen-json-schema,schema.json)

schema-gen-owl:
	$(call run_gen_owl,$(SCHEMA))

schema-gen-rdf:
	$(call run_gen_rdf,$(SCHEMA))

schema-gen-erdiagram:
	$(call run_gen_erdiagram,$(SCHEMA))

schema-gen-doc:
	$(call run_gen_doc,$(SCHEMA))

schema-gen-proto:
	$(call run_gen,$(SCHEMA),gen-proto,schema.proto)

schema-gen-plantuml:
	$(call run_gen_plantuml,$(SCHEMA))

schema-gen-examples:
	@domain=$(call schema_domain,$(SCHEMA)); \
	name=$(call schema_name,$(SCHEMA)); \
	example=examples/$$domain/$$name-eksempel.yaml; \
	[ -f "$$example" ] || { echo "Ingen eksempelfil: $$example (hoppar over)"; exit 0; }; \
	generate_yaml=$(dir $(SCHEMA))generate.yaml; \
	if [ -f "$$generate_yaml" ] && grep -q "^  example_rdf: false" "$$generate_yaml"; then \
		echo "Hoppar over linkml-convert for $$example (example_rdf: false)"; exit 0; \
	fi; \
	mkdir -p $(GEN_DIR)/$$domain/$$name; \
	if [ -f tests/fixtures/$$name-fixture.yaml ]; then \
		schema_arg=tests/fixtures/$$name-fixture.yaml; \
	else \
		schema_arg=$(SCHEMA); \
	fi; \
	echo "$(CLR_STEP)→ linkml-convert  $$example$(CLR_RST)"; \
	$(LINKML_RUN) linkml-convert \
		--schema $$schema_arg \
		--output-format ttl \
		--no-validate \
		--output $(GEN_DIR)/$$domain/$$name/$$name-eksempel.ttl \
		$$example
```

Legg `schema-gen-linkml schema-gen-context schema-gen-shapes schema-gen-python schema-gen-json-schema schema-gen-owl schema-gen-rdf schema-gen-erdiagram schema-gen-doc schema-gen-proto schema-gen-plantuml schema-gen-examples` til `.PHONY`.

---

## Steg 2 — Matriseskript: `.github/scripts/build-generate-matrix.sh`

Skriptet les alle `generate.yaml`-filer og skriv ein JSON-matrise til stdout.
Berre (skjema, artefakt)-par der artefakten er aktivert vert inkluderte.

I tillegg bereknar skriptet ein `deps_hash` per skjema: ein SHA256-hash av innhaldet
til skjemaet sjølv pluss alle transitive lokale importar (løyst rekursivt frå
`imports:`-feltet i YAML). Denne hashen kjem med i kvart matriseelement og vert
brukt som del av cache-nøkkelen — slik at ei endring i t.d. `dcat-ap-no` automatisk
invaliderer cache for alle skjema som importerer det.

Skriptet er skrive i Python for å handtere YAML-parsing og rekursiv import-løysing:

```python
#!/usr/bin/env python3
# .github/scripts/build-generate-matrix.py
import hashlib, json, sys
from pathlib import Path
import yaml   # pyyaml er tilgjengeleg på ubuntu-22.04 runners

REPO = Path(".")
ARTIFACT_FIELD = {
    "context": "jsonld_context", "shapes": "shacl", "python": "python",
    "json_schema": "json_schema", "owl": "owl", "rdf": "rdf",
    "erdiagram": "erdiagram", "doc": "docs", "proto": "protobuf",
    "plantuml": "plantuml", "examples": "example_rdf",
}

def local_imports(schema_path: Path) -> list[Path]:
    """Returner direkteimporterte lokale skjemafiler."""
    schema_dir = schema_path.parent
    try:
        data = yaml.safe_load(schema_path.read_text())
    except Exception:
        return []
    result = []
    for imp in (data or {}).get("imports", []):
        if imp.startswith("linkml:"):
            continue
        candidate = (schema_dir / (imp + ".yaml")).resolve()
        if candidate.exists():
            result.append(candidate)
    return result

def all_deps(schema_path: Path, visited: set | None = None) -> set[Path]:
    """Returnerer alle transitive lokale avhengigheiter rekursivt."""
    if visited is None:
        visited = set()
    p = schema_path.resolve()
    if p in visited:
        return set()
    visited.add(p)
    deps = {p}
    for imp in local_imports(p):
        deps |= all_deps(imp, visited)
    return deps

def deps_hash(schema_path: Path) -> str:
    h = hashlib.sha256()
    for dep in sorted(all_deps(schema_path)):
        h.update(dep.read_bytes())
    return h.hexdigest()[:16]

entries = []
for yaml_file in sorted(REPO.glob("src/linkml/*/*/generate.yaml")):
    if "/common/" in str(yaml_file):
        continue
    domain = yaml_file.parts[2]
    model  = yaml_file.parts[3]
    schema = REPO / f"src/linkml/{domain}/{model}/{model}-schema.yaml"
    if not schema.exists():
        continue

    cfg = yaml.safe_load(yaml_file.read_text()).get("generators", {})
    dhash = deps_hash(schema)

    for artifact, field in ARTIFACT_FIELD.items():
        val = cfg.get(field, True)
        if val is False:
            continue
        entries.append({
            "domain": domain, "model": model,
            "schema": str(schema),
            "artifact": artifact,
            "deps_hash": dhash,
        })

print(json.dumps({"include": entries}))
```

**Output-døme:**
```json
{
  "include": [
    {"domain":"fint","model":"fint-administrasjon",
     "schema":"src/linkml/fint/fint-administrasjon/fint-administrasjon-schema.yaml",
     "artifact":"context","deps_hash":"a3f1c8e2b9d04712"},
    ...
  ]
}
```

`deps_hash` er lik for alle artefaktar frå same skjema. Han endrar seg når skjemaet
sjølv eller nokon av importane (t.d. `dcat-ap-no`, `fint-common`) endrar seg.

Skriptet vert kalla frå `setup`-jobben:
```yaml
run: python3 .github/scripts/build-generate-matrix.py
```

> **Merk:** skriptet er flytta frå `.sh` til `.py` for å handtere YAML-parsing og
> rekursiv import-løysing utan ekstra verktøy.

---

## Steg 3 — Oppdater composite actions

Alle eksisterande `gen-*` composite actions brukar berre `domain`-input og kallar
`make domain-gen-* DOMAIN=...`. Legg til `schema`-input og eit steg som kallar
`make schema-gen-* SCHEMA=...` dersom `schema` er sett.

**Mønster (vist for `gen-shapes`):**

```yaml
name: Generer shapes.ttl (SHACL)
description: Køyrer gen-shacl for alle skjema i domenet eller for eitt skjema

inputs:
  domain:
    description: Domenenamn (ap-no, fair, fint, ngr, oreg, samt)
    required: false
  schema:
    description: Sti til enkeltskjema
    required: false

runs:
  using: composite
  steps:
    - name: Generer shapes.ttl (SHACL) — domene
      if: ${{ inputs.domain != '' }}
      shell: bash
      run: make domain-gen-shapes DOMAIN=${{ inputs.domain }}
    - name: Generer shapes.ttl (SHACL) — enkeltskjema
      if: ${{ inputs.schema != '' }}
      shell: bash
      run: make schema-gen-shapes SCHEMA=${{ inputs.schema }}
```

Dette bevarar bakover-kompatibilitet: eksisterande bruk med `domain:` held fram å fungere.

Oppdater alle 11 `gen-*` actions etter same mønster
(`gen-context`, `gen-shapes`, `gen-python`, `gen-json-schema`, `gen-owl`, `gen-rdf`,
`gen-erdiagram`, `gen-doc`, `gen-proto`, `gen-plantuml`, `gen-examples`).

---

## Steg 4 — Oppdater `generate.yml`

### Ny `setup`-jobb

```yaml
setup:
  runs-on: ubuntu-22.04
  outputs:
    matrix: ${{ steps.build.outputs.matrix }}
  steps:
    - uses: actions/checkout@v6
    - name: Bygg genererings-matrise
      id: build
      run: |
        matrix=$(bash .github/scripts/build-generate-matrix.sh)
        echo "matrix=$matrix" >> $GITHUB_OUTPUT
```

### Ny matrise-jobb `generate`

Erstattar alle domene-spesifikke `generate-ap-no`, `generate-fair`, osv.

Jobbnamnet set artefakttypen først slik at GitHub Actions-UI-en sorterer og
grupperer jobbar visuelt etter artefakt (alle `shapes`-jobbar saman, alle
`context`-jobbar saman osv.):

```yaml
generate:
  name: "${{ matrix.artifact }} / ${{ matrix.domain }} / ${{ matrix.model }}"
  needs: [ensure-images, setup]
  runs-on: ubuntu-22.04
  permissions:
    contents: read
    packages: read
    actions: write
  strategy:
    matrix: ${{ fromJson(needs.setup.outputs.matrix) }}
    fail-fast: false
  steps:
    - uses: actions/checkout@v6

    - name: Cache genererte artefaktar (${{ matrix.model }}-${{ matrix.artifact }})
      id: cache-generated
      uses: actions/cache@v5
      with:
        path: generated/${{ matrix.domain }}/${{ matrix.model }}/
        key: generated-${{ matrix.domain }}-${{ matrix.model }}-${{ matrix.artifact }}-${{ hashFiles(
               format('src/linkml/{0}/{1}/**', matrix.domain, matrix.model),
               'src/assets/containers/Dockerfile.linkml',
               'src/templates/**',
               'Makefile',
               '.github/workflows/generate.yml',
               '.github/actions/**'
             ) }}

    - uses: ./.github/actions/load-images
      if: steps.cache-generated.outputs.cache-hit != 'true'

    - uses: ./.github/actions/gen-${{ matrix.artifact }}
      if: steps.cache-generated.outputs.cache-hit != 'true'
      with:
        schema: ${{ matrix.schema }}

    - uses: actions/upload-artifact@v4
      with:
        name: generated-${{ matrix.domain }}-${{ matrix.model }}-${{ matrix.artifact }}
        path: generated/${{ matrix.domain }}/${{ matrix.model }}/
        retention-days: 1
```

### Oppdater `publish`-jobben

```yaml
publish:
  needs: [generate]
  ...
  steps:
    - uses: actions/checkout@v6
    - name: Last ned alle genererte artefaktar
      uses: actions/download-artifact@v4
      with:
        pattern: generated-*
        path: generated/
        merge-multiple: true
    ...
```

### Fjern dei gamle domene-jobbane

Fjern `generate-ap-no`, `generate-fair`, `generate-fint`, `generate-ngr`,
`generate-oreg`, `generate-samt`.

---

## Avvegingar

### Jobbantal

Med 19 skjema × 11 artefakttypar = 209 moglege jobbar, minus deaktiverte (~20)
= ~189 generate-jobbar + `setup` + `ensure-images` + `publish` = **~192 jobbar totalt**.
GitHub Actions-grensa er 256. Romsleg margin.

### Cache-nøklar og importavhengigheiter

Cache-nøkkelen brukar `src/linkml/<domain>/<model>/**` — berre det aktuelle skjemaet.
Det betyr at ei endring i eitt skjema berre invaliderer cache for det skjemaet, ikkje
for heile domenet.

Problemet som gjenstår er transitive importar: `fint-administrasjon` importerer
`fint-common` og `ap-no`, og endringar der vil ikkje slå ut i cache-nøkkelen.

To val:
- **Konservativt (trygt):** inkluder `src/linkml/**` (alle skjema) i cache-nøkkelen
  → alltid korrekt, men mister per-skjema-granulariteten
- **Presis (anbefalt):** legg til `import_deps`-felt i `generate.yaml` med liste
  over importerte domenestigar, og la matriseskriptet inkludere dei i cache-nøkkelen

Plan legg opp til konservativ strategi i første omgang. `import_deps`-feltet
kan innførast seinare som eige steg.

### `gen-linkml` (lint) per skjema

Eksisterande workflow køyrer `gen-linkml` (syntakssjekk) som eige steg i kvar
domenejobb. Med per-skjema-matrise kan `gen-linkml` anten:
a. Leggjast til som eit eige `artifact: linkml`-innslag i matrisa (eitt steg per skjema)
b. Behaldast i ein eigen `validate-linkml`-jobb per domene utanfor matrisa

Alternativ (a) er konsistent med resten av planen.

---

## Rekkjefølgje

1. Legg til `schema-gen-*`-mål i `Makefile` og oppdater `.PHONY`
2. Lag `src/assets/scripts/build-generate-matrix.sh`
3. Oppdater alle 11 `gen-*` composite actions med `schema`-input
4. Oppdater `generate.yml`: legg til `setup`-jobb, erstatt domenejobbar med matrise-jobb
5. Test med `workflow_dispatch` og verifiser at alle artefaktar vert genererte
6. Verifiser at `publish`-jobben samlar korrekt
