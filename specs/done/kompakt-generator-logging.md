# Kompakt logging for generator-makroar i make domain-&lt;domain&gt;

## Bakgrunn

`run_parallel_with_timer` i `make/10-generator-macros.mk` er delt av 6
generator-makroar (`run_gen_parallel` — brukt for gen-jsonld-context,
gen-shacl, gen-python, gen-json-schema — samt `run_gen_owl_parallel`,
`run_gen_rdf_parallel`, `run_gen_doc_parallel`, `run_gen_erdiagram_parallel`,
`run_gen_plantuml_parallel`, `run_gen_linkml_parallel`). Han logger i dag
`log_debug "[domain/name] Startar <generator>: ..."` for **alle** skjema før
build.yaml-flagget vert sjekka, deretter — inne i sjølve genererings-
kommandoen (3. argument) — ein separat `Hoppar over <generator> (... ikkje
sett i build.yaml)` per skjema utan flagget. Resultat: to linjer per hoppa-
over skjema, interfoldia mellom parallelle xargs-arbeidarar, per
generator-type — ugjennomsiktig CI-logg (sjå eksempel frå brukar, alle 9
skjema i ap-no logga individuelt for gen-jsonld-context, sjølv om berre 2
faktisk fekk artefaktet generert).

## Steg

1. Endre `run_parallel_with_timer` (`make/10-generator-macros.mk`) til å ta
   eit valfritt 4. argument (`$4` = build.yaml-flaggnamn, tom streng = inga
   filtrering):
   - Filtrer skjemalista mot `$4` i build.yaml **før** xargs-parallelliseringa
     startar (éin bash-løkke i det ytre steget, ikkje inne i kvar arbeidar)
   - Skriv éi deloverskrift via `log_info`: `→ <generator>: domain/skjema1,
     domain/skjema2, ...` (eller `(ingen skjema aktivert)` om lista er tom)
   - Skriv éi samla `log_debug`-linje for dei som vert hoppa over:
     `hoppar over (<flag> ikkje sett): domain/skjemaX, domain/skjemaY` —
     berre synleg på `LOGLVL=DEBUG`
   - Køyr xargs berre på dei filtrerte (aktiverte) skjemaa
2. Fjern det no overflødige per-skjema flagg-sjekk-og-hopp-over-blokka frå
   kvart av dei 6 kallande makroane (`run_gen_parallel`,
   `run_gen_owl_parallel`, `run_gen_rdf_parallel`, `run_gen_doc_parallel`,
   `run_gen_erdiagram_parallel`, `run_gen_plantuml_parallel`) — flagget vert
   no gitt som 4. argument til `run_parallel_with_timer` i staden.
3. `run_gen_linkml_parallel` (merge-imports, ingen flagg) kallar med tomt 4.
   argument — ingen filtrering, men får framleis deloverskrifta.
4. **Utanfor scope, urørt:** `run_gen_with_check_parallel` (openapi/asyncapi
   — ekstra sjekk på manglande input-fil) og `run_gen_xsd` (serial, eiga
   løkke) — strukturelt ulike skip-vilkår.
5. Verifiser med `make -n domain-fair` (dry-run, syntakssjekk av
   make-escaping) før reell køyring.
6. Reell test: `make domain-fair` (minste domenet, 1 skjema) — stadfest at
   deloverskrift + eventuelt skip-samandrag vert vist korrekt, og at
   artefakt-generering framleis fungerer identisk til før endringa.
7. Reell test med `LOGLVL=DEBUG make domain-fair` — stadfest at
   skip-samandraget vert vist.

## Handlingsliste

- [x] Endre `run_parallel_with_timer` med filtrering + deloverskrift + samla skip-logg
- [x] Forenkle dei 6 kallande makroane (fjern duplikat flagg-sjekk)
- [x] `make -n domain-fair` dry-run
- [x] `make domain-fair` reell test (INFO-nivå)
- [x] `LOGLVL=DEBUG` skip-logg verifisert isolert (skip-formatering + at linja er usynleg på INFO)
- [x] Commit-melding

## Utført

`run_parallel_with_timer` filtrerer no `$1` mot `$4` (build.yaml-flagg) FØR
xargs-parallelliseringa startar, skriv éi deloverskrift via `log_info` med
domain/skjema-lista som får artefaktet (eller `(ingen skjema aktivert)`), og
— berre på `LOGLVL=DEBUG` — éi samla `log_debug`-linje med kva som vart
hoppa over og kvifor. Dei 6 kallande makroane (`run_gen_parallel`,
`run_gen_owl_parallel`, `run_gen_rdf_parallel`, `run_gen_doc_parallel`,
`run_gen_erdiagram_parallel`, `run_gen_plantuml_parallel`) er forenkla —
den duplikate per-skjema flagg-sjekk-og-hopp-over-blokka er fjerna, flagget
vert no gitt som 4. argument til `run_parallel_with_timer`.
`run_gen_linkml_parallel` (ingen flagg) kallar med tomt 4. argument.

Verifisert med `make -n domain-fair` (dry-run, korrekt make-escaping) og
reell `make domain-fair`-køyring — ny logg:

```
→ merge-imports: fair/fair-metadata
→ merge-imports  fair/fair-metadata (8.6s)
→ gen-jsonld-context: (ingen skjema aktivert)
→ gen-shacl: fair/fair-metadata
→ gen-shacl  fair/fair-metadata (8.4s)
...
```

Skip-samandraget testa isolert (bash-simulering av filter-/logg-logikken
mot fleire ap-no-skjema): på `LOGLVL=DEBUG` vert
`[DEBUG]   hoppar over (jsonld_context ikkje sett): ap-no/common-ap-no,
ap-no/dcat-ap-no, ...` vist; på default `LOGLVL=INFO` er linja usynleg.

`run_gen_with_check_parallel` (openapi/asyncapi) og `run_gen_xsd` urørt som
planlagt — strukturelt ulike skip-vilkår (manglande input-fil).
