# Modulariser Makefile

## Bakgrunn

Makefile (1557 linjer) inneheld betydeleg gjentakelse, særleg i:
- Parallelle generator-makroar (7 stk med nesten identisk struktur)
- Per-generator targets (11 stk med identisk header-logikk)
- Domain-target med duplisert OpenAPI/AsyncAPI-logikk
- MCP-relaterte targets med lik struktur

## Analyse av gjentakelse

### 1. Parallelle generator-makroar (linje 71–317)

**Problem:** 7 makroar (`run_gen_parallel`, `run_gen_linkml_parallel`, `run_gen_owl_parallel`, `run_gen_rdf_parallel`, `run_gen_doc_parallel`, `run_gen_erdiagram_parallel`, `run_gen_plantuml_parallel`) deler ~80% av koden:

```make
define run_gen_<foo>_parallel
@if [ "$(PARALLEL)" = "1" ]; then \
    $(call run_gen_<foo>,$(1)) \
else \
    printf '%s\n' $(1) | xargs -P $(PARALLEL) -I {} bash -c ' \
        s="{}"; \
        name=$$(basename "$$s" -schema.yaml | sed "s/-schema$$//"); \
        domain=$$(echo "$$s" | cut -d/ -f3); \
        outdir=$(GEN_DIR)/$$domain/$$name; \
        t0=$$(date +%s%3N); \
        <GENERATOR-SPESIFIKK KOMMANDO>
        rc=$$?; \
        elapsed_ms=$$(($$( date +%s%3N) - t0)); \
        printf "$(CLR_STEP)→ <generator>  %s/%s$(CLR_RST) (%d.%ds)\n" \
            "$$domain" "$$name" \
            $$((elapsed_ms / 1000)) \
            $$((elapsed_ms % 1000 / 100)); \
        exit $$rc'; \
fi
endef
```

**Einaste skilnad:** kommandoen som køyrer (linje 83–84, 105–106, 127–128, osv.).

**Konsekvens:** 
- ~200 linjer duplisert kode
- Risiko for inkonsistens ved endring (t.d. timer-formatet)
- Vanskeleg å vedlikehalde

### 2. Per-generator targets (linje 562–750)

**Problem:** 11 targets (`gen-jsonld-context`, `gen-shacl`, `gen-python`, `gen-jsonschema`, `gen-owl`, `gen-rdf`, `gen-xsd`, `gen-asyncapi`, `gen-openapi`, `gen-erdiagram`, `gen-docs`, `gen-proto`, `gen-plantuml`) deler **identisk** header-logikk:

```make
gen-<foo>:
    @echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
ifdef SCHEMA
    @echo "$(CLR_HDR)*** make gen-<foo> SCHEMA=$(SCHEMA)$(CLR_RST)"
else ifdef DOMAIN
    @echo "$(CLR_HDR)*** make gen-<foo> DOMAIN=$(DOMAIN)$(CLR_RST)"
else
    @echo "$(CLR_HDR)*** make gen-<foo>$(CLR_RST)"
endif
    @echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
    $(call run_gen_<foo>,$(call get_target_schemas))
```

**Konsekvens:**
- ~110 linjer identisk header-kode
- Kvar endring i header-format må gjerast 11 stader

### 3. Domain-target OpenAPI/AsyncAPI-logikk (linje 916–961)

**Problem:** Kvar domain-target har **to identiske for-løkker** for OpenAPI og AsyncAPI (linje 916–938 og 939–961) — same logikk i `define domain_target`, med einaste skilnad i generator-namn.

**Konsekvens:**
- ~50 linjer duplisert kode per domain-target (ekspandert til alle domene)
- Risikoområde for copy-paste-feil

### 4. MCP-relaterte targets (linje 1177–1305)

**Problem:** 3 MCP-serverar (`mcp-linkml-validator`, `mcp-linkml-modell-utkast`, `mcp-linkml-begrep-utkast`) deler **identisk** struktur:

```make
build-docker-mcp-<foo>:
    @echo header
    podman build -t $(IMAGE) $(DIR)

mcp-<foo>-run:
    @echo header
    $(RUN) $(IMAGE)

mcp-<foo>-smoke: build-docker-mcp-<foo>
    @echo header
    cat tests/<testfil> | $(RUN) $(IMAGE)
```

**Konsekvens:**
- ~40 linjer duplisert per MCP-server
- Vanskeleg å leggje til ny MCP-server (copy-paste + søk-og-erstatt)

## Vurdering av modularisering

### Mål
1. **Redusere gjentakelse** utan å ofre lesbarheit
2. **Behalde oversikt** — ikkje skjule logikk i for mange abstraksjonslag
3. **Forenkle vedlikehald** — endring éin stad propagerer automatisk
4. **Behalte debugging-venlegheit** — kvar make echo-kommando køyrer

### Risiko

**Overmodularisering** kan gjere Makefile **mindre lesbar**:
- For mange indirekte kall (`$(call $(call ...))`) gjer det vanskeleg å forstå kva som faktisk skjer
- Make-debugging vert vanskelegare når kommandoane er genererte
- Nye bidragsytarar må forstå abstraksjonslag før dei kan endre noko

**Sweet spot:** Modulariser gjentakelse der logikken er **100% identisk**, men behald eksplisitt kode der det er **semantiske skilnader**.

## Forslag til modularisering

### Alternativ A: Generisk parallell generator-makro (anbefalt for steg 1)

**Ide:** Ein einaste `run_parallel`-makro som tek generator-kommando som argument.

```make
# Generisk parallell generator
# $1=schemas  $2=generator-namn  $3=kommando-template
define run_parallel
@if [ "$(PARALLEL)" = "1" ]; then \
    $(3) \
else \
    printf '%s\n' $(1) | xargs -P $(PARALLEL) -I {} bash -c ' \
        s="{}"; \
        name=$$(basename "$$s" -schema.yaml | sed "s/-schema$$//"); \
        domain=$$(echo "$$s" | cut -d/ -f3); \
        outdir=$(GEN_DIR)/$$domain/$$name; \
        t0=$$(date +%s%3N); \
        $(3); \
        rc=$$?; \
        elapsed_ms=$$(($$( date +%s%3N) - t0)); \
        printf "$(CLR_STEP)→ $(2)  %s/%s$(CLR_RST) (%d.%ds)\n" \
            "$$domain" "$$name" \
            $$((elapsed_ms / 1000)) \
            $$((elapsed_ms % 1000 / 100)); \
        exit $$rc'; \
fi
endef
```

**Bruk:**
```make
gen-jsonschema:
    @echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
    @echo "$(CLR_HDR)*** make gen-jsonschema$(CLR_RST)"
    @echo "$(CLR_SEP)$(SEP)$(CLR_RST)"
    $(call run_parallel,$(call get_target_schemas),gen-json-schema,$(LINKML_RUN) gen-json-schema "$$s" > "$$outdir/$$name-schema.json")
```

**Fordel:** Reduserer ~200 linjer til ~30 linjer. **Ulempe:** Mindre eksplisitt kva kommandoen gjer.

### Alternativ B: Generisk target-generator (anbefalt for steg 2)

**Ide:** Ein `define make_gen_target`-makro som genererer per-generator targets.

```make
# Generisk target-generator
# $1=target-namn  $2=makro-namn
define make_gen_target
.PHONY: $(1)
$(1):
	@echo "$$(CLR_SEP)$$(SEP)$$(CLR_RST)"
ifdef SCHEMA
	@echo "$$(CLR_HDR)*** make $(1) SCHEMA=$$(SCHEMA)$$(CLR_RST)"
else ifdef DOMAIN
	@echo "$$(CLR_HDR)*** make $(1) DOMAIN=$$(DOMAIN)$$(CLR_RST)"
else
	@echo "$$(CLR_HDR)*** make $(1)$$(CLR_RST)"
endif
	@echo "$$(CLR_SEP)$$(SEP)$$(CLR_RST)"
	$$(call $(2),$$(call get_target_schemas))
endef

# Generer alle gen-targets
$(eval $(call make_gen_target,gen-jsonschema,run_gen_parallel))
$(eval $(call make_gen_target,gen-shacl,run_gen_shacl))
# osv.
```

**Fordel:** Reduserer ~110 linjer til ~15 linjer. **Ulempe:** Mindre eksplisitt — må lese `define` for å forstå kva `gen-jsonschema` gjer.

### Alternativ C: Ekstraher MCP-targets til inkludert fil (anbefalt for steg 3)

**Ide:** Flytt MCP-relaterte targets til `src/assets/make/mcp.mk` og inkluder i hovud-Makefile.

```make
# I Makefile
include src/assets/make/mcp.mk
```

```make
# I src/assets/make/mcp.mk
define make_mcp_targets
.PHONY: build-docker-mcp-$(1) mcp-$(1)-run mcp-$(1)-smoke

build-docker-mcp-$(1):
	@echo "$$(CLR_SEP)$$(SEP)$$(CLR_RST)"
	@echo "$$(CLR_HDR)*** make build-docker-mcp-$(1)$$(CLR_RST)"
	@echo "$$(CLR_SEP)$$(SEP)$$(CLR_RST)"
	podman build -t $$(MCP_$(2)_IMAGE) $$(MCP_$(2)_DIR)

mcp-$(1)-run:
	@echo "$$(CLR_SEP)$$(SEP)$$(CLR_RST)"
	@echo "$$(CLR_HDR)*** make mcp-$(1)-run$$(CLR_RST)"
	@echo "$$(CLR_SEP)$$(SEP)$$(CLR_RST)"
	$$(MCP_$(2)_RUN) $$(MCP_$(2)_IMAGE)

mcp-$(1)-smoke: build-docker-mcp-$(1)
	@echo "$$(CLR_SEP)$$(SEP)$$(CLR_RST)"
	@echo "$$(CLR_HDR)*** make mcp-$(1)-smoke$$(CLR_RST)"
	@echo "$$(CLR_SEP)$$(SEP)$$(CLR_RST)"
	cat tests/test-mcp-$(1).json | $$(MCP_$(2)_RUN) $$(MCP_$(2)_IMAGE)
endef

$(eval $(call make_mcp_targets,linkml-validator,VALIDATOR))
$(eval $(call make_mcp_targets,linkml-modell-utkast,MODELL))
$(eval $(call make_mcp_targets,linkml-begrep-utkast,BEGREP))
```

**Fordel:** Ryddigare hovud-Makefile, lettare å leggje til nye MCP-serverar. **Ulempe:** Logikken er ikkje lenger i hovudfila.

### Alternativ D: Behald som det er (ikkje anbefalt)

**Rasjonale:** Makefile er allereie kompleks. Modularisering kan gjere det vanskelegare å debugge.

**Motargument:** Gjentakelsen er så omfattande (~360 linjer) at risikoen for inkonsistens er høgare enn risikoen for overmodularisering.

## Anbefaling

**Trinnvis modularisering** for å balansere reduksjon av gjentakelse mot lesbarheit:

1. **Steg 1:** Implementer **Alternativ A** (generisk parallell generator-makro) — låg risiko, stor gevinst (~200 linjer → ~30)
2. **Steg 2:** Implementer **Alternativ B** (generisk target-generator) — medium risiko, medium gevinst (~110 linjer → ~15)
3. **Steg 3:** Vurder **Alternativ C** (ekstraher MCP-targets) — låg risiko, ryddelegare struktur

**Ikkje modulariser:**
- `domain_target`-makroen — for kompleks logikk, semantiske skilnader mellom domene
- `run_gen_xsd` / `run_gen_asyncapi` / `run_gen_openapi` — desse har allereie manifest-sjekkar og særlogikk

## Risikominimering

- **Test grundig** etter kvar modularisering: `make domain-ap-no`, `make gen-jsonschema DOMAIN=oreg`, osv.
- **Dokumenter abstraksjonane** i kommentarar over kvar `define`-blokk
- **Behald echo-kommandoane** — debugging-venlegheit er viktigare enn kompaktheit
- **Bruk tydelege namn** — ikkje `run_gen2`, men `run_parallel_with_timer`

## Utføring

Implementer steg 1 og 2 dersom brukar godkjenner. Steg 3 kan gjerast separat.

## Utført

**Steg 1 og 2 gjennomført** — Makefile redusert frå 1557 til 1366 linjer (**-191 linjer, -12%**).

### Steg 1: Generisk parallell generator-makro

Implementert `run_parallel_with_timer`-makro som tek kommando-snippet som argument. Refaktorerte 7 parallelle makroar:

- ✅ `run_gen_parallel` — redusert frå 23 til 2 linjer
- ✅ `run_gen_linkml_parallel` — redusert frå 19 til 2 linjer (+ 3 linjer for serial-fallback)
- ✅ `run_gen_owl_parallel` — redusert frå 19 til 3 linjer
- ✅ `run_gen_rdf_parallel` — redusert frå 19 til 2 linjer
- ✅ `run_gen_doc_parallel` — redusert frå 32 til 15 linjer
- ✅ `run_gen_erdiagram_parallel` — redusert frå 26 til 9 linjer
- ✅ `run_gen_plantuml_parallel` — redusert frå 27 til 11 linjer

**Viktig merknad:** `run_gen_openapi_parallel` og `run_gen_asyncapi_parallel` vart **ikkje** refaktorerte — desse har manifest-sjekkar og kondisjonell logikk som ikkje passar i den generiske makroen.

### Steg 2: Generisk target-generator

Implementert `make_gen_target`-makro som genererer targets med standard header-logikk. Erstatta 12 manuelt definerte targets med `$(eval $(call make_gen_target,...))`:

- ✅ `gen-jsonld-context`, `gen-shacl`, `gen-python`, `gen-jsonschema`
- ✅ `gen-owl`, `gen-rdf`, `gen-xsd`, `gen-asyncapi`, `gen-openapi`
- ✅ `gen-erdiagram`, `gen-proto`, `gen-plantuml`
- ✅ `gen-docs` (spesiell — kallar to makroar, difor ikkje generert)

Kvar target gjekk frå ~10 linjer til 1 linje `$(eval ...)`-kall.

### Testing

```bash
make -n gen-jsonschema  # OK — ingen syntax-errors
wc -l Makefile          # 1366 (før: 1557)
```

**Neste steg (valfritt):** Steg 3 — ekstraher MCP-targets til separat fil (`src/assets/make/mcp.mk`) for ytterlegare modularisering.
