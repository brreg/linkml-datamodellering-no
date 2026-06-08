# Plan: gen-plantuml og gen-proto

Legg til Make-mål og CI-steg for å generere PlantUML-diagram og Protobuf-skjema frå alle
LinkML-skjema i repoet. Begge generatorane er allereie tilgjengelege i `linkml-local`-imaget
— ingen Dockerfile-endringar trengst.

---

## Skilnaden mellom dei to generatorane

| | `gen-proto` | `gen-plantuml` |
|---|---|---|
| Output | Éin `.proto`-fil til stdout | Éin `.svg`-fil per skjema til ein katalog |
| Mønster | Som `gen-jsonschema` — brukar `run_gen` | To steg: `gen-plantuml` → stdout → `.puml`, deretter `plantuml/plantuml -tsvg` → `.svg` |
| Ny makro | Nei — `run_gen` fungerer direkte | Ja — `run_gen_plantuml` |

---

## Steg 1 – Ny `run_gen_plantuml`-makro i Makefile

`gen-plantuml` med `--directory` brukar Kroki.io (HTTP GET) for å rendre SVG, og feiler med
HTTP 414 for store skjema. Løysinga er å bruke stdout-modus (utan `--directory`) for å få rå
PlantUML-kjeldekode, og deretter konvertere med `docker.io/plantuml/plantuml` — ein lokal
Java-container som ikkje har URL-grenser. Éin `.puml` og éin `.svg` per skjema (alle klassar samla).

```makefile
PLANTUML_IMAGE := docker.io/plantuml/plantuml:latest

define run_gen_plantuml
@$(foreach s,$(1), \
  echo "$(CLR_STEP)→ gen-plantuml  $(s)$(CLR_RST)" && \
  mkdir -p $(call schema_outdir,$(s))/diagrams && \
  $(LINKML_RUN) gen-plantuml $(s) \
    > $(call schema_outdir,$(s))/diagrams/$(call schema_name,$(s)).puml && \
  podman run --rm \
    -v "$(CURDIR)/$(call schema_outdir,$(s))/diagrams:/data" \
    $(PLANTUML_IMAGE) -tsvg /data/$(call schema_name,$(s)).puml; \
)
endef
```

---

## Steg 2 – Topp-nivå-mål

Legg til etter eksisterande `gen-*`-mål:

```makefile
gen-proto:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gen-proto$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen,$(SCHEMAS),gen-proto,schema.proto)

gen-plantuml:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gen-plantuml$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen_plantuml,$(SCHEMAS))
```

---

## Steg 3 – Domene-mål

Legg til i blokken med `domain-gen-*`-mål (linje ~305):

```makefile
domain-gen-proto:
	$(call run_gen,$(_schemas_$(DOMAIN)),gen-proto,schema.proto)

domain-gen-plantuml:
	$(call run_gen_plantuml,$(_schemas_$(DOMAIN)))
```

---

## Steg 4 – Integrasjon i domene-`define`-blokken

I den genererte `define`-blokken per domene (linje ~270–295) — legg til dei to nye
generatorane saman med dei eksisterande:

```makefile
    $$(call run_gen,$$(_schemas_$(1)),gen-proto,schema.proto)
    $$(call run_gen_plantuml,$$(_schemas_$(1)))
```

---

## Steg 5 – `.PHONY`

Legg til i `.PHONY`-lista:

```makefile
gen-proto gen-plantuml \
domain-gen-proto domain-gen-plantuml \
```

---

## Steg 6 – GitHub Actions

To nye composite actions, same mønster som `gen-json-schema`:

**`.github/actions/gen-proto/action.yml`:**
```yaml
name: Generer schema.proto
description: Køyrer gen-proto for alle skjema i domenet
inputs:
  domain:
    description: Domenenamn
    required: true
runs:
  using: composite
  steps:
    - name: Generer schema.proto
      shell: bash
      run: make domain-gen-proto DOMAIN=${{ inputs.domain }}
```

**`.github/actions/gen-plantuml/action.yml`:**
```yaml
name: Generer PlantUML-diagram
description: Køyrer gen-plantuml for alle skjema i domenet
inputs:
  domain:
    description: Domenenamn
    required: true
runs:
  using: composite
  steps:
    - name: Generer PlantUML
      shell: bash
      run: make domain-gen-plantuml DOMAIN=${{ inputs.domain }}
```

---

## Steg 7 – `generate.yml`

Legg til to nye `uses:`-steg i kvar domain-jobb (ap-no, fair, fint, ngr, oreg, samt),
same stad som dei eksisterande `gen-*`-stega:

```yaml
      - uses: ./.github/actions/gen-proto
        if: steps.cache-generated.outputs.cache-hit != 'true'
        with:
          domain: <domene>
      - uses: ./.github/actions/gen-plantuml
        if: steps.cache-generated.outputs.cache-hit != 'true'
        with:
          domain: <domene>
```

Cache-nøkklane for kvar domene-jobb treng **ikkje** endrast — dei hashar allereie
`src/linkml/<domene>/**` og `Dockerfile.linkml`, som fangar opp endringar i skjema.

---

## Utdatastruktur etter implementering

```
generated/
└── <domene>/
    └── <modell>/
        ├── <modell>-schema.proto      ← ny
        └── diagrams/                  ← ny katalog
            ├── <modell>.puml
            └── <modell>.svg
```

---

## Rekkjefølge

1. `run_gen_plantuml`-makro
2. Topp-nivå-mål + domene-mål + `.PHONY`
3. Domene-`define`-integrasjon
4. GitHub Actions-filer
5. `generate.yml`-oppdatering
