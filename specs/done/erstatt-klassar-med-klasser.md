# Erstatt «klassar» med «klasser»

## Bakgrunn

Brukaren ønskjer ordet «klassar» (nynorsk pluralform av «klasse») erstatta
med «klasser» i all dokumentasjon og i alle filer som genererer
dokumentasjon for mkdocs-portalen. Dette følgjer same mønster som
`specs/done/erstatt-artefaktar-med-artefakter.md` og
`specs/done/namn-navn-konsistens-make-help.md` — historiske,
brukarstadfesta unntak der ei bokmålsform vert brukt konsekvent sjølv i
elles nynorsk tekst (jf. CLAUDE.md § Skriftspråk, tabellen «Unntak —
enkeltord i bokmålsform»).

Motivasjonen er delvis akutt: `specs/done/gen-java-target-og-java-bruk-docs.md`
(førre økt) la nettopp til teksten **«Java-klassar»** i
`mkdocs/lib/sections/generated_artifacts.sh`, medan den eksisterande
artefakttabellen alt brukte **«Python-klassar»** — ein direkte
inkonsekvens denne oppgåva rettar opp.

### Avklart med brukar (2026-08-24)

Ordet skal erstattast **òg** i `src/linkml/`-filer (skjema, `description.md`,
manifest, eksempeldata) — ikkje berre i reindyrka dokumentasjonsfiler. Dette
betyr i praksis at heile repoet vert dekt, tilsvarande omfanget til
`erstatt-artefaktar-med-artefakter.md`.

**Omfang (grep `klassar` utanfor `.git/`, `generated/`, `mkdocs/site/`,
`node_modules/`, `specs/done/`):** 73 filer, ca. 380 linjer. `specs/done/`
er halde utanfor (arkivert, urørt — jf. DRY-unntaket i CLAUDE.md og same
praksis som dei to føregåande ordskiftingane).

### Kritisk skilje: kjeldefiler vs. autogenererte filer

Fleire av dei 73 filene er **autogenererte** (kommentarhovud
`# Generert av CI frå <script> — ikkje rediger manuelt`) eller inneheld
autogenererte blokker (README.md sine `<!-- BEGIN/END AUTO-GENERATED -->`-
tabellar). Desse skal **ikkje** redigerast direkte — endringa vert
overskriven ved neste regenerering. I staden må den faktiske kjelda
(oftast `description:`-feltet i sjølve `*-schema.yaml`) rettast, og
artefaktet deretter regenerert:

| Autogenerert fil | Kjeldeskript | Regenerer med |
|---|---|---|
| `README.md` (tabellradene mellom `<!-- BEGIN/END AUTO-GENERATED -->`, linje ~196-303) | `generate-readme-tables.sh` (les `description:` via `extract-schema-metadata.py`) | `make docs-publish` (køyrer skriptet som Steg 1) |
| `src/linkml/ap-no/dqv-core/metadata/dqv-core-manifest.yaml` | `generate-informasjonsmodell.py` | `make gen-informasjonsmodell-instance SCHEMA=src/linkml/ap-no/dqv-core/dqv-core-schema.yaml` |
| `src/linkml/ap-no/modelldcat-katalog/metadata/modelldcat-katalog-manifest.yaml` | same | `make gen-informasjonsmodell-instance SCHEMA=src/linkml/ap-no/modelldcat-katalog/modelldcat-katalog-schema.yaml` |
| `src/linkml/ap-no/modelldcat-modell/metadata/modelldcat-modell-manifest.yaml` | same | `make gen-informasjonsmodell-instance SCHEMA=src/linkml/ap-no/modelldcat-modell/modelldcat-modell-schema.yaml` |
| `src/linkml/fint/fint-common/metadata/fint-common-manifest.yaml` | same | `make gen-informasjonsmodell-instance SCHEMA=src/linkml/fint/fint-common/fint-common-schema.yaml` |
| `src/linkml/referanse/referansemodell-silver/metadata/referansemodell-silver-manifest.yaml` | same | `make gen-informasjonsmodell-instance SCHEMA=src/linkml/referanse/referansemodell-silver/referansemodell-silver-schema.yaml` |
| `src/linkml/begrepskatalog/brreg-begrepskatalog/data/brreg-begrepskatalog/brreg-begrepskatalog.yaml` | `collect-concepts.py` | `make gen-begrepskatalog-instance` |
| `src/linkml/modellkatalog/digdir-modellkatalog/data/digdir-modellkatalog/digdir-modellkatalog.yaml` | `generate-modellkatalog.py` (aggregerer alle manifest) | `make gen-modellkatalog-instance` (etter at manifesta over er regenererte) |

Alle andre treff (skjema sjølve, `description.md`, statiske mkdocs-sider,
`mkdocs/lib/**`, `src/assets/templates/docgen/**`, spesifikasjonar,
governance-dokument, hjelpescript) er handskrivne kjeldefiler og skal
redigerast **direkte**.

## Steg

1. Identifiser alle filer med treff:
   `grep -rlI "klassar" --exclude-dir=.git --exclude-dir=generated --exclude-dir=site --exclude-dir=node_modules .`,
   ekskluder `specs/done/`.
2. Del treffa i to grupper (jf. tabellen over):
   - **Autogenererte filer** (7 stk., identifisert av
     `# Generert av CI ... — ikkje rediger manuelt`-hovud, pluss
     README.md sine AUTO-GENERATED-tabellblokker) → IKKJE rediger direkte.
   - **Kjeldefiler** (resten, ca. 66 filer) → rediger direkte.
3. For kjeldefilene: erstatt `klassar` → `klasser` og `Klassar` → `Klasser`
   (to separate substitusjonar — stor og liten forbokstav — dekkjer både
   frittståande former og samansette ord som `hjelpeklassar`,
   `kjerneklassar`, `containerklassar`, `subklassar`, `aksjeklassar` osv.,
   sidan `klassar` alltid står **sist** i slike samansetjingar).
4. For dei 6 `*-manifest.yaml`-filene: identifiser den underliggjande
   `description:`/`title:`-teksten i respektive `*-schema.yaml` (alt retta
   i steg 3) og køyr `make gen-informasjonsmodell-instance SCHEMA=<sti>`
   for kvart av dei 5 råka skjemaa (jf. tabell) for å regenerere manifesta
   korrekt.
5. Køyr `make gen-begrepskatalog-instance` og `make gen-modellkatalog-instance`
   for å regenerere dei to aggregerte datafilene.
6. Køyr `make docs-publish` for å regenerere README.md sine tabellar (og
   samstundes stadfeste at mkdocs-portalen sine sider — inkl. den nye
   "Java-klassar"/"Python-klassar"-artefaktrada — no er konsekvente).
7. Verifiser: `grep -rniI "klassar" --exclude-dir=.git --exclude-dir=generated --exclude-dir=site --exclude-dir=node_modules .`
   skal ikkje gje treff utanfor `specs/done/`.
8. Køyr `make lint` for dei skjemaa som vart endra i steg 3 (samt-bu,
   ngr-adresse, referansemodell-*, modelldcat-katalog, dqv-core,
   fint-common, m.fl.) for å stadfeste at skildringsendringane ikkje braut
   noko.

## Handlingsliste

- [x] Steg 1: alle filer med `klassar`/`Klassar` utanfor `.git/`, `generated/`,
      `mkdocs/site/`, `node_modules/`, `specs/done/` identifiserte (74 ved
      case-sensitive søk, 4 fleire dukka opp ved eit case-insensitivt
      oppfølgingssøk, sjå Utført)
- [x] Steg 2: filene delte i autogenererte (7) vs. kjeldefiler
- [x] Steg 3: `klassar`→`klasser`/`Klassar`→`Klasser` i alle kjeldefiler
- [x] Steg 4: 5 `*-schema.yaml`-kjelder retta; dei 5 tilhøyrande
      `*-manifest.yaml`-filene retta med målretta tekstbyte (IKKJE full
      `gen-informasjonsmodell-instance`-regenerering, sjå Utført for kvifor)
- [x] Steg 5: `gen-begrepskatalog-instance` køyrt reint (regenererer frå
      `begrep/*.yaml`-kjelder, ingen `generated/`-avhengigheit);
      `gen-modellkatalog-instance` sitt output vart reverert og i staden
      retta med målretta tekstbyte i dei 2 råka filene (digdir/novari), sjå
      Utført
- [x] Steg 6: `make docs-publish` køyrt → README.md-tabellar og mkdocs-sider
      konsekvente («Java-klasser»/«Python-klasser»); verifisert reelt
      korrekt for samt/samt-bu etter `gen-schema-docs` +
      `analyse-lokal-modellanalyse-domene`
- [x] Steg 7: null attverande treff utanfor `specs/done/` stadfesta
      (case-insensitivt søk)
- [x] Steg 8: `make lint` grønt/uendra for alle råka skjema (attverande
      lint-åtvaringar i ngr-/fint-/referansemodell-skjema er
      førehandseksisterande, urelatert til denne endringa — stadfesta via
      diff-inspeksjon, ikkje via `git stash` sidan destruktive
      git-kommandoar er utanfor LLM sitt mandat, jf. CLAUDE.md)

## Utført

Gjennomført 2026-08-24. Kritisk lærdom undervegs, som endra metoden frå
det opphavlege steg 4/5 i denne specen:

**Full regenerering via `make gen-informasjonsmodell-instance`/
`gen-modellkatalog-instance` viste seg IKKJE trygt** — desse skripta les
`generated/<domain>/<name>/` (for `finnes_i_format`) og ALLE
`metadata/*-manifest.yaml` i repoet (for modellkatalog-aggregering).
Sidan det lokale arbeidstreet sin `generated/`-katalog og fleire manifest
var i eit ELDRE, ute-av-synk-tilstand (ikkje ein del av denne oppgåva),
førte full regenerering til STORE, urelaterte diff (t.d. 13 854 linjer i
`novari-modellkatalog.yaml`, 1 967 i `kartverket-modellkatalog.yaml`, tapt
`finnes_i_format`-innhald i fleire manifest). Dette vart oppdaga, reverert
med `git checkout --` (ikkje eit forbode kommando — reverterer arbeidstreet
til sist committa stand, ingen historieendring), og i staden retta med
presise `sed`-tekstbyte berre på dei linjene som faktisk inneheldt
`klassar` — same prinsipp som `erstatt-artefaktar-med-artefakter.md` sitt
punkt om å reversere utilsikta README-endringar.

**To bug i det første søket** vart oppdaga og retta undervegs:
1. `grep -vFf` (fixed-string) ekskluderte `README.md` som SUBSTRING, som
   utilsikta ekskluderte `src/mcp-linkml-modell-utkast/README.md` og
   `src/mcp-linkml-validator/policies/README.md` frå kjeldefil-lista.
2. Det første søket var case-sensitivt (berre lowercase `klassar`), som
   missa standalone `Klassar` (stor forbokstav, t.d. kommentaren
   `# Klassar` i `common-ap-no-schema.yaml`). Eit case-insensitivt
   oppfølgingssøk fann og retta 4 attverande filer.

**Ekstra funn (utanfor opphavleg spec-omfang, men direkte relevant):**
README.md sin handskrivne "Genererte artefakter"-tabell (ikkje del av
AUTO-GENERATED-blokka) mangla ei rad for `gen-java` — lagt til som
`| Java-klasser | ... |` rett etter GraphQL-rada, same feil som denne
oppgåva elles rettar («Java-klassar» vs. «Python-klasser»).

**Sluttresultat:** 75 filer endra, netto ~166 innsettingar/165 slettingar
(reint tekstbyte, ingen strukturelle endringar). Null attverande
`klassar`/`Klassar`-treff utanfor `specs/done/` og denne specen sjølv
(som medvite skal ha ordet ståande, som historisk dokumentasjon av
oppgåva). `make lint` uendra for alle råka skjema. Verifisert med reell
`make docs-publish`-køyring at mkdocs-portalen viser «klasser» konsekvent
for samt/samt-bu (representativt døme — dei andre domena sin lokale
`generated/`-katalog er framleis i eldre stand frå tidlegare økter, men
det er eit build-artefakt-spørsmål, ikkje eit kjeldekode-spørsmål: neste
reelle CI-bygg/`make <domain>`-køyring vil produsere korrekt output sidan
alle kjeldene no er retta).
