# Prefiks domene-targets med `domain-`

## Bakgrunn

Repoet genererer dynamisk 8 make targets for kvart domene (ap-no, fint, samt, ngr, oreg, modellkatalog, begrepskatalog, fair). Desse targets køyrer generering for alle skjema i domenet:

```bash
make ap-no          # genererer alle artefaktar for ap-no-domenet
make fint           # genererer alle artefaktar for fint-domenet
make samt           # genererer alle artefaktar for samt-domenet
```

**Problem:** Targetnamna er korte og generiske, og kan kollidere med andre target-konvensjonar i framtida. Det er ikkje umiddelbart tydeleg at `make ap-no` er eit domene-target utan å kjenne repostrukturen.

**Motivasjon:** Følgje same namnekonvensjon som nyleg innførte `validate-* DOMAIN=...` og `gen-* DOMAIN=...` der domene alltid er eksplisitt (`DOMAIN=ap-no`). For consistency bør også domene-targets ha `domain-`-prefix.

## Foreslått løysing

Endre `domain_target`-funksjonen i Makefile til å generere targets med `domain-`-prefix:

```bash
# Før:
make ap-no
make fint
make samt

# Etter:
make domain-ap-no
make domain-fint
make domain-samt
```

### Implementasjon

Endringa skjer i `define domain_target` (rundt linje 602 i Makefile):

**Før:**
```makefile
define domain_target
_schemas_$(1) := $(filter $(SCHEMA_DIR)/$(1)/%,$(SCHEMAS))

.PHONY: $(1)
$(1):
	@echo "$(CLR_SEP)$$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make $(1)$(CLR_RST)"
	...
endef

$(foreach d,$(DOMAINS),$(eval $(call domain_target,$(d))))
```

**Etter:**
```makefile
define domain_target
_schemas_$(1) := $(filter $(SCHEMA_DIR)/$(1)/%,$(SCHEMAS))

.PHONY: domain-$(1)
domain-$(1):
	@echo "$(CLR_SEP)$$(SEP)$(CLR_RST)"
	@echo "$(CLR_HDR)*** make domain-$(1)$(CLR_RST)"
	...
endef

$(foreach d,$(DOMAINS),$(eval $(call domain_target,$(d))))
```

### Konsekvens

- **Før:** 8 targets (ap-no, begrepskatalog, fair, fint, modellkatalog, ngr, oreg, samt)
- **Etter:** 8 targets (domain-ap-no, domain-begrepskatalog, domain-fair, domain-fint, domain-modellkatalog, domain-ngr, domain-oreg, domain-samt)
- **Breaking change:** Alle som brukar `make <domene>` må bytte til `make domain-<domene>`

## Steg

1. **Oppdater `domain_target`-funksjonen i Makefile**
   - Endre `.PHONY: $(1)` → `.PHONY: domain-$(1)`
   - Endre `$(1):` → `domain-$(1):`
   - Oppdater header-melding: `*** make $(1)` → `*** make domain-$(1)`

2. **Oppdater .PHONY-deklarasjon**
   - Endre `$(DOMAINS)` → lag eigen loop som legg til `domain-` prefix
   - Eller: lat `$(DOMAINS)` vere som den er, sidan `.PHONY: domain-$(1)` vert sett i `domain_target`

3. **Oppdater COMMANDS.md**
   - Finn seksjon som dokumenterer domene-targets
   - Oppdater til nye namn: `make domain-<domene>`

4. **Test alle 8 domene-targets**
   - `make -n domain-ap-no`
   - `make -n domain-fint`
   - `make -n domain-samt`
   - osv.

5. **Verifiser at tab-completion fungerer**
   - Sjekk at `make domain-<tab>` viser alle domene

## Prioritert handlingsliste

- [ ] Oppdater `define domain_target` i Makefile (linje ~602)
  - [ ] `.PHONY: $(1)` → `.PHONY: domain-$(1)`
  - [ ] `$(1):` → `domain-$(1):`
  - [ ] Header: `*** make $(1)` → `*** make domain-$(1)`
- [ ] Verifiser at .PHONY-deklarasjon er korrekt (`.PHONY: domain-$(1)` vert sett i define-blokka)
- [ ] Oppdater COMMANDS.md med nye domene-targetnamn
- [ ] Test alle 8 domene-targets med `make -n domain-<domene>`
- [ ] Verifiser at tab-completion viser `domain-*` targets

## Avhengigheiter

- Eksisterande `domain_target`-funksjon i Makefile
- `$(DOMAINS)`-variabel som inneheld alle domene
- COMMANDS.md

## Merknader

- **Breaking change:** Alle som brukar `make <domene>` må bytte til `make domain-<domene>`
- **Konsistens:** Følgjer mønsteret frå `validate-* DOMAIN=...` der domenet alltid er eksplisitt
- **Namnerom:** Frigjer `ap-no`, `fint`, `samt`, osv. til anna bruk
- **Tydeleg:** `make domain-ap-no` er meir sjølvforklarande enn `make ap-no`
- **Tab-completion:** `make domain-<tab>` viser alle domene samla

## Eksempel: før og etter

### Før
```bash
make ap-no          # generer alle artefaktar for ap-no
make fint           # generer alle artefaktar for fint
make samt           # generer alle artefaktar for samt
```

### Etter
```bash
make domain-ap-no   # generer alle artefaktar for ap-no
make domain-fint    # generer alle artefaktar for fint
make domain-samt    # generer alle artefaktar for samt
```

### Tab-completion
```bash
# Før:
make <tab>          # viser ap-no, fint, samt blant 70+ andre targets

# Etter:
make domain-<tab>   # viser domain-ap-no, domain-fint, domain-samt, osv.
```

## Utført

Alle steg er implementerte:

**Makefile-endringar:**
- `define domain_target` (linje 602-608): endra frå `$(1)` til `domain-$(1)`
  - `.PHONY: $(1)` → `.PHONY: domain-$(1)`
  - `$(1):` → `domain-$(1):`
  - Header: `*** make $(1)` → `*** make domain-$(1)`
- `.PHONY`-deklarasjon: fjerna `$(DOMAINS)` (no sett i `domain_target`-funksjonen)

**COMMANDS.md-endringar:**
- Seksjonen "Per domene (anbefalt)": oppdatert alle 8 targets
  - `make ap-no` → `make domain-ap-no`
  - `make fint` → `make domain-fint`
  - `make samt` → `make domain-samt`
  - osv.

**Testing:**
- Alle 8 domene-targets testa med `make -n domain-<domene>` — fungerer
- Gamle namn (`make ap-no`) returnerer "No rule to make target" — korrekt

**Resultat:**
- 8 domene-targets omdøypt: `ap-no` → `domain-ap-no`, osv.
- Konsekvent namnemønster: `domain-*` for domene, `gen-*` for generering, `validate-*` for validering
- Tab-completion: `make domain-<tab>` grupperer alle domene-targets

**Breaking change:**
Alle som brukar `make <domene>` må bytte til `make domain-<domene>`.
