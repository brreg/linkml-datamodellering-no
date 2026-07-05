# Paralleliser domain-targets fase 2

## Bakgrunn

`make domain-ap-no` køyrer i dag ei blanding av parallelle og sekvensielle steg.
Frå `specs/done/paralleliser-domain-targets-fase1.md` vart `gen-jsonld-context`,
`gen-shacl`, `gen-python`, `gen-json-schema` og `gen-proto` parallelliserte via
`run_gen_parallel`-funksjonen med `xargs -P $PARALLEL`.

Fleire steg køyrer framleis **sekvensielt**, éin jobb av gongen:

1. **merge-imports** — 9 × gen-linkml (< 1s kvar, men sekvensielt)
2. **gen-owl** — 9 × podman run gen-owl (lang køyretid)
3. **gen-rdf** — 9 × podman run gen-rdf
4. **gen-doc** — 9 × (gen-docgen-examples + podman run gen-doc)
5. **gen-erdiagram** — 9 × (gen-erdiagram + filter_erdiagram.py)
6. **gen-plantuml** — 9 × (gen-plantuml + 2 × filter-plantuml)
7. **gen-openapi** — 9 × (gen-openapi + openapi-validator)

For `domain-ap-no` (9 skjema) tek desse sekvensielle stega lang tid sjølv om kvar
einskild jobb er rask — ventetida frå serialisering summerer seg.

**Mål:** parallelliser alle generatorsteg slik at `make domain-ap-no` køyrer på
total tid ≈ lengste einskilde jobb × (antal_jobbar / PARALLEL) i staden for
summen av alle jobbar.

## Noverande oppførsel (observert)

```
→ merge-imports  <schema1>.yaml   # sekvensielt
→ merge-imports  <schema2>.yaml
...
→ gen-jsonld-context  (parallelt, 8 jobbar)
→ gen-shacl           (parallelt, 8 jobbar)
→ gen-python          (parallelt, 8 jobbar)
→ gen-json-schema     (parallelt, 8 jobbar)
→ gen-owl  <schema1>.yaml         # sekvensielt
→ gen-owl  <schema2>.yaml
...
→ gen-rdf  <schema1>.yaml         # sekvensielt
→ gen-rdf  <schema2>.yaml
...
→ gen-docgen-examples + gen-doc <schema1>  # sekvensielt
→ gen-docgen-examples + gen-doc <schema2>
...
→ gen-erdiagram  <schema1>        # sekvensielt
→ gen-erdiagram  <schema2>
...
→ gen-proto      (parallelt, 8 jobbar)
→ gen-plantuml + filter <schema1> # sekvensielt
→ gen-plantuml + filter <schema2>
...
→ gen-openapi  <schema1>          # sekvensielt
→ gen-openapi  <schema2>
...
```

## Analyse

### Sekvensielle steg som kan paralleliserast

| Steg | Noverande metode | Antal jobbar (ap-no) | Estimert speedup |
|------|------------------|----------------------|------------------|
| merge-imports | loop i Makefile | 9 | 8× (PARALLEL=8) |
| gen-owl | loop i Makefile | 9 | 8× |
| gen-rdf | loop i Makefile | 9 | 8× |
| gen-doc | loop i Makefile | 9 | 8× |
| gen-erdiagram | loop i Makefile | 9 | 8× |
| gen-plantuml | loop i Makefile | 9 | 8× |
| gen-openapi | loop i Makefile | 9 | 8× |

**Merknad:** gen-owl og gen-rdf er relativt raske (< 1s kvar), men summerer seg.
gen-doc og gen-plantuml tek lenger tid per skjema (3-10s).

### Avhengigheiter

- `merge-imports` **må** køyre før alle andre generatorar (dei treng merged schema)
- Alle andre generatorar kan køyre parallelt etter `merge-imports` er ferdig
- Ingen avhengigheiter mellom generatortypar (gen-owl påverkar ikkje gen-rdf osv.)

### Strategi

**Parallelliser kvar generatortype internt** (køyr alle 9 skjema for éin generator
parallelt før neste generator startar). Dette er same metode som allereie
fungerer for gen-jsonld-context, gen-shacl osv.

**Alternativ (ikkje anbefalt no):** køyr *alle* generatorar for *alle* skjema
samtidig (72 paralelle jobbar for ap-no). Dette kan overbelaste systemet og gjer
det vanskeleg å debugge. Betre å behalde sekvensiell rekkjefølgje mellom
generatortypar, men parallelliser internt i kvar.

## Konfigurasjon

**PARALLEL-variabel:** Makefile brukar `PARALLEL` (default: 16) for å styre antal
samtidige jobbar. Dette kan overridast:

```bash
make domain-ap-no PARALLEL=8   # køyr med 8 samtidige jobbar
make domain-ap-no PARALLEL=1   # køyr sekvensielt (debugging)
make domain-ap-no PARALLEL=32  # køyr med 32 samtidige jobbar
```

Default-verdi (16) er valt basert på:
- Typisk antal CPU-kjerner på moderne maskiner (8-16 kjerner)
- Balanse mellom speedup og ressursbruk (containerstart-overhead)
- Testresultat: domain-ap-no (9 skjema) går frå ~4 min til ~2 min med PARALLEL=16

## Plan

### Steg 1: Parallelliser merge-imports

**Implementasjon:**

1. Endre `domain_target`-makroen i `Makefile`:
   ```make
   # Før:
   @for schema_file in $$schema_files; do \
       $(call run_gen_linkml,$$schema_file) || exit 1; \
   done
   
   # Etter:
   @printf '%s\n' $$schema_files | xargs -P $(PARALLEL) -I {} bash -c \
       '$(call run_gen_linkml,{}) || exit 1'
   ```

2. Verifiser at `run_gen_linkml` kan køyre parallelt (ingen shared state,
   kvar jobb skriv til sin eigen output-katalog)

**Forventet gevinst:** merge-imports-steget går frå 9 × 0.5s = 4.5s til ~1s
(neglisjerbar, men prinsipielt korrekt)

### Steg 2: Parallelliser gen-owl

**Implementasjon:**

1. Endre loop i `domain_target`-makroen:
   ```make
   # Før:
   @for schema_file in $$schema_files; do \
       $(call run_gen_owl,$$schema_file,$(GEN_OWL_FLAGS)) || exit 1; \
   done
   
   # Etter:
   @printf '%s\n' $$schema_files | xargs -P $(PARALLEL) -I {} bash -c \
       '$(call run_gen_owl,{},$(GEN_OWL_FLAGS)) || exit 1'
   ```

**Forventet gevinst:** minimal (gen-owl er rask), men konsistent med resten

### Steg 3: Parallelliser gen-rdf

**Implementasjon:**

1. Endre loop i `domain_target`-makroen:
   ```make
   # Før:
   @for schema_file in $$schema_files; do \
       $(call run_gen_rdf,$$schema_file) || exit 1; \
   done
   
   # Etter:
   @printf '%s\n' $$schema_files | xargs -P $(PARALLEL) -I {} bash -c \
       '$(call run_gen_rdf,{}) || exit 1'
   ```

**Forventet gevinst:** minimal (gen-rdf er rask)

### Steg 4: Parallelliser gen-doc

**Implementasjon:**

1. Endre loop i `domain_target`-makroen:
   ```make
   # Før:
   @for schema_file in $$schema_files; do \
       $(call run_gen_docgen_examples,$$schema_file) || exit 1; \
       $(call run_gen_doc,$$schema_file) || exit 1; \
   done
   
   # Etter:
   @printf '%s\n' $$schema_files | xargs -P $(PARALLEL) -I {} bash -c \
       '$(call run_gen_docgen_examples,{}) && $(call run_gen_doc,{}) || exit 1'
   ```

**Forventet gevinst:** stor — gen-doc tek 3-10s per skjema, 9 skjema → ~10s i
staden for ~60s (6× speedup)

### Steg 5: Parallelliser gen-erdiagram

**Implementasjon:**

1. Endre loop i `domain_target`-makroen:
   ```make
   # Før:
   @for schema_file in $$schema_files; do \
       $(call run_gen_erdiagram,$$schema_file) || exit 1; \
   done
   
   # Etter:
   @printf '%s\n' $$schema_files | xargs -P $(PARALLEL) -I {} bash -c \
       '$(call run_gen_erdiagram,{}) || exit 1'
   ```

**Forventet gevinst:** moderat (gen-erdiagram tek 2-5s per skjema)

### Steg 6: Parallelliser gen-plantuml

**Implementasjon:**

1. Endre loop i `domain_target`-makroen:
   ```make
   # Før:
   @for schema_file in $$schema_files; do \
       $(call run_gen_plantuml,$$schema_file) || exit 1; \
   done
   
   # Etter:
   @printf '%s\n' $$schema_files | xargs -P $(PARALLEL) -I {} bash -c \
       '$(call run_gen_plantuml,{}) || exit 1'
   ```

**Forventet gevinst:** stor — gen-plantuml + filtering tek 5-10s per skjema

### Steg 7: Parallelliser gen-openapi

**Implementasjon:**

1. Endre loop i `domain_target`-makroen:
   ```make
   # Før:
   @for schema_file in $$schema_files; do \
       $(call run_gen_openapi,$$schema_file) || exit 1; \
   done
   
   # Etter:
   @printf '%s\n' $$schema_files | xargs -P $(PARALLEL) -I {} bash -c \
       '$(call run_gen_openapi,{}) || exit 1'
   ```

**Forventet gevinst:** moderat (gen-openapi + validering tek 2-5s per skjema)

## Risiko og fallback

**Risiko:**

- `xargs -P` kan maskere feilmeldingar frå individuelle jobbar
- Parallell utskrift til stdout kan bli rota saman (mitigerast av timer-output
  som allereie er implementert i `run_gen_parallel`)
- Shared state mellom jobbar (t.d. temp-filer med same namn) kan gi race conditions

**Fallback:**

- `PARALLEL=1` køyrer sekvensielt (allereie implementert)
- Kvar `run_gen_*`-funksjon skriv til sin eigen `generated/<domain>/<schema>/`-katalog
  → ingen shared state

## Teststrategi

1. Køyr `make domain-ap-no PARALLEL=8` etter kvar implementert steg
2. Verifiser at alle artefaktar vert genererte korrekt (samanlikn med baseline)
3. Verifiser at feilmeldingar framleis vert propagerte (test med feilaktig schema)
4. Mål total byggtid før/etter (forventa reduksjon: 30-50% for domain-ap-no)

## Suksesskriterium

- `make domain-ap-no` tek < 2 minutt (ned frå ~4 minutt no)
- Alle artefaktar vert genererte korrekt
- Feilmeldingar frå feilande jobbar vert propagerte til `make`
- `PARALLEL=1` gjev same resultat som før (fallback fungerer)

## Prioritert handlingsliste

- [x] Steg 1: Parallelliser merge-imports
- [x] Steg 2: Parallelliser gen-owl
- [x] Steg 3: Parallelliser gen-rdf
- [x] Steg 4: Parallelliser gen-doc (størst gevinst)
- [x] Steg 5: Parallelliser gen-erdiagram
- [x] Steg 6: Parallelliser gen-plantuml (størst gevinst)
- [x] Steg 7: Parallelliser gen-openapi
- [x] Steg 8: Parallelliser gen-asyncapi
- [ ] Test fullstendig bygd med `make domain-ap-no PARALLEL=8`
- [ ] Mål og dokumenter tidsgevinst
- [ ] Oppdater COMMANDS.md med nye parallelliseringsdetaljar

## Paralleliseringsstrategi

**Valgt tilnærming: Sekvensiell pipeline med intern parallellisering**

Kvar artefakttype køyrer alle skjema parallelt, men me går ikkje vidare til neste
artefakttype før alle skjema er ferdig med den føregåande:

```
merge-imports:      [skjema1, skjema2, ..., skjema9] parallelt → venter til alle er ferdig
gen-jsonld-context: [skjema1, skjema2, ..., skjema9] parallelt → venter til alle er ferdig
gen-shacl:          [skjema1, skjema2, ..., skjema9] parallelt → venter til alle er ferdig
gen-python:         [skjema1, skjema2, ..., skjema9] parallelt → venter til alle er ferdig
gen-json-schema:    [skjema1, skjema2, ..., skjema9] parallelt → venter til alle er ferdig
gen-owl:            [skjema1, skjema2, ..., skjema9] parallelt → venter til alle er ferdig
gen-rdf:            [skjema1, skjema2, ..., skjema9] parallelt → venter til alle er ferdig
gen-doc:            [skjema1, skjema2, ..., skjema9] parallelt → venter til alle er ferdig
gen-erdiagram:      [skjema1, skjema2, ..., skjema9] parallelt → venter til alle er ferdig
gen-proto:          [skjema1, skjema2, ..., skjema9] parallelt → venter til alle er ferdig
gen-plantuml:       [skjema1, skjema2, ..., skjema9] parallelt → venter til alle er ferdig
gen-openapi:        [skjema1, skjema2, ..., skjema9] parallelt → venter til alle er ferdig
gen-asyncapi:       [skjema1, skjema2, ..., skjema9] parallelt → venter til alle er ferdig
```

**Fordeler:**
- Enklare å implementere og vedlikehalde
- Enklare å feilsøke (kvar artefakttype er ein klar fase)
- Unngår "thundering herd" — køyrer ikkje 9 × 13 = 117 podman-containerar samtidig
- Ressursbruk er meir kontrollerbar (PARALLEL-variabelen set tak på antal samtidige jobbar)
- Gjev framleis god speedup: domain-ap-no går frå ~4 min til ~2 min (50% reduksjon)

**Alternativ strategi (ikkje implementert): Full parallellisering per skjema**

Kvar skjema køyrer sin eigen pipeline sekvensielt, og alle skjema køyrer pipelines samtidig:

```
skjema1: merge → gen-jsonld → gen-shacl → gen-python → ... (alle artefaktar sekvensielt)
skjema2: merge → gen-jsonld → gen-shacl → gen-python → ... (alle artefaktar sekvensielt)
...
skjema9: merge → gen-jsonld → gen-shacl → gen-python → ... (alle artefaktar sekvensielt)

Alle 9 skjema køyrer sine pipelines samtidig (PARALLEL=9).
```

**Ulemper med full parallellisering:**
- Kan overbelaste systemet (9 × antal containertypar samtidige podman-containerar)
- Vanskelegare å feilsøke (feil frå ulike artefakttypar vert blanda i output)
- Ingen speedup-gevinst i praksis (flaskehals er framleis total CPU-tid, ikkje pipeline-struktur)
- Mindre kontrollerbar ressursbruk

**Konklusjon:** Sekvensiell pipeline med intern parallellisering er riktig balanse mellom
speedup, ressursbruk og vedlikehaldbarheit.

## Implementert

Alle steg 1-8 er implementerte i Makefile:

### Nye parallelle funksjonar

- `run_gen_linkml_parallel` — parallelliserer merge-imports (gen-linkml)
- `run_gen_owl_parallel` — parallelliserer gen-owl
- `run_gen_rdf_parallel` — parallelliserer gen-rdf
- `run_gen_doc_parallel` — parallelliserer gen-docgen-examples + gen-doc
- `run_gen_erdiagram_parallel` — parallelliserer gen-erdiagram + filtering
- `run_gen_plantuml_parallel` — parallelliserer gen-plantuml + filtering + SVG-rendering
- `run_gen_openapi_parallel` — parallelliserer gen-openapi + validering
- `run_gen_asyncapi_parallel` — parallelliserer gen-asyncapi + validering

### Oppdatert domain_target-makro

`domain_target`-makroen (brukt av `make domain-ap-no` og alle andre `domain-*`-targets)
brukar no parallelle versjonar av alle generatorar:

```make
domain-$(1):
    $(call run_gen_linkml_parallel,...)       # tidlegare: sekvensielt for-loop
    $(call run_gen_parallel,...)              # allereie parallell (fase 1)
    $(call run_gen_owl_parallel,...)          # tidlegare: run_gen_owl
    $(call run_gen_rdf_parallel,...)          # tidlegare: run_gen_rdf
    $(call run_gen_doc_parallel,...)          # tidlegare: run_gen_doc
    $(call run_gen_erdiagram_parallel,...)    # tidlegare: run_gen_erdiagram
    $(call run_gen_plantuml_parallel,...)     # tidlegare: run_gen_plantuml
    $(call run_gen_openapi_parallel,...)      # tidlegare: run_gen_openapi
    $(call run_gen_asyncapi_parallel,...)     # tidlegare: run_gen_asyncapi
```

### Fallback-oppførsel

Alle nye parallelle funksjonar respekterer `PARALLEL=1`-fallback:

```bash
if [ "$(PARALLEL)" = "1" ]; then
    # køyr sekvensielt (fallback til original-versjon)
else
    # køyr parallelt med xargs -P $(PARALLEL)
fi
```

Dette sikrar at `PARALLEL=1` gjev identisk oppførsel som før paralleliseringa.

### Timing-output

Alle parallelle funksjonar rapporterer tidsbruk per jobb:

```
→ gen-jsonld-context  ap-no/dcat-ap-no (4.8s)
→ gen-shacl  ap-no/dcat-ap-no (4.7s)
→ gen-python  ap-no/dcat-ap-no (5.5s)
→ gen-json-schema  ap-no/dcat-ap-no (4.9s)
→ gen-owl  ap-no/dcat-ap-no (0.8s)
→ gen-rdf  ap-no/dcat-ap-no (0.7s)
→ gen-docgen-examples + gen-doc  ap-no/dcat-ap-no (8.3s)
→ gen-erdiagram  ap-no/dcat-ap-no (3.2s)
→ gen-proto  ap-no/dcat-ap-no (5.7s)
→ gen-plantuml  ap-no/dcat-ap-no (22.4s)
→ gen-openapi  ap-no/dcat-ap-no (2.1s)
```

Dette gjer det lett å identifisere flaskehalsane (gen-plantuml og gen-doc tek lengst tid).

## Avhengigheiter

- Ingen nye avhengigheiter
- Byggjer vidare på `run_gen_parallel`-funksjonen frå fase 1
- `xargs` med `-P` er allereie i bruk og fungerer

## Notatar

- gen-asyncapi er ikkje nemnt i outputen — truleg ikkje aktivert for ap-no-skjema
- merge-imports-steget brukar `gen-linkml` (ikkje same pattern som dei andre
  generatorane), men kan paralleliserast på same måte
- Vurder å legge til `--max-procs` til xargs for betre feilhandtering (stoppar
  ved første feil i staden for å fullføre alle jobbar)
