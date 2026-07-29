# Plan for modularisering av Makefile

## Føremål

Målet er å dele dagens store Makefile opp i mindre, tematisk avgrensa `.mk`-filer som er enklare å lese, enklare å teste og enklare å endre utan å øydelegge andre delar av byggeløpet.

Planen byggjer på tre prinsipp:

1. DRY: felles mønster skal definerast éin stad og brukast fleire stader.
2. Lesbarheit: ein utviklar skal raskt kunne finne ut kvar eit target er definert, kva det gjer, og kva wrapper/container det brukar.
3. Låg risiko: modulariseringa bør kunne gjerast stegvis utan å endre funksjonell oppførsel i første omgang.

---

## Kort vurdering av dagens Makefile

Dagens Makefile fungerer, men har fleire teikn på at han er moden for modularisering:

- Han blandar konfigurasjon, container-wrapperar, generator-makroar, domenetarget, validering, dokumentasjonsbygg, MCP-target og Gource-target i éi fil.
- Fleire target gjentek same struktur: header, separator, skjemaliste, loop, timing, mkdir og containerkall.
- `domain_target` og `domain-begrepskatalog` har mykje nesten identisk innhald.
- Nokre Python-kall går via container, medan andre går direkte på hosten.
- Inline Python i Makefile gjer quoting og lesbarheit vanskelegare.
- Generert `config.mk` blir inkludert, men resten av Makefile-en er ikkje strukturert som eit modulsystem.

GNU Make støttar dette godt: `include` kan lese andre makefile-fragment inn i hovudfila, og `eval`/`call` kan brukast til å generere like target frå malar. Sjå referansar bakerst.

---

## Foreslått katalogstruktur

Anbefalt ny struktur:

- `Makefile`
  - Tynn inngangsfil med `include` av modulane i rett rekkefølgje.
- `mk/00-settings.mk`
  - Shell-flagg, standardvariablar, fargar, katalogar og image-namn.
- `mk/01-containers.mk`
  - Alle Podman-wrapperar: `LINKML_RUN`, `PYTHON_RUN`, `DOCS_RUN`, `MCP_RUN`, osv.
- `mk/02-schema-discovery.mk`
  - `SCHEMAS`, `DOMAINS`, `schema_domain`, `schema_name`, `schema_outdir`, `schema_key`, `get_target_schemas`.
- `mk/03-output.mk`
  - Felles header-/logging-makroar.
- `mk/10-generator-macros.mk`
  - `run_gen`, `run_parallel_with_timer`, `run_gen_parallel`, `run_gen_doc_parallel`, `run_gen_erdiagram_parallel`, osv.
- `mk/11-generator-targets.mk`
  - Dei genererte `gen-*`-targeta basert på `make_gen_target`.
- `mk/20-domain-targets.mk`
  - Generering av `domain-*`-target og spesialtilfelle for `begrepskatalog`.
- `mk/30-instances.mk`
  - `gen-begrepskatalog-instance`, `gen-modellkatalog-instance`, `gen-informasjonsmodell-instance`, validering av instansar.
- `mk/40-validation.mk`
  - `validate`, `lint`, `validate-bronze`, `validate-data`, `validate-examples`, `validate-capture`, `log-*`.
- `mk/50-docs.mk`
  - `docs-publish`, `docs-build`, `docs-serve`, MkDocs-image.
- `mk/60-mcp.mk`
  - MCP-validator, modellutkast, begrepsutkast og relaterte target.
- `mk/70-scaffolding.mk`
  - `new-model`, `new-modellkatalog`, `new-begrepssamling`, `update-valid-scopes`.
- `mk/80-images.mk`
  - Alle `build-docker-*` target.
- `mk/90-tools.mk`
  - Gource og andre verktøy-target.
- `config.mk`
  - Framleis generert, men inkludert etter schema discovery og før target som treng konfigurasjonsvariablar.

Denne strukturen gjer at ein menneskeleg lesar først møter overordna oppsett, deretter fellesfunksjonar, deretter konkrete target per tema.

---

## Ny hovud-Makefile

Hovudfila bør bli svært kort og berre forklare lastrekkefølgja.

Foreslått innhald, konseptuelt:

- Definer `SHELL` og `.SHELLFLAGS` heilt øvst, slik at alle inkluderte filer får same shell-oppførsel.
- Inkluder `mk/00-settings.mk`.
- Inkluder `mk/01-containers.mk`.
- Inkluder `mk/02-schema-discovery.mk`.
- Inkluder `config.mk` med `-include config.mk`.
- Inkluder output/logging.
- Inkluder makroar.
- Inkluder tematiske target-filer.
- Ha eit `help`-target som standard første target.

Viktig: dersom de vil behalde eksisterande standardtarget, må `help` ikkje automatisk bli første target utan at det er tilsikta.

---

## Modul 1: settings

`mk/00-settings.mk` bør innehalde berre statiske og overordna variablar:

- `GEN_DIR`
- `SCHEMA_DIR`
- `MCP_DIR`
- `PARALLEL`
- `SEP`
- fargevariablar
- image-namn og Dockerfile-stiar, dersom de ikkje vil samle akkurat image-info i containerfila

Anbefaling:

- Bruk `?=` for verdiar som utviklar eller CI skal kunne overstyre.
- Bruk `:=` for avleidde verdiar som ikkje bør evaluerast på nytt kvar gong.
- Unngå shell-kall i variablar så langt det er mogleg.

---

## Modul 2: containers

`mk/01-containers.mk` bør definere alle container-wrapperar samla.

Hovudmål:

- Éin tydeleg stad for containerstrategi.
- Alle Python-kall skal gå via `PYTHON_RUN` eller `LINKML_RUN`.
- Alle wrapperar bør bruke same volum- og arbeidskatalogkonvensjon når mogleg.

Anbefalt konvensjon:

- Repoet mountast som `/work`.
- Containeren køyrer med `-w /work`.
- Script kallast med `/work/...` for å gjere skiljet mellom host og container tydeleg.
- Read-only mount kan brukast for target som berre les, men ikkje bland read-only og write-target utan tydeleg grunn.

Lag gjerne hjelpevariablar:

- `WORK_MOUNT := -v "$(CURDIR):/work" -w /work`
- `WORK_MOUNT_RO := -v "$(CURDIR):/work:ro" -w /work`

Då blir wrapperane kortare og meir konsistente.

---

## Modul 3: schema discovery

`mk/02-schema-discovery.mk` bør samle automatisk oppdaging av schema og domenar:

- `SCHEMAS`
- `DOMAINS`
- `schema_domain`
- `schema_name`
- `schema_outdir`
- `schema_key`
- `get_target_schemas`

Dette er kjernen i Makefile-en og bør kommenterast godt.

Anbefaling:

- Forklar mappestrukturen eksplisitt: `src/linkml/<domain>/<model>/<model>-schema.yaml`.
- Forklar kvifor `schema_name` hentar katalognamn og ikkje nødvendigvis filprefix.
- Legg inn eit diagnostisk target som kan vere nyttig for menneske, til dømes `print-schema-discovery`, som skriv ut `DOMAINS` og talet på schema.

---

## Modul 4: logging og lesbar output

Dagens Makefile gjentek mykje header-logikk.

Lag fellesmakroar i `mk/03-output.mk`:

- `print_header`
- `print_step`
- `print_warning`
- `print_error`
- `time_step` dersom de ønskjer felles timing.

Mål:

- Alle target får lik loggstruktur.
- Nye target blir enklare å skrive.
- Mindre støy i target-definisjonane.

Eksempel på ønskja bruk i target:

- `$(call print_header,gen-jsonschema)`
- `$(call print_step,gen-jsonschema,$$schema)`

---

## Modul 5: generator-makroar

`mk/10-generator-macros.mk` bør vere den største tekniske modulen, men berre innehalde generiske byggemønster.

Flytt hit:

- `run_gen`
- `run_parallel_with_timer`
- `run_gen_parallel`
- `run_gen_linkml_serial`
- `run_gen_linkml_parallel`
- `run_gen_owl_parallel`
- `run_gen_rdf_parallel`
- `run_gen_doc_parallel`
- `run_gen_erdiagram_parallel`
- `run_gen_plantuml_parallel`
- `run_gen_openapi_parallel`
- `run_gen_asyncapi_parallel`
- serialvariantane som framleis trengst

DRY-forbetringar:

1. Samle felles parallell-loop i éin makro.
2. La kvar generator berre definere kommando-snippetet.
3. Flytt manifest-sjekk for OpenAPI/AsyncAPI/XSD til ein felles shell-funksjon eller make-makro.
4. Standardiser output-paths med `schema_outdir` og `schema_name`.

Anbefalt refaktorering:

- Lag eitt felles mønster for generatorar som tek `schema -> output-file`.
- Lag eitt felles mønster for generatorar som berre skal køyre dersom `build.yaml` har ein flaggverdi, som `openapi: true`, `asyncapi: true` eller `xsd: true`.
- Lag eitt felles mønster for generatorar som treng postprosessering.

---

## Modul 6: generator-target

`mk/11-generator-targets.mk` bør innehalde `make_gen_target` og alle `$(eval $(call make_gen_target,...))`-linjene.

Mål:

- Det skal vere enkelt å sjå kva `gen-*`-target som finst.
- Ein ny generator bør kunne leggast til med éi linje, dersom han følgjer standardmønsteret.

Anbefaling:

- Del enkle generatorar og spesialgeneratorar med kommentaroverskrifter.
- Bruk same namnestandard: `gen-jsonschema`, `gen-openapi`, `gen-docs`, osv.
- Vurder å samle generator metadata i variablar, til dømes `GEN_JSONSCHEMA_COMMAND`, `GEN_JSONSCHEMA_SUFFIX`, men berre dersom det faktisk gjer fila meir lesbar.

---

## Modul 7: domain-targets

Dette er den største DRY-gevinsten.

I dag er `domain_target` og `domain-begrepskatalog` nesten like, men `begrepskatalog` har eit førehandssteg: `gen-begrepskatalog-instance`.

Anbefalt ny modell:

- Behald éin generell `domain_target`-mal.
- Innfør ein variabel for pre-target per domene.
- Definer `DOMAIN_PRE_begrepskatalog := gen-begrepskatalog-instance`.
- La `domain_target` bruke `$(DOMAIN_PRE_$(1))` som prerequisite eller første steg.

Då treng de ikkje ein full eksplisitt override for `domain-begrepskatalog`.

Prinsippet:

- `domain-ap-no` og `domain-fair` får tom pre-step.
- `domain-begrepskatalog` får `gen-begrepskatalog-instance`.
- Dersom eit nytt domene treng spesialsteg seinare, legg de berre inn `DOMAIN_PRE_<domain>`.

Dette vil fjerne mykje duplisering og gjere begrepskatalog-unntaket synleg på éin stad.

---

## Modul 8: instances

`mk/30-instances.mk` bør samle target som genererer eller validerer instansdata:

- `gen-begrepskatalog-instance`
- `gen-modellkatalog-instance`
- `gen-informasjonsmodell-instance`
- `run_gen_informasjonsmodell_instance`
- `validate-informasjonsmodell-instance`
- `validate-modellkatalog-instance`

Anbefalt opprydding:

- Containeriser direkte Python-kall.
- Flytt `collect-concepts.py` frå `.github/scripts` til `src/assets/scripts/makefile`.
- Bruk same logging-makroar som resten av Makefile.
- Gjer det tydeleg kva target som skriv til `src/linkml/...` og kva target som berre skriv til `generated/...`.

---

## Modul 9: validation

`mk/40-validation.mk` bør samle validering:

- `validate`
- `lint`
- `validate-instance`
- `validate-bronze`
- `validate-data`
- `validate-examples`
- `validate-capture`
- `mcp-linkml-validate`
- `log-mcp-validate`
- `log-validate-instance`

DRY-forbetringar:

- Lag éin felles makro for `DOMAIN`-påkravd target.
- Lag éin felles makro for å iterere schema i eit domene.
- Flytt inline Python til små script.
- Standardiser korleis valideringslogg blir lagra.

Menneskeleg lesbarheit:

- Del validering i tre seksjonar: LinkML-validering, MCP-validering, logging/capture.
- Forklar skilnaden mellom `validate-*` og `log-*`.

---

## Modul 10: docs

`mk/50-docs.mk` bør samle dokumentasjonsbygg:

- `build-docker-mkdocs`, dersom image-target ikkje blir samla i `mk/80-images.mk`
- `docs-serve`
- `docs-build`
- `docs-publish`

Vurdering:

- `DOCS_RUN` er litt annleis enn dei andre container-wrapperane fordi han mountar delkatalogar individuelt.
- Dette bør forklarast i `mk/01-containers.mk` eller i `mk/50-docs.mk`.

Anbefaling:

- Hald docs-target enkle.
- Flytt eventuell tabellgenerering og publish-logikk ut i script dersom det veks.

---

## Modul 11: MCP

`mk/60-mcp.mk` bør samle alt som har med MCP-serverane å gjere:

- MCP validator
- modellutkast
- begrepsutkast
- smoke-testar
- pytest-target
- request/response-generering

DRY-forbetringar:

- Lag felles mønster for `build`, `run`, `smoke`, `test` der det gir meining.
- Flytt inline Python til script.
- Gjer det tydeleg kva target som krev image frå før, og kva target som byggjer image automatisk.

---

## Modul 12: image-bygging

`mk/80-images.mk` bør samle alle `build-docker-*` target:

- `build-docker-linkml`
- `build-docker-python`
- `build-docker-avrotize`
- `build-docker-asyncapi`
- `build-docker-mkdocs`
- `build-docker-plantuml`
- `build-docker-mcp-validator`
- `build-docker-mcp-modell-utkast`
- `build-docker-mcp-begrep-utkast`
- `build-docker-gource`

DRY-forbetring:

- Lag ein generell `build_image_target`-mal som tek targetnamn, Dockerfile, image og context.
- Vurder dette berre dersom det faktisk blir meir lesbart. For få image kan eksplisitte target vere betre.

---

## Korleis redusere duplisering i domain-generering

Dette er den viktigaste konkrete refaktoreringa.

### Problem i dag

`domain-begrepskatalog` er ein nesten komplett kopi av generelt `domain_target`, berre med `gen-begrepskatalog-instance` først.

### Foreslått løysing

Bruk domenespesifikke hooks:

- `DOMAIN_PRE_<domain>`: target eller kommandoar som skal køyrast før standard generering.
- `DOMAIN_POST_<domain>`: target eller kommandoar som skal køyrast etter standard generering.
- `DOMAIN_SKIP_<domain>` eller manifest-styring dersom eit domene skal hoppe over visse steg.

For begrepskatalog:

- `DOMAIN_PRE_begrepskatalog := gen-begrepskatalog-instance`

Då kan same `domain_target`-mal brukast for alle domene.

### Gevinst

- Mindre risiko for at genereringsrekkefølgja blir ulik mellom domene.
- Nye genereringssteg treng berre leggjast til éin stad.
- Spesialtilfelle blir synlege som data, ikkje som kopiert kode.

---

## Korleis gjere Makefile-en lettare å forstå for menneske

### 1. Legg inn eit `help`-target

Eit godt `help`-target bør gruppere target slik:

- Vanleg bruk
- Generering
- Validering
- Dokumentasjon
- Docker/Podman images
- MCP
- Vedlikehald

Det bør vise korte forklaringar, ikkje intern implementasjon.

### 2. Bruk konsekvent namnsetjing

Anbefalt mønster:

- `gen-*` for å generere artefaktar
- `validate-*` for å validere utan nødvendigvis å skrive varig logg
- `log-*` for validering med persistent logg
- `build-docker-*` for image-bygging
- `domain-*` for full generering av domene
- `mcp-*` for MCP-relaterte target

### 3. Skil mellom offentlege og interne target

Interne target kan få prefiks `_`, til dømes:

- `_gource-render`
- `_print-domain-plan`
- `_check-domain`

Dokumenter at desse ikkje er meint for direkte bruk.

### 4. Kommenter kvifor, ikkje berre kva

Døme:

- Kvifor `begrepskatalog` har pre-step.
- Kvifor `DOCS_RUN` mountar delkatalogar i staden for heile repoet.
- Kvifor enkelte script må bruke `LINKML_RUN` i staden for `PYTHON_RUN`.

### 5. Bruk korte seksjonskommentarar i kvar modul

Kvar `.mk`-fil bør starte med:

- Føremål
- Kva variablar han definerer
- Kva target han eksponerer
- Kva filer han er avhengig av

---

## Stegvis migreringsplan

### Fase 0: Sikre noverande oppførsel

Før refaktorering:

1. Køyr eksisterande CI på main og noter grøne target.
2. Lag ein enkel lokal røyk-test for sentrale target: `make gen-config`, eitt `domain-*`, `docs-build`, eitt valideringstarget.
3. Lagre output frå `make -pn` eller i det minste `make -n domain-begrepskatalog` før endring, slik at de kan samanlikne kommandostruktur.

Målet er å kunne sjå at refaktoreringa ikkje endrar semantikk utilsikta.

### Fase 1: Flytt reine variablar

1. Opprett `mk/00-settings.mk`.
2. Flytt statiske variablar dit.
3. Opprett `mk/01-containers.mk`.
4. Flytt container-wrapperar dit.
5. La resten av Makefile-en stå uendra.

Risiko: låg.

### Fase 2: Flytt schema discovery og config-include

1. Opprett `mk/02-schema-discovery.mk`.
2. Flytt `SCHEMAS`, `DOMAINS` og schema-funksjonar dit.
3. Behald `-include config.mk` i hovud-Makefile rett etter schema discovery.

Risiko: låg til middels.

### Fase 3: Flytt generator-makroar

1. Opprett `mk/10-generator-macros.mk`.
2. Flytt alle `define run_*`-makroar dit.
3. Køyr `make -n` på fleire target for å kontrollere at ekspansjonane er like.

Risiko: middels, på grunn av escaping i `define`, `foreach`, `xargs` og shell-variablar.

### Fase 4: Flytt generator-target

1. Opprett `mk/11-generator-targets.mk`.
2. Flytt `make_gen_target` og `$(eval ...)`-linjene.
3. Test enkle generatorar først før domain-target.

Risiko: middels.

### Fase 5: Fjern duplisering i domain-targets

1. Opprett `mk/20-domain-targets.mk`.
2. Flytt `domain_target` dit.
3. Innfør domenespesifikke pre-hooks.
4. Fjern manuell override av `domain-begrepskatalog`.
5. Test `make -n domain-begrepskatalog` og samanlikn med tidlegare output.

Risiko: høgaste fasen, fordi dette påverkar hovudflyten i CI.

### Fase 6: Flytt tematiske target

Flytt i denne rekkjefølgja:

1. Instans-target til `mk/30-instances.mk`.
2. Validering til `mk/40-validation.mk`.
3. Docs til `mk/50-docs.mk`.
4. MCP til `mk/60-mcp.mk`.
5. Scaffolding til `mk/70-scaffolding.mk`.
6. Image-bygging til `mk/80-images.mk`.
7. Gource/verktøy til `mk/90-tools.mk`.

Risiko: låg til middels når makroar og variablar allereie er flytta.

### Fase 7: Containeriser Python og rydd inline-kode

Dette kan gjerast parallelt med eller etter modularisering, men bør helst skje etter at modulstrukturen er på plass.

1. Endre host-Python-kall til `$(PYTHON_RUN)` eller `$(LINKML_RUN)`.
2. Flytt inline `python3 -c` til små script.
3. Legg script under `src/assets/scripts/makefile/`.
4. Fjern byggelogikk frå `.github/scripts`.

Risiko: middels.

---

## Akseptansekriterium

Modulariseringa bør reknast som vellukka når desse punkta er oppfylt:

1. `Makefile` er kort og fungerer som inngangsfil.
2. Alle tematiske delar ligg i `mk/*.mk`.
3. `domain-begrepskatalog` er ikkje lenger ein kopi av standard domain-target.
4. Nye generatorar kan leggjast til utan å kopiere store blokker.
5. Alle direkte Python-kall er anten containeriserte eller eksplisitt dokumenterte som bevisst host-kall.
6. `make -n domain-begrepskatalog` gir forventa rekkefølgje.
7. CI køyrer grønt for minst eitt fullstendig bygg av alle domene.
8. `help`-target gir ein ny utviklar oversikt over vanlege kommandoar.
9. Kvar `.mk`-fil har kort toppkommentar med føremål.

---

## Risikoar og tiltak

### Risiko: Make-escaping blir øydelagt ved flytting

Tiltak:

- Flytt éin makro om gongen.
- Bruk `make -n` for å samanlikne før og etter.
- Ver ekstra merksam på `$$`, `$$$$`, `$(eval ...)` og `define`.

### Risiko: include-rekkefølgje blir feil

Tiltak:

- Hald hovud-Makefile eksplisitt og kommentert.
- Plasser variablar før makroar, og makroar før target som brukar dei.
- Bruk `make --warn-undefined-variables` i ein eigen test dersom støyen er handterbar.

### Risiko: For mykje abstraksjon

Tiltak:

- Ikkje lag generiske makroar berre for å redusere linjetal.
- Dersom ein eksplisitt target er lettare å lese enn ein avansert makro, vel eksplisitt target.
- DRY skal støtte forståing, ikkje skjule logikk.

### Risiko: Domain-hooks gjer flyten usynleg

Tiltak:

- Ha eit `print-domain-plan`-target som viser kva steg eit domene vil køyre.
- Dokumenter `DOMAIN_PRE_*` og `DOMAIN_POST_*` tydeleg.

---

## Foreslått prioritering

### Første PR: trygg struktur

- Opprett `mk/`.
- Flytt settings, containers og schema discovery.
- Behald target-definisjonar mest mogleg uendra.

### Andre PR: generatorar

- Flytt generator-makroar og generator-target.
- Ingen funksjonelle endringar.

### Tredje PR: domain-target DRY

- Innfør pre-hooks.
- Fjern duplisert `domain-begrepskatalog`.
- Test grundig i CI.

### Fjerde PR: tematisk opprydding

- Flytt validation, docs, MCP, images og tools.
- Legg til `help`.

### Femte PR: Python/container-opprydding

- Gjer direkte Python-kall containeriserte.
- Flytt inline Python til script.
- Flytt `collect-concepts.py` ut av `.github/scripts`.

---

## Anbefalt sluttbilete

Ein utviklar som opnar repoet bør kunne forstå byggesystemet slik:

1. `Makefile` viser kva modular som finst.
2. `mk/00-settings.mk` og `mk/01-containers.mk` forklarer miljøet.
3. `mk/02-schema-discovery.mk` forklarer korleis schema blir funne.
4. `mk/10-generator-macros.mk` forklarer genereringsmønsteret.
5. `mk/20-domain-targets.mk` viser rekkefølgja for domain-bygg.
6. Tematiske filer viser konkrete target for validering, docs, MCP og verktøy.

Dette gir lågare kognitiv last, mindre duplisering og mindre risiko for at endringar i eitt domene eller eitt target må kopierast manuelt fleire stader.

---

## Referansar

- GNU Make-dokumentasjonen skildrar `include` som mekanismen for å lese andre makefile-fragment inn i ei hovudfil. Dette er grunnlaget for å dele Makefile-en i tematiske `.mk`-filer. Kjelda omtalar også at `include` ofte blir brukt når fleire makefiler skal dele felles variabeldefinisjonar eller reglar: https://www.gnu.org/software/make/manual/html_node/Include.html
- GNU Make-dokumentasjonen skildrar `eval` som ein måte å definere makefile-konstruksjonar dynamisk på, til dømes target og reglar frå malar. Dokumentasjonen påpeikar også at uttrykket blir ekspandert to gonger, noko som forklarer behovet for forsiktig escaping med `$`: https://www.gnu.org/software/make/manual/html_node/Eval-Function.html

