# Konvensjon for inlining i LinkML-skjema — analyse og forslag

## Bakgrunn

`PRINCIPLES.md` § "Lenking fremfor inlining" seier alt at klasser som kan
opptre sjølvstendig skal ha eit `id`-slot og at referansar til dei **ikkje**
skal ha `inlined: true`. Det som manglar er ei systematisk kartlegging av om
regelen faktisk vert etterlevd i heile kjeldekoden, og ein presisering av dei
tilfella regelen ikkje seier noko eksplisitt om: kva gjer vi med klasser som
*bevisst* ikkje har identifikator (verdiobjekt), og kva gjer vi når inlining
kolliderer med kjende verktøyfeil?

Denne specen er ein full kodebase-analyse av all bruk av LinkML-inlining
(`inlined: true` / `inlined_as_list: true`) under `src/linkml/`, kryssa mot
det faktiske importhierarkiet (for å avgjere om ein referert klasse *reelt*
har ein identifikator, ikkje berre lokalt i same fil) og mot alt dokumenterte
feil i `BUGS.md`/`bugs/`. Målet er eit konkret, verifisert grunnlag for ein
utvida konvensjon — ikkje ei gjetning.

## Metode

1. Alle 38 `*-schema.yaml`-filer under `src/linkml/` vart parsa med eit
   eige Python-script (ikkje via `make`/podman — reint lesande analyse, ingen
   LinkML-verktøy vart køyrt). Kvar `inlined`/`inlined_as_list`-deklarasjon
   (500 totalt) vart klassifisert som anten:
   - **container-attributt** (`attributes:` på ein `tree_root`-klasse — den
     dokumenterte unntaket i CLAUDE.md), eller
   - **domene-slot** (globalt `slots:`-oppslag eller `slot_usage`-overstyring
     på ein ikkje-container-klasse — det som "Lenking fremfor inlining"
     faktisk regulerer).
2. For kvar domene-slot vart target-klassen (`range:`) sin identifikator-status
   løyst **transitivt gjennom `imports:`** (rekursiv samanslåing av
   `classes:`/`slots:` frå importerte skjema, inkl. `is_a`-kjeder) — ikkje
   berre sjekka lokalt i same fil. Ei første, enklare utgåve av scriptet som
   berre såg i same fil gav mange falske positivar (t.d. `Datasett` i
   `dcat-ap-no-schema.yaml` såg ut til å mangle `id`, men `id` er faktisk
   definert i `common-ap-no-schema.yaml` og importert inn) — dette vart retta
   før funna under vart notert.
3. Funna vart kryssa mot `BUGS.md`/`bugs/*.md` og opne spesifikasjonar i
   `specs/backlog/` for å unngå å duplisere alt kjent/planlagt arbeid.

## Funn

### A. Overordna etterleving er høg

- 500 `inlined`/`inlined_as_list`-deklarasjonar totalt, i 28 av 38 skjema.
- **430 (86 %)** er container-attributt på `tree_root`-klasser — alle
  korrekte etter dagens konvensjon (ingen container brukte `slots:` i staden
  for `attributes:`, eller omvendt).
- Av dei resterande **70 domene-slota**, fann den importløyste analysen
  **null** tilfelle der inlining er sett på ein referanse til ein klasse som
  faktisk har `identifier: true` andre stad i import-kjeda. Med andre ord:
  **ingen stadfesta brot** på "Lenking fremfor inlining" slik regelen er
  formulert i dag.
- **61 av dei 70** er verifiserte, legitime verdiobjekt-mønster — klasser
  utan sjølvstendig identitet som alltid høyrer til nøyaktig éin forelder
  (stikkprøve: `Periode`, `Identifikator`, `Personnavn`, `Adresse`,
  `Kontaktinformasjon` i `fint-common-schema.yaml`; `Tilgangsmetadata`,
  `Gjenbruksmetadata`, `Proveniensmetadata`, `Katalogregistrering` i
  `fair-metadata-schema.yaml`). Desse er korrekt modellerte og treng ikkje
  endrast.

Konklusjonen er at repoet i hovudsak følgjer prinsippet godt — dei
attverande funna under er presiseringar og enkeltcase, ikkje eit
systemisk problem.

### B. Daud konfigurasjon — `inlined` på primitiv range (9 tilfelle)

`inlined`/`inlined_as_list` har berre effekt på klasse-verdsette slot.
Ni slot i to skjema set nøkkelen på ein **primitiv** range
(`string`/`integer`/`decimal`/`date`), der han vert stille ignorert av alle
generatorane:

| Fil | Slot | Range | Linje |
|---|---|---|---|
| `register-over-aksjeeiere-schema.yaml` | `navn` | `string` | 243 |
| `register-over-aksjeeiere-schema.yaml` | `beskrivelse` | `string` | 247 |
| `register-over-aksjeeiere-schema.yaml` | `antall` | `integer` | 251 |
| `register-over-aksjeeiere-schema.yaml` | `belop` | `decimal` | 255 |
| `register-over-aksjeeiere-schema.yaml` | `dato` | `date` | 259 |
| `register-over-aksjeeiere-schema.yaml` | `har_antall_aksjer` | `integer` | 267 |
| `register-over-aksjeeiere-schema.yaml` | `har_palydende_belop` | `decimal` | 275 |
| `register-over-aksjeeiere-schema.yaml` | `tidspunkt` | `date` | 307 |
| `fint-common-schema.yaml` | `adresselinje` | `string` (multivalued) | 139-143 |

Mønsteret i `register-over-aksjeeiere-schema.yaml` (generiske skildringar som
"Navn på instansen", "Numerisk verdi", éin `inlined: true` på **kvart einaste**
primitiv-slot i fila) tyder på mekanisk/generert boilerplate, ikkje eit
medvite val. Dette er reint støy for ein lesar — nøkkelen ser ut som han gjer
noko, men gjer det ikkje. Same kategori problem som "Ingen stille feil" skal
hindre, berre på skjema-forfattar-tidspunkt i staden for køyretid: noko er
deklarert, har null effekt, og ingenting varslar om det.

### C. To under-modellerte klasser i `fint-arkiv-schema.yaml`

- **`Klasse`** (linje 1377): feltet `klasseId` er skildra ordrett som
  "Eintydig identifikasjon av klassen innanfor klassifikasjonssystemet"
  (linje 397), men er **ikkje** `identifier: true`. `Klasse` vert difor
  inlina uavhengig, tre separate stader (`Mappe.klasse` via
  `inlined_as_list`, `Registrering.klasse` via `inlined`,
  `Klassifikasjonssystem.klasse` via `inlined_as_list`) — same
  klassifikasjonskode kan dukke opp fullt utskriven i mange arkivenheiter
  utan éi felles kjelde.
- **`Part`** (linje 1468) / **`Korrespondansepart`** (linje 1405): begge har
  felt (`orgnummer`, `foedselsnummer`) som er reelle,
  verkelegheitsforankra identifikatorar for personen/verksemda parten
  gjeld — men klassen sjølv manglar `identifier: true`. Same person/
  verksemd som opptrer som part i mange saksmapper får namn, adresse og
  kontaktinformasjon fullt duplisert ved kvart førekomst, i staden for at
  éi post vert referert.

Til samanlikning er dei 61 verdiobjekta i funn A verifiserte til å **ikkje**
ha eit slikt reelt nøkkelfelt — skiljet mellom "korrekt inlina verdiobjekt"
og desse to er nettopp om klassen har eit felt som fungerer som ein unik
nøkkel i verkelegheita.

**Avgjerd:** sjølv om heile FINT-domenet er eit medvite unntak frå fleire
navnekonvensjonar fordi det speglar FINT API-spesifikasjonen direkte (jf.
CONVENTIONS.md sitt `camelCase`-unntak), gjeld ikkje det unntaket for klassar
med eit reelt nøkkelfelt. `Klasse` og `Part`/`Korrespondansepart` får difor
`identifier: true` og vert refererte via lenkje i staden for å bli inlina —
sjå Handlingsliste punkt 3.

### D. Alt dokumenterte verktøyfeil knytt til inlining (kryssreferanse, ikkje nye funn)

| Bug | Kopling til inlining | Konsekvens |
|---|---|---|
| [BUG-2](../../bugs/inlined-as-list-rdflib-roundtrip.md) | `rdflib_loader` feiler når ein container-attributt er `inlined_as_list: true` **og** range-klassen har `identifier: true` | `test_roundtrip_ttl` og `test_convert_rdf` er **heilt hoppa over** for `ngr-adresse`, `ngr-eiendom`, `ngr-virksomhet`. Sidan container-inlining er ein ufravikeleg regel (R5), er dette akseptert som ein permanent, kjend avgrensing i verktøykjeda inntil `linkml-runtime` rettar feilen — ikkje eit teikn på feil skjemadesign som skal rettast ved å fjerne inlining |
| [BUG-8](../../bugs/polymorphic-inlined-list-yaml-loader.md) | `inlined_as_list` med **abstrakt/mixin** `range:` og faktiske subklasse-instansar krasjar YAML/SchemaLoader-lasting, sjølv om JSON Schema-validering (feilaktig) godkjenner instansen | Falskt positivt frå `make validate-instance`, hard krasj i `linkml-convert`/`gen-rdf`. Regelen buggen sjølv formulerer ("konkret range obligatorisk") ligg berre i `bugs/`, ikkje i PRINCIPLES.md/CLAUDE.md — ein som designar ein ny container finn han ikkje utan å alt vite å leite i `bugs/` |
| [BUG-9](../../bugs/avrotize-falsk-circular-dependency-warning.md) | `avrotize` sin dependency-resolver gir ei ikkje-deterministisk falsk "circular dependency"-åtvaring for kvar container med **to eller fleire** `inlined_as_list`-attributt, ved `xsd: true` | Ufarleg i dag (berre `samt-bu` har `xsd: true`), men vil dukke opp att for kvar ny domenemodell som slår på XSD-generering |

`specs/backlog/fix-roundtrip-ngr-inlined-as-list.md` er alt ein open spec
for BUG-2. Dens "Alternativ A" (fjern container-inlining) er no avvist —
sjå R5 og Handlingsliste punkt 4 under.

## Forslag til konvensjon

**R1 — Eksplisitt inlining for verdiobjekt.** Ein klasse utan
`identifier: true` vert i dag stille inlina av LinkML som default, sjølv om
`inlined`/`inlined_as_list` ikkje er sett noko stad. Krev at referansar til
slike klasser **alltid** set `inlined: true` (eller `inlined_as_list: true`
for multivalued) eksplisitt ved referansepunktet, uavhengig av at det
teknisk er default. *Grunngjeving (lesbarheit):* ein lesar/revisor skal
kunne avgjere om inlining er eit medvite val utan å måtte følgje heile
import-kjeda til target-klassen. *Kostnad:* svært lågt — berre eitt gap
funne (`klasse`-slotet i `fint-arkiv-schema.yaml`, linje 49-52).

**R2 — Aldri `inlined`/`inlined_as_list` på primitiv range.** Legg til ein
lint-/policy-sjekk (t.d. i `src/mcp-linkml-validator/policies/`, same mønster
som `slot_names_snake_case`) som flaggar `inlined`/`inlined_as_list` sett på
ein slot der `range:` løyser til ein innebygd type, ikkje ein klasse.
*Grunngjeving (logging/feilsluking):* dette er akkurat den typen "stille
feil" CLAUDE.md sitt "Ingen stille feil"-prinsipp skal hindre — noko er
deklarert, gjer ingenting, og ingenting seier frå.

**R3 — Klassar med eit reelt nøkkelfelt skal ha `identifier: true` og
refererast via lenkje.** Når ein klasse har eit felt som fungerer som unik
nøkkel i verkelegheita (org.nr, fødselsnummer, kode) og/eller kan bli
referert frå meir enn éin forelder, skal klassen ha `identifier: true` og
refererast via lenkje — ikkje inlinast. `Klasse` og `Part`/`Korrespondansepart`
(funn C) er dei første konkrete tilfella: dei får `identifier: true`, og alle
referansar til dei vert endra frå inlining til lenkje (Handlingsliste punkt 3).

**R4 — Konkret `range:` er obligatorisk for `inlined`/`inlined_as_list`.**
Flytt regelen som alt er formulert i `bugs/polymorphic-inlined-list-yaml-loader.md`
("ein `inlined`/`inlined_as_list`-slot skal alltid ha konkret `range:`,
aldri ei abstrakt eller mixin-klasse") inn i PRINCIPLES.md § "Lenking fremfor
inlining" eller CLAUDE.md sin "Containerklasse"-seksjon. *Grunngjeving
(lesbarheit/oppdagbarheit):* regelen finst alt, men berre for den som
allereie har trefft BUG-8 og leita i `bugs/` — han bør stå der ein
skjema-designar faktisk ser han **før** feilen oppstår.

**R5 — Container-inlining er ein ufravikeleg regel, uavhengig av
`identifier: true`.** Containerklassen (`tree_root: true`) sitt føremål er å
vere eit sjølvstendig, komplett eksportdokument — attributta hennar skal
difor **alltid** bruke `inlined`/`inlined_as_list`, også når range-klassen
har `identifier: true`, og også når det elles ville vore lenka utanfor
containeren etter "Lenking fremfor inlining". Dette gjeld ikkje som eit val
frå sak til sak, men som ein absolutt regel for containerattributt.
Konsekvensen er at kombinasjonen som trigger BUG-2 (`inlined_as_list` +
`identifier: true` i eit containerattributt) er ei akseptert følgje av dette
designvalet, ikkje eit avvik som skal rettast ved å fjerne inlining frå
containeren. *Grunngjeving (testbarheit — medviten avveging, ikkje ei
eintydig gevinst):* BUG-2 sitt tap av roundtrip-testdekning for
`ngr-adresse`/`ngr-eiendom`/`ngr-virksomhet` vert difor ståande som ein
kjend, akseptert grense i verktøykjeda (Alternativ B i
`specs/backlog/fix-roundtrip-ngr-inlined-as-list.md`) inntil `linkml-runtime`
rettar `rdflib_loader` — ikkje løyst ved å endre containerdesignet
(Alternativ A i same spec er avvist).

**R6 — Dokumenter BUG-9 sin friksjon der `xsd: true` vert vurdert.** Ingen
skjemaendring krevst i dag, men legg ei kort notis i
`CONVENTIONS.md`/`COMMANDS.md` sin omtale av `build.yaml`-manifestet om at
`xsd: true` saman med to eller fleire `inlined_as_list`-containerattributt
gir ei kjend, ufarleg `WARNING`-støy i DEBUG-loggen (BUG-9) — slik at ho
ikkje vert mistolka som ein ny feil neste gong nokon slår på XSD for ein ny
domenemodell.

## Handlingsliste

1. Fjern `inlined`/`inlined_as_list` frå dei 9 slota med primitiv range:
   `register-over-aksjeeiere-schema.yaml` (`navn`, `beskrivelse`, `antall`,
   `belop`, `dato`, `har_antall_aksjer`, `har_palydende_belop`,
   `tidspunkt`) og `fint-common-schema.yaml` (`adresselinje`). [R2]
2. ~~Legg til eksplisitt `inlined: true` på det globale `klasse`-slotet i
   `fint-arkiv-schema.yaml`~~ — **utgår:** tiltak 3 gjer `klasse`-slotet til
   ei lenkje i staden (`Klasse` får `identifier: true`), så det er ikkje
   lenger noko implisitt inlining-gap å gjere eksplisitt her. R1 gjeld
   framleis som generell regel for eventuelle framtidige tilfelle.
3. `Klasse` og `Part`/`Korrespondansepart` i `fint-arkiv-schema.yaml` får
   `identifier: true` (via det delte `id`-slotet frå `fint-common-schema.yaml`)
   og vert refererte via lenkje i staden for å bli inlina — fjern
   `inlined`/`inlined_as_list` frå alle referansepunkt (dei globale slota
   `part` og `korrespondansepart`, og `slot_usage`-overstyringane for
   `Mappe.klasse`, `Registrering.klasse`, `Klassifikasjonssystem.klasse`).
   Oppdater eksempeldatafila tilsvarande. [R3]
4. Containerklassen (`tree_root`) sitt bruk av inlining er ein ufravikeleg
   regel og skal **ikkje** fjernast for NGR. `specs/backlog/fix-roundtrip-ngr-inlined-as-list.md`
   sitt "Alternativ A" (fjern container-inlining) er difor avvist —
   "Alternativ B" (vent på upstream-fix i `linkml-runtime`) er den
   standande løysinga. Oppdater den specen til å reflektere avgjerda; behald
   skip-vilkåra i `tests/test_make.sh` uendra. [R5]
5. Legg regelen om at containerattributt **alltid** skal bruke
   `inlined`/`inlined_as_list` (R5) og "konkret range"-regelen frå
   `bugs/polymorphic-inlined-list-yaml-loader.md` (R4) inn i CLAUDE.md sin
   "Containerklasse"-seksjon, slik at begge er synlege der ein
   skjema-designar faktisk ser dei. [R4, R5]
6. Legg til ein automatisert sjekk (policy-sjekk eller eige script) som
   varslar dersom `inlined`/`inlined_as_list` er sett på ein slot med
   primitiv range, slik at funn B ikkje kjem tilbake. [R2]
7. Legg ei kort notis om BUG-9-støy til `CONVENTIONS.md`/`COMMANDS.md` sin
   omtale av `xsd: true`-generatorflagget i `build.yaml`. [R6]

## Utført

Alle punkt over er no utførte (punkt 2 er markert utgått, sjå grunngjeving
i sjølve punktet):

1. Fjerna `inlined`/`inlined_as_list` frå dei 9 primitiv-range-slota i
   `register-over-aksjeeiere-schema.yaml` og `fint-common-schema.yaml`.
   Verifisert med `make roundtrip` for begge skjema (2 OK, 0 feil) og
   `make lint` (ingen nye åtvaringar).
2. Utgår — sjå punkt 3.
3. `Klasse`, `Part` og `Korrespondansepart` i `fint-arkiv-schema.yaml` fekk
   `- id` lagt til i `slots:`-lista (det delte, importerte `id`-slotet med
   `identifier: true` frå `fint-common-schema.yaml`). `inlined`/
   `inlined_as_list` fjerna frå dei globale slota `part` og
   `korrespondansepart`, og frå `slot_usage`-overstyringane for
   `Mappe.klasse`, `Registrering.klasse` og `Klassifikasjonssystem.klasse`.
   Ingen eksempeldata refererte til desse klassane frå før, så ingen
   eksempelfil måtte endrast. Verifisert med `make validate-instance`
   ("No issues found"), `make roundtrip` (2 OK, 0 feil) og
   `make mcp-linkml-valider-modell` (dei tre `all_classes_have_identifier`-
   åtvaringane for `Klasse`/`Part`/`Korrespondansepart` er borte; dei 4
   attverande feila i silver-rapporten er urelaterte, pre-eksisterande
   `container_missing_required_class`-funn).
4. `specs/backlog/fix-roundtrip-ngr-inlined-as-list.md` oppdatert: "Alternativ A"
   (fjern container-inlining) er formelt avvist, "Alternativ B" (vent på
   upstream-fix i `linkml-runtime`) er stadfesta som den standande løysinga.
   Ingen skjemaendring gjort i `ngr-adresse`/`ngr-eiendom`/`ngr-virksomhet`,
   og skip-vilkåra i `tests/test_make.sh` er uendra (dei implementerer alt
   Alternativ B). Den specen vert verande i `specs/backlog/` sidan punkt 1
   der (overvaking av upstream-issue) framleis er ope.
5. CLAUDE.md § "Containerklasse" fekk to nye punkt: containerattributt skal
   alltid bruke `inlined`/`inlined_as_list` (uavhengig av `identifier: true`
   på range-klassen), og eit slikt attributt sin `range` skal alltid vere
   ein konkret klasse (aldri abstrakt/mixin), med kryssreferansar til denne
   specen og til BUG-2/BUG-8.
6. Ny bronze-policy-sjekk `no_inlined_on_primitive_range` lagt til i
   `src/mcp-linkml-validator/server.py` (funksjon + registrering i
   `_CHECK_HANDLERS`) og `src/mcp-linkml-validator/policies/bronze.yaml`,
   dokumentert i `src/mcp-linkml-validator/policies/README.md`. Verifisert
   ved å køyre `make mcp-linkml-valider-modell POLICY=bronze` mot tre ulike
   skjema (ingen falske positivar), og ved mellombels å attinnføre eit av
   dei fjerna tilfella frå punkt 1 for å stadfeste at sjekken faktisk slår
   ut (endringa vart reverta etter verifisering, ikkje committa).
7. Kort notis om BUG-9-støy lagt til i `COMMANDS.md` sin `gen-xsd`-rad.

**Ikkje utført av denne specen (bevisst utanfor scope):** upstream-fiksen for
BUG-2 sjølv (linkml-runtime), og eventuell vidare opprydding i FINT-domenet
utover `Klasse`/`Part`/`Korrespondansepart` — desse tre var dei einaste
konkrete funna med eit reelt nøkkelfelt (funn C). Dei andre ~58 FINT-
verdiobjekta i funn A vart verifiserte som korrekt modellerte og skal
ikkje endrast.
