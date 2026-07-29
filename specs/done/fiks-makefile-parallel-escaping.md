# Fiks Makefile parallel escaping-feil i CI

## Bakgrunn

CI-jobben `generate / ap-no` feiler med feilmelding:

```
Error: Invalid value for 'YAMLFILE': File '3368s' does not exist.
```

Rotårsak: Commit `b99df8e0` endra escaping i `run_parallel_with_timer` frå `$$$$` til `$$` i bash-c-strengen (linje 82-94), men kallarane til denne funksjonen (linje 101, 111, 117 osv.) brukar framleis `$$$$`.

**Konsekvens:**
- `$(call run_parallel_with_timer,...)` ekspanderer `$$$$s` → `$$s`
- Desse `$$s` vert sette inn i `$(4)` (linje 86 i bash-c-strengen)
- Bash ser `$$s` i staden for `$s`, som gjer at `$$` blir PID (t.d. `3368`) + bokstaven `s`

**Forklaring av escaping-nivå:**

```make
define run_gen_linkml_parallel
$(call run_parallel_with_timer,$(1),merge-imports,run_gen_linkml_serial,$(LINKML_RUN) gen-linkml "$$s" > /dev/null)
endef
```

1. Make-expansion i `define`: `$$s` → `$s` (i call-argumentet)
2. `call` setter `$(4)` til `linkml-run gen-linkml "$s" > /dev/null`
3. Bash-c-strengen får `$s` (som refererer til bash-variabelen definert på linje 81: `s="{}";`)

**Feil escaping (før fix):**
- `$$$$s` → `$$s` (etter call) → bash ser `$$s` → PID + "s" → `3368s`

**Korrekt escaping (etter fix):**
- `$$s` → `$s` (etter call) → bash ser `$s` → verdien av `s`-variabelen

## Steg

### 1. Identifiser alle kallar til `run_parallel_with_timer`

```bash
grep -n "run_parallel_with_timer" Makefile
```

Finn alle linjer som kallar funksjonen og sjekk at argument `$(4)` brukar korrekt escaping.

### 2. Rett escaping i `run_gen_parallel` (linje 101)

Endre frå:
```make
$(call run_parallel_with_timer,$(1),$(2),run_gen,mkdir -p "$$$$outdir" && $(LINKML_RUN) $(2) "$$$$s" > "$$$$outdir/$$$$name-$(3)")
```

Til:
```make
$(call run_parallel_with_timer,$(1),$(2),run_gen,mkdir -p "$$outdir" && $(LINKML_RUN) $(2) "$$s" > "$$outdir/$$name-$(3)")
```

### 3. Rett escaping i `run_gen_linkml_parallel` (linje 111)

Endre frå:
```make
$(call run_parallel_with_timer,$(1),merge-imports,run_gen_linkml_serial,$(LINKML_RUN) gen-linkml "$$$$s" > /dev/null)
```

Til:
```make
$(call run_parallel_with_timer,$(1),merge-imports,run_gen_linkml_serial,$(LINKML_RUN) gen-linkml "$$s" > /dev/null)
```

### 4. Rett escaping i `run_gen_owl_parallel` (linje 117)

Endre frå:
```make
$(call run_parallel_with_timer,$(1),gen-owl,run_gen_owl,mkdir -p "$$$$outdir" && $(LINKML_RUN) gen-owl $(OWL_DEFAULT_FLAGS) "$$$$s" > "$$$$outdir/$$$$name-ontology.ttl")
```

Til:
```make
$(call run_parallel_with_timer,$(1),gen-owl,run_gen_owl,mkdir -p "$$outdir" && $(LINKML_RUN) gen-owl $(OWL_DEFAULT_FLAGS) "$$s" > "$$outdir/$$name-ontology.ttl")
```

### 5. Rett escaping i `run_gen_plantuml_parallel`

Finn linja og rett `$$$$`-referansar til `$$`.

### 6. Test lokalt

```bash
make domain-ap-no PARALLEL=4
```

Verifiser at:
- Ingen feilmeldingar om "File '3368s' does not exist"
- Merge-imports køyrer for alle ap-no skjema
- Timer-output viser korrekt domene/namn

### 7. Verifiser i CI

Push til ein test-branch og sjekk at `generate / ap-no` køyrer utan feil.

## Handlingsliste

- [x] Grep alle `run_parallel_with_timer`-kallar
- [x] Rett escaping i `run_gen_parallel` (linje 101): `$$$$` → `$$`
- [x] Rett escaping i `run_gen_linkml_parallel` (linje 111): `$$$$` → `$$`
- [x] Rett escaping i `run_gen_owl_parallel` (linje 117): `$$$$` → `$$`
- [x] Rett escaping i `run_gen_rdf_parallel` (linje 122): `$$$$` → `$$`
- [x] Rett escaping i `run_gen_doc_parallel` (linje 127-141): `$$$$` → `$$`
- [x] Rett escaping i `run_gen_erdiagram_parallel` (linje 146-154): `$$$$` → `$$`
- [x] Rett escaping i `run_gen_plantuml_parallel` (linje 159-169): `$$$$` → `$$`
- [x] Test lokalt: `make domain-ap-no PARALLEL=4` — exit code 0, ingen `File '3368s'`-feil
- [ ] Verifiser i CI

## Rotårsak-oppsummering

Commit `b99df8e0` korrigerte escaping i `bash -c`-strengen (linje 82-94) frå `$$$$` til `$$`, men gløymde å oppdatere kallarane som sender kommandoar til `$(4)`. Desse må også bruke `$$` i staden for `$$$$`, sidan `$(call ...)` allereie ekspanderer éin gong.

## Utført

Alle 7 `run_*_parallel`-definisjonar (linje 101, 111, 117, 122, 127, 146, 159) er oppdaterte frå `$$$$` til `$$` for alle variabelreferansar (`s`, `name`, `domain`, `outdir`).

**Verifisert lokalt:**
```bash
make domain-ap-no PARALLEL=4
```

Output:
```
→ merge-imports  ap-no/common-ap-no (3.3s)
→ merge-imports  ap-no/cpsv-ap-no (4.3s)
...
→ gen-proto  ap-no/modelldcat-modell (4.6s)
```

- Exit code: 0
- Ingen feilmeldingar om `File '3368s' does not exist`
- Alle parallelle generatorar køyrde korrekt

**Neste steg:** Push til CI og verifiser at `generate / ap-no` køyrer utan feil.
