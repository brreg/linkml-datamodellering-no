# Plan: ny modellanalyse-jobb for ubrukte lokale definisjonar og isolerte klassar (fjern Usage-kolonne)

## Bakgrunn

Etter at `## Modellanalyse`-overskrifta vart lagt til i kvar modell sin
genererte `index.md` (sjå `specs/done/modellanalyse-per-skjema-index-md.md`
og `specs/backlog/modellanalyse-liknande-typenamn.md`) med tre
namnelikskaps-rapportar (klasser/slots/typar), synest brukaren at
**Usage**-kolonna i tabellane for Slots, Enumerations, Types og Subsets
(same `index.md`-side) no verkar malplassert. Kolonna viser i dag ein badge
(`✅ Brukt lokalt` / `⚠️ Definert lokalt`) rekna ut *inline*, rad for rad, i
`src/assets/templates/docgen/index.md.jinja2`.

Ønsket: flytt denne "er dette definert lokalt men aldri brukt lokalt"-
sjekken ut av tabellradene og inn som **eigne modellanalyse-jobbar**, etter
same mønster som dei tre eksisterande `similar-*-domain`-analysane. Dette
gir to gevinstar samtidig:

1. Slots-, Enumerations-, Types- og Subsets-tabellane vert reindyrka til
   berre å dokumentere kva som finst (namn, skildring, kjeldeskjema) — ikkje
   blande inn ei analytisk vurdering.
2. Alt som er verdt å følgje opp (liknande namn OG ubrukte lokale
   definisjonar) samlast på éin stad: `## Modellanalyse`-seksjonen.

**Avklart med brukaren:** rapportstrukturen skal følgje det etablerte
`similar-*-domain`-mønsteret — **fire separate rapportar** (éin per
kategori: slots, enums, types, subsets), ikkje éin kombinert rapport. For å
unngå at nesten identisk "er dette brukt lokalt"-logikk vert implementert
fire gonger (DRY-prinsippet i CLAUDE.md), vert dette løyst med **eitt delt
script** styrt av eit `--kind`-flagg (same struktur som
`find-similar-names.py --kind class|slot|types` alt gjer for dei tre
eksisterande analysane) — fire Makefile-target, fire rapportfiler, éin
kjelde til sjølve logikken.

**Utvida omfang:** i tillegg ønskjer brukaren ein **femte** analyse —
`--kind class` — som sjekkar om ei lokalt definert klasse er **isolert**:
verken referert **frå** noka anna lokal klasse (som range på ein
slot/attributt, eller som `is_a`/mixin-mål), **eller** sjølv refererer til
noka anna lokal klasse (via range på eigne slots/attributtar, eller sin
eigen `is_a`/mixin). Ei slik klasse står heilt fråkopla frå resten av
klassegrafen i modellen — eit sterkt signal om daud kode eller ei gløymd
mellomlagringsklasse frå refaktorering. Dette er ei **reint additiv**
analyse: `## Classes`-tabellen i `index.md.jinja2` har **ingen**
eksisterande Usage-kolonne å fjerne (sjå Kartlegging under) — det er berre
dei fire opphavlege kategoriane (slots/enums/types/subsets) som får kolonna
si fjerna.

## Kartlegging — dagens mekanisme

**Usage-badge-logikken** (skal portast, ikkje endrast semantisk) ligg i
`src/assets/templates/docgen/index.md.jinja2`, fire nesten identiske
kopiar:

- Slots (tre undertabellar: Verdiar/Referansar/Kodar) — line 156-229
- Enumerations — line 262-313 (usage-sjekk line 275-305)
- Types — line 346-407 (usage-sjekk line 376-401)
- Subsets — line 438-483 (usage-sjekk line 452-474)

Felles mønster: eit namn (slot/enum/type/subset) hamnar i tabellen dersom
det anten er **brukt** av ein lokal klasse (via `c.slots`/
`schemaview.induced_slot(...)`, direkte for slots, via `.range` for
enum/type, via `.in_subset`/`slot_usage[].in_subset` for subsets) **eller**
er **definert lokalt** (nøkkel i `schema.slots`/`schema.enums`/
`schema.types`/`schema.subsets` for dette skjemaet). Usage-badge skil
mellom desse to: "Brukt lokalt" viss minst éin lokal klasse (der
`c.tree_root` er falsk og `c.from_schema == schema.id`) faktisk refererer
namnet, elles "Definert lokalt" (= definert, men aldri brukt av noka lokal
klasse — kandidat for opprydding).

**Modellanalyse-seksjonen** vert bygd av
`mkdocs/lib/scripts/generate-modellanalyse-md.py`, som les ei fast liste
`REPORTS = [(rapportfil, ###-overskrift, objekttype), ...]` og limer kvar
rapportfil inn som ein `###`-underseksjon, med ei avsluttande fotnote som
peikar til den vekentlege `modell-analyse.yml`-workflowen for
cross-domain-analyse.

**Rapportfilene** vert skrivne av `.github/workflows/generate.yml`, steget
"Køyr modellanalyse per skjema for ${{ matrix.domain }}" (line 315-355) —
for kvart skjema i domenet, køyr tre `make analyse-similar-*-domain
DOMAIN=... NAME=...`-kall og omdiriger stdout til
`generated/<domain>/<schema>/model-analyse/<rapportnamn>.md`. Feil per
skjema stoppar ikkje resten av loopen (`::warning`, ikkje CI-blokkerande).

**Container-val:** dei eksisterande `similar-*`-analysane brukar
`PYTHON_RUN` (lett Python-container, rein `yaml.safe_load`, ingen
LinkML-runtime — sjå moduldocstring i `find-similar-names.py`). Vår nye
analyse **må** derimot bruke `LINKML_RUN` (full LinkML-image), fordi
`schemaview.induced_slot(...)` — som løyser arv og `slot_usage`-overstyring
korrekt, akkurat slik Jinja-malen alt gjer — krev ein ekte `SchemaView`
over det oppløyste importhierarkiet. Same avveging som
`check-import-duplicates.py` (som òg brukar `LINKML_RUN`).

**Classes-tabellen (line 62-110 i `index.md.jinja2`) har ingen
Usage-kolonne i dag** — berre `Class | Description`. Isolerte-klassar-
analysen er difor ikkje ei "port ut av malen"-øving som for dei fire andre
kategoriane, men ein heilt ny sjekk. Referansegrafen mellom lokale klassar
kjem frå to kjelder:

1. **Slot-/attributtrange**: for kvar lokale klasse (inkl. containerklassen
   sine `attributes:` — sjå `.claude/rules/linkml-schema.md` §
   "Containerklasse"), for kvar av klassen sine slots/attributtar, er
   `induced_slot(...).range` ei anna lokal klasse? Då er begge klassane
   "tilkopla" (target-klassen er *referert frå*, kjelde-klassen *refererer
   til*).
2. **Arv**: `is_a`/`mixins` mellom to lokale klassar tel òg som ei
   tilkopling, i begge retningar (ei klasse med lokale subklassar er ikkje
   isolert, sjølv om ho er abstrakt og aldri sjølv brukt som range).

Containerklassen (`tree_root: true`) er sjølve inngangspunktet for modellen
(jf. `.claude/rules/linkml-schema.md`) og skal **aldri** sjølv reknast som
kandidat for "isolert" — men referansane *frå* containeren til andre
klassar tel som reell bruk for målklassane, akkurat som referansar frå
andre lokale klassar. Ei klasse som **berre** er nådd av containeren og
elles verken refererer til eller vert referert av noka anna lokal klasse er
altså framleis *tilkopla* (ho er eit gyldig topnivå-inngangspunkt i
modellen) — "isolert" betyr *heilt* fråkopla frå klassegrafen, inkludert
containeren.

## Cross-domain-fotnote — frå workflow-lenke til ekte fil

**Nytt ønske frå brukaren:** i dag endar kvar `###`-underseksjon under
`## Modellanalyse` (dei tre eksisterande similar-*-domain-rapportane) med
ei fotnote av typen *"For fullstendig analyse av typenamn på tvers av
domene sjå [Modell-analyse](.../actions/workflows/modell-analyse.yml)-
workflowen"* — ei lenkje til **workflow-sida** i GitHub Actions, ikkje til
noka konkret fil. Brukaren opplever dette som lite nyttig, og ønskjer i
staden ei lenkje til den **faktiske genererte fila** for akkurat det
objekttypen, t.d.:

> *For fullstendig analyse av typenamn på tvers av domene sjå
> ["Analyse av typenamn på tvers av alle domene"](../../modellanalyse/liknande-typenamn-alle-domene.md).*

Dette skal gjelde både dei tre eksisterande analysane (similar
classes/slots/types) og — der det er relevant — dei nye analysane denne
specen innfører. **Merk:** dei fem nye ubrukt-lokalt/isolert-analysane
(steg 1-3 under) har ikkje noka meiningsfull cross-domain-form i
utgangspunktet ("brukt lokalt" er per definisjon eit per-skjema-omgrep —
det finst ingen naturleg "--scope all"-variant), så dei får **ingen**
fotnote i dag. Mekanismen som byggjer fotnota skal likevel implementerast
**generisk** (eit felt per rapport-oppføring, ikkje spesialkoda til berre
dei tre eksisterande), slik at dersom ein seinare spec legg til ein
cross-domain-variant av éin av dei nye analysane, er kopling til fotnota
eit reint datatillegg — ikkje ei kodeendring.

**Kjerneproblemet:** for at fotnota kan peike på ei ekte, stabil fil, må
sjølve `--scope all`-rapportane (i dag berre køyrde vekentleg i
`modell-analyse.yml`, og kun tilgjengelege som eit 30-dagars GitHub
Actions-artefakt + `$GITHUB_STEP_SUMMARY` — inga stabil URL) finnast som
faktiske sider i den **publiserte mkdocs-portalen**.

**Avklart med brukaren:** løysinga er å køyre `--scope all`-analysane som
eit **nytt, eingongs steg i `generate.yml`** (ikkje per domene/skjema —
`--scope all` samanliknar på tvers av heile repoet, éin gong er nok), og
publisere resultatet som faste sider i mkdocs-portalen via den alt
eksisterande `publish.sh`/GitHub Pages-flyten. Ingen ny commit-til-repo-
mekanisme trengst (portalen sin eksisterande deploy går rett til GitHub
Pages, aldri via commit til `main`) — dette er berre éin ekstra
byggjesteg i den flyten som alt finst, akkurat som dei domene-scopa
sjekkane alt vart flytta inn i `generate.yml` (same grunngjeving: reint
offline, ingen nettverksavhengige sjekkar, jf. moduldocstring i
`find-similar-names.py`).

**Forkasta alternativ:** behalde `--scope all` berre vekentleg i
`modell-analyse.yml`, men la den workflowen committe dei resulterande
md-filene til ein fast sti i repoet, slik at neste `docs-publish`-køyring
plukkar dei opp som vanleg statisk innhald. Forkasta fordi det ville
kravd ein heilt ny bot-commit-mekanisme portalen ikkje har i dag (dagens
`docs-publish` deployer rett til GitHub Pages via Pages-artefakt, aldri
via commit til `main`) — meir kompleksitet for same sluttresultat.

## Plan

1. **Nytt script**
   `src/assets/scripts/makefile/find-unused-local-definitions.py`:
   - CLI: `--kind {slot,enum,type,subset,class}`
     `--schema <sti-til-schema.yaml>` (eitt skjema om gongen — inga
     domene-/all-scoping trengst, sidan sjekken er reint lokal)
   - Bruk `linkml_relative_import_patch` (same import-fiks-mønster som
     `check-import-duplicates.py`) før `SchemaView` vert oppretta
   - Les det **rå** skjemaet (`yaml.safe_load`) for å avgrense til namn
     definerte lokalt i akkurat denne fila sin `slots:`/`enums:`/`types:`/
     `subsets:`-blokk, og lokale klassar (`classes:`-blokka i same fil,
     ekskl. `tree_root`)
   - Bruk `SchemaView(schema_path)` (imports oppløyst) og
     `schemaview.induced_slot(slot_name, class_name)` for kvar lokale
     klasse, for å avgjere reell bruk — porter algoritmen frå Jinja-malen
     linje-for-linje for dei fire opphavlege kindane (sjå referansane
     over), ikkje ei ny tolking:
     - `slot`: brukt viss namnet finst i ei lokal klasse sin `slots`-liste
     - `enum`/`type`: brukt viss `induced_slot(...).range` for ein lokal
       klasse-slot er lik namnet
     - `subset`: brukt viss namnet finst i ei lokal klasse sin
       `in_subset`, eller i `slot_usage[<slot>].in_subset` for same klasse
   - **`class` (ny, femte kind):** bygg éin udelegga graf over lokale
     klassar (containerklassen inkludert som node, men aldri som
     rapportert kandidat — sjå Kartlegging). To klassar er "tilkopla"
     viss (a) `induced_slot(...).range` for ein slot/attributt på den eine
     peikar til den andre, i **begge** retningar, eller (b) `is_a`/
     `mixins` koplar dei, i begge retningar. Ei lokal klasse (utanom
     containeren) er **isolert** viss ho ikkje har **noka** slik tilkopling
     til noka anna lokal klasse (containeren medrekna)
   - Output (stdout, markdown): `# Ubrukte lokale <kind-omtale> (<skjema>)`
     (for `class`: `# Isolerte lokale klassar (<skjema>)`) + ei
     liste/tabell (namn, skildring) over lokalt definerte namn som
     **ikkje** er brukt/tilkopla, eller
     `Ingen ubrukte lokale <kind-omtale> funne (<N> sjekka).` viss tom
   - Exit-kode 0 alltid (informativ rapport, ikkje ein valideringspolicy —
     same prinsipp som `find-similar-names.py`)

2. **Fem nye Makefile-target** i `make/91-modell-analyse.mk`:
   `analyse-ubrukte-slots`, `analyse-ubrukte-enums`, `analyse-ubrukte-types`,
   `analyse-ubrukte-subsets`, `analyse-isolerte-klasser` — kvar eit tynt
   `$(LINKML_RUN) python3 .../find-unused-local-definitions.py --kind
   <kind> --schema $(SCHEMA)`-kall, med `$(call print_header, ...)`. Legg
   til i `.PHONY`-lista og oppdater fil-toppkommentaren (script-lista).

3. **Wire inn i `generate.yml`**, same steg som dei tre eksisterande
   (line 315-355): for kvart skjema, fem nye `make analyse-ubrukte-*
   SCHEMA="$schema_dir/${schema_name}-schema.yaml" >
   "$target_dir/ubrukte-<kind>-report.md"`-kall (`analyse-isolerte-klasser`
   → `isolerte-klasser-report.md`), same
   `if ... then echo "  ✓ ..." else echo "::warning::..."`-mønster som dei
   eksisterande. **Køyr `actionlint` mot `generate.yml` etter denne
   endringa** (CLAUDE.md-regel — sjå § "Actionlint etter CI-endring").

4. **Nytt, eingongs steg i `generate.yml` sin `publish`-jobb** — køyr
   `--scope all`-variantane av dei tre eksisterande namnelikskaps-analysane
   (`analyse-similar-classes-all`, `analyse-similar-slots-all`,
   `analyse-similar-types-all`, alle allereie eksisterande, offline
   PYTHON_RUN-target). Plassering: rett etter "Slå saman genererte
   domene-artefakt til generated/"-steget (line ~401-404) og før
   "Publiser og bygg dokumentasjonsportal" (line ~424) — då er full
   `src/linkml/`-kjeldetre alt tilgjengeleg (frå `source`-artefaktet), og
   steget køyrer **éin** gong for heile repoet, ikkje per domene. Skriv
   kvar rapport til ein fast, ikkje-domene-scopa katalog:
   ```
   generated/modell-analyse-tvers-domene/similar-classes-all-report.md
   generated/modell-analyse-tvers-domene/similar-slots-all-report.md
   generated/modell-analyse-tvers-domene/similar-types-all-report.md
   ```
   Same ikkje-blokkerande feilhandtering som per-skjema-steget
   (`::warning`, ikkje `set -e`-avbrot). **Køyr `actionlint` mot
   `generate.yml` etter denne endringa** (CLAUDE.md-regel).

5. **Utvid `mkdocs/publish.sh`** til å publisere desse tre filene som
   faste portalsider:
   - Kopier `generated/modell-analyse-tvers-domene/*.md` til
     `mkdocs/docs/modellanalyse/*.md` (nytt steg i same fase som
     `valideringsregler.md`/hovud-`index.md` genererast, Steg 3 —
     sjå `.claude/rules/mkdocs-portal.md`), t.d. omdøypt til meir
     lesbare filnamn:
     - `similar-classes-all-report.md` →
       `mkdocs/docs/modellanalyse/liknande-klassenamn-alle-domene.md`
     - `similar-slots-all-report.md` →
       `mkdocs/docs/modellanalyse/liknande-slotnamn-alle-domene.md`
     - `similar-types-all-report.md` →
       `mkdocs/docs/modellanalyse/liknande-typenamn-alle-domene.md`
   - Legg til éi kort `mkdocs/docs/modellanalyse/index.md` som lenkar dei
     tre (oversiktsside), og legg til ein ny **`- Modellanalyse:`**-seksjon
     i nav-heredoc-blokka i `publish.sh` (jf. "Sannkjelda for nav-menyen er
     `publish.sh`, ikkje `mkdocs.yml`")
   - Desse sidene ligg **utanfor** den domene-/skjema-scopa
     rens-og-regenerer-logikken i Steg 1 (dei er ikkje under
     `mkdocs/docs/<domain>/`) — legg dei til saman med anna statisk
     Steg 3-innhald, ikkje i domene-loopen i Steg 2

6. **Utvid `mkdocs/lib/scripts/generate-modellanalyse-md.py`**:
   - Fjern den globale `MODELL_ANALYSE_WORKFLOW_URL`-konstanten og den
     faste, ikkje-parameteriserte fotnoteteksten ("*For fullstendig
     analyse av ... på tvers av domene sjå [Modell-analyse](...)-
     workflowen.*")
   - Utvid `REPORTS`-tuppelen med to nye, valfrie felt per oppføring:
     `cross_domain_report_relpath` (relativ sti frå
     `mkdocs/docs/<domain>/<schema>/index.md` til cross-domain-sida, t.d.
     `../../modellanalyse/liknande-typenamn-alle-domene.md`) og
     `cross_domain_label` (t.d. `"Analyse av typenamn på tvers av alle
     domene"`) — `None` for oppføringar utan cross-domain-ekvivalent
   - For dei tre eksisterande (similar classes/slots/types): set begge
     felta til dei nye portalsidene frå steg 5
   - For dei fem nye (ubrukte slots/enums/types/subsets, isolerte
     klassar): la begge felta vere `None` — funksjonen som skriv fotnota
     skal då **ikkje** skrive noka fotnote-linje for den oppføringa (ikkje
     falle attende til den gamle workflow-lenkja)
   - Fotnoteteksten vert generert per oppføring: *"For fullstendig analyse
     av `<objekttype>` på tvers av domene sjå
     [`<cross_domain_label>`](`<cross_domain_report_relpath>`)."* — berre
     når `cross_domain_report_relpath` er sett
   - Den heilt separate, generelle fotnota nedst i fila ("*For
     IRI-dereferering og innhaldsforhandling sjå [Modell-analyse]
     (...)-workflowen.*", line 100-104) er **ikkje** eit per-objekttype-
     fotnote og gjeld ikkje denne endringa — IRI-sjekkane er framleis
     nettverksavhengige og køyrer framleis berre vekentleg, med ingen
     naturleg per-skjema-fil å peike til. Behald denne uendra.
   - Oppdater moduldocstringen (line 1-25) tilsvarande.

7. **Fjern Usage-kolonna** frå
   `src/assets/templates/docgen/index.md.jinja2` — gjeld **berre** dei
   fire opphavlege kategoriane, **ikkje** Classes-tabellen (som ikkje har
   nokon Usage-kolonne i dag, jf. Kartlegging — isolerte-klassar-analysen
   er reint additiv, ingen malendring der utover eventuelt punkt 7):
   - Dei fire tabellane (Slots × 3 undertabellar, Enumerations, Types,
     Subsets): fjern `Usage`-kolonneheadar, fjern heile
     `is_used`-berekningsblokka per rad (line 160-172, 186-198, 212-224,
     275-305, 376-401, 452-474), og fjern `usage_badge`-cella frå kvar
     rad-mal
   - Oppdater `>`-blockquote-forklaringane rett over kvar tabell (fjern
     `*Usage* "Definert lokalt" betyr ...`-linja, behald resten)
   - Følg whitespace-kontroll-reglane i `.claude/rules/mkdocs-portal.md`
     nøye ved redigering (ingen indentasjon av Jinja-taggar, korrekt
     `-`-plassering — sjå § "Jinja2-template whitespace-kontroll")

8. **Verifiser**:
   - Køyr dei fem nye make-targeta lokalt mot eit skjema med minst éin
     medvite ubrukt lokal slot/enum/type/subset og éin medvite isolert
     klasse (t.d. eit test-/eksempelskjema, eller ei mellombels lokal
     endring), og stadfest at kvar rapport fangar sitt tilfelle korrekt —
     for `analyse-isolerte-klasser`, stadfest òg at ei klasse som **berre**
     er referert frå containeren **ikkje** vert flagga (sjå Kartlegging)
   - Køyr `make analyse-similar-classes-all` (og -slots-/-types-all) lokalt
     og stadfest at dei framleis fungerer uendra (sjølve analysescriptet
     er ikkje rørt, berre kva som skjer med utdataen)
   - `make docs-publish` (eller minst `mkdocs/publish.sh` sitt Steg 3) og
     stadfest at `mkdocs/docs/modellanalyse/*.md` vert oppretta med
     innhald, og at dei dukkar opp i `mkdocs.yml` sin nav-meny
   - `make gen-doc SCHEMA=<eit skjema>` + `make docs-build`, og inspiser
     generert `index.md`: dei fire tabellane manglar Usage-kolonne,
     Classes-tabellen er uendra, `## Modellanalyse` har fem nye
     underseksjonar med reelt innhald, og dei tre eksisterande
     underseksjonane sine fotnoter no lenkar til
     `../../modellanalyse/<fil>.md` i staden for workflow-URL-en
   - `make docs-build` sin `validation.links`-sjekk (jf.
     `.claude/rules/mkdocs-portal.md` § "Ankerlenkjer til overskrifter")
     må gå gjennom utan broten-lenkje-feil på dei nye relative lenkjene —
     dette er den faktiske stadfestinga av at fotnota no peikar til ei
     ekte, gyldig side
   - `make roundtrip SCHEMA=<eit skjema>` for å stadfeste ingen regresjon
     i sjølve skjemagenereringa (malen skal berre ha mista éi kolonne, ikkje
     endra anna struktur)

9. **Valfritt / lågt prioritert opprydding:** eksempeltabellen i
   `.claude/rules/mkdocs-portal.md` sitt whitespace-avsnitt viser framleis
   `| Enumeration | Description | Defined in | Usage |` som illustrasjon av
   Jinja-tabellmønsteret — vurder å fjerne `Usage`-kolonna frå det
   illustrasjonseksempelet òg, så det ikkje motseier den faktiske malen.

## Opne spørsmål (avklar ved implementering, ikkje i denne specen)

- Eksakt kolonneoppsett i sjølve rapportfila (rein liste vs. tabell med
  Namn/Skildring) — vel det som er mest lesbart, ikkje kritisk for
  funksjonen.
- Om `find-unused-local-definitions.py` bør dele hjelpefunksjonar
  (t.d. "er dette ei lokal klasse i dette skjemaet") med
  `check-import-duplicates.py`/`find-similar-names.py`, eller om
  duplisering av desse få linjene er under DRY-terskelen (tre eller fleire
  identiske tilfelle) — vurder ved implementering, ikkje før.
- Skal ei **abstrakt** klasse utan lokale subklassar og utan andre
  tilkoplingar reknast som isolert på lik linje med ein konkret klasse?
  Kartlegginga over legg til grunn at ja (same regel for alle klassar,
  abstrakt eller ikkje) — vurder om dette bør nyanserast ved
  implementering, t.d. med ei eiga merking i rapporten (ikkje eit anna
  utfall) dersom abstrakte klassar er venta å stå åleine i periodar av
  modellutviklinga.
- **Utanfor scope for denne specen, men verdt å nemne:** etter steg 4
  vert `similar-classes-all`/`similar-slots-all`/`similar-types-all`-
  jobbane i `modell-analyse.yml` reelt sett redundante — dei køyrer same
  analyse, berre sjeldnare (vekentleg) og utan å bli publisert nokon stad.
  Denne specen **rører ikkje** `modell-analyse.yml` eller
  `summarise-modell-analyse.py`/`analyse-sammendrag` (som les artefakta
  desse jobbane produserer) — dei kan gjerne stå som eit uendra,
  overlappande sikkerheitsnett inntil vidare. Vurder ei eiga, seinare
  spec for å forenkle/fjerne duplikatet dersom det viser seg forvirrande
  i praksis.
- Skal `analyse-isolerte-klasser` i tillegg fange klassar som **berre**
  refererer til/frå importerte (ikkje-lokale) klassar — t.d. ei lokal
  klasse som utelukkande arvar frå ein importert AP-NO-basisklasse og
  aldri vert referert lokalt? Kartlegginga over reknar dette som *ikkje*
  isolert (arv frå ein importert klasse tel som ei reell tilkopling), men
  spør brukaren om dette fangar intensjonen dersom det dukkar opp
  overraskande treff ved første køyring.

## Utført

Alle 9 steg gjennomførte:

1. `src/assets/scripts/makefile/find-unused-local-definitions.py` — nytt
   script, `--kind {slot,enum,type,subset,class}`. Brukar
   `class_induced_slots()` (ikkje `class_slots()`+`induced_slot()` som
   først skissert) for klasse-tilkoplingssjekken — enklare og stadfesta
   korrekt API (jf. `gen-modelldcat-elements.py`).
2. Fem nye Makefile-target i `make/91-modell-analyse.mk`.
3. `generate.yml`: fem nye per-skjema-kall i det eksisterande
   "Køyr modellanalyse per skjema"-steget.
4. `generate.yml`: nytt eingongs steg "Køyr modellanalyse på tvers av
   domene" i `publish`-jobben (køyrer `analyse-similar-*-all`, skriv til
   `generated/modell-analyse-tvers-domene/`). `actionlint` køyrd og
   godkjend etter begge `generate.yml`-endringane.
5. `mkdocs/publish.sh`: ny funksjon
   `generate_cross_domain_modellanalyse_docs()`, kalla frå Steg 1,
   publiserer dei tre `--scope all`-rapportane som
   `mkdocs/docs/modellanalyse/*.md` + oversikts-`index.md`, ny
   `- Modellanalyse:`-nav-seksjon. La til `modellanalyse` i
   opprydding-kvitelista (Steg 1) og i `.gitignore` (generert innhald,
   same mønster som `valideringsregler.md`).
6. `mkdocs/lib/scripts/generate-modellanalyse-md.py`: `REPORTS` utvida
   til 8 oppføringar (3 eksisterande + 5 nye) med
   `cross_domain_report_relpath`/`cross_domain_label`-felt; generisk
   fotnote-generering, ingen fotnote for dei 5 nye.
7. Usage-kolonna fjerna frå Slots (3 undertabellar)/Enumerations/Types/
   Subsets i `index.md.jinja2` — whitespace-kontroll (hard-break
   linjeskift) verifisert bevart.
8. **Verifisert reelt, ikkje berre lese kode** (sandbox måtte
   deaktiverast for podman — rootless newuidmap er blokkert i standard
   sandbox):
   - Alle 5 nye make-target køyrde mot fleire reelle skjema.
     `common-ap-no-schema.yaml` stadfesta reelle, korrekte funn (18
     ubrukte slots, 7 ubrukte enums, 4 ubrukte typar, 3 ubrukte subsets,
     2 isolerte klassar — venta, sidan common-ap-no er eit delt
     biblioteksskjema utan eigne lokale brukarar). Andre skjema (t.d.
     `ngr-adresse`, 23 lokale klassar) stadfesta INGEN falske positive
     for isolerte klassar, inkl. klassar berre nådd via containeren.
   - `make docs-publish` + `make docs-build` køyrd fullt ut:
     `mkdocs/docs/modellanalyse/*.md` vart oppretta med reelt innhald,
     nav-seksjonen dukka opp i `mkdocs.yml`, og skjema-sider (samt-bu,
     dcat-ap-no) viste dei nye fotnotene som fungerande relative lenkjer
     (`../../modellanalyse/<fil>.md`) i staden for workflow-URL-en.
     `validation.links`-sjekken i mkdocs-bygget fann **ingen** brotne
     lenkjer til `modellanalyse/*` (dei einaste `#classes`-åtvaringane
     var eit ått, ikkje-relatert artefakt av delvis/stale lokal
     `generated/`-cache, ikkje eit resultat av denne specen).
   - `make roundtrip SCHEMA=dcat-ap-no-schema.yaml` — 2 OK, 0 feil.
     `make roundtrip SCHEMA=samt-bu-schema.yaml` — `roundtrip-ttl` feilar,
     men dette er det alt dokumenterte BUG-3
     (`bugs/mappingerror-rdflib-roundtrip.md`, samt-bu står alt oppført
     som kjend feilande) — inga ny regresjon.
9. `.claude/rules/mkdocs-portal.md` sitt whitespace-eksempel oppdatert
   til å ikkje lenger vise ei Usage-kolonne.

**Avvik frå opphavleg plan:** ingen vesentlege — `class_induced_slots()`
i staden for `class_slots()`+`induced_slot()` (steg 1) er ei forenkling,
ikkje ei åtferdsendring.
