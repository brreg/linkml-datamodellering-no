# Evaluering: flytt domene-/skjema-dokumentasjonsgenerering (Steg 2) ut av `publish`-jobben

## Bakgrunn

Brukaren spør om innhaldsgenereringa per domene og skjema som i dag skjer
i `mkdocs/publish.sh` sitt **Steg 2** (kalla frå `make docs-publish`,
sjølve steget heiter "Generer innhald per domene og skjema (parallelt)",
sjå `.claude/rules/mkdocs-portal.md`) kan flyttast **inn i**
`generate`-matrisa i `.github/workflows/generate.yml` (éin gong per
domene, saman med `make domain-<domain>`) eller køyrast **parallelt
med** `generate`-matrisa, under føresetnaden at ein alt veit kva
`make generate`/`make domain-<domain>` skal produsere. Målet er å korte
ned totaltida for `generate.yml`.

Dette er ei **evaluering**, ikkje eit implementeringsoppdrag — ingen
filer under `.github/` er endra. Konklusjonen avgjer om, og eventuelt
korleis, arbeidet bør takast vidare.

Denne specen byggjer direkte på to eksisterande spesifikasjonar:
- `specs/backlog/reduser-generate-workflow-under-5min.md` — målt
  tidsfordeling for heile `generate.yml`, konkluderer at `make
  docs-build` (mkdocs-bygget sjølv, ~155 s / 40 % av heile workflowen)
  er den klart største, i hovudsak irreduserbare enkeltposten
- `specs/done/splitt-validering-modellanalyse-eigen-jobb.md` — flytta
  validering + domene-scopa modellanalyse **UT av** `generate`-jobben og
  inn i ei eiga parallell `valider-og-analyser`-jobb, nettopp for å
  unngå at desse la sekvensiell tid til domenejobben sin kritiske sti.
  Denne precedensen er direkte relevant: forslaget om å flytte Steg 2
  **inn i** `generate`-matrisa peikar i motsett retning av kva den
  specen konkluderte var rett.

## Metode

- Lest `mkdocs/publish.sh` (alle steg 1-3) og heile `mkdocs/lib/`
  (`copy_artifacts.sh`, `generate_index.sh`, `utils/*.sh`,
  `sections/*.sh`) for å kartleggje kva Steg 2 faktisk les og skriv.
- Lest `.github/workflows/generate.yml` og
  `.github/actions/{merge-generated-artifacts,generate-domain}/action.yml`
  for jobbgrafen og artefakt-flyten mellom jobbar.
- Henta faktiske jobb- og steg-tidsstempel for ei nyleg køyring
  (`gh run view 32734908418 --json jobs` og
  `gh api .../actions/jobs/<id>/logs`) for å måle kor mykje Steg 2
  faktisk kostar i dag, ikkje berre anta det.
- Kryssjekka import-grafen på tvers av domene
  (`grep`-basert oppslag av `imports:`-lister i alle `*-schema.yaml`)
  for å avgjere om Steg 2 har reelle cross-domain-avhengigheiter til
  **generert** innhald i andre domene, ikkje berre til kjeldeskjema.

## Funn 1 — kva Steg 2 faktisk kostar i dag

Frå køyring `32734908418` (2026-08-24, push-utløyst,
`feat(check-import-duplicates)`-commiten), `publish`-jobben:

| Steg | Tid |
|---|---|
| Steg 1 (README-tabellar, index.md, valideringsregler.md, cross-domain-modellanalyse-kopi, domene/skjema-oppdaging, metadata-oppslag) | 5,6 s |
| **Steg 2 (innhald per domene og skjema, parallelt)** | **26,9 s** |
| Steg 3 (mkdocs.yml) | 0,0 s |
| **`make docs-build` (sjølve mkdocs-bygget)** | **155,5 s** |
| Oppsett før `make docs-publish` (nedlasting, artefakt-samanslåing, site-cache-sjekk, crun/GHCR/image-pull) | ~23 s |

Steg 2 — objektet for denne evalueringa — utgjer **26,9 sekund av ein
total workflow-tid på 6-7 minutt**, altså under 10 %. Til
samanlikning: `make docs-build` åleine er **~6× så stort**. Dette
avgrensar kor mykje ei flytting av Steg 2 i det heile kan gje, uansett
korleis flyttinga vert gjennomført.

## Funn 2 — Steg 2 har ei reell cross-domain-avhengigheit til GENERERT innhald i andre domene

Føresetnaden i spørsmålet ("under forutsetning av at vi veit kva
make:generate skal produsere") held **ikkje fullt ut**. Kartlegginga
fann éin konkret stad der Steg 2 les **innhaldet** av eit anna domene
sin `generate`-jobb-output, ikkje berre kjeldeskjemaet:

`mkdocs/lib/sections/classes.sh` (`build_import_links()`, line 67) les
`generated/${imported_domain}/${imported_clean}/docs/index.md` — den
**gen-doc-genererte** Markdown-fila til eit importert skjema — for å
avgjere om det importerte skjemaet faktisk har **lokale definisjonar**
i kvar seksjon (Classes/Slots/Enumerations/Types/Subsets), før det
viser ei "Importerte klasser: …"-lenkje. Dette krev at det importerte
skjemaet sin `generate`-jobb alt har køyrt til fullført gen-doc-output —
ikkje berre at ein veit kva **filer** som kjem, men kva **innhald**
(klassetal, "Defined in"-kolonne) dei faktisk får.

Kor ofte skjer dette på tvers av domene? Eit repo-vidt oppslag av
`imports:`-lister mot kva domene kvart importerte skjema høyrer til,
viser at dette er **strukturelt, ikkje eit sjeldan unntak**:

| Domene | Importerer frå `ap-no`-domenet |
|---|---|
| `begrepskatalog` | `skos-ap-no-schema` |
| `modellkatalog` (6 skjema) | `modelldcat-ap-no-schema` |
| `oreg` (7 skjema) | `dcat-ap-no-schema` |
| `referanse` | `dcat-ap-no-schema` |
| `samt` | `dqv-ap-no-schema` |

**7 av 9 domene** (alle unnateke `ap-no` sjølv og `fint`, som berre
importerer sin eigen `fint-common-schema`) importerer frå `ap-no`. Dette
er sjølve poenget med importhierarkiet (PRINCIPLES.md § 3 — AP-NO-
profilane er meint å gjenbrukast på tvers av domene), så det er ikkje
noko som kan reduserast/omgåast utan å endre modelleringsprinsippa.

**Konsekvens:** Steg 2 for dei 7 avhengige domena kan **ikkje** trygt
byrje før `ap-no` sin `generate`-jobb er ferdig. Ei flytting av Steg 2
inn i **kvar enkelt** `generate`-matrisejobb (slik at t.d. `oreg` sin
eigen jobb genererer sine eigne docs rett etter `make domain-oreg`) vil
i beste fall gje feil "Importerte klasser"-lenkjer for desse 7 domena
(bygd mot eit `ap-no`-generated-tre som endå ikkje finst, eller finst i
ein eldre/delvis tilstand) dersom `ap-no` sin jobb ikkje tilfeldigvis er
ferdig først — noko det **ikkje** finst nokon garanti for i ei
`fail-fast: false`-matrise der alle domene startar samstundes.

## Funn 3 — kvifor "kombiner med `generate`- eller `valider-og-analyser`-jobben" går imot ein alt etablert konklusjon

`specs/done/splitt-validering-modellanalyse-eigen-jobb.md` vurderte
eksplisitt om validering + modellanalyse skulle køyre i **same jobb**
som `generate` (bakgrunnsprosessar på tvers av steg-grensa, "Tiltak 2"
der) og **avviste** det — dels fordi teknikken (prosessar som overlever
steg-grensa i GitHub Actions) er uprøvd i dette repoet og utgjer ein
alvorleg regresjonsrisiko for ei hard byggjesperre, dels fordi ei
**eiga jobb** (ikkje kombinert) gjev reinare feilsemantikk og alt
verifisert GitHub Actions-native parallellitet.

Å no foreslå å flytte Steg 2 **inn i** `generate`-jobben (eller
`valider-og-analyser`) ville gjeninnføre nett det mønsteret den specen
avviste — pluss at det ikkje løyser cross-domain-avhengigheita i Funn 2.
Det finst ingen ny informasjon i denne evalueringa som endrar den
tidlegare konklusjonen.

## Vurderte design-alternativ

**1. Slå saman `generate` + `valider-og-analyser` + Steg 2 til éi jobb
per domene.** *Avvist* — motseier Funn 3, løyser ikkje Funn 2
(cross-domain-avhengigheita finst uansett kva jobb Steg 2 køyrer i).

**2. Eiga ny parallell matrise-jobb `domene-dokumentasjon` per domene,
`needs:` heile `generate`-matrisa (alle domene, ikkje berre eige) +
`valider-og-analyser` for eige domene.** Mekanisk trygt (løyser Funn 2
ved å vente på alt), men gjev truleg **null eller negativ** gevinst:
- Steg 2 køyrer alt internt parallelt (alle ~50 skjema på tvers av alle
  domene, 26,9 s totalt) via bakgrunnsprosessar i éin jobb — å splitte
  dette over 9 jobbar sparer ikkje noko dersom kvar ny jobb har eige
  faste oppsettkostnad (nedlasting av `source` + alle 9×2
  `generated-<domain>`/`-checks`-artefakt, sidan cross-domain-sjekken i
  Funn 2 krev heile treet, ikkje berre eige domene).
- 9 nye jobbar × nedlasting av **heile** det samanslegne
  `generated/`-treet kvar (i staden for éin nedlasting i dagens
  `publish`-jobb) er meir total I/O, ikkje mindre.
- Same "jobb-oppsett-overhead kan ete opp gevinsten"-risiko som
  `splitt-validering-modellanalyse-eigen-jobb.md` eksplisitt flagga for
  éin ny jobb per domene — her multiplisert med at kvar av dei 9 nye
  jobbane også må laste ned alt.

**3. To-nivå/hub-basert staging** — sidan `ap-no` er den einaste
cross-domain-avhengigheita i dag (jf. tabellen i Funn 2), kunne ein i
teorien late `ap-no` sin `generate`+docs køyre fyrst, og dei 8 andre
domena sin Steg 2 vente berre på (eige domene + `ap-no`), ikkje på
kvarandre. *Vurdert, ikkje tilrådd no*: i den målte køyringa
(Funn 1) er `ap-no` **sjølv det tregaste domenet** i `generate`-matrisa
(01:34, seinare enn alle andre inkl. det historisk trege `oreg`, som
sidan er optimalisert i `reduser-generate-workflow-under-5min.md`
tiltak 2/relatert endring). Gevinsten av denne staginga er difor **heilt
avhengig av at `ap-no` ikkje er det tregaste domenet** — noko som kan
endre seg over tid etter kvart som `build.yaml`-generatorflagg og
skjemastorleik endrar seg, og som må re-målast før kvar vurdering. Lagt
attpå dette kjem vesentleg kompleksitet: `discover-domains`-actionen
(brukt av 4+ delar av pipelinen, jf. tiltak 2-vurderinga i
`reduser-generate-workflow-under-5min.md`) må utvidast med eit
hub/leaf-omgrep. For ei gevinst som i beste fall er nokre av dei 26,9
sekunda Steg 2 alt bruker, er dette ikkje verdt kompleksiteten no.

**4. La Steg 1 sine domene-uavhengige delsteg (README-tabellar,
`index.md` frå `README.md`, `valideringsregler.md`) køyre i den alt
eksisterande `modellanalyse-tvers-domene`-jobben** (som alt berre treng
`checkout-source` og ikkje noko frå `generate`-matrisa) **i staden for
i `publish`-jobben.** Dette er trygt — desse tre funksjonane
(`write_index_from_readme`, `generate_validation_docs`,
`generate-readme-tables.sh`) les kun `README.md`,
`src/mcp-linkml-validator/policies/README.md` og statiske filer, ingen
`generated/`-avhengigheit. Estimert gevinst: **~5-6 s**, målt direkte i
Funn 1. Låg risiko, låg verdi — kosmetisk mikrotiltak, ikkje ei
strukturell forbetring.

## Tilråding

**Ikkje implementer alternativ 1-3.** Dei bryt anten ein alt etablert
arkitekturvalg (Funn 3) eller føreset noko som ikkje held (Funn 2), og
i alle tilfelle er den **maksimalt** oppnåelege gevinsten (Steg 2 sine
26,9 s, jf. Funn 1) liten samanlikna med kompleksiteten/risikoen dei
introduserer.

**Alternativ 4 kan takast med som eit uavhengig mikrotiltak** dersom
det gjerast, men bør ikkje prioriterast åleine — 5-6 s monar lite.

**Den faktiske høgverdi-målsettinga står uendra i
`specs/backlog/reduser-generate-workflow-under-5min.md`:** `make
docs-build` (155 s, 40 % av heile workflowen) er framleis den einaste
posten stor nok til å gje merkbar reduksjon. Den specen sitt tiltak 1
(site-cache på `mkdocs/site/`, nøkla på **input** i staden for output)
er alt implementert, men **ikkje verifisert i faktisk CI-køyring** — det
er den naturlege neste handlinga, ikkje denne evalueringa sine
alternativ. For køyringar med reelt innhaldsendring (der site-cachen
bommar per design) står tiltak 2 (profilert `oreg`-splitting, ikkje
implementert) og dei eksplisitt utsette tiltak 4/5 (søk-innsnevring,
mkdocs-sharding) att som einaste vidare handlingsrom.

## Handlingsliste

- [ ] Avklar med brukaren om alternativ 4 (Steg 1 sine
      domene-uavhengige delsteg inn i `modellanalyse-tvers-domene`-jobben)
      skal implementerast som eige, isolert mikrotiltak, gitt den vesle
      gevinsten (~5-6 s)
- [ ] Elles: ingen kodeendring frå denne specen — heldigheita/verdien i
      å arbeide vidare med `reduser-generate-workflow-under-5min.md`
      (verifisere tiltak 1 i CI, vurdere tiltak 2) bør prioriterast
      framfor alternativa evaluerte her

## Akseptansekriterium

- [x] Kartlagt kva Steg 2 faktisk les/skriv (kjeldetre vs. `generated/`)
- [x] Målt faktisk tidskostnad for Steg 1/2/3 og `docs-build` i ei
      reell CI-køyring
- [x] Identifisert og dokumentert den konkrete cross-domain-
      generert-innhald-avhengigheita som avgrensar handlingsrommet
      (`classes.sh` sin `build_import_links()`)
- [x] Vurdert alternativ 1-4 med eksplisitt grunngjeving, kryssreferert
      mot dei to relevante eksisterande spesifikasjonane
- [x] Konklusjon/tilråding skriven — **inga implementering utført**,
      denne specen er ei evaluering brukaren skal ta stilling til

## Relaterte filer

- `mkdocs/publish.sh` — Steg 1/2/3, objektet for evalueringa
- `mkdocs/lib/sections/classes.sh` — `build_import_links()`, kjelda til
  cross-domain-avhengigheita i Funn 2
- `mkdocs/lib/scripts/collect-schema-metadata.py`,
  `mkdocs/lib/utils/imported_schemas.sh` — kjeldetre-baserte oppslag
  (domene-uavhengige, billige, ikkje ei avgrensing)
- `.github/workflows/generate.yml` — `generate`, `valider-og-analyser`,
  `modellanalyse-tvers-domene`, `publish`-jobbane
- `specs/backlog/reduser-generate-workflow-under-5min.md` — målt
  tidsfordeling, `docs-build`-kostnaden, site-cache-tiltaket (tiltak 1,
  implementert/ikkje verifisert)
- `specs/done/splitt-validering-modellanalyse-eigen-jobb.md` —
  precedens for kvifor jobb-samanslåing (alternativ 1) er avvist
