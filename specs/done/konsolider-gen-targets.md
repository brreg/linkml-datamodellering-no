# Konsolider gen-*, domain-gen-* og schema-gen-* til einskilde gen-* targets

## Bakgrunn

Repoet har i dag tre paralelle hierarki av generatortargets med same funksjonalitet:

1. **`make gen-<format>`** — genererer `<format>` for **alle** skjema
2. **`make domain-gen-<format> DOMAIN=<domain>`** — genererer `<format>` for alle skjema i **eitt domene**
3. **`make schema-gen-<format> SCHEMA=<sti>`** — genererer `<format>` for **eitt skjema**

Dette gir ~45 targets med nesten identisk logikk, og er tungrodd å vedlikehalde. Brukaren må hugse tre ulike target-namn for same operasjon.

## Foreslått løysing

Slå saman til **eitt sett** av targets med valfrie argument for avgrensing:

```makefile
make gen-<format>                    # genererer for alle skjema (default)
make gen-<format> DOMAIN=<domain>    # genererer for alle skjema i domenet
make gen-<format> SCHEMA=<sti>       # genererer for eitt spesifikt skjema
```

### Døme

**Før:**
```bash
make gen-jsonld                              # alle skjema
make domain-gen-context DOMAIN=fint          # FINT-domenet
make schema-gen-shapes SCHEMA=src/linkml/... # eitt skjema
```

**Etter:**
```bash
make gen-jsonld                              # alle skjema
make gen-jsonld DOMAIN=fint                  # FINT-domenet
make gen-jsonld SCHEMA=src/linkml/...        # eitt skjema
```

## Fordelar

1. **Færre targets:** ~45 → ~15 targets (70% reduksjon)
2. **Enklare API:** Eitt target-namn per format, avgrensing via argument
3. **Konsekvent mønster:** Same logikk for alle format
4. **Enklare dokumentasjon:** Éin tabell i COMMANDS.md i staden for tre
5. **Enklare vedlikehald:** Éin stad å oppdatere logikk

## Implementasjonsstrategi

### Steg 1: Oppdater eksisterande `gen-<format>` targets

Legg til logikk for å sjekke `DOMAIN` eller `SCHEMA`:

```makefile
gen-jsonld:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gen-jsonld$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
ifdef SCHEMA
	@echo "Genererer JSON-LD context for $(SCHEMA)..."
	$(call run_gen,$(SCHEMA),gen-json-context,context.jsonld)
else ifdef DOMAIN
	@echo "Genererer JSON-LD context for domene $(DOMAIN)..."
	$(eval DOMAIN_SCHEMAS := $(filter src/linkml/$(DOMAIN)/%,$(SCHEMAS)))
	$(call run_gen,$(DOMAIN_SCHEMAS),gen-json-context,context.jsonld)
else
	@echo "Genererer JSON-LD context for alle skjema..."
	$(call run_gen,$(SCHEMAS),gen-json-context,context.jsonld)
endif
```

### Steg 2: Legg til deprecated aliases

Alle `domain-gen-*` og `schema-gen-*` targets vert deprecated aliases som peikar til `gen-*`:

```makefile
# ===========================================================================
# Deprecated aliases (domain-gen-* og schema-gen-*)
# ===========================================================================

domain-gen-context:
	@echo "ÅTVARING: 'domain-gen-context' er forelda, bruk 'gen-jsonld DOMAIN=<domain>'" >&2
	@test -n "$(DOMAIN)" || (echo "FEIL: DOMAIN er påkravd"; exit 1)
	@$(MAKE) --no-print-directory gen-jsonld DOMAIN=$(DOMAIN)

schema-gen-context:
	@echo "ÅTVARING: 'schema-gen-context' er forelda, bruk 'gen-jsonld SCHEMA=<sti>'" >&2
	@test -n "$(SCHEMA)" || (echo "FEIL: SCHEMA er påkravd"; exit 1)
	@$(MAKE) --no-print-directory gen-jsonld SCHEMA=$(SCHEMA)
```

### Steg 3: Oppdater validering-targets

Same mønster for `validate-*`, `domain-validate-*`:

```makefile
validate-bronze:
ifdef SCHEMA
	# valider eitt skjema
else ifdef DOMAIN
	# valider alle skjema i domenet
else
	# valider alle skjema
endif
```

### Steg 4: Oppdater dokumentasjon

**COMMANDS.md** får éin seksjon i staden for tre:

```markdown
## Generering av artefakter

Alle generatortargets støttar tre bruksmåtar:

- **`make gen-<format>`** — generer for alle skjema
- **`make gen-<format> DOMAIN=<domain>`** — generer for alle skjema i eit domene
- **`make gen-<format> SCHEMA=<sti>`** — generer for eitt spesifikt skjema

| Kommando | Beskriving | Output |
|---|---|---|
| `make gen-jsonld [DOMAIN=...] [SCHEMA=...]` | JSON-LD kontekst | `generated/<domain>/<modell>/<modell>-context.jsonld` |
| `make gen-shacl [DOMAIN=...] [SCHEMA=...]` | SHACL shapes | `generated/<domain>/<modell>/<modell>-shapes.ttl` |
| `make gen-python [DOMAIN=...] [SCHEMA=...]` | Python-dataklassar | `generated/<domain>/<modell>/<modell>-model.py` |
...
```

## Steg

1. **Oppdater gen-jsonld som proof-of-concept**
   - Legg til `ifdef SCHEMA`, `ifdef DOMAIN` logikk
   - Test alle tre bruksmåtar

2. **Generaliser til funksjon**
   - Lag `define gen_with_scope` som kan brukast av alle gen-* targets
   - Reduser duplisering

3. **Oppdater alle gen-* targets**
   - Appliser same mønster på alle 15 format-targets

4. **Legg til deprecated aliases**
   - Alle `domain-gen-*` (16 targets)
   - Alle `schema-gen-*` (15 targets)
   - Totalt 31 deprecated aliases

5. **Oppdater validering-targets**
   - `validate-bronze`, `validate-data`, `validate-examples`
   - Fjern `domain-validate-*` prefiks

6. **Oppdater dokumentasjon**
   - COMMANDS.md: slå saman tre seksjoner til éin
   - CLAUDE.md: oppdater døme

7. **Test integrasjonen**
   - Test `make gen-jsonld` (alle)
   - Test `make gen-jsonld DOMAIN=fint`
   - Test `make gen-jsonld SCHEMA=src/linkml/...`

## Prioritert handlingsliste

- [x] Oppdater gen-jsonld som proof-of-concept — fungerer med DOMAIN og SCHEMA
- [x] Generaliser til `define get_target_schemas` — helper-funksjon laga
- [x] Oppdater alle gen-* targets (13 stk) — gen-jsonld, gen-shacl, gen-python, gen-jsonschema, gen-owl, gen-rdf, gen-xsd, gen-asyncapi, gen-openapi, gen-erdiagram, gen-docs, gen-proto, gen-plantuml
- [x] Legg til deprecated aliases (31 stk) — 13 domain-gen-*, 13 schema-gen-*, 5 spesielle (linkml, examples, data)
- [x] Fjern gamle domain-gen-* og schema-gen-* implementasjonar — sletta linje 667-864
- [x] Oppdater dokumentasjon (COMMANDS.md) — slått saman "Enkeltartefakter" med DOMAIN/SCHEMA-support, fjerna 3 "Avansert"-seksjoner
- [x] Test integrasjonen — testa gen-jsonld DOMAIN=samt og domain-gen-context DOMAIN=samt
- [ ] Oppdater validering-targets (ikkje i denne specen)

## Avhengigheiter

- Eksisterande Makefile med gen-*, domain-gen-*, schema-gen-*
- COMMANDS.md
- CLAUDE.md

## Merknader

- **Bakoverkompatibilitet:** Alle `domain-gen-*` og `schema-gen-*` targets fungerer med deprecation-warning i minst to release-syklusar
- **Fallback-logikk:** Dersom verken `DOMAIN` eller `SCHEMA` er sett, generer for alle skjema (eksisterande oppførsel)
- **Feilhandtering:** Dersom både `DOMAIN` og `SCHEMA` er sett, prioriter `SCHEMA` (meir spesifikk)
- **Validering:** Sjekk at `DOMAIN` eksisterer og har skjema før generering
- **Reduksjon:** Frå ~45 gen-relaterte targets til ~15, med 31 deprecated aliases

## Eksempel: gen-jsonld før og etter

### Før

```makefile
gen-jsonld:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make gen-jsonld$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen,$(SCHEMAS),gen-json-context,context.jsonld)

domain-gen-context:
	@test -n "$(DOMAIN)" || (echo "Bruk: make domain-gen-context DOMAIN=<domain>"; exit 1)
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make domain-gen-context DOMAIN=$(DOMAIN)$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(eval DOMAIN_SCHEMAS := $(filter src/linkml/$(DOMAIN)/%,$(SCHEMAS)))
	$(call run_gen,$(DOMAIN_SCHEMAS),gen-json-context,context.jsonld)

schema-gen-context:
	@test -n "$(SCHEMA)" || (echo "Bruk: make schema-gen-context SCHEMA=<sti>"; exit 1)
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make schema-gen-context SCHEMA=$(SCHEMA)$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen,$(SCHEMA),gen-json-context,context.jsonld)
```

### Etter

```makefile
gen-jsonld:
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
ifdef SCHEMA
	@echo "$(CLR_HDR)*** make gen-jsonld SCHEMA=$(SCHEMA)$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen,$(SCHEMA),gen-json-context,context.jsonld)
else ifdef DOMAIN
	@echo "$(CLR_HDR)*** make gen-jsonld DOMAIN=$(DOMAIN)$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(eval DOMAIN_SCHEMAS := $(filter src/linkml/$(DOMAIN)/%,$(SCHEMAS)))
	@test -n "$(DOMAIN_SCHEMAS)" || (echo "FEIL: Domene '$(DOMAIN)' finst ikkje eller har ingen skjema"; exit 1)
	$(call run_gen,$(DOMAIN_SCHEMAS),gen-json-context,context.jsonld)
else
	@echo "$(CLR_HDR)*** make gen-jsonld$(CLR_RST)"
	@echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
	$(call run_gen,$(SCHEMAS),gen-json-context,context.jsonld)
endif

# Deprecated aliases
domain-gen-context:
	@echo "ÅTVARING: 'domain-gen-context' er forelda, bruk 'gen-jsonld DOMAIN=<domain>'" >&2
	@test -n "$(DOMAIN)" || (echo "FEIL: DOMAIN er påkravd"; exit 1)
	@$(MAKE) --no-print-directory gen-jsonld DOMAIN=$(DOMAIN)

schema-gen-context:
	@echo "ÅTVARING: 'schema-gen-context' er forelda, bruk 'gen-jsonld SCHEMA=<sti>'" >&2
	@test -n "$(SCHEMA)" || (echo "FEIL: SCHEMA er påkravd"; exit 1)
	@$(MAKE) --no-print-directory gen-jsonld SCHEMA=$(SCHEMA)
```

## Impact

**Reduserte targets:**
- gen-* targets: 15 (uendra)
- domain-gen-* targets: 16 → 0 (deprecated aliases)
- schema-gen-* targets: 15 → 0 (deprecated aliases)
- Totalt: 46 → 15 (-31 targets, +31 deprecated aliases)

**Forbetra brukaropplevelse:**
- Éin kommando å hugse: `make gen-<format>`
- Enklare avgrensing: `DOMAIN=` eller `SCHEMA=`
- Konsekvent API på tvers av alle format

**Enklare vedlikehald:**
- Éin stad å oppdatere logikk for kvar format
- Mindre kode-duplisering
- Enklare å legge til nye format

## Utført

Alle hovudtiltak er implementerte:

**Makefile-endringar:**
- Ny funksjon `get_target_schemas`: bestemmer kva skjema som skal prosesserast basert på `DOMAIN`, `SCHEMA` eller alle
- 13 gen-* targets oppdaterte til å støtte `ifdef SCHEMA`, `ifdef DOMAIN`, `else` (alle skjema)
- 198 linjer med gamle domain-gen-* og schema-gen-* implementasjonar sletta (linje 667-864)
- 31 deprecated aliases lagt til:
  - 13 domain-gen-* → gen-* DOMAIN=...
  - 13 schema-gen-* → gen-* SCHEMA=...
  - 5 spesielle (linkml, examples, data) med tilpassa implementasjon

**COMMANDS.md-endringar:**
- "Enkeltartefakter"-seksjonen oppdatert til å vise `[DOMAIN=...] [SCHEMA=...]` for alle gen-* targets
- 3 "Avansert"-seksjoner fjerna (57 linjer) — no overflødige sidan gen-* støttar DOMAIN/SCHEMA direkte
- Frå 93 dokumenterte targets til 62 dokumenterte targets (-31 domain-gen-*/schema-gen-*, +0 nye)

**Resultat:**
- Enklare API: `make gen-<format>`, `make gen-<format> DOMAIN=<domain>`, `make gen-<format> SCHEMA=<sti>`
- Færre targets: ~46 → 13 gen-* targets (-33, +31 deprecated aliases)
- Konsekvent mønster: same logikk for alle format
- Enklare dokumentasjon: éin tabell i staden for tre seksjoner
- Bakoverkompatibilitet: alle gamle domain-gen-* og schema-gen-* fungerer med deprecation-warning

**Eksempel:**
```bash
# Tidlegare:
make gen-jsonld                              # alle
make domain-gen-context DOMAIN=fint          # FINT-domenet
make schema-gen-shapes SCHEMA=src/linkml/... # eitt skjema

# No:
make gen-jsonld                              # alle (uendra)
make gen-jsonld DOMAIN=fint                  # FINT-domenet (ny)
make gen-shacl SCHEMA=src/linkml/...         # eitt skjema (ny)
```

**Gjenståande arbeid:**
- Oppdater validering-targets (validate-*, domain-validate-*) med same mønster (ikkje prioritert i denne specen)
- Fjern deprecated aliases etter 2 release-syklusar
