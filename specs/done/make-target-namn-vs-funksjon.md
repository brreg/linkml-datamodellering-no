# Gjennomgang — make-target-namn vs. faktisk funksjonalitet

## Bakgrunn

Brukaren bad om ein full gjennomgang av alle make-target i `Makefile` og
`make/*.mk`, der namnet på kvart target vert samanlikna med kva oppskrifta
faktisk utfører. Der namnet ikkje er 100 % dekkande, skal eit forslag til
nytt namn dokumenterast.

Dette er ei anna vinkling enn den tidlegare, arkiverte
`specs/done/make-kommando-inkonsistens-audit.md` — den auditen såg primært
på *innbyrdes konsistens* mellom søsken-target (verb/substantiv-mønster,
norsk/engelsk, suffiks-sett) og på strukturelle bugs (stale script-stiar,
daud kode). Denne gjennomgangen vurderer i staden kvart einskilt target
isolert: **beskriv namnet presist kva oppskrifta gjer, uavhengig av kva
andre target heiter?** Fire av funna frå den tidlegare auditen
(`new-model` → `new-modell`, `mcp-linkml-validate` → `mcp-linkml-valider-modell`,
m.fl.) er alt gjennomførte og reflekterte i dagens kode.

Dette er ein *dokumenterande* gjennomgang — ingen endringar er utførte.
Kvart namngjevingsfunn har eit konkret forslag som kan takast som eit eige
tiltak seinare, etter brukargodkjenning.

## Metode

- Las heile `Makefile` og alle 16 filene i `make/*.mk` (00-settings →
  91-modell-analyse) i sin heilheit — 1555 linjer totalt.
- For kvart av dei 84 targeta: samanlikna `## `-hjelpeteksten (kjelda for
  `make help`) og namnet mot den faktiske oppskrifta/makroen/scriptet som
  vert kalla.
- Kryssjekka overlappande/like-lydande target-par (t.d. `convert-rdf` vs.
  `gen-linkml-convert`, `update-modellkatalog` vs. `gen-modellkatalog-instance`)
  ved å lese dei underliggande Python-scripta sine docstringar.
- Verifiserte éin mistanke om eit heilt manglande target med `make -n
  check-published-uris` og `git log -S` mot `Makefile`/`make/`.
- Las `specs/done/make-kommando-inkonsistens-audit.md` og
  `specs/done/commands-md-manglande-make-targets.md` for å unngå å gjenta
  funn som alt er handterte, og for å finne historisk kontekst på funn 1
  under.

## Funn

### Funn 1 (kritisk, ikkje eit namngjevingsfunn) — `check-published-uris` finst ikkje som target

`check-published-uris` er:
- lista i `.PHONY` (`Makefile:82`)
- kalla direkte frå CI (`.github/workflows/validate.yml:260`, steget «Sjekk
  at publiserte URI-ar ikkje er fjerna»)
- dokumentert i `COMMANDS.md`, `mkdocs/docs/publisering/publisering-modell.md`
  og `mkdocs/docs/publisering/publisering-begrep.md`
- stadfesta å ha eksistert i `specs/done/commands-md-manglande-make-targets.md`
  (2026-06-19, då han vart lagt til i `COMMANDS.md`-dokumentasjonen)

men det finst **ingen `check-published-uris:`-oppskrift** nokon stad i
`Makefile` eller `make/*.mk`. `make -n check-published-uris` stadfestar:

```
make: Nothing to be done for 'check-published-uris'.
```

Sidan targetet er `.PHONY` utan oppskrift, gjer `make check-published-uris`
**ingenting og returnerer exit code 0**. CI-steget «Sjekk at publiserte
URI-ar ikkje er fjerna» i `validate.yml` køyrer difor alltid «vellykka» utan
å faktisk sjekke noko — den dokumenterte tryggleiksmekanismen
(«Feiler viss ei URI i lock-fila manglar frå katalogfila») er ikkje aktiv i
dag. `git log -S "check-published-uris:"` viser at oppskrifta forsvann i
ein av dei tre `refactor(make): konsolider gen-* targets med DOMAIN/SCHEMA
support`-commitane, truleg ved eit uhell.

Dette bryt CLAUDE.md sitt prinsipp «Ingen stille feil» direkte — dette er
ikkje eit namngjevingsspørsmål, men bør rettast som eiga, prioritert sak
(gjenopprett oppskrifta, eller fjern alle referansar dersom sjekken ikkje
lenger trengst). Teke med her fordi han vart oppdaga undervegs i denne
gjennomgangen.

### Funn 2 — `convert-rdf` og `gen-linkml-convert` slåast saman til éin `convert-instance-rdf`

Kombinerer to tidlegare separate funn (namneoverlapp med `gen-rdf`, og
funksjonsduplikat med `gen-linkml-convert`) — same underliggande problem,
éi løysing.

- **`convert-rdf`** (`Makefile:120`) og **`gen-linkml-convert`**
  (`make/20-domain-targets.mk:19`) kallar begge det same underliggande
  scriptet, `convert-examples.sh` (kommentert eksplisitt i scriptet: «Delt
  av `make convert-rdf` ... og `domain_target` ... via $1»), etterfølgt av
  `batch-generate-instances.py --generator convert`. Begge konverterer
  eksempelfiler (`examples/*-eksempel.yaml`) til RDF/Turtle.
- Einaste funksjonelle skilnaden er at `convert-rdf` køyrer over alle
  skjema (ingen DOMAIN-filtrering vert sendt til scriptet), medan
  `gen-linkml-convert` er domene-avgrensa (brukt internt av
  `domain-<domain>`-pipelinen). `convert-examples.sh` støttar alt eit
  valfritt domene-argument — filtreringa manglar berre i `convert-rdf`
  sitt eige kall.
- Namnet `gen-linkml-convert` signaliserer feilaktig at targetet høyrer
  til «gen-linkml-*»/generator-familien (`gen-jsonschema`, `gen-owl`,
  `gen-rdf` osv.), men det er i realiteten domene-varianten av
  `convert-rdf` — same verb (`convert`), ikkje `gen`.
- `convert-rdf` sitt eige namn skil seg heller ikkje tydeleg frå `gen-rdf`
  (`make/11-generator-targets.mk:35`), som serialiserer **sjølve skjemaet**
  til RDF/Turtle (`## Generer RDF/Turtle-skjemaserialisering`) — eit heilt
  anna artefakt frå ei heilt anna kjelde enn `convert-rdf`, som konverterer
  **eksempelinstansar**. Sidan `convert-data` (som konverterer
  `data/*/*.yaml`) alt følgjer mønsteret `convert-<kjelde>`, bør
  `convert-rdf` namngjevast etter kjelda (instansdata), ikkje målformatet
  (rdf), for å gjere skiljet mot `gen-rdf` eksplisitt.

**Vedtak:** `convert-rdf` vert omdøypt til **`convert-instance-rdf`**, med
eit valfritt `DOMAIN=<domene>`-argument lagt til (same mønster som dei
fleste andre `gen-*`/`convert-*`-target, absorberer domene-filtreringa
`gen-linkml-convert` i dag gjer). `gen-linkml-convert` fjernast heilt
(target, `.PHONY`-oppføring), og `domain_target`-pipelinen
(`make/20-domain-targets.mk`) sitt kall vert endra til å kalle
`$(MAKE) convert-instance-rdf DOMAIN=$(1)` i staden.

### Funn 3 — `gen-linkml-merge` er reint ei validering, ikkje ein generator

`gen-linkml-merge` (`make/11-generator-targets.mk:29`) sin eigen
hjelpetekst seier det rett ut: **«Valider skjema (gen-linkml, fail-fast,
ingen fil skriven)»**. Han kallar `run_gen_linkml_parallel`
(`make/10-generator-macros.mk:44`) — den nøyaktig same makroen som
`validate`-targetet (`make/40-validation.mk:24`) kallar direkte. Ein
brukar som køyrer `make gen-linkml-merge` og forventar eit generert
artefakt (slik alle andre `gen-*`-target produserer) vil ikkje finne noko —
sidan han berre validerer merge-imports og diskarderer output.

**Forslag:** `gen-linkml-merge` → `validate-linkml-merge` (droppar
`gen-`-prefikset som lovar eit artefakt han ikkje produserer, og signaliserer
i staden at han er ein valideringsvariant av `validate`, berre med
DOMAIN/SCHEMA-støtte frå `make_gen_target`-malen).

### Funn 4 — `gen-docs` kolliderer namnemessig med `docs-serve`/`docs-build`/`docs-publish`

`gen-docs` (`make/11-generator-targets.mk:73`) genererer per-skjema
klassereferanse-Markdown og ER-diagram til `generated/<domain>/<schema>/`
— eitt steg i den store `gen-*`-familien. `docs-serve`, `docs-build` og
`docs-publish` (`make/50-docs.mk`) opererer derimot på eit heilt anna nivå:
sjølve **mkdocs-portalen** (statisk nettstad bygd av `generated/`-innhaldet,
inkludert det `gen-docs` produserte). Dei fire namna
(`gen-docs`/`docs-serve`/`docs-build`/`docs-publish`) deler alle
`docs`-stammen, men høyrer til to heilt ulike steg i pipelinen
(skjemadokumentasjon vs. portalpublisering), og rekkjefølgja dei må
køyrast i (`gen-docs` før `docs-publish` kan ha noko å kopiere) er ikkje
synleg av namna åleine. Ein brukar kan lett tru `gen-docs` genererer
portalen, eller at `docs-build` genererer skjemadokumentasjonen.

**Forslag:** `gen-docs` → `gen-schema-docs` (skil han visuelt frå
`docs-*`-portalfamilien og presiserer kva han faktisk dokumenterer).

### Funn 5 — `update-modellkatalog` fjernast (avløyst av `gen-modellkatalog-instance`)

`update-modellkatalog` (`Makefile:146`) og `gen-modellkatalog-instance`
(`make/30-instances.mk:47`) opererer begge på per-org
modellkatalog-datafiler, men gjer heilt ulike ting:

- `update-modellkatalog.py` **patchar** eit avgrensa sett felt
  (`utgiver`, `endringsdato`, `utgivelsesdato`, `status`, `versjonsnummer`)
  i **eksisterande** katalogoppføringar, og let resten (`tittel`,
  `beskrivelse`, `tema`, `lisens`, `kontaktpunkt` m.m.) stå urørt.
- `generate-modellkatalog.py` (bak `gen-modellkatalog-instance`)
  **regenererer heile katalogfila frå botnen** ut frå alle
  Informasjonsmodell-instansar. Docstringen i scriptet seier det
  eksplisitt: *«Dette scriptet erstatter update-modellkatalog.py ved å
  generere komplette katalogfiler i staden for berre oppdatere
  eksisterande felt.»*

Namnet `update-modellkatalog` gav ingen indikasjon på at scriptet bak det
sjølv hevda å vere avløyst av eit anna, nyare target — to target med
overlappande domene («modellkatalog») og usynleg forrang-rekkjefølgje
mellom dei.

**Vedtak:** `update-modellkatalog` fjernast heilt: target i `Makefile`,
`.PHONY`-oppføringa, scriptet
`src/assets/scripts/makefile/update-modellkatalog.py`, og alle referansar
i `COMMANDS.md`/dokumentasjon/scaffolding-script.
`gen-modellkatalog-instance` dekkjer behovet fullt ut.

### Funn 6 — `gen-erdiagram` deler namn med portalens PlantUML-baserte «ER-diagram»-seksjon

**Opphavleg vurdering (forkasta):** Vurdert som ikkje eit namngjevingsfunn,
sidan targetnamnet er presist for sin eigen operasjon (genererer eit
Mermaid-basert ER-diagram, `erdiagram.md`).

**Ny vurdering:** Terminologikollisjonen er reell, og kjelda til henne er
nettopp make-target-namnet, ikkje berre dokumentasjonen. Heile systemet
brukar «ER-diagram» for to ulike artefakt: Mermaid-fila frå `gen-erdiagram`
(lista direkte i artefakttabellen som `erdiagram.md`), og PlantUML-SVG-en
frå `gen-plantuml` (vist under portalseksjonen «## ER-diagram» i genererte
`index.md`-sider, jf. CLAUDE.md). Ein brukar som ser «## ER-diagram» i
portalen og leitar etter kva make-target som produserte han, vil naturleg
gjette `gen-erdiagram` — og få feil svar, sidan det faktisk er
`gen-plantuml`.

**Alternativ:** Omdøyp `gen-erdiagram` → `gen-erdiagram-mermaid`. Gjer
forma eksplisitt i namnet, fjernar tvitydigheita mot portalseksjonen, og
krev ingen endring i `gen-plantuml` eller sjølve seksjonstittelen.

### Funn 7 — `log-mcp-validate`/`log-validate-instance` bryt det dominerande `validate-*`-mønsteret

**Opphavleg vurdering (forkasta):** Grammatisk mønsterbrot alt vurdert og
medvite ikkje endra i `specs/done/make-kommando-inkonsistens-audit.md`
(namnekonsistens 4) — men den auditen vurderte *konsolidering* av
funksjonalitet, ikkje eit reint namnebyte.

**Ny vurdering:** Denne spec-en (Funn 3) stadfestar at `validate-*` er det
klart dominerande mønsteret i make-laget (`validate-instance`,
`validate-data`, `validate-examples`, `validate-bronze`,
`validate-linkml-merge` etter Funn 3). `log-mcp-validate` og
`log-validate-instance` er dei einaste to av 84 target som startar med eit
anna ord enn sjølve handlingsverbet — dei gøymer seg bak «log-» og dukkar
difor ikkje opp ved tab-fullføring av `validate-` eller ved skumlesing av
den `validate-*`-gruppa i `make help`.

**Alternativ:** Omdøyp `log-mcp-validate` → `validate-policy-logg` og
`log-validate-instance` → `validate-instance-logg`. Held `validate-`-
prefikset konsekvent og flyttar logg-eigenskapen til eit suffiks, slik at
dei gruppar seg naturleg saman med dei ikkje-loggande søskena sine.

### Funn 8 — `update-valid-scopes` vert einaste attverande «update-»-target etter Funn 5

**Opphavleg vurdering (forkasta):** Vurdert som akseptabelt, sidan
«oppdater til å reflektere gjeldande tilstand» er ei vanleg tolking av
«update» for genererte lister-filer.

**Ny vurdering:** Den vurderinga føresette at `update-modellkatalog`
også brukte «update-»-prefikset (med ein annan, inkrementell
patch-semantikk), så «update-» var ikkje eintydig i make-laget frå før.
No som Funn 5 vedtek å **fjerne** `update-modellkatalog` heilt, vert
`update-valid-scopes` ståande att som det **einaste** targetet i heile
make-laget som brukar `update-`-prefikset — og han gjer, som før nemnt,
ei full omskriving (`find | sed | sort > .github/valid-scopes.txt`), ikkje
ei inkrementell oppdatering. Utan noko `update-modellkatalog` att å
samanliknast med, står han åleine og brukar eit prefiks resten av
kodebasen reserverer for `gen-*`.

**Alternativ:** Omdøyp `update-valid-scopes` → `gen-valid-scopes`, i tråd
med `gen-config` (som òg regenererer ei fil frå `find`-oppdaga kjelder) og
resten av `gen-*`-familien.

### Funn 9 — `new-begrepskatalog` fjernast

**Opphavleg vurdering (forkasta):** Alt grundig handtert i
`specs/done/make-kommando-inkonsistens-audit.md` — dokumentert legacy,
ikkje eit alias for `new-begrepssamling`.

**Mellomsteg (forkasta):** Legacy-statusen finst i dag berre i
kjeldekodekommentaren og i `## `-hjelpeteksten
(`## Legacy scaffolding for monolittisk BegrepContainer-format`) — synleg
berre for ein brukar som alt køyrer `make help` eller les
`make/70-scaffolding.mk` direkte. Eit omdøypingsalternativ
(`new-begrepskatalog` → `new-begrepskatalog-legacy`) vart vurdert for å
gjere legacy-statusen synleg direkte i kommandonamnet.

**Vedtak:** `new-begrepskatalog` fjernast heilt i staden for å omdøypast —
target i `make/70-scaffolding.mk`, `.PHONY`-oppføringa i `Makefile`,
scriptet `src/assets/scripts/scaffolding/new-begrepskatalog.sh`, og alle
referansar i `COMMANDS.md`/dokumentasjon/mkdocs. Merk avhengigheita som
grunngav at targetet vart halde ved like i utgangspunktet:
`src/linkml/begrepskatalog/brreg-begrepskatalog` brukar i dag det
monolittiske `BegrepContainer`-formatet dette scriptet scaffoldar. Fjerning
av targetet hindrar ikkje den eksisterande katalogen i å halde fram som han
er (ingen re-scaffolding trengst av eksisterande filer), men fjernar
moglegheita til å scaffolde **nye** katalogar i det gamle formatet — bør
difor berre gjerast dersom det er stadfesta at ingen fleire katalogar skal
opprettast i det monolittiske formatet framover.

## Vurdert, men ikkje flagga som namngjevingsfunn

- Alle øvrige 70+ target (`gen-jsonschema`, `gen-owl`, `validate-instance`,
  `mcp-linkml-*`-familien, resten av scaffolding-targeta, `analyse-*`-
  familien, `build-docker-*`, `gource-*` m.fl.) har namn som samsvarer
  presist med hjelpeteksten og den faktiske oppskrifta — ingen funn, og
  ingen av dei vart omvurderte i denne runden.

## Handlingsliste

- [x] Funn 1: `check-published-uris`-oppskrifta gjenoppretta
- [x] Funn 2: `convert-rdf` → `convert-instance-rdf` med
      `DOMAIN=<domene>`-støtte; `gen-linkml-convert` fjerna, `domain_target`-
      pipelinen kallar no `convert-instance-rdf DOMAIN=$(1)`
- [x] Funn 3: `gen-linkml-merge` → `validate-linkml-merge`
- [x] Funn 4: `gen-docs` → `gen-schema-docs`
- [x] Funn 5: `update-modellkatalog`-**targetet** fjerna (sjå avvik under —
      sjølve scriptet måtte behaldast)
- [x] Funn 6: `gen-erdiagram` → `gen-erdiagram-mermaid`
- [x] Funn 7: `log-mcp-validate` → `validate-policy-logg`,
      `log-validate-instance` → `validate-instance-logg`
- [x] Funn 8: `update-valid-scopes` → `gen-valid-scopes`
- [x] Funn 9: `new-begrepskatalog` fjerna (target + script + referansar)

## Utført

Alle ni funn er gjennomførte. Fullstendig fil-for-fil-oversikt i commit-
meldinga; oppsummering av dei viktigaste stega og to avvik frå den
opphavlege planen under.

**Funn 1 — `check-published-uris` gjenoppretta:**
- Henta den fullstendige, opphavlege oppskrifta attende frå git-historikken
  (`git log -S`, commit `ee9b0e4c`/`1ea25971`, fjerna i ein seinare
  `refactor(make): konsolider gen-*`-commit). Verifiserte at
  datafil-stien recipen føreset (`<domain>/<modell>/data/<modell>/<modell>.yaml`)
  framleis stemmer med dagens katalogstruktur.
- Skreiv recipen på nytt i moderne stil (`print_header`, `LOG_FUNCTIONS`/
  `log_error` med `::error file=...`-annotasjon, i staden for rå `echo`) —
  same mønster som resten av `Makefile`.
- **Verifiseringsfunn:** Ein faktisk køyring av det gjenoppretta targetet
  avdekte eit reelt, tidlegare usett avvik: URI-en
  `https://begrep.brreg.no/samlingar/registerbegrep-2025` står i
  `src/linkml/begrepskatalog/brreg-begrepskatalog/published-uris.lock`,
  men manglar frå den tilhøyrande datafila. Dette har vore usjekka sidan
  targetet forsvann. **Krev brukaroppfølging** — anten legg URI-en til i
  datafila, eller fjern lock-linja dersom han er feilaktig/aldri reelt
  publisert. Fram til då vil `make check-published-uris` (og dermed
  `validate.yml`-CI-steget) feile for `begrepskatalog`-domenet.
- Lagt til i `help.sh` sin «Validering»-kategoriregel (var usynleg i
  `make help` òg før han forsvann).

**Funn 2 — `convert-rdf`/`gen-linkml-convert` slått saman:**
- `Makefile`: `convert-rdf` omdøypt til `convert-instance-rdf`, no med
  `DOMAIN=$(DOMAIN)` sendt til `convert-examples.sh` (som alt støtta eit
  valfritt domeneargument).
- `make/20-domain-targets.mk`: `gen-linkml-convert`-targetet sletta.
- `src/assets/scripts/makefile/run-domain-pipeline.sh`: kallet i Fase 1
  peikar no på `convert-instance-rdf DOMAIN="$domain"`.

**Funn 3 — `gen-linkml-merge` → `validate-linkml-merge`:**
- `make/11-generator-targets.mk`: `make_gen_target`-eval-kallet og
  hjelpeteksten omdøypt.
- `run-domain-pipeline.sh`: Fase 1-kallet oppdatert.

**Funn 4 — `gen-docs` → `gen-schema-docs`:**
- `make/11-generator-targets.mk`: target, `.PHONY` og hjelpetekst omdøypt.
- `run-domain-pipeline.sh`: Fase 1-kallet oppdatert.

**Funn 5 — `update-modellkatalog` (avvik frå planen):**
- Sletta i utgangspunktet både target og
  `src/assets/scripts/makefile/update-modellkatalog.py` heilt, slik planen
  sa.
- **Oppdaga under verifisering:** `gen-modelldcat-elements.py` importerer
  seks funksjonar og ein konstant **dynamisk** frå
  `update-modellkatalog.py` (`importlib.util.spec_from_file_location`) for
  å gjenbruke org-/skjemaoppslagslogikk (eksplisitt DRY-grunngjeving i
  kjeldekoden) — sletting av fila ville brote eit anna, framleis aktivt
  target (`make gen-modelldcat-elements`).
- **Retta:** fila gjenoppretta frå git (`git checkout --`), med ein ny
  kommentar øvst som forklarer at ho ikkje lenger er eksponert som
  make-target, men held fram som delt modul for
  `gen-modelldcat-elements.py`. Berre **make-targetet**
  (`update-modellkatalog` i `Makefile`, `.PHONY`-oppføringa) er fjerna —
  Funn 5 sitt faktiske mål («ingen `make update-modellkatalog`-kommando
  lenger») er likevel oppnådd.

**Funn 6 — `gen-erdiagram` → `gen-erdiagram-mermaid`:**
- `make/11-generator-targets.mk`: target og hjelpetekst omdøypt.
- `.github/workflows/release-please.yml:207`: CI-kall oppdatert (verifisert
  reelt CI-kall, ikkje falsk positiv) — `actionlint` køyrt etterpå, berre
  pre-eksisterande `[shellcheck]`-funn (ikkje-blokkerande per CLAUDE.md).
- `Kommando (i container)`-kolonna i `mkdocs/docs/automasjon/artefakt-generering.md`
  er **ikkje** endra der ho viser til `linkml gen-erdiagram` — det er
  LinkML sitt eige CLI-verktøynamn, ikkje vårt make-target.

**Funn 7 — `log-mcp-validate`/`log-validate-instance` → `validate-policy-logg`/`validate-instance-logg`:**
- `make/40-validation.mk`: begge target, feilmeldingar og kommentarar
  oppdaterte.
- **Verifiserte at ingen CI-endring trengst:** `.github/workflows/{generate,validate}.yml`
  kallar det underliggande scriptet (`run-validation.sh`) direkte, ikkje
  via make-targeta — dei to CI-arbeidsflytene er difor upåverka av
  omdøypinga.

**Funn 8 — `update-valid-scopes` → `gen-valid-scopes`:**
- `make/70-scaffolding.mk`: target og hjelpetekst omdøypt.
- Alle sju kallarar oppdaterte: fire scaffolding-script
  (`new-modell.sh`, `new-modellkatalog.sh`, `new-begrepssamling.sh`,
  `remove-modell.sh`), demo-scriptet (`javazone-demo-script.sh`, 2 stader),
  `help.sh` sin kategoriregel, og `CONVENTIONS.md`.

**Funn 9 — `new-begrepskatalog` fjerna:**
- Target og forklarande kommentarblokk fjerna frå `make/70-scaffolding.mk`;
  `.PHONY`-oppføring fjerna frå `Makefile`.
- `src/assets/scripts/scaffolding/new-begrepskatalog.sh` sletta.
- `mkdocs/docs/kom-i-gang/ny-begrepsmodell.md`: åtvaringsboks lagt til
  øvst som peikar til `new-begrepssamling`; dei to bokstavelege
  kommandolinjene i sjølve rettleiinga nøytraliserte til referansetekst
  (heile denne 260-liners rettleiinga skildrar elles framleis det
  monolittiske formatet — **ikkje omskriven** for `new-begrepssamling`,
  sidan det er ei eiga, større innhaldsoppgåve utanfor namngjevings-
  gjennomgangen).

**Dokumentasjons-/referansesveip (alle ni funn samla):**
Oppdaterte `COMMANDS.md` (ankerlenkjer + fem tabellrader),
`mkdocs/docs/kom-i-gang/kommandoar.md`, `mkdocs/docs/kom-i-gang/ny-org.md`
(Steg 4 omskriven med åtvaringsboks om patch- vs. full-regenerering-
skilnaden mellom gamalt og nytt target), `mkdocs/docs/automasjon/artefakt-generering.md`,
`README.md`, `GOVERNANCE.md`, `CONTRIBUTING.md`, `CODEOWNERS.md`,
`make/README.md`, `src/mcp-linkml-validator/policies/README.md`,
`src/assets/templates/docgen/README.md`, to opne (`open`/`upstream`) bug-
filer (`mermaid-classdiagram-eitt-click-per-boks.md`,
`mermaid-link-ekstern-uri-prefiks.md`) og fire interne script-kommentarar
(`batch-rdf-validate.py`, `batch-convert.py`, `batch-docs-validate.py`,
`batch-generate-instances.py`, `convert-examples.sh`). `specs/done/*` og
løyste/historiske `bugs/*`-filer (status `løyst`) er medvite **ikkje**
rørte, i tråd med DRY-unntaket i CLAUDE.md for arkivert innhald.

**Verifisert:**
- `make -n help`, `make -n check-published-uris`,
  `make -n convert-instance-rdf DOMAIN=test`,
  `make -n validate-linkml-merge DOMAIN=test`,
  `make -n gen-schema-docs DOMAIN=test`,
  `make -n gen-erdiagram-mermaid DOMAIN=test`, `make -n gen-valid-scopes`,
  `make -n validate-policy-logg ...`, `make -n validate-instance-logg ...`
  — alle løyser korrekt.
- Dei seks gamle namna (`gen-linkml-convert`, `gen-linkml-merge`,
  `gen-docs`, `update-modellkatalog`, `new-begrepskatalog`,
  `update-valid-scopes`, `log-mcp-validate`) feilar no korrekt med
  «No rule to make target».
- `make -n domain-samt` og `make -n domain-begrepskatalog` (full
  domenepipeline-dryrun) løyser med dei nye namna gjennomgåande.
- `make help` køyrer feilfritt og viser alle nye/omdøypte target i rett
  kategori (inkl. det gjenoppretta `check-published-uris`).
- `bash -n`/`python3 -m py_compile` på alle endra shell-/Python-script —
  ingen syntaksfeil.
- `actionlint` mot `.github/workflows/release-please.yml` — berre
  pre-eksisterande `[shellcheck]`-stilråd.

**Ikkje gjort (bevisst utanfor omfang):**
- Full omskriving av `mkdocs/docs/kom-i-gang/ny-begrepsmodell.md` sitt
  260-linjers tutorial-innhald til å skildre `new-begrepssamling` sin
  filstruktur i staden for det fjerna, monolittiske formatet.
- Retting av den nyoppdaga `published-uris.lock`-avviket for
  `brreg-begrepskatalog` (Funn 1) — datainnhaldsavgjerd, ikkje ein del av
  namngjevingsgjennomgangen.
- Ei rekkje pre-eksisterande, urelaterte staleness-funn oppdaga undervegs
  (t.d. `mcp-begrep-build`/`mcp-val-build` i same `ny-begrepsmodell.md`,
  feil `src/assets/scripts/update-modellkatalog.py`-sti utan `makefile/`-
  segment fleire stader) er **ikkje** retta, sidan dei ikkje stammar frå
  denne gjennomgangens ni funn.
