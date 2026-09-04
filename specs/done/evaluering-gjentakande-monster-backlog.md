# Evaluering: gjentakande problemstillingar på tvers av specs/backlog

## Bakgrunn

Brukaren bad om ein ny gjennomgang av alle filer i `specs/backlog/` (24
filer) for å evaluere om det finst problemstillingar som går igjen og
fører til gjentakande feil — ikkje eit samandrag av kvar enkelt spec, men
mønster på tvers av dei.

## Metode

Alle 24 filer i `specs/backlog/` er lesne i sin heilskap. Kryssjekka mot
`BUGS.md` (alle 21 registrerte bugs) og enkelt-bug-filer for å avgjere om
eit mønster ein spec føreslår ein fiks for, alt har materialisert seg som
ein registrert bug — éin eller fleire gonger.

**Runde 2 (utgreiing):** Brukaren bad om djupare utgreiing av konkrete
løysingsalternativ for P5, P2 og P3/P4. Tre parallelle fork-agentar
undersøkte kvart sitt tema (implementasjon, git-historikk/datoar, faktisk
omfang via grep/committa valideringsloggar) og leverte konkrete
løysingsforslag med filer/linjer. Funna er lagt inn som eigne
"Løysingsforslag"-underavsnitt under kvart mønster nedanfor. Framleis rein
utgreiing — ingen kodeendring er utført.

## Funn — mønster som går igjen

### P1 — `linkml-runtime` sin RDF-roundtrip er strukturelt skjør (6 registrerte bugs, same komponent)

**Bevis:** `BUGS.md` listar **seks** separate bugs i `rdflib_loader`
(BUG-1 LangString, BUG-2 `inlined_as_list`+identifier, BUG-3
`MappingError` for domene-URI, BUG-15 `https://`→`https:/`-kollaps ved
relativ import, BUG-18 CURIE ikkje re-ekspandert, BUG-19
datetime-separator) — alle i **same** upstream-komponent.
`specs/backlog/fix-roundtrip-ngr-inlined-as-list.md` er ei **open,
uløyst** instans av BUG-2, som eksplisitt konkluderer med å vente på
upstream-fiks (Alternativ B), sidan den einaste andre løysinga
(Alternativ A: URI-lister i staden for inlining) vart avvist fordi ho
bryt containerklasse-regelen (R5, `specs/done/inlining-konvensjon.md`).

**Rotårsak:** Umoden funksjonalitet i eit eksternt bibliotek
(`linkml-runtime`), ikkje noko repoet sjølv kan fikse — men mønsteret av
**stadig nye** roundtrip-bugs i akkurat denne loader-komponenten (seks
på under eit år) tyder på at RDF-roundtrip generelt er eit høgrisikoområde
ved ny skjemamodellering, ikkje eit avslutta problem.

### P2 — Override/redefinering av importerte klassar/slots krasjar LinkML (ramma tre gonger uavhengig)

**Bevis:**
- BUG-6 (`dqv-standard-class-override.md`) og BUG-7
  (`duplicate-slot-merge-konflikt.md`, eksplisitt kalla "slot-variant av
  BUG-6" i `BUGS.md`) — dei opphavlege, registrerte instansane.
- `specs/backlog/del-opp-ap-no-profilar-i-moduler.md` § «Avgrensingar»
  punkt 1 siterer BUG-6 direkte som **hard konstraint** som gjer at
  «Alternativ 2» (fjern DQV-kopling frå `dcat-ap-no`) må avvisast.
- `specs/backlog/javazone-demo-plan.md` § «Ferdig kopierbar
  klassedefinisjon» dokumenterer at eit **fyrste utkast** til
  demo-skjemaet trefte **same feilklasse på nytt**, live, under vanleg
  modellering: eit forsøk på å definere ein lokal `tittel:`-slot
  kolliderte med den alt importerte globale `tittel`-sloten. Retta ved å
  gjenbruke i staden for å skugge — men understrekar at feilen framleis
  er lett å trå i, sjølv for erfarne bidragsytarar.

**Rotårsak:** LinkML sin import-merge-mekanisme støttar ikkje trygg
redefinering av eit alt-importert slot/klasse-namn — regelen «gjenbruk,
skugg aldri» er dokumentert i kommentarar og i denne spec-samlinga, men
finst ikkje som ei automatisk, føre-var-sjekk (t.d. i `make new-modell`
eller ein lint-regel) som fangar forsøket **før** det når
`mcp-linkml-valider-modell`/generator-krasj.

**Løysingsforslag (utgreidd runde 2):** Datoverifisering (`git log -S`)
viser at `src/assets/scripts/makefile/check-import-duplicates.py` (som
**alt** dekker heile BUG-6/BUG-7-mønsteret — han kallar
`SchemaLoader(mergeimports=True).resolve()` direkte, same interne
mekanisme som gir "Conflicting URIs"-krasjen) vart innført **2026-08-23**,
**etter** alle tre P2-hendingane (BUG-6/BUG-7: 2026-06-20,
javazone-demo-kollisjonen: 2026-08-19). Verktøyet vart bygd som respons på
ein *fjerde*, uavhengig instans (`specs/done/oreg-scaffold-generering-feiler.md`).
Ingen av dei tre hendingane er altså bevis på eit hòl i sjølve
sjekk-logikken — verktøyet fanst rett og slett ikkje enno.

Det **reelle, verifiserte gapet i dag** er wiring, ikkje logikk:
`check-import-duplicates.py` køyrer via `make validate`/`make test`/
`make new-modell` og CI (`make/40-validation.mk`), men **ikkje** via
`make lint` (same fil, `lint:`-oppskrifta kallar berre `batch-lint.py`).
CLAUDE.md § "Valider arbeidet ditt" listar likevel `make lint SCHEMA=<sti>`
som **første** kommando å køyre etter kvar skjemaendring — nettopp
kommandoen ein reflekterer til under aktiv modellering hoppar over
kollisjonssjekken, som dermed først fangar seint (ved `validate`/CI).

Føreslått fiks (avgrensa, ingen endring i `check-import-duplicates.py`
sjølv — han er alt korrekt): legg til eit `check-import-duplicates.py`-kall
i `lint:`-oppskrifta i `make/40-validation.mk`, etter `batch-lint.py`, med
same `$(if $(SCHEMA),$(SCHEMA),$(SCHEMAS))`-mønster. **Avveging:** dette
legg eit nytt `$(LINKML_RUN)`-containerkall (og `linkml`-importens
~5-8 s oppstartskost) til `lint`, som elles er meint å vere raskaste
sjekk. Alternativ med null runtime-kost: dokumenter i staden
`check-import-duplicates` som obligatorisk **andre steg** rett etter
`make lint` i CLAUDE.md, på bekostning av å vere avhengig av at nokon
faktisk hugsar å køyre begge. `slot_usage`-overstyring av eit importert
slot (den dokumenterte, trygge måten å avgrense eit felt på) er **ikkje**
same mønster og er ikkje råka.

### P3 — Overbreie CI-cache-nøkkel-glob er ein tilbakevendande feilklasse, ikkje éin isolert bug

**Bevis:** `specs/done/docs-only-endring-cache-miss-alle-domene.md` fiksa
akkurat dette for `'make/**'`-globet i `generate`-jobben sin cache-nøkkel
(erstatta med eksplisitt fil-liste). `specs/backlog/scripts-glob-cache-miss-generate-jobb.md`
dokumenterer at **same feilklasse** deretter oppstod for
`'src/assets/scripts/**'` i **same cache-nøkkel** — ei reell,
observert unødvendig full rekjøring av alle domene-jobbar frå ei
commit som berre rørte to filer heilt utanfor kallgrafen.

**Rotårsak:** Det finst ingen systematisk sjekk («er kvar
`hashFiles(...)`-glob i denne workflow-fila verifisert mot den faktiske
kallgrafen?») — kvart avvik vert oppdaga og retta **reaktivt**, éin glob
om gongen, etter at nokon merkar unødvendig cache-miss i praksis.

**Løysingsforslag (utgreidd runde 2):** Alle 8 `hashFiles(...)`-bruk i
`.github/workflows/*.yml` er kartlagde. Dei fleste (`generate.yml`:166,
271, 619; `lenkje-og-mermaid-sjekk.yml`:366; `validate.yml`:187) brukar
alt eksplisitte fil-lister — trygge. `generate.yml:519` (`v4-generated`)
er fiksa 2026-08-27 (jf. P6, ligg i backlog og ventar berre på
CI-stadfesting).

**Ny, konkret P3-instans funne:** `lenkje-og-mermaid-sjekk.yml:125` brukar
**same nøkkelnamn** (`v4-generated`) og har ein kommentar som seier
ordrett at formelen er «identisk med generate.yml — deler dermed
cache-innslag på tvers av workflowar» (dokumentert, målt gevinst i
`specs/done/lenkjesjekk-reduser-clock-time.md`). Men 2026-08-27-fiksen
endra **berre** `generate.yml` sin variant til ei innsnevra fil-liste —
`lenkje-og-mermaid-sjekk.yml:125` har framleis den breie
`'src/assets/scripts/**'`. Konsekvens, dobbel: (1) same P3-symptom står
att uretta i denne workflow-fila, **og** (2) sidan `hashFiles(...)`-inputa
no skil seg mellom dei to filene, deler dei **ikkje lenger** cache-innslag
i det heile — den dokumenterte cross-workflow-gevinsten er stille broten
av ein fiks som aldri vart spegla til begge stader.

Føreslått tiltak, to delar:
1. **Umiddelbar retting:** kopier den innsnevra fil-lista frå
   `generate.yml:519` til `lenkje-og-mermaid-sjekk.yml:125`, oppdater
   kommentaren (siterer i dag feil linjenummer og ei formel som ikkje
   lenger er identisk).
2. **Systematisk verifisering, avgrensa omfang:** eit nytt script
   (t.d. `check-cache-key-coverage.py`, same familie som
   `find-similar-names.py`) som — i staden for å løyse det generelle
   "er globet korrekt"-spørsmålet — berre finn cache-nøklar med same
   namneprefiks på tvers av workflow-filer og feilar dersom deira
   `hashFiles(...)`-argument ikkje er byte-for-byte like. Fangar nett
   denne regresjonsklassen (to stader som skal vere synkroniserte, driv
   frå kvarandre). Kan leggjast til som `analyse-cache-key-konsistens` i
   `make/91-modell-analyse.mk`, køyrt saman med dei andre `analyse-*`-måla
   (informativt, feilar aldri byggjet).

### P4 — `new-modell.sh` sitt standard-import skaper varig, uoppfølgd importgjeld

**Bevis:** `specs/backlog/del-opp-ap-no-profilar-i-moduler.md` § «Alternativ 5»
identifiserer **seks** skjema (`javazonetalk`,
`bvrbekreftelse`/`bvrettersendingavvedlegg`/`bvrstiftelsesdokument`/
`bvrinnfelles`/`frivilligorganisasjonapi`) som alle framleis har den
**uendra** `# TODO: endre/legg til imports etter behov`-kommentaren frå
`new-modell.sh`, og importerer full `dcat-ap-no` (29 klassar) utan å
bruke meir enn 0-2 av dei. `specs/backlog/avvik-peikarar-til-offentlege-ressursar.md`
fann uavhengig at `javazonetalk` sitt scaffold-etterslep òg gav ein
urelatert, feilaktig `example.no`-URI-referanse i same skjemafamilie —
same rot (scaffold aldri følgt opp), ulikt symptom.

**Rotårsak:** Scaffoldinga legg inn ein **passiv TODO-kommentar** i
staden for anten å spørje brukaren aktivt eller flagge det seinare (t.d.
i lint/CI) — det finst ingen mekanisme som fangar opp ein uendra TODO
etter at skjemaet er teke i bruk.

**Løysingsforslag (utgreidd runde 2):** Kjelda er stadfesta presist —
`src/assets/scripts/scaffolding/new-modell.sh:198-204`, ei ubetinga
strengerstatning som alltid legg til full `dcat-ap-no`-import + TODO,
uavhengig av `DOMAIN`/`NAME`. Statusen på dei seks skjemaa frå
`del-opp-ap-no-profilar-i-moduler.md` er oppdatert: `enhetsregisteret-bvrinnfelles`
har **alt** fått importen fjerna (uavhengig opprydding). Dei **fem**
attverande (`javazonetalk`, `enhetsregisteret-bvrbekreftelse`,
`-bvrettersendingavvedlegg`, `-bvrstiftelsesdokument`,
`-frivilligorganisasjonapi`) er verifisert med grep: **0 av 29**
`dcat-ap-no`-klassar er i bruk (`range:`/`is_a:`) i noka av dei.

Tre tiltak, aukande i omfang:
1. **Oppryddingsplan no, for dei fem attverande** — fjern
   `dcat-ap-no`-importlinja + TODO-kommentaren frå alle fem (trygt,
   stadfesta 0-bruk). For `javazonetalk` vert resultatet eit reint
   2-linjers `imports:`-avsnitt (berre `linkml:types` att). Verifiser
   kvar med `make lint`/`make roundtrip` etter fjerning.
2. **CI-/analyse-flagg for framtidige uendra TODO-ar:** nytt script i
   `analyse-*`-familien (`make/91-modell-analyse.mk`) som `grep`-ar etter
   den eksakte TODO-strengen i alle `*-schema.yaml`, sjekkar
   opprettingstidspunkt via `git log --diff-filter=A`, og rapporterer
   skjema eldre enn t.d. 90 dagar i `## Modellanalyse`-avsnittet
   (informativt, feilar aldri byggjet — same mønster som resten av
   `analyse-*`).
3. **Gjer scaffoldinga meir aktiv** (større, eiga åtferdsendring i eit
   sentralt script) — t.d. la `DOMAIN` styre kva (om noko) som vert
   føreslått importert, eller spør eksplisitt. Krev eigen, liten spec med
   uttrykkjeleg brukargodkjenning (jf. CLAUDE.md sin endringsterskel for
   sentrale script) — ikkje noko å gjere stilltiande saman med punkt 1-2.

### P5 — Silver/gold sitt `container_har_katalog`/`container_kvalitetsmaal`-krav er eit kjent, ubetinga policy-gap — oppdaga to gonger uavhengig

**Bevis:** `del-opp-ap-no-profilar-i-moduler.md` § «Opne spørsmål» punkt 1
stadfesta med ein faktisk `mcp-linkml-valider-modell`-køyring at
`samt-bu-schema.yaml` har stått med `valid: false` (silver) over **fleire
utgjevne versjonar** (1.0.0→1.10.1) på grunn av eit ubetinga
containerklasse-krav (`Katalog`/`Kvalitetsmaal`/`Kvalitetsmaaling`) som
gjeld **uansett** om skjemaet faktisk modellerer eit katalog-/
kvalitetsmåling-scenario. Rotårsaka er spora til to
omdøypingscommitar (`ap-no-catalog.yaml`→`ap-no.yaml`→`silver.yaml`)
utan grunngjeving for utvida omfang — «utilsikta scope creep frå
omdøyping». `specs/backlog/javazone-demo-plan.md` § «Steg 9» (skrive
seinare, uavhengig) **traff nøyaktig same fire feil** på eit heilt nytt,
urelatert demo-skjema (`javazonetalk`), og måtte forklare dei til
publikum som «urelaterte, strukturelle DCAT/DQV-krav» framfor noko som
kan rettast.

**Rotårsak:** Eit policy-gap identifisert og godt dokumentert i éin spec
har ikkje vore synleg nok til å hindre at eit **heilt anna** arbeid
(demo-forbereding) treffer akkurat same veggen månader seinare.
`del-opp-ap-no-profilar-i-moduler.md` føreslår sjølv at dette bør
handterast som ein eigen spec, uavhengig av sjølve import-splittinga.

**Løysingsforslag (utgreidd runde 2) — omfanget er vesentleg større enn
opphavleg dokumentert.** Sjekken (`_check_container_has_class`,
`src/mcp-linkml-validator/server.py:395-427`) har **to** uavhengige
feilmodusar, ikkje éin:

- **Modus A (domenemodellar med container, manglar krevde klassar):**
  **13-14 skjema** (alle `tree_root=1`, `validation_policy: silver`) —
  heile FINT-familien (6), heile BVR-familien (6),
  `javazonetalk`, `samt-bu`. Stadfesta i committa `validation/*/silver.json`.
- **Modus B (NY — ikkje i den opphavlege analysen): vokabularskjema utan
  container i det heile.** **10 skjema** (`dcat-ap-no`, `dqv-ap-no`,
  `dqv-core`, `modelldcat-ap-no`, `modelldcat-katalog`, `modelldcat-modell`,
  `skos-ap-no`, `xkos-ap-no`, `cpsv-ap-no`, `fair-metadata`,
  `validation_policy: gold`) har `tree_root=0` per **eksplisitt
  repo-konvensjon** (`.claude/rules/linkml-schema.md`: "AP-NO-modellar og
  fair-modellar skal ikkje ha eigen containerklasse") — sjekken feilar
  difor **strukturelt og permanent**, stadfesta i committa
  `validation/*/gold.json` (`no_container_class`), maskert av andre feil
  så det åleine avgjer ikkje `valid:false`, men er likevel eit varig
  falskt signal for alle 10.
- **Separat, ekte implementasjonsbug funne:** `no_container_class`-issuen
  (containerklasse manglar heilt) er **hardkoda til `"error"`-severity**
  i koden (linje ~406) — ignorerer `config["severity"]` frå policy-YAML.
  Bør rettast **uavhengig** av kva hovudalternativ som veljast, sidan han
  påverkar alle framtidige `container_has_class`-sjekkar.

**To løysingsalternativ, vurderte mot kvarandre:**

| | (a) Innhaldsbasert, betinga sjekk | (b) `exclude_schemas`-liste |
|---|---|---|
| Metode | Krev berre klassen dersom han faktisk er brukt som `range` på **noka global slot/attributt** i skjemaet (ikkje berre tilgjengeleg via import) | Kopier det alt eksisterande `config.get("exclude_schemas", [])`-mønsteret (brukt to andre stader i `server.py:187,202`) inn i `_check_container_has_class` |
| Vedlikehald | Framtidssikra — nye skjema treng ingen manuell registrering | Manuelt: 23 skjema (13+10) må leggjast inn no, kvart nytt unntak seinare må hugsast |
| Implementeringskostnad | Éin ny hjelpefunksjon + kall frå eksisterande sjekk | Billegare — ingen ny logikk, berre config |
| Presisjon | Måler faktisk bruk, ikkje berre skjemakategori | Trefsikkert, men "dømmer etter namn" ikkje innhald |

`gold.yaml` treng **ikkje** eiga endring for noko av alternativa —
`TestPolicyKoherens` (`tests/test_mcp_policies.py:1101-1132`) sjekkar
berre warning→error-parity, ikkje `container_has_class`-config, og gull
arvar sølv sine felt uendra via `{**parent, **child}`-merge.

**Tilråding frå utgreiinga:** alternativ (a) — dekker begge feilmodusane
utan manuell liste å vedlikehalde, og løyser Modus B strukturelt
(vokabularskjema utan container vil aldri feilaktig krevjast å ha éin).

### P6 — Fleire specs er reelt ferdige, men fastlåste i backlog av same strukturelle årsak

**Bevis:** `reduser-generate-workflow-under-5min.md`,
`scripts-glob-cache-miss-generate-jobb.md` og
`codeql-unused-imports-genererte-model-py.md` har alle ei
`## Utført`-seksjon som dokumenterer fullført kodeendring, men vert
**medvite** verande i `specs/backlog/` fordi siste steg krev ein reell
CI-køyring/push som eg ikkje kan utføre eller observere sjølv (jf.
CLAUDE.md sitt forbod mot at LLM gjer git-operasjonar).

**Vurdering:** Ikkje ein feil, men eit tydeleg, gjentakande mønster verdt
å synleggjere — desse tre treng berre ei rask brukar-stadfesting
(«stemte cache-hit/-miss slik forventa i neste køyring?») for å kunne
flyttast til `specs/done/`. Eit mogleg tiltak: eit fast avsnitt/tag i
spec-malen for «attstår berre brukarverifisering i CI», slik at desse er
lette å finne igjen som gruppe.

### P7 — Verktøymiljøet mitt manglar fungerande rootless podman

**Bevis:** `javazone-demo-auto-innsetjing.md` og
`javazone-demo-plan.md` (steg 5-utvidinga og steg 9) måtte **begge**,
uavhengig av kvarandre, falle tilbake til statisk `grep`-basert
verifisering i staden for ein faktisk
`make mcp-linkml-valider-modell`-køyring, med identisk grunngjeving:
*«podman rootless var utilgjengeleg i verktøymiljøet på
verifiseringstidspunktet»* (feil: `newuidmap: write to uid_map failed:
Operation not permitted`).

**Vurdering:** Dette er ikkje ein bug i repoet, men eit strukturelt
avgrensa punkt ved *mitt eige* arbeidsmiljø i enkelte økter — same tema
som spørsmålet tidlegare i denne økta om rootless podman/WSL2. Verdt å
merke seg: når eg seier "verifisert", bør det alltid framgå **korleis**
(faktisk containerkøyring vs. statisk grep) — begge dei nemnde specs-ane
gjer dette eksplisitt og korrekt alt, eit godt mønster å halde fram.

## Isolerte specs (ingen gjenkjenna mønster med andre)

`bytt-separate-pull-requests-false.md`, `codeql-dobbel-koyring.md`,
`json-schema-lint.md`, `konsolider-feltnaervaer-sjekk-i-checks-mekanismen.md`,
`lock-github-action-versjonar.md`, `ekstern-kodeverk-versjonering.md`,
`dx-prof-linkml-modell.md`, `plan-demo-repo-dcat-ap-no.md`,
`nasjonal-datamesh-arkitektur.md`, `rename-schema-til-linkml-yaml.md`,
`vurdering-codegraph-kompatibilitet.md`, `TODO.md`,
`plan-konsekvent-begrepsidentifikator.md`. (`begrepsidentifikator-gap-liste-fase2.md`
er eit datavedlegg til `plan-konsekvent-begrepsidentifikator.md`, ikkje
ein sjølvstendig spec.)

`flytt-domene-docs-generering-til-matrise.md` er òg isolert (ingen
gjenkjenna P-mønster), men **heng tematisk saman med P6**: ho er ei rein
evaluering (eksplisitt "ingen kodeendring frå denne specen") som byggjer
direkte på og stadfestar konklusjonen i `reduser-generate-workflow-under-5min.md`
(sjølv eit P6-medlem) — den faktiske høgverdi-målsettinga («verifiser
site-cache-tiltaket i CI») ligg framleis der, ikkje i denne specen. Attstår
berre eit ope, lite spørsmål til brukaren (skal alternativ 4, eit
5-6 sekund mikrotiltak, implementerast?) — ikkje ei CI-verifisering som P6,
difor ikkje talt som eit fjerde P6-medlem, men verdt å nemne saman med det.

**Ei separat merknad, ikkje eit mønster:** `vurdering-codegraph-kompatibilitet.md`
har ei fullstendig `## Utført`-seksjon og «Ingen filer er endra i repoet»
— ho ser ut til å vere reelt ferdig (ei rein vurdering, ikkje eit
gjennomført tiltak som ventar på CI) og kunne truleg flyttast til
`specs/done/` utan vidare arbeid, i motsetnad til dei tre P6-nemnde.

## Anbefaling

Ingen kodeendring er utført av denne evalueringa/utgreiinga — begge rundar
er kartlegging brukaren skal ta stilling til. Etter runde 2 sin djupare
utgreiing er alle fire punkt no konkrete nok til å setjast i verk direkte,
utan ytterlegare research. Prioritert etter kor mykje kvart mønster alt
har kosta reelt arbeid, og kor konkret/avgrensa fiksen er:

1. **P5** (silver/gold-containerkrav) — høgast verdi: 23 skjema råka (ikkje
   berre 14 som opphavleg dokumentert), to uavhengige feilmodusar. Tilrådd
   fiks: innhaldsbasert betinga sjekk i `_check_container_has_class`
   (`src/mcp-linkml-validator/server.py:395-427`) + separat retting av den
   hardkoda `no_container_class`-severity-en. Størst enkeltinnsats, men òg
   størst dekning.
2. **P2** (import-override-fella) — minst kostnad å rette: éi ny linje i
   `lint:`-oppskrifta (`make/40-validation.mk`) som legg til det alt
   eksisterande, korrekte `check-import-duplicates.py`-kallet. Vurder
   runtime-kost-avveginga (nytt containerkall i `lint`) mot
   dokumentasjons-alternativet før val.
3. **P3** — to delar: umiddelbar re-synkronisering av
   `lenkje-og-mermaid-sjekk.yml:125` sin cache-glob mot `generate.yml`
   (kort, konkret retting av ein alt oppdaga regresjon), pluss eit nytt,
   avgrensa `analyse-cache-key-konsistens`-steg for å fange framtidige
   avvik systematisk.
4. **P4** — tre delar aukande i omfang: (a) fjern uendra
   `dcat-ap-no`-import frå dei fem attverande skjemaa (trygt, stadfesta
   0-bruk), (b) nytt `analyse-*`-steg som flaggar framtidige uendra TODO,
   (c) større, eigen spec for meir aktiv scaffolding (krev separat
   brukargodkjenning).
5. **P6** — reint prosess-tiltak, uendra: brukar stadfestar dei tre
   nemnde specs-ane sin CI-åtferd, flyttar dei til `specs/done/`.

## Avgjerder

- **Verifiserte fork-analysen sitt filtal før eg presenterte resultatet.**
  Både min eigen fork-prompt og fork-rapporten sjølv talde 22 filer i
  `specs/backlog/` — faktisk tal er 24 (`ls | wc -l`). To filer
  (`flytt-domene-docs-generering-til-matrise.md`,
  `plan-konsekvent-begrepsidentifikator.md`) var ikkje nemnde i verken
  mønster- eller isolert-lista. Grunngjeving for å rette før levering: eit
  krav om "full gjennomgang" som stille hoppar over 2 av 24 filer ville
  undergrave nett den tilliten evalueringa er meint å byggje.
- **Las begge manglande filer sjølv i staden for å sende fork-en attende.**
  Grunngjeving: begge var korte nok til å lese direkte (under 300 linjer
  kvar), raskare enn ein ny fork-runde, og eg kunne då vurdere plasseringa
  (isolert vs. mønster) med same kontekst som resten av evalueringa.
- **`plan-konsekvent-begrepsidentifikator.md` plassert som isolert, ikkje
  kopla til P5** sjølv om begge nemner `samt-bu-schema.yaml`.
  Grunngjeving: root causes er urelaterte (P5 er eit ubetinga
  containerklasse-policy-krav; denne specen gjeld manglande
  `begrepsidentifikator`-annotasjonar) — same skjema råka av to
  uavhengige ting er ikkje eit mønster.
- **`flytt-domene-docs-generering-til-matrise.md` nemnd saman med P6, men
  ikkje talt som eit fjerde medlem.** Grunngjeving: P6 sin definerte
  root cause er "ferdig kodeendring som ventar på CI-verifisering"; denne
  specen har **ingen** kodeendring i det heile og ventar i staden på ei
  brukaravgjerd om eit lite, valfritt mikrotiltak — nær nok til å nemne,
  ulikt nok til ikkje å telje som same mønster.
- **Nytta tre parallelle forkar (éin per tema: P5, P2, P3+P4) for
  runde 2-utgreiinga, i staden for éin sekvensiell.** Grunngjeving: temaa
  er uavhengige (ulike filer, ulik kode), og kvar utgreiing kravde djup
  lesing (git-historikk, committa JSON-valideringsloggar,
  implementasjonskode) som ikkje trong påverke dei andre — parallelt
  sparar tid utan å tape kvalitet, sidan forkane ikkje er avhengige av
  kvarandre sine funn.
- **La utgreiingsfunna erstatte/utvide dei opphavlege
  Bevis/Rotårsak-avsnitta i staden for å skrive eit nytt, separat
  dokument.** Grunngjeving: brukaren bad eksplisitt om å "oppdatere
  specen" — held alt samla på éin stad, med tydeleg
  "Løysingsforslag (utgreidd runde 2)"-merking slik at kjelde/tidspunkt
  for kvart funn framleis er sporbart.
- **Nedgraderte ikkje `## Anbefaling` sin ordlyd frå "vurder"/"kan takast
  som eigen spec" til meir handlingsretta språk**, sidan alle fire punkt
  no har konkrete filer/linjer/tiltak — men **utførte framleis ingen
  kodeendring**, sidan brukaren bad om utgreiing, ikkje implementering.

## Opent spørsmål

Alle fire hovudpunkt (P5, P2, P3, P4) har no konkrete, avgrensa
løysingsforslag med eksakte filer å endre. Skal eg gå vidare til
**implementering** av eitt eller fleire av dei (som eigne specs, jf.
CLAUDE.md sin arbeidsflyt), og i så fall i kva rekkjefølgje — eller
ønskjer du først å ta stilling til dei nemnde avveginane (særleg P2 sin
runtime-kost-avveging og P5 sitt val mellom alternativ (a)/(b))?

## Utført

Brukaren stadfesta P5, P2, P3, P4 (del a+b) og P6 — alle realiserte:

**P5 — innhaldsbasert betinga sjekk (alternativ a) + exclude_schemas
(alternativ b), begge kombinerte:**
- `src/mcp-linkml-validator/server.py::_check_container_has_class`:
  omskriven. `no_container_class` bruker no `config["severity"]` (var
  hardkoda `"error"`). Nytt `exclude_schemas`-gard øvst (Modus B). Nytt
  `_container_class_requirement_applies()`: for `error`-nivå krevst
  target_class **sjølv** brukt som `range` nokon stad i skjemaet (streng,
  per-klasse) — for `warning`-nivå held det at skjemaet alt er
  katalog-forma via éin av dei fire kjerneklassane (Modus A).
- **Verkeleg funn undervegs, ikkje i den opphavlege utgreiinga:** ein rein
  per-klasse-brukt-som-range-vakt (fork sitt opphavlege forslag) braut tre
  eksisterande testar, sidan `_SILVER_PASS`-fixturen sin
  Distribusjon-åtvaring og to andre testar implisitt kravde anten
  schema-vid katalog-forming eller det opphavlege ubetinga kravet. Løyst
  ved å skilje error- frå warning-nivå-logikken (sjå over) — verifisert
  mot faktiske skjema (`samt-bu`: dei to falske Katalog/Kvalitetsmaal-felen
  borte, den ekte Kvalitetsmaaling/Datasett-kravet står att; `fint-administrasjon`:
  `valid: true`, ingen container-feil; `dcat-ap-no`: ingen `no_container_class`;
  `referansemodell-silver`/`-gold`: framleis `valid: true`, ingen regresjon).
- **`exclude_schemas` måtte òg leggjast til i `gold.yaml`**, ikkje berre
  `silver.yaml` — eit funn den opphavlege utgreiinga ikkje fanga: `gold.yaml`
  **redeklarerer** 4 av dei 8 `container_*`-sjekkane (for å oppgradere
  severity til error), og shallow-merge-mekanismen (`{**parent, **child}`)
  gjer at ei redeklarering utan `exclude_schemas` mister han heilt, sjølv
  om `silver.yaml` har han. YAML-anker er dessutan fil-scopa — lista måtte
  difor duplíserast (kommentert som "må haldast i synk manuelt") i
  `gold.yaml`, ikkje delast via same anker.
- `src/mcp-linkml-validator/policies/silver.yaml`: `container_exclude_schemas`-anker
  (15 skjema) lagt til over `checks:`, referert frå alle 8 `container_*`-sjekkane.
- `src/mcp-linkml-validator/policies/gold.yaml`: same anker duplisert,
  referert frå dei 4 redeklarerte `container_*`-sjekkane.
- `tests/test_mcp_policies.py`: `test_container_utan_katalog_gir_feil` sin
  fixture oppdatert (må no faktisk referere Katalog for at kravet skal
  vere meiningsfullt). To nye regresjonstestar lagt til:
  `test_domenemodell_utan_katalogscenario_utloyser_ikkje_container_krav`
  (Modus A) og `test_vokabularskjema_i_exclude_schemas_utloyser_ikkje_no_container`
  (Modus B). Full testsuite (47 testar) grøn.

**P2 — check-import-duplicates.py i make lint:**
- `make/40-validation.mk`: `lint:`-oppskrifta kallar no
  `check-import-duplicates.py $(call get_target_schemas)` etter
  `batch-lint.py`. Verifisert med `make -n lint`.

**P3 — cache-nøkkel-resynkronisering + nytt analyse-steg:**
- `.github/workflows/lenkje-og-mermaid-sjekk.yml`: `v4-generated`-cache-nøkkelen
  sin `hashFiles(...)`-fil-liste synkronisert mot `generate.yml` (var
  drive frå kvarandre). Actionlint køyrt (kun eit urelatert
  `[shellcheck]`-funn, ikkje blokkerande).
- `src/assets/scripts/makefile/check-cache-key-coverage.py`: nytt script.
  Verifisert både at det IKKJE flaggar noko etter fiksen, og — via ein
  mellombels kopi av den urørte HEAD-versjonen av
  `lenkje-og-mermaid-sjekk.yml` — at det FAKTISK ville fanga regresjonen
  før fiksen.
- `make/91-modell-analyse.mk`: nytt mål `analyse-cache-key-konsistens`.
  Køyrt i faktisk containermiljø — stadfesta "Ingen avvik funne".

**P4a — gjennomgang av dei fem attverande scaffold-TODO-skjemaa:**
- **Viktig retting undervegs:** den opphavlege utgreiinga sin
  "0 av 29 dcat-ap-no-klassar i bruk" var korrekt for *klassar*, men fanga
  ikkje at alle fem skjema likevel treng `id`/(`javazonetalk` òg `tittel`
  + `LangString`) — desse globale slotsa/typane kjem transitivt frå
  `common-ap-no-schema` via AP-NO-importen, ikkje frå sjølve DCAT-klassane.
  Prøvde først å fjerne importen og definere `id`/`tittel` lokalt i staden —
  braut `make lint` (udeklarerte slots) og stod i direkte konflikt med
  importhierarki-regelen i `.claude/rules/linkml-schema.md`
  ("Domenemodellar importerer AP-NO-profilene... ikkje common-ap-no-schema
  direkte"). Reverterte til å **behalde** importen i alle fem, og fjerna
  berre den forelda TODO-kommentaren (no vurdert og stadfesta nødvendig).
- Endra filer: `javazonetalk-schema.yaml`,
  `enhetsregisteret-bvrbekreftelse-schema.yaml`,
  `enhetsregisteret-bvrettersendingavvedlegg-schema.yaml`,
  `enhetsregisteret-bvrstiftelsesdokument-schema.yaml`,
  `enhetsregisteret-frivilligorganisasjonapi-schema.yaml`. Alle fem
  verifisert grøne med `make lint` + `make roundtrip`.

**P4b — analyse-steg for framtidige uendra scaffold-TODO:**
- `src/assets/scripts/makefile/check-scaffold-todo-age.py`: nytt script
  (git-historikk-basert alder på scaffold-TODO).
- `src/assets/containers/Dockerfile.python`: `git` lagt til (`apk add`) —
  ny bundla verktøyavhengigheit i eit publisert (GHCR) containerbilete.
  Lisens sjekka (GPL-2.0) og lagt til attributions-tabellen i
  `mkdocs/docs/om.md`, jf. CONTRIBUTING.md § "Nye verktøyavhengigheiter".
- `make/91-modell-analyse.mk`: nytt mål `analyse-scaffold-todo-alder`.
  Bilete bygd på nytt (`make build-docker-python`) og målet køyrt i
  faktisk containermiljø — stadfesta "Ingen skjema... (47 skjema sjekka)".

**P6 — dei tre stadfesta specs-ane flytta til `specs/done/`:**
`reduser-generate-workflow-under-5min.md`,
`scripts-glob-cache-miss-generate-jobb.md`,
`codeql-unused-imports-genererte-model-py.md` — kvar med ei
stadfestingslinje lagt til før flytting.
