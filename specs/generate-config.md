# Konfigurasjonsfil per modell — plan

## Bakgrunn og mål

I dag er generatorkonfigurasjon berre mogleg på domenivå via hardkoda Makefile-variablar:

```makefile
GEN_RDF_SKIP_fint   := true
GEN_RDF_SKIP_samt   := true
SHACL_FLAGS_fint    := --exclude-imports
OWL_FLAGS_fint      := --log_level ERROR
```

Dette gjer det umogleg å slå av eller justere ein generator for éin enkelt modell utan å
påverke heile domenet. Målet er at kvar modell har ei eiga `generate.yaml`-fil som
spesifiserer kva artefakter som skal genererast og med kva flagg.

---

## Konfigurasjonsfil-format

**Plassering:** `src/linkml/<domene>/<modell>/generate.yaml`

**Namngjeving:** `generate.yaml` (fast namn — modellnamnet er allereie gitt av katalogen)

```yaml
# src/linkml/oreg/register-over-aksjeeiere/generate.yaml
generators:
  jsonld_context: true    # <modell>-context.jsonld
  shacl:                  # <modell>-shapes.ttl
    enabled: true
    flags: []
  python: true            # <modell>-model.py
  json_schema: true       # <modell>-schema.json
  owl:                    # <modell>-ontology.ttl
    enabled: true
    flags: []
  rdf: true               # <modell>-schema.ttl
  protobuf: true          # <modell>-schema.proto
  erdiagram: true         # <modell>-erdiagram.md
  docs: true              # docs/
  plantuml: true          # diagrams/<modell>.puml + .svg
  example_rdf: true       # <modell>-eksempel.ttl
```

**Kortform:** Ein generator utan flagg-behov kan skrivast som ein boolsk:

```yaml
generators:
  rdf: false              # hopp over denne generatoren
  shacl:                  # treng flagg — bruk utvida form
    enabled: true
    flags: [--exclude-imports]
```

---

## Standardverdiar per domene

Tabellen viser kva `generate.yaml` kvar modell skal ha etter migrering.
Alle felt som ikkje er lista opp brukar standardverdien `true` med tomme flagg.

| Domene | Modell(ar) | `rdf` | `shacl.flags` | `owl.flags` | `example_rdf` |
|---|---|---|---|---|---|
| **ngr** | alle | `true` | `[]` | `[]` | `true` |
| **oreg** | alle | `true` | `[]` | `[]` | `true` |
| **fint** | alle | `false` | `[--exclude-imports]` | `[--log_level ERROR]` | `true` |
| **samt** | alle | `false` | `[]` | `[]` | `true` |
| **ap-no** | alle | `true` | `[]` | `[]` | `false` * |
| **fair** | fair-metadata | `true` | `[]` | `[]` | `false` * |

\* AP-NO-profilar og fair-metadata har ikkje `tree_root` og ingen eksempelfil — `example_rdf`
skal difor vera `false`.

**Standardkonfig (mal for nye modellar):**

```yaml
generators:
  jsonld_context: true
  shacl:
    enabled: true
    flags: []
  python: true
  json_schema: true
  owl:
    enabled: true
    flags: []
  rdf: true
  protobuf: true
  erdiagram: true
  docs: true
  plantuml: true
  example_rdf: true
```

---

## Implementasjon

### Steg 1 — Python-skript: `scripts/read-generate-configs.py`

Skriptet les alle `generate.yaml`-filer og skriv ut eit Makefile-fragment (`config.mk`)
med per-modell-variablar.

**Input:** Alle `src/linkml/<domene>/<modell>/generate.yaml`-filer

**Output:** `config.mk` med variablar på forma:

```makefile
# Generert av scripts/read-generate-configs.py — ikkje rediger manuelt

GEN_RDF_SKIP_fint_administrasjon   := true
GEN_RDF_SKIP_fint_arkiv             := true
GEN_RDF_SKIP_samt_bu                := true
SHACL_FLAGS_fint_administrasjon     := --exclude-imports
OWL_FLAGS_fint_administrasjon       := --log_level ERROR
EXAMPLE_RDF_SKIP_dcat_ap_no         := true
```

Nøkkelforma er `<domene>_<modell>` (bindestrekar i domene/modellnamn erstatta med `_`).

### Steg 2 — Makefile-endringar

1. Inkluder det genererte fragmentet:
   ```makefile
   -include config.mk
   ```

2. Legg til eit `config`-mål som genererer `config.mk`:
   ```makefile
   config.mk: $(shell find src/linkml -name 'generate.yaml')
       python3 scripts/read-generate-configs.py > config.mk
   ```
   Makefile-fragmentet vert automatisk regenerert når ei `generate.yaml`-fil endrar seg.

3. Erstatt dei hardkoda domenevariablane med per-modell-variablar i generator-makroane:
   ```makefile
   # Før:
   ifeq ($(GEN_RDF_SKIP_$(domain)),true)
   # Etter:
   ifeq ($(GEN_RDF_SKIP_$(domain)_$(model_key)),true)
   ```

4. Fjern dei gamle hardkoda Makefile-variablane etter at `config.mk` er på plass.

### Steg 3 — Oppdater `new-model.sh`

Scaffolding-skriptet skal opprette ei standard `generate.yaml` ved sidan av skjemaet:

```bash
# I new-model.sh, etter at skjemafila er oppretta:
cat > "${MODEL_DIR}/generate.yaml" << EOF
generators:
  jsonld_context: true
  shacl:
    enabled: true
    flags: []
  python: true
  json_schema: true
  owl:
    enabled: true
    flags: []
  rdf: true
  protobuf: true
  erdiagram: true
  docs: true
  plantuml: true
  example_rdf: true
EOF
```

---

## Eksisterande modellar som treng `generate.yaml`

Alle modellar under `src/linkml/` som følgjer mønsteret `<domene>/<modell>/<modell>-schema.yaml`:

**NGR (standardkonfig):**
- `ngr/ngr-adresse/generate.yaml`
- `ngr/ngr-eiendom/generate.yaml`
- `ngr/ngr-person/generate.yaml`
- `ngr/ngr-virksomhet/generate.yaml`

**OREG (standardkonfig):**
- `oreg/register-over-aksjeeiere/generate.yaml`

**FINT (`rdf: false`, SHACL- og OWL-flagg):**
- `fint/fint-common/generate.yaml`
- `fint/fint-administrasjon/generate.yaml`
- `fint/fint-arkiv/generate.yaml`
- `fint/fint-okonomi/generate.yaml`
- `fint/fint-personvern/generate.yaml`
- `fint/fint-ressurs/generate.yaml`
- `fint/fint-utdanning/generate.yaml`

**SAMT (`rdf: false`):**
- `samt/samt-bu/generate.yaml`

**AP-NO (`example_rdf: false`):**
- `ap-no/cpsv-ap-no/generate.yaml`
- `ap-no/dcat-ap-no/generate.yaml`
- `ap-no/dqv-ap-no/generate.yaml`
- `ap-no/modelldcat-ap-no/generate.yaml`
- `ap-no/skos-ap-no/generate.yaml`
- `ap-no/xkos-ap-no/generate.yaml`

**FAIR (`example_rdf: false`):**
- `fair/fair-metadata/generate.yaml`

> **`ap-no/common/`** er allereie ekskludert frå generering via Makefile-mønsteret og
> treng ingen `generate.yaml`.

---

## Rekkjefølgje

1. **Definer filformatet** (dette dokumentet) — ferdig
2. **Lag `generate.yaml` for alle eksisterande modellar** — éin fil per modell, sjå lista
   over. Start med fint og samt sidan dei har avvikande konfig.
3. **Lag `scripts/read-generate-configs.py`** — les alle `generate.yaml`-filer og skriv
   `config.mk`
4. **Oppdater Makefile** — legg til `config.mk`-mål, oppdater generator-makroane til å
   bruke per-modell-variablar
5. **Test** — køyr `make config && make fint` og `make ngr` og verifiser at utdata er
   identisk med dagens resultat
6. **Fjern hardkoda domenevariablar** frå Makefile
7. **Oppdater `new-model.sh`** — generer standard `generate.yaml` ved scaffold
