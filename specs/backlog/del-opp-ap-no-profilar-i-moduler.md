# Del opp AP-NO-profilane (DCAT-AP-NO, DQV-AP-NO) i mindre importmodular

## Bakgrunn

Brukaren peika på at import av AP-NO-profilar (særleg `dcat-ap-no` og
`dqv-ap-no`) ofte gjer den endelege (merga) modellen meir enn dobbelt så
stor som domenemodellen sjølv, og bad om forslag til korleis
`dcat-ap-no` og `dqv-ap-no` kan delast opp i mindre, meir spissa
importmodular — med omsyn til kva klassar valideringspolicyane
(bronse/sølv/gull/felles-datakatalog/felles-begrepskatalog) faktisk
krev frå desse profilane.

Dette heng saman med eit funn i
`specs/backlog/reduser-generate-workflow-under-5min.md`: `merge`-steget
(rein LinkML-importvalidering, uavhengig av kva generatorar som er på)
er det klart tregaste Fase 1-steget for `oreg`-domenet, og vart knytt
til «iboende skjemakompleksitet ... fleire klasser/slots/importar» —
altså nett den typen importoppblåsing denne specen kartlegg. Denne
specen er eit sjølvstendig forslag til **kva** som bør delast opp, ikkje
ei vidareføring av CI-tidsmålinga i den specen.

## Målt data: kor stor er oppblåsinga i praksis?

**Konkret døme (`samt-bu`, `validation_policy: silver`):** skjemaet
definerer **11 eigne klassar**, men importerer `dqv-ap-no-schema` →
`dcat-ap-no-schema` (som sjølv importerer `dqv-core-schema`) →
`common-ap-no-schema`. Generert `samt-bu-schema.json` inneheld **48**
klassedefinisjonar totalt — over **4×** talet på eigne klassar. Av dei
37 importerte klassane brukar `samt-bu` faktisk berre 10
(`Aktoer`, `Datasett`, `Distribusjon`, `Kontaktopplysning`,
`Kvalitetsdimensjon`, `Kvalitetsmaaling`, `Kvalitetsmerknad`,
`RegulativRessurs`, `Standard`, `Tidsrom`) — dei resterande ~20-27
(`Katalog`, `Katalogpost`, `Datasettserie`, `Datatjeneste`,
`KatalogisertRessurs`, `Konsept`, `Begrepssamling`, `Mediatype`,
`Lisensdokument`, `Gebyr`, `Identifikator`, `Relasjon`,
`Rettighetserklaring`, `Sjekksum`, `Kvalitetsdeldimensjon`,
`Kvalitetsmaal`, `Brukartilbakemelding`, `Kvalitetssertifikat`,
`Tekstdel`, `DqvMotivasjon` m.fl.) vert generert og publisert utan å
vere i bruk.

**Verre døme — skjema som ikkje bruker AP-NO-klassar i det heile:**
`src/linkml/oreg/javazonetalk/javazonetalk-schema.yaml` importerer
(via absolutt, versjonslåst URL) full `dcat-ap-no-schema` men
refererer **null** klassar/typar/subsett derfrå — reint scaffold-etterslep.
Fleire `enhetsregisteret-*`-skjema (`bvrbekreftelse`,
`bvrettersendingavvedlegg`, `bvrstiftelsesdokument`,
`frivilligorganisasjonapi`) importerer same fulle profil, men brukar i
praksis berre `common-ap-no` sine typar/subsett (`LangString`,
`in_subset` osv.) — **ikkje** noko `dcat-ap-no`-klasse direkte (unntatt
enkeltklassar som `Gebyr` i `bvrinnfelles` og `Identifikator` i
`frivilligorganisasjonapi`). Alle desse har den same, uendra kommentaren
`# TODO: endre/legg til imports etter behov` generert av
`new-modell.sh` (sjå `specs/done/gjeninnfor-dcat-ap-no-import-doc-new-modell.md`)
— eit teikn på at TODO-en aldri vert følgt opp i praksis.

**Modellkatalog-familien** (`digdir-`, `brreg-`, `kartverket-`,
`ksdigital-`, `novari-`, `skatteetaten-modellkatalog`) importerer
`modelldcat-ap-no-schema`, som transitivt drar inn
`modelldcat-modell-schema` (27 eigne klassar) **og** full
`dcat-ap-no-schema` (17 klassar, + `dqv-core` sine 8 via transitiv
import) — til saman ~56 klassar. Faktisk bruk frå `dcat-ap-no`-sida er
berre `Aktoer`, `Kontaktopplysning`, `KatalogisertRessurs`, `Standard`,
`Tidsrom` (via `modelldcat-katalog-schema.yaml`) og for `brreg-` òg
`Kvalitetsmaaling` — **ikkje** `Datasett`, `Katalog`, `Katalogpost`,
`Datasettserie` eller `Datatjeneste`.

## Noverande importstruktur (målt)

| Skjema | Eigne klassar | Importerer | Merknad |
|---|---|---|---|
| `common-ap-no-schema` | 4 (`Metadata`-subset, `Lisensdokument`, `Mediatype`, `Konsept`, `Begrepssamling`) + typar/enum/subsett | `linkml:types` | Fundament — nesten alle AP-NO-skjema treng dette |
| `dqv-core-schema` | 8 (`Kvalitetsdimensjon`, `Kvalitetsdeldimensjon`, `Kvalitetsmaal`, `Kvalitetsmerknad`, `Brukartilbakemelding`, `Kvalitetssertifikat`, `Kvalitetsmaaling`, `Tekstdel`) | (ingen AP-NO-avhengigheit) | Sjølvstendig — ingen referanse til `dcat` |
| `dcat-ap-no-schema` | 17 (`Aktoer`, `Kontaktopplysning`, `Tidsrom`, `Standard`, `RegulativRessurs`, `Identifikator`, `Rettighetserklaring`, `Sjekksum`, `Gebyr`, `Relasjon`, `KatalogisertRessurs`, `Distribusjon`, `Datasett`, `Datasettserie`, `Datatjeneste`, `Katalogpost`, `Katalog`) | `common-ap-no` + **`dqv-core`** (ubetinga, for `har_kvalitetsmerknad`/`har_kvalitetsmaaling` på `Datasett`) | Alle konsumentar av `dcat-ap-no` får DQV-vokabularet «gratis», sjølv om dei ikkje brukar det |
| `dqv-ap-no-schema` | 0 (berre `har_maal.range`-innsnevring) | `common-ap-no` + `dcat-ap-no` | Reint tynt lag oppå `dcat-ap-no` |
| `modelldcat-modell-schema` | 27 | `common-ap-no` | Sjølvstendig informasjonsmodell-vokabular, ikkje avhengig av `dcat-ap-no` |
| `modelldcat-katalog-schema` | 3 (`Dokument`, `Modellkatalog`, `Informasjonsmodell`) | `common-ap-no` + `modelldcat-modell` + **full `dcat-ap-no`** | Brukar berre `Aktoer`, `Kontaktopplysning`, `KatalogisertRessurs`, `Standard`, `Tidsrom` frå `dcat-ap-no` |
| `modelldcat-ap-no-schema` | 0 | `modelldcat-katalog` | Facade |
| `xkos-ap-no-schema` | 5 | `common-ap-no` + full `dcat-ap-no` | Ikkje undersøkt i detalj her |

**Nøkkelinnsikt:** `dcat-ap-no` er i praksis éin udelt blokk på 29
klassar (17 + 8 DQV + 4 common) uansett om konsumenten treng éin klasse
(`Aktoer`) eller alle 17. Same problem arvar `modelldcat-ap-no` og
`xkos-ap-no`, sidan begge importerer heile `dcat-ap-no`.

## Avgrensingar som styrer kva som er mogleg

1. **LinkML støttar ikkje delvis utviding av ei importert klasse på
   tvers av skjema** (BUG-6, dokumentert i
   `src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml` sin kommentar og
   `specs/bugs/dqv-standard-class-override.md`). Det er difor **ikkje**
   mogleg å definere `Datasett` sine DQV-relaterte slots
   (`har_kvalitetsmerknad`, `har_kvalitetsmaaling`) i eit anna skjema
   enn der `Datasett` sjølv vert definert — dei to slot-referansane må
   liggje i same `slots:`-liste som resten av `Datasett`. Dette set ei
   nedre grense for kor langt DQV-kopling kan brytast frå `dcat-ap-no`:
   sjølve klassedefinisjonen av `Datasett` vil alltid krevje at
   `har_kvalitetsmerknad`/`har_kvalitetsmaaling` (og dermed klassane dei
   peikar på) er importerbare når `Datasett` vert lasta.
2. **Policy-sjekkar av typen `class_has_slot_with_uri` er avgrensa til
   skjemaet sine EIGNE klassar** (`src/mcp-linkml-validator/server.py`,
   `_check_class_has_slot_with_uri`: `own_class_names =
   set(schema.classes.keys())`, hoppar over dersom klassen ikkje er
   eigendefinert). Dei fleste sølv/gull-sjekkane på `Katalog`,
   `Datasett`, `Distribusjon`, `Datatjeneste` (t.d.
   `katalog_tittel`, `distribusjon_lisens`) er difor **inaktive** for
   domenemodellar som berre importerer desse klassane — dei gjeld reelt
   berre valideringa av `dcat-ap-no-schema.yaml` sjølv. Ei oppdeling av
   `dcat-ap-no` påverkar difor **ikkje** desse sjekkane for eksisterande
   konsumentar.
3. **Men: `container_has_class`-sjekkane i sølv/gull er ubetinga per
   skjema, uavhengig av om skjemaet er katalog-forma.** `silver.yaml`
   krev (severity `error`) at containerklassen har eit attributt med
   range `Katalog` **og** `Datasett` **og** `Kvalitetsmaal` **og**
   `Kvalitetsmaaling` — uansett kva domenemodellen faktisk skildrar.
   Målt mot `samt-bu` (silver, container manglar både `Katalog` og
   `Kvalitetsmaal` i dag) ser dette ut til alt å vere eit gap mellom
   policy-teksten og faktisk skjemainnhald, **uavhengig av** denne
   specen sitt forslag. Sjå «Opne spørsmål» — dette må avklarast før
   domenemodellar kan gå ned til eit smalare import-lag og framleis
   hevde sølv-konformitet.
4. **`must_import`/`schema_importerer_modelldcat_ap_no`-sjekken
   (felles-datakatalog) godtek transitiv import** (matchar delstreng i
   `schema.imports`, med `characteristic_class`-fallback for merga
   skjema) — ei oppdeling er trygg her så lenge éin av dei nye
   modulane framleis heiter noko som inneheld `modelldcat-ap-no-schema`,
   eller `Modellkatalog`-klassen framleis er tilgjengeleg transitivt.
5. **Versjonslåste, eksterne referansar til `dcat-ap-no-schema.yaml`**
   finst (`raw.githubusercontent.com/.../dcat-ap-no-v<versjon>/.../dcat-ap-no-schema`,
   generert av `new-modell.sh`, låst mot
   `.github/release-please-manifest.json`). Filstien og filnamnet
   `dcat-ap-no-schema.yaml` må difor halde fram å eksistere og
   fungere som eit fullstendig, sjølvstendig import-punkt (facade) —
   oppdeling kan leggje til nye, mindre filer ved sida av, men kan
   ikkje fjerne eller endre semantikken til den eksisterande fila utan
   å bryte alle eksisterande, versjonslåste importar.

## Kartlegging: policy-krav mot dcat-ap-no/dqv-ap-no-klassar

| Policy | Klassar/slots som vert kravd frå dcat-ap-no/dqv-ap-no (dersom klassen finst i skjemaet) |
|---|---|
| **bronse** | Ingen spesifikke DCAT/DQV-klassar — generelle strukturkrav (namngjeving, `class_uri`, identifikator, `class_count_limit`) |
| **sølv** | `Katalog` (tittel, kontaktpunkt, beskrivelse, utgiver), `Katalogpost`, `Datasett` (kontaktpunkt, tema, `applicableLegislation`), `Distribusjon` (`accessURL`), `Datatjeneste` (`endpointURL`, kontaktpunkt) — **pluss** containerklassen skal (error) referere `Katalog`, `Datasett`, `Kvalitetsmaal`, `Kvalitetsmaaling`, og bør (warning) referere `Distribusjon`, `Datatjeneste`, `Kvalitetsdimensjon`, `Kvalitetsmerknad` |
| **gull** | Same som sølv, strengare (fleire krav oppgraderte frå warning til error, t.d. `distribusjon_lisens`) |
| **felles-datakatalog** | Krev import av `modelldcat-ap-no-schema` (transitivt godteke), `dcat:`-prefiks, containerklasse med `Modellkatalog` + `Informasjonsmodell`, samt obligatoriske slots på desse to |
| **felles-begrepskatalog** | Krev `Begrep`/`Samling` frå SKOS-AP-NO — **ingen** avhengigheit til `dcat-ap-no`/`dqv-ap-no` |

**Konsekvens:** ei oppdeling av `dcat-ap-no` er ufarleg for
bronse/felles-begrepskatalog. For sølv/gull er det trygt for alle
per-klasse-sjekkane (dei er inaktive utanfor `dcat-ap-no-schema.yaml`
sjølv), men containerklasse-krava (punkt 3 over) må handterast
eksplisitt — sjå «Opne spørsmål».

## Forslag til modulstruktur

### Alternativ 1 — Lagdelt splitting av `dcat-ap-no` (tilrådd kjerne)

Del `dcat-ap-no-schema.yaml` i fem filer etter kor breitt klassane
faktisk vert brukt (målt over), pluss ei tynn facade-fil som held fram
å hete `dcat-ap-no-schema.yaml`:

| Nytt lag | Klassar | Importerer | Kven treng dette (målt) |
|---|---|---|---|
| `dcat-ap-no-aktoer-schema` | `Aktoer`, `Kontaktopplysning` | `common-ap-no` | Alle modellkatalog-skjema, dei fleste andre |
| `dcat-ap-no-ressurs-schema` | `KatalogisertRessurs`, `Tidsrom`, `Standard`, `RegulativRessurs`, `Identifikator`, `Rettighetserklaring`, `Sjekksum`, `Gebyr`, `Relasjon` | `dcat-ap-no-aktoer-schema` | `modelldcat-katalog` (`Standard`, `Tidsrom`, `KatalogisertRessurs`), `bvrinnfelles` (`Gebyr`), `frivilligorganisasjonapi` (`Identifikator`) |
| `dcat-ap-no-datasett-schema` | `Datasett`, `Distribusjon` | `dcat-ap-no-ressurs-schema` + tynn DQV-bru (sjå alternativ 3) | `samt-bu`, `referansemodell` |
| `dcat-ap-no-katalog-schema` | `Katalog`, `Katalogpost`, `Datasettserie` | `dcat-ap-no-datasett-schema` | Fullverdige katalog-publiserande modellar |
| `dcat-ap-no-tjeneste-schema` | `Datatjeneste` | `dcat-ap-no-datasett-schema` | API-eksponerande modellar |
| `dcat-ap-no-schema` (facade, **filnamn uendra**) | 0 (berre imports) | Alle fem laga over | Eksisterande konsumentar som ikkje migrerer — **null brot** |

Klassane er ordna slik at kvart lag berre importerer laget rett under
seg (ikkje sideveges), slik at ein konsument som berre treng
`dcat-ap-no-ressurs-schema` ikkje dreg med seg `Katalog`/`Datatjeneste`.

### Alternativ 2 — Fjern DQV-koplinga frå `dcat-ap-no` heilt (vurdert, **ikkje tilrådd**)

Ville løyst det at *alle* konsumentar av `Datasett` i dag får dei 8
DQV-klassane «gratis». Men BUG-6 (sjå «Avgrensingar» punkt 1) gjer dette
ikkje gjennomførbart utan å flytte sjølve `Datasett`-klassedefinisjonen
ut av `dcat-ap-no` — noko som ville bryte prinsippet om éin
autoritativ definisjonsstad for klassen (DRY, jf. CLAUDE.md) og skape
to konkurrerande `Datasett`-definisjonar. **Tilråding: ikkje forfølg
dette alternativet** — behald koplinga, men gjer han billegast mogleg
(sjå alternativ 3).

### Alternativ 3 — Tynn ut `dqv-core` sjølv (reduser kostnaden av DQV-broa)

Del `dqv-core-schema.yaml` i to, ettersom berre 2 av 8 klassar faktisk
er del av DQV-broa på `Datasett`:

| Nytt lag | Klassar | Kven treng dette |
|---|---|---|
| `dqv-slots-schema` | `Kvalitetsmerknad`, `Kvalitetsmaaling` (dei to klassane `har_kvalitetsmerknad`/`har_kvalitetsmaaling` peikar på) | Importert **ubetinga** av `dcat-ap-no-datasett-schema` — minimal, fast kostnad |
| `dqv-vokabular-schema` | `Kvalitetsdimensjon`, `Kvalitetsdeldimensjon`, `Kvalitetsmaal`, `Brukartilbakemelding`, `Kvalitetssertifikat`, `Tekstdel` | Berre modellar som aktivt forfattar kvalitetsmålingar (t.d. `samt-bu`, via `dqv-ap-no`) |
| `dqv-core-schema` (facade, **filnamn uendra**) | 0 | Eksisterande konsumentar — null brot |

Dette kuttar den «usynlege» DQV-kostnaden for alle `Datasett`-brukarar
frå 8 til 2 klassar, utan å røre BUG-6-avgrensinga.

### Alternativ 4 — Retilkopling av `modelldcat-katalog` (automatisk gevinst av 1+3)

`modelldcat-katalog-schema.yaml` sitt import av full `dcat-ap-no`
(linje 35) bør endrast til å importere berre
`dcat-ap-no-ressurs-schema` (som transitivt gjev `Aktoer`,
`Kontaktopplysning`, `KatalogisertRessurs`, `Standard`, `Tidsrom` — alt
`modelldcat-katalog` faktisk brukar). Dette fjernar `Katalog`,
`Katalogpost`, `Datasettserie`, `Datatjeneste`, `Datasett`,
`Distribusjon` og heile `dqv-vokabular`-laget frå modellkatalog-
familien sin genererte modell — ingen eigen splitting av
`modelldcat-modell` (27 klassar) er naudsynt, sidan den fila alt er eit
sjølvstendig, ikkje-oppblåst vokabular.

### Alternativ 5 — Prosess/tooling: fiks scaffolding og migrer TODO-skjema

Uavhengig av sjølve modulstrukturen: `new-modell.sh` sitt standardval
(full, versjonslåst `dcat-ap-no-schema`-import med
`# TODO: endre/legg til imports etter behov`) er årsaka til at
`javazonetalk` og fleire `enhetsregisteret-*`-skjema ber på ubrukt
importvekt i dag. Foreslått tiltak:
- La `make new-modell` spørje kva AP-NO-lag brukaren treng (eller ikkje
  treng AP-NO i det heile — `common-ap-no` åleine, eller ingenting),
  i staden for å hardkode full `dcat-ap-no`.
- Som eige oppfølgingstiltak (ikkje del av sjølve modul-splittinga):
  gå gjennom dei identifiserte TODO-skjemaa
  (`javazonetalk`, `bvrbekreftelse`, `bvrettersendingavvedlegg`,
  `bvrstiftelsesdokument`, `bvrinnfelles`, `frivilligorganisasjonapi`)
  og bytt til det minimale laget kvart treng (evt. `common-ap-no`
  åleine, eller ingen AP-NO-import for `javazonetalk`).

## Tilråding

Kombiner **alternativ 1 + 3 + 4 + 5**. Alternativ 2 vert medvite ikkje
forfølgt (BUG-6-avgrensing). Facade-filene
(`dcat-ap-no-schema.yaml`, `dqv-core-schema.yaml`) held eksisterande
import-stiar (inkludert versjonslåste, eksterne) uendra og fungerande —
migrering til dei tynnare laga vert difor **opt-in**, ikkje eit
tvungent brot, og kan gjerast gradvis per domenemodell.

## Venta gevinst (estimert klassetal, før → etter)

| Konsumentgruppe | Før (målt) | Etter (estimert, opt-in migrering) |
|---|---|---|
| `javazonetalk` (ingen AP-NO-bruk) | 29 (4 common + 17 dcat + 8 dqv-core) | 0 |
| `bvrbekreftelse`/`bvrettersendingavvedlegg`/`bvrstiftelsesdokument` (berre common-ap-no-typar) | 29 | 4 (berre `common-ap-no`) |
| `bvrinnfelles` (treng `Gebyr`) | 29 | 15 (4 common + 2 aktoer + 9 ressurs) |
| `frivilligorganisasjonapi` (treng `Identifikator`) | 29 | 15 |
| Modellkatalog-familien (6 skjema, treng `Aktoer`/`Kontaktopplysning`/`Standard`/`Tidsrom`/`KatalogisertRessurs`) | 4+17+8+27=56 | 4+2+9+27=42 |
| `samt-bu` (Datasett + full DQV-vokabular) | 29 | 4+2+9+2+2+6=25 |

Størst relativ gevinst for skjema som i dag berre bruker éin liten del
(eller ingenting) av `dcat-ap-no` — dette er òg den talrikaste gruppa
(11 av 19 kartlagde konsumentskjema).

## Opne spørsmål / risiko

1. **Silver/gull sitt `container_har_katalog`/`container_kvalitetsmaal`-krav
   er ubetinga per skjema** (sjå «Avgrensingar» punkt 3) — **stadfesta
   som eit reelt, aktivt gap, ikkje berre teoretisk**, ved å faktisk
   køyre `make mcp-linkml-valider-modell SCHEMA=src/linkml/samt/samt-bu/samt-bu-schema.yaml
   POLICY=silver`: `valid: false`, med
   `container_missing_required_class` for både `Katalog` og
   `Kvalitetsmaal`. Det committa valideringssnapshotet
   (`src/linkml/samt/samt-bu/validation/1.10.0/silver.json`, git-spora)
   viser same to feil — dette har altså vore ein vedvarande,
   registrert-men-uløyst `valid: false`-tilstand for `samt-bu` over
   fleire utgjevne versjonar (1.0.0 → 1.10.1).

   **Rotårsak spora via git-historikk:** sjekken vart opphavleg innført
   (commit `56b346408`, 2026-04-30) som ein **eigen, eksplisitt opt-in
   policy** (`ap-no-catalog.yaml`, køyrt via `POLICY=ap-no-catalog`),
   dokumentert for å validere om eit skjema **publiserer ein full
   DCAT-AP-NO/DQV-AP-NO-katalog**. Denne vart så omdøypt to gonger
   (`ap-no-catalog.yaml` → `ap-no.yaml` i `a92f4e7f7`, deretter →
   `silver.yaml` i `2facd9d0` — «endrer profilnavna til bronze, silver
   og gold») — begge reine omdøypingscommitar utan grunngjeving for å
   utvide omfanget. Kravet om at **alle** sølv-skjema skal sjå ut som
   ein full katalog+kvalitetsmålings-publisør ser dermed ut til å vere
   utilsikta scope creep frå omdøyping, ikkje eit medvite designval.

   **Omfang truleg større enn `samt-bu`:** minst 7 `fint-*`-skjema,
   fleire `oreg/enhetsregisteret-*`-skjema og `javazonetalk` deklarerer
   `validation_policy: silver` og manglar `Katalog`/`Kvalitetsmaal` i
   containeren sin (verifisert via grep for representative skjema) —
   dei feilar truleg same vegen. Unntaket er
   `referansemodell-silver`/`referansemodell-gold`, som **har**
   `Katalog`/`Kvalitetsmaal`/`Datasett` i containeren — desse ser ut
   til å vere reindyrka demo-skjema bygde spesifikt for å tilfredsstille
   sjekken, ikkje representative for typiske domenemodellar.

   **Vurdert fiksretning (ikkje implementert):** «avvikle» tilbake mot
   det opphavlege designet — skil generelle sølv/gull-krav frå
   katalog-fullstendigheitskrava, anten ved å (a) gjere
   `container_har_katalog`/`container_kvalitetsmaal`/`container_kvalitetsmaaling`
   betinga av at skjemaet faktisk *modellerer* eit katalog-/kvalitets-
   scenario (ikkje berre at klassen finst importert — sjå funnet i
   «Bakgrunn» om at nesten alle skjema importerer heile profilen
   uansett bruk, så «finst i skjema» er ikkje eit godt filter), eller
   (b) gjeninnføre eit eige, eksplisitt opt-in katalog-tillegg til
   sølv/gull (t.d. `POLICY=silver+katalog`) som berre skjema som
   *faktisk skal* publisere full katalog (som `referansemodell-silver`)
   treng slå på. **Krev brukarvedtak om retning** — påverkar
   valideringsutfallet for eit tosifra tal eksisterande skjema på tvers
   av `fint`, `oreg`, `samt` og `referanse`, og er ei endring i delt
   valideringsinfrastruktur (`src/mcp-linkml-validator/`), ikkje berre i
   AP-NO-skjemaa sjølve. Føreslått som **eiga, sjølvstendig spec** —
   handterer eit reelt, aktivt valideringsgap uavhengig av om
   AP-NO-splittinga i denne specen vert gjennomført.
2. Klasse-til-lag-tilordninga over er verifisert mot eit representativt
   utval konsumentskjema (grep etter `range:`-referansar), ikkje alle
   19 kartlagde skjema i detalj (t.d. `xkos-ap-no`, `referansemodell`
   sin faktiske klassebruk er ikkje fullstendig verifisert — begge
   fekk 0 treff på det avgrensa søkemønsteret, som kan bety anten
   ingen bruk eller bruk via mønster søket ikkje dekte, t.d.
   `is_a:`-arv). Må stadfestast før implementering.
3. Eksterne, versjonslåste referansar (raw.githubusercontent.com) til
   `dcat-ap-no-schema.yaml` frå skjema utanfor dette repoet (om nokon)
   er ikkje kartlagde her — facade-tilnærminga (uendra filnamn/sti) er
   valt spesifikt for å eliminere denne risikoen, men bør stadfestast
   ved implementering.

## Neste steg (krev eige vedtak/spec — ikkje del av denne specen)

1. Brukarvedtak: godkjenn/juster tilrådd lagdeling (alternativ 1+3+4)
2. Verifiser klasse-til-lag-tilordning mot alle 19 konsumentskjema (jf.
   opne spørsmål punkt 2)
3. Avklar/rett silver/gull sitt `container_*`-krav (opne spørsmål punkt 1)
   — truleg eiga, mindre spec før modul-migrering kan reknast som
   sølv-konform for smalare lag
4. Implementer sjølve fil-splittinga (`dcat-ap-no-*-schema.yaml`,
   `dqv-slots-schema.yaml`, `dqv-vokabular-schema.yaml`) + facade-import
   i eksisterande `dcat-ap-no-schema.yaml`/`dqv-core-schema.yaml`
5. Oppdater `modelldcat-katalog-schema.yaml` til å importere
   `dcat-ap-no-ressurs-schema` i staden for full `dcat-ap-no-schema`
6. Oppdater `new-modell.sh` til å spørje om AP-NO-lag i staden for å
   hardkode full `dcat-ap-no`-import
7. Migrer identifiserte lette konsumentar
   (`javazonetalk`, `bvrbekreftelse`, `bvrettersendingavvedlegg`,
   `bvrstiftelsesdokument`, `bvrinnfelles`, `frivilligorganisasjonapi`)
   til minimale importar, fjern «TODO: endre/legg til imports etter
   behov»-kommentaren
8. Mål faktisk `make lint`/`make validate`/`generate.yml`
   `merge`-steg-tidsgevinst i CI for migrerte domene, koordiner med
   `specs/backlog/reduser-generate-workflow-under-5min.md`

## Akseptansekriterium (for denne specen — sjølve forslaget)

- [x] Målt noverande importstruktur og klassetal per AP-NO-skjema
- [x] Kartlagt faktisk klassebruk per konsumentskjema (representativt
      utval på tvers av oreg, modellkatalog, samt, referanse)
- [x] Kartlagt policy-krav (bronse/sølv/gull/felles-datakatalog/
      felles-begrepskatalog) mot dcat-ap-no/dqv-ap-no-klassar
- [x] Identifisert LinkML-avgrensing (BUG-6) som styrer kva splitting
      som er mogleg, og kva alternativ som difor vert avvist
- [x] Skrive konkret forslag til lagdeling med tilråding og estimert
      gevinst
- [x] Identifisert opent policy-gap (`container_har_katalog`/
      `container_kvalitetsmaal`) som må avklarast før smalare lag kan
      hevde sølv-konformitet
- [ ] Brukarvedtak om kva alternativ som skal implementerast — **ikkje
      gjort, krev brukarinput**. Specen vert verande i `specs/backlog/`
      til vedtak er gjort.

## Relaterte filer

- `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml` — skjemaet som
  føreslås delt i lag (alternativ 1)
- `src/linkml/ap-no/dqv-core/dqv-core-schema.yaml` — skjemaet som
  føreslås delt i `dqv-slots`/`dqv-vokabular` (alternativ 3)
- `src/linkml/ap-no/dqv-ap-no/dqv-ap-no-schema.yaml` — inneheld
  BUG-6-kommentaren som grunngjev kvifor alternativ 2 er avvist
- `src/linkml/ap-no/modelldcat-katalog/modelldcat-katalog-schema.yaml` —
  retilkoplingsmål for alternativ 4
- `src/mcp-linkml-validator/policies/{bronze,silver,gold,felles-datakatalog,felles-begrepskatalog}.yaml`,
  `src/mcp-linkml-validator/server.py` (`_check_class_has_slot_with_uri`,
  `_check_container_has_class`, `_check_schema_imports`,
  `_check_merged_class_has_slot_with_uri`) — grunnlag for
  policy-kartlegginga og punkt 3 i «Avgrensingar»
- `src/assets/scripts/scaffolding/new-modell.sh` — kjelde til
  TODO-scaffold-mønsteret (alternativ 5)
- `src/linkml/oreg/javazonetalk/javazonetalk-schema.yaml`,
  `src/linkml/oreg/enhetsregisteret-{bvrbekreftelse,bvrettersendingavvedlegg,bvrstiftelsesdokument,bvrinnfelles,frivilligorganisasjonapi}/*.yaml`,
  `src/linkml/samt/samt-bu/samt-bu-schema.yaml`,
  `src/linkml/modellkatalog/*/*.yaml` — konkrete konsumentskjema brukt
  i den målte kartlegginga
- `specs/backlog/reduser-generate-workflow-under-5min.md` — relatert
  CI-tidsproblem som denne modulariseringa kan avhjelpe, men som ikkje
  er direkte del av denne specen
- `specs/done/ap-no-konsolidering-common.md`,
  `specs/done/ap-no-metadata-subset.md`,
  `specs/done/avvik-dqv-ap-no.md`,
  `specs/done/avvik-modelldcat-ap-no.md`,
  `specs/done/silver-policy-samla-tabell.md` — tidlegare arbeid med
  AP-NO-importhierarkiet og policy-innhaldet denne specen byggjer vidare på
