# build.yaml generator-flagg vert ignorerte i domain-<domain>-pipelinen

## Bakgrunn

Brukaren observerte at `make domain-ap-no` genererer `context.jsonld` for
alle ap-no-profilane, sjølv om kvart einaste `build.yaml` under
`src/linkml/ap-no/*/` har `jsonld_context: false`.

Undersøking synte at dette gjeld ni av dei generatorane som
`generators:`-blokka i `build.yaml` dokumenterer (jf. CONVENTIONS.md §
Manifestformat): `jsonld_context`, `shacl`, `python`, `json_schema`, `owl`,
`rdf`, `protobuf`, `docs`, `erdiagram`. Dei tilhøyrande makroane i
`make/10-generator-macros.mk` — `run_gen_parallel`, `run_gen_owl_parallel`,
`run_gen_rdf_parallel`, `run_gen_doc_parallel`, `run_gen_erdiagram_parallel`
— les aldri `build.yaml` før dei køyrer. Berre `plantuml`, `xsd`, `openapi`
og `asyncapi` har eit faktisk gate mot manifestet (`run_gen_plantuml_parallel`,
`run_gen_xsd`, `run_gen_with_check_parallel`).

Stikkprøve synte at alle 27 skjema-`build.yaml`-filer i repoet eksplisitt
set alle ni flagga (ingen manglar nøklar), og at ingen skjemakatalog manglar
`build.yaml` — så eit "skip dersom flagg ikkje er `true`"-gate er trygt utan
fallback-spesialtilfelle.

Desse fem makroane vert **berre** brukte frå `domain-<domain>`-pipelinen i
`make/20-domain-targets.mk`. Dei frittståande enkelt-skjema-debug-targeta
(`make gen-jsonld-context SCHEMA=...` osv. i `make/11-generator-targets.mk`)
brukar separate, serielle makroar (`run_gen`, `run_gen_shacl`, `run_gen_owl`,
`run_gen_rdf`, `run_gen_doc`, `run_gen_erdiagram`) og vert **ikkje** endra —
dei skal framleis kunne tvinge fram eit enkelt artefakt under feilsøking
uavhengig av `build.yaml`, slik `xsd`/`openapi`/`asyncapi` sine serielle
variantar alt er eit unntak frå (dei er gata i begge modus i dag).

## Steg

1. I `make/10-generator-macros.mk`:
   - Legg til eit `build.yaml`-gate (same mønster som
     `run_gen_plantuml_parallel`) i `run_gen_parallel`, med eit nytt 4.
     parameter for manifest-flaggnamnet.
   - Legg til tilsvarande gate i `run_gen_owl_parallel` (flagg `owl`),
     `run_gen_rdf_parallel` (flagg `rdf`), `run_gen_doc_parallel` (flagg
     `docs`) og `run_gen_erdiagram_parallel` (flagg `erdiagram`).
2. I `make/20-domain-targets.mk`: oppdater dei fem kalla til
   `run_gen_parallel` med rett flaggnamn (`jsonld_context`, `shacl`,
   `python`, `json_schema`, `protobuf`).
3. Køyr `make domain-ap-no` og stadfest at `gen-jsonld-context`,
   `gen-shacl`, `gen-python`, `gen-json-schema` faktisk vert hoppa over
   (debug-logglinje) for profilar med flagget sett til `false`, og at dei
   køyrer for profilar med `true` (t.d. `shacl: true` i `dcat-ap-no`).
4. Køyr `make domain-fint` (eller eit anna domene med fleire `true`-flagg,
   t.d. `python: true`, `protobuf: true`) og stadfest at artefakta framleis
   vert generert der flagget er `true`.
5. Diff `generated/`-treet mot `git status` for å stadfese at berre
   artefakt frå no-av-flagga generatorar forsvinn (ingen andre regresjonar).

## Handlingsliste

- [x] Steg 1 — gate i `10-generator-macros.mk`
- [x] Steg 2 — oppdater kallstader i `20-domain-targets.mk`
- [x] Steg 3 — verifiser ap-no
- [x] Steg 4 — verifiser eit domene med `true`-flagg
- [x] Steg 5 — diff generated/ for regresjonar

## Utført

- `make/10-generator-macros.mk`: la til `build.yaml`-gate (same mønster som
  `run_gen_plantuml_parallel`) i `run_gen_parallel` (nytt 4. parameter for
  manifest-flagg), `run_gen_owl_parallel` (`owl`), `run_gen_rdf_parallel`
  (`rdf`), `run_gen_doc_parallel` (`docs`) og `run_gen_erdiagram_parallel`
  (`erdiagram`)
- `make/20-domain-targets.mk`: oppdaterte dei fem `run_gen_parallel`-kalla
  med flaggnamn (`jsonld_context`, `shacl`, `python`, `json_schema`,
  `protobuf`)
- Verifisert med `make domain-ap-no LOGLVL=DEBUG`: `gen-jsonld-context`,
  `gen-python`, `gen-json-schema`, `gen-proto` hoppa over for alle
  ap-no-profilar (alle har flagget `false`); `gen-shacl`/`gen-owl`/`gen-rdf`
  hoppa over berre for `common-ap-no` (einaste med `false`) og køyrde for
  resten (`true`) — matchar kvart skjema sitt `build.yaml` nøyaktig
- Verifisert med `make domain-fint LOGLVL=DEBUG` (alle ni flagg `true`):
  ingen av dei ni generatorane vart hoppa over, 0 uventa feil
- Ingen skjema manglar `build.yaml` eller nøklar i `generators:`-blokka
  (stikkprøve mot alle 27 skjema-manifest), så "skip dersom flagg ikkje er
  `true`"-fallback vert aldri utløyst utilsikta
- Standalone enkelt-skjema-targeta (`make gen-jsonld-context SCHEMA=...` osv.
  i `make/11-generator-targets.mk`) er urørte — dei brukar framleis dei
  serielle, ugata makroane for feilsøkingsbruk
