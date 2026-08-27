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

## Negative konsekvensar ved oppdeling (utreda 2026-08-27)

Brukar bad spesifikt om ei utreiing av negative konsekvensar. Dei fem
funna under er **ikkje** dekte av «Avgrensingar»-seksjonen over (som
gjeld kva som er *teknisk mogleg*) — dei gjeld i staden den **varige
drifts- og governance-kostnaden** av sjølve oppdelinga, verifisert mot
repoets eigne reglar, ikkje berre LinkML-tekniske avgrensingar.

**1. `CONVENTIONS.md` sin «Éin modell per katalog»-regel gjeld
«unntaksfritt» og gjer kvart nytt lag til ein eigen, fullt versjonert
pakke — ikkje berre ei ny fil.** Regelen (`CONVENTIONS.md` linje 17-24)
seier eksplisitt at «alle modellar, inkludert modellar som er nære
knytte til kvarandre (t.d. delar av same eksterne spesifikasjon), får
kvar sin eigen `<domain>/<modell>/`-katalog, sjølvstendig `build.yaml`
og sjølvstendig release-please-pakke» — og brukar nettopp
`modelldcat-ap-no`/`modelldcat-katalog`/`modelldcat-modell`
(same relasjon som denne specen sitt forslag) som det etablerte dømet.
Alternativ 1+3 sitt forslag om «fem/to nye filer» er difor i realiteten
eit forslag om **7 nye, fullstendige modellpakkar**
(`dcat-ap-no-aktoer`, `dcat-ap-no-ressurs`, `dcat-ap-no-datasett`,
`dcat-ap-no-katalog`, `dcat-ap-no-tjeneste`, `dqv-slots`,
`dqv-vokabular`), kvar med eigen katalog, `build.yaml`, `CHANGELOG.md`,
`description.md` og semver-versjon — verifisert mot dagens
`src/linkml/ap-no/*/`-struktur, der **alle** 10 eksisterande profilar
følgjer nett dette éin-fil-per-katalog-mønsteret utan unntak.

**2. Kvart nytt lag vert automatisk «felles infrastruktur» under
`GOVERNANCE.md` — ein varig, ikkje eingongs, godkjenningskostnad.**
`GOVERNANCE.md` (linje 99-103) definerer `src/linkml/ap-no/` som
«Felles infrastruktur»: alle endringar krev review/godkjenning frå
**repo-administrator**, og brotande endringar krev full RFC-prosess
(GitHub Issue, 14-dagars diskusjonsfrist, konsensus — linje 269-277).
Dette gjeld ikkje berre sjølve oppdelinga (éin gong), men **kvar
framtidig endring** i dei 7 nye laga, for alltid — same
godkjenningsbyrde som dei 10 eksisterande AP-NO-profilane har i dag,
no fordelt på 17 pakkar i staden for 10.

**3. `release-please` sporar allereie 37 pakkar manuelt — denne
oppdelinga åleine legg til 7 (≈19 % auke).** Både
`.github/release-please-config.json` og
`.github/release-please-manifest.json` krev **manuell** registrering
per pakke (`component`/`release-type` i config, startversjon i
manifest) — ingen auto-oppdaging. Alternativ 1+3 sine 7 nye lag måtte
leggjast til manuelt i begge filer, og vil frå då av generere eigne
CHANGELOG-oppføringar og eigne versjonsbump-linjer i kvar
`release-please`-PR i overskodeleg framtid — meir støy per release,
ikkje berre eit eingongsarbeid.

**4. `mkdocs`-portalen genererer éin nav-oppføring per skjemakatalog —
7 nye interne "lag" ville dukke opp saman med dei ekte, sjølvstendige
profilane.** `mkdocs/publish.sh` (linje 272-275) discoverer
nav-strukturen automatisk frå katalogar under kvar domenekatalog i
`GEN`. Dei 7 nye laga har ingen sjølvstendig eksistens i den eksterne
DCAT-AP-NO-/DQV-spesifikasjonen (dei er eit reint internt
implementasjonsgrep) — dei ville likevel få eigne portalsider og
nav-oppføringar side om side med `skos-ap-no`, `cpsv-ap-no` osv.,
noko som utvatnar portalen sin bruksverdi for eksterne lesarar som
leitar etter den faktiske DCAT-AP-NO/DQV-AP-NO-dokumentasjonen.

**5. Oppdelinga fjernar 1:1-sporbarheita mot den eksterne standarden
dette skjemaet skal spegle.** `dcat-ap-no-schema.yaml` sin
`build.yaml` har eit eksplisitt `external_spec_url`-felt
(`https://informasjonsforvaltning.github.io/dcat-ap-no/`, Digdir sin
offisielle spesifikasjon), og `description.md` viser til
`specs/done/avvik-dcat-ap-no.md` for dokumenterte avvik. Denne
kopling føreset i praksis at éin fil ≈ éin spesifikasjon, slik at
framtidige spesifikasjonsoppdateringar (jf. `GOVERNANCE.md` sitt eige
RFC-døme: «DCAT-AP-NO v3.0 krev no dct:publisher») kan sporast og
implementerast på éin stad. Alternativ 1 sin lagdeling (aktør/
ressurs/datasett/katalog/tjeneste) er ei **repo-intern** inndeling utan
tilsvarande struktur i den eksterne spesifikasjonen — framtidige
spec-oppdateringar må difor manuelt kartleggjast på tvers av 5 filer i
staden for 1, noko som aukar risikoen for drift mellom repoet sin
implementasjon og den faktiske standarden. Same gjeld `dqv-core` mot
DQV-spesifikasjonen (alternativ 3).

**6. `ap-no` er sjølv eit CI-matrise-domene — oppdeling aukar
skjematalet i den jobben sin eigen `generate`/`valider-og-analyser`-
køyring.** Stadfesta med `make print-domains`: `ap-no` er eitt av
domena som får si eiga matrise-jobb-instans i `generate.yml`
(`checkout-source` → `discover-domains` → `make print-domains`, som
listar kvar toppnivåkatalog under `src/linkml/` som eit domene). 7
nye skjemafiler under `src/linkml/ap-no/` aukar difor talet på
skjema `make domain-ap-no` (og tilsvarande `valider-og-analyser`-
jobben) må generere/validere/analysere per køyring — dette motverkar
delvis, for `ap-no`-domenet sin eigen del, den CI-tidsgevinsten som
opphavleg motiverte denne specen (jf. «Bakgrunn», koplinga til
`specs/backlog/reduser-generate-workflow-under-5min.md`), sjølv om
nettogevinsten for **konsument**-domena (`oreg`, `samt`,
`modellkatalog` osv.) framleis truleg er positiv. Ikkje målt i
konkrete sekund her — bør målast før implementering (jf. «Neste
steg» punkt 8).

**Konsekvens for tilrådinga:** Alternativ 1+3 (lagdelinga sjølv) er
framleis den tekniske løysinga som løyser importoppblåsinga, men
kostnaden er vesentleg høgare enn «del ei fil i fem» — det er eit
forslag om å **doble+ talet på formelt styrte AP-NO-pakkar** (10 → 17)
med varig godkjennings-, versjonerings- og dokumentasjonsomkostnad.
To realistiske vegar vidare, begge krev eksplisitt brukarvedtak (sjå
oppdatert «Neste steg»):
- **(a) Godta kostnaden** — implementer som skissert, registrer 7 nye
  release-please-pakkar, aksepter det varige governance-/CI-/portal-
  overheadet mot importgevinsten i tabellen over.
- **(b) Avvik medvite frå «éin modell per katalog»** for berre denne
  splittinga — anten (b1) fleire `*-schema.yaml`-filer i **same**
  `dcat-ap-no/`-katalog (den gamle `submodels:`-varianten, nettopp
  fjerna — sjå eiga utgreiing under), eller (b2) eit **nytt
  katalognivå** under `dcat-ap-no/` (t.d.
  `dcat-ap-no/<lag>/<lag>-schema.yaml`) — **verifisert infeasible utan
  systemisk refaktorering, sjå «Kunne eit nytt katalognivå under
  modell løyst dette?» under.**

## Kunne eit nytt katalognivå under modell løyst dette? (utreda 2026-08-27)

Brukar spurde konkret om eit nytt katalognivå under `<modell>/` (t.d.
`dcat-ap-no/<delmodell>/<delmodell>-schema.yaml`) kunne brukast til å
samle delmodellar knytte til éin modell — som eit tredje alternativ
mellom «7 heilt sjølvstendige toppnivå-pakkar» (opsjon a) og «same
katalog, delt manifest» (opsjon b1, den fjerna `submodels:`-varianten).

**Repoet har alt vurdert nøyaktig dette spørsmålet, to gonger, og
kome til nei begge gongar:**

1. `specs/done/modellkatalog-fleire-skjema-evaluering.md` (arkivert
   evaluering, spørsmål 3: «Treng vi eit tredje grupperingsnivå
   (domene → modellgruppe → modell)?») konkluderte **nei**: «Eit
   generelt tredje nivå ville krevje å endre katalogstien ... for
   **alle** ~41 skjema ... det påverkar `new-modell`-scaffolding,
   `valid-scopes.txt`-generering, mkdocs nav-menyoppbygging,
   gen-doc-stiar og alle Makefile-targets som i dag antek
   `<domain>/<modell>/` som fast dybde.»
2. `specs/done/submodels-eigne-modellkatalogar-vurdering.md` (2026-08-17,
   10 dagar før denne utgreiinga) gjekk **motsett veg av eit tredje
   nivå**: fjerna den einaste eksisterande delte-katalog-mekanismen
   (`submodels:` — `dqv-core` i `dqv-ap-no/`, `modelldcat-katalog`/
   `-modell` i `modelldcat-ap-no/`) og gjorde alle tre til vanlege,
   sjølvstendige `<domain>/<modell>`-katalogar. Grunngjevinga var
   konkret og alvorleg: delt katalog gjorde at `release-please` (som
   er katalogbasert) **ikkje kunne versjonere submodellane
   uavhengig** — `dqv-core` og `modelldcat-katalog` stod fast på
   `version: "1.0.0"` heilt sidan dei vart oppretta — **og** kravde
   dokumentert spesialkode i minst 6 filer
   (`mkdocs/lib/sections/delmodellar.sh`, `har_del`-feltet i
   `generate-informasjonsmodell.py`, `mkdocs/lib/generate_index.sh`,
   `mkdocs/lib/scripts/collect-schema-metadata.py`,
   `src/assets/scripts/scaffolding/remove-modell.sh` m.fl.) — kode som
   framleis ligg dormant i repoet (verifisert:
   `mkdocs/lib/sections/delmodellar.sh` finst framleis, uendra sidan
   fjerninga). Spec-en sitt eige punkt 4 stadfesta eksplisitt at dette
   **ikkje** utfordra konklusjonen om at eit tredje grupperingsnivå er
   unødvendig — tvert imot gjorde det spørsmålet «endå meir
   irrelevant».

**Ny, konkret kodeverifisering (denne utgreiinga) stadfestar at
grunngjevinga i punkt 1 framleis held, og er breiare enn det den
opphavlege evalueringa fann:** minst **8** stader i verktøykjeda
hardkodar ei fast, eksakt djupn på nøyaktig to katalognivå
(`<domain>/<modell>/`) mellom `src/linkml/` og sjølve skjemafila —
eit skjema lagt éitt nivå djupare (`<modell>/<delmodell>/...`) ville
vere **usynleg** for alle desse, ikkje berre feilhandtert:

| Fil | Mekanisme |
|---|---|
| `make/02-schema-discovery.mk:13` | `SCHEMAS := find ... -mindepth 3 -maxdepth 3 -name '*-schema.yaml'` — **hovud-skjemaoppdaginga**, brukt av `make print-domains`, CI-domeneoppdaging og alle domene-mål |
| `make/40-validation.mk:113` | `find src/linkml/$(DOMAIN) -mindepth 2 -maxdepth 2 -name '*-schema.yaml'` — domene-scopa skjemaliste for validering |
| `src/assets/scripts/makefile/gen-config.sh:18` | `find src/linkml -mindepth 3 -maxdepth 3 -name 'build.yaml'` — **manifest-/config-oppdaging**; ei `build.yaml` for eit nytt delmodell-lag ville aldri verte lasta |
| `src/assets/scripts/makefile/check-iri-resolution.py:66-67` | `glob("*/*/*-schema.yaml")` |
| `src/assets/scripts/makefile/find-similar-names.py:69-70` | `glob("*/*/*-schema.yaml")` |
| `src/assets/scripts/makefile/find-unused-local-definitions.py:348` | `glob(f"{domain}/*/*-schema.yaml")` |
| `src/assets/scripts/makefile/update-modellkatalog.py:86` | `glob(f"{root}/*/*/*.yaml")` |
| `mkdocs/publish.sh:272,275` | to nøsta `find -mindepth 1 -maxdepth 1 -type d`-lag (domene → modell) for nav-/sidegenerering — eit tredje nivå ville ikkje få eiga portalside utan kodeendring |

Dette er nøyaktig same kostnadstype som den arkiverte evalueringa
peika på i 2026 (scaffolding, `valid-scopes.txt`, mkdocs-nav,
gen-doc-stiar), berre no stadfesta med konkrete linjenummer og utvida
med skjemaoppdaginga og config-oppdaginga sjølv (dei mest kritiske —
utan desse to køyrer verktøykjeda ikkje i det heile på eit nøsta
skjema).

**Konklusjon: nei, eit nytt katalognivå under `<modell>/` er ikkje eit
levedyktig alternativ utan ein sjølvstendig, systemisk refaktorering**
av minst dei 8 punkta over (og truleg fleire, ikkje uttømmande
grep-søkt) — ei endring som råkar **heile** repoet (alle ~41 skjema
sin skjemaoppdaging), ikkje berre AP-NO-splittinga, for eit behov som
i dag (som i 2026-evalueringa) berre gjeld éin enkelt splitting.
Kostnaden er minst på nivå med, truleg større enn, kostnaden ved
opsjon (a) (7 nye sjølvstendige pakkar) — og attforverre same
type versjonerings-/spesialkode-problem som `submodels:`-fjerninga
nettopp løyste, dersom dei nøsta laga skulle dele manifest med
foreldremodellen (b1-varianten). Sjølv om kvart nøsta lag fekk **eiga**
`build.yaml`/release-please-pakke (unngår versjoneringsproblemet),
måtte discovery-mekanismane over likevel endrast for at dei skulle
verte funne i det heile — og gevinsten framfor opsjon (a) (same
mengd sjølvstendige pakkar, berre fysisk nøsta) er då redusert til
reint kosmetisk katalog-gruppering, som ikkje forsvarar kostnaden av
å endre 8 stader i verktøykjeda.

**Tilråding ved fyrste gjennomgang:** forkast opsjon (b2) (nytt
katalognivå) heilt. Ved nærare, meir presis kodeverifisering (sjå neste
seksjon) viste dette seg å vere for kategorisk — sjølve
*djupn-utvidinga* er billegare enn fyrste gjennomgang antok. Konklusjonen
under nyanserer difor dette punktet.

## Kan målretta, avgrensa tiltak få eit nytt katalognivå til å fungere? (utreda, oppdatert 2026-08-27)

Brukar spurde konkret om vi kunne gjort **avgrensa** tiltak (ikkje ein
brei refaktorering av «alle script») for å støtte eit nytt katalognivå.
Svaret, etter å ha lese kvart av dei 8 kallstadene i kontekst (ikkje
berre søkjemønsteret, men KVA dei gjer med resultatet etterpå):

**Dei fleste av dei 8 stadene er alt djupn-agnostiske i logikken sin —
berre sjølve søkjemønsteret må lausnast, éi linje kvar:**

- `schema_domain`/`schema_name`-makroane i `make/02-schema-discovery.mk`
  (brukt av `SCHEMAS`/`DOMAINS` og alle domene-mål) hentar domene via
  **fast absolutt posisjon** (`$(word 3, ...)` — alltid 3. komponent
  frå repo-rota, uavhengig av kor djupt fila ligg) og modellnamn via
  `notdir(dir(...))` (næraste foreldrekatalog) — **begge er allereie
  korrekte for vilkårleg djupn**. Same mønster stadfesta i
  `find-similar-names.py:74` (`parts[0]`),
  `find-unused-local-definitions.py:354`/`find-similar-names.py:146,224`
  (`.parent.name`), `update-modellkatalog.py:94` (`parts[2]`, fast
  absolutt indeks) og dei tre `cut -d/ -f3`-kalla i
  `batch-gen-xsd.sh`/`batch-asyncapi-validate.sh`/`batch-render-plantuml.sh`/
  `make/10-generator-macros.mk:97` (alle hentar **berre domene**, som
  er trygt). For desse held det å fjerne `-maxdepth`/utvide
  glob-mønsteret (`*/*/`  → `**/`) — ei mekanisk endring utan
  åtferdsendring for eksisterande flate skjema.
- `.github/workflows/generate.yml` sine cache-nøklar (`hashFiles(format(
  'src/linkml/{0}/**', matrix.domain))`, stadfesta linje 271, 519) brukar
  alt rekursiv `**`-glob — **krev ingen endring i det heile**.

**Tre reelle unntak — stader der logikken (ikkje berre mønsteret) må
endrast, alle trivielle enkeltlinje-fiksar, men reelle likevel:**

1. **`src/assets/scripts/makefile/gen-config.sh:23`:**
   `model=$(echo "$yaml" | cut -d/ -f4)` — fast posisjon, ville gje
   **feil** verdi for eit nøsta skjema (t.d. mellomkatalogen sitt namn
   i staden for den faktiske eigarkatalogen sitt). Dette bygger
   `key`-en som `GEN_RDF_SKIP_${key}`/`SHACL_FLAGS_${key}` osv. vert
   namngjeve med i `config.mk` — ein feil her ville gje **stille**
   mismatch mot `schema_key`-makroen (som brukar korrekt
   `notdir(dir(...))`) andre stader, altså at `build.yaml`-overstyringar
   for eit nøsta skjema ville slutte å verke utan synleg feilmelding
   (jf. CLAUDE.md § «Ingen stille feil»). Fiks: byt til
   `model=$(basename "$(dirname "$yaml")")`, same mønster som
   `schema_name`-makroen alt brukar.
2. **`mkdocs/publish.sh:336`:**
   `domain=$(basename "$(dirname "$(dirname "$schema_yaml")")")` — går
   **nøyaktig to nivå opp** frå skjemafila for å finne domene. Korrekt
   for dagens flate struktur (domene/modell/fil), men ville gje **feil**
   domene for eit skjema nøsta eitt nivå djupare (ville returnere
   mellomkatalogen, t.d. "dcat-ap-no", i staden for "ap-no"). Kommentaren
   over (linje 330-331) viser at denne logikken opphavleg vart skriven
   for den no fjerna `submodels:`-mekanismen (delt katalog, ikkje ekstra
   djupn) — kommentaren er alt **forelda** sidan den migreringa. Fiks:
   hent domene som fyrste stikomponent etter `src/linkml/`, uavhengig av
   djupn (t.d. strip `$REPO_ROOT/src/linkml/`-prefiks, ta fyrste
   attverande komponent), ikkje eit fast tal nivå frå fila og oppover.
3. **`find-similar-names.py:263`** (`resolve_name`, brukt av
   `--name`-oppslag): `SCHEMA_DIR.glob(f"*/{name}/{name}-schema.yaml")`
   — eksakt to nivå. Må lausnast til rekursiv glob dersom eit
   `--name dcat-ap-no-aktoer`-oppslag skal finne eit nøsta skjema.

**Kva desse fiksane IKKJE løyser — kostnadsbiletet frå «Negative
konsekvensar» står uendra:**

- **Versjonering:** for at eit nøsta lag skal få uavhengig
  release-please-versjon (unngå akkurat problemet
  `submodels:`-fjerninga løyste — sjå «Kunne eit nytt katalognivå ...»
  over), må det framleis ha **eiga** `build.yaml`/`CHANGELOG.md`/
  release-please-pakke, registrert med sin fulle, nøsta sti som
  pakkenøkkel (release-please støttar vilkårleg nøsta pakkesti, ikkje
  berre éitt nivå — dette er ikkje ein teknisk hindring). Talet på
  formelt styrte AP-NO-pakkar (10 → 17) og heile
  governance-/release-overheadet i «Negative konsekvensar» punkt 1-3 er
  difor **uendra** av å nøste katalogane — det løyser eit anna problem
  (kor filene *ligg*), ikkje kor mange *pakkar* som må styrast.
- **mkdocs-portal-nav:** Steg 1.4 i `publish.sh` (linje 272-291) bygger
  nav-strukturen frå `generated/<domain>/<modell>/`, **ikkje** frå
  `src/linkml/`. `schema_outdir`-makroen (`make/02-schema-discovery.mk`)
  brukar berre domene + næraste foreldrekatalog-namn for output-stien,
  uavhengig av kor mange nivå djupare kjeldefila ligg — eit nøsta
  kjeldeskjema får difor same **flate** `generated/ap-no/<lag>/`-struktur
  som eit ikkje-nøsta skjema ville fått. Nøsting i `src/linkml/` gir
  difor **ingen** synleg gruppering i den publiserte portalen — punkt 4
  i «Negative konsekvensar» (nav-clutter) er difor **òg uendra**.

**Revidert konklusjon:** eit nytt katalognivå er **teknisk gjennomførbart
med eit smalt, identifisert sett målretta fiksar** (3 reelle
logikkendringar + eit titals mekaniske mønster-lausningar) — fyrste
gjennomgang sin karakteristikk «systemisk refaktorering» var for sterkt
formulert. Men den einaste reelle gevinsten samanlikna med opsjon (a)
(7 heilt flate søskenkatalogar under domenet, som krev **null**
skriptendringar og er den etablerte konvensjonen i dag) er **reint
kosmetisk kjeldetre-gruppering** — korleis `dcat-ap-no/`-katalogen ser ut
i ein filutforskar/`ls`. Det løyser verken versjonerings-/
governance-kostnaden (uendra pakketal) eller nav-clutter i portalen
(uendra, sidan generert output er flatt uansett). I tillegg innfører
det ein **andre strukturkonvensjon** (flat vs. nøsta) som kvart
framtidig script som gjer skjemaoppdaging må hugse å støtte — ein liten,
men varig, vedlikehaldstillegg som opsjon (a) ikkje har.

**Tilråding (ved denne gjennomgangen):** ikkje forfølg eit nytt
katalognivå åleine for gevinsten «penare kjeldetre» — kostnaden (3
målretta men reelle kodeendringar, pluss ein ny, varig
strukturkonvensjon å vedlikehalde) overstig ein rein estetisk gevinst
som ikkje løyser noko av dei faktiske problema (governance,
versjonering, nav-clutter) frå «Negative konsekvensar». Dersom den
menneskelege lesbare grupperinga («desse høyrer saman») er det faktiske
behovet, dekkjer `imports:`-grafen og kryssreferansar i
`description.md` dette alt i dag — same løysing som
`specs/done/submodels-eigne-modellkatalogar-vurdering.md` punkt 5 kom
fram til for dei tre tidlegare submodels. **Neste seksjon** utreier
likevel eit brukarframlegg som endrar delar av dette biletet — å droppe
`build.yaml` heilt for delmodell-skjema og hardkode dokumentasjon-berre
generering i staden.

## Kunne vi droppa eiga `build.yaml` per delmodell og hardkode «berre dokumentasjon»? (utreda 2026-08-27)

Brukar føreslo å ikkje krevje ein sjølvstendig `build.yaml` (med fullt
`generators:`-oppsett) for kvart delmodell-skjema, men i staden
**hardkode i pipelinen** at slike skjema berre skal få
dokumentasjonsartefakt generert (ikkje RDF/SHACL/OWL/JSON Schema osv.).
Dette er eit reelt tredje alternativ som delvis, men ikkje heilt,
reduserer kostnaden frå dei to førre seksjonane.

### Manglande `build.yaml` er alt eit godt støtta unntak — men med éitt viktig unntak

Kodeverifisering viser at fråvær av `build.yaml` **allereie** er ein
gracefully handtert tilstand dei fleste stader:

- `src/assets/scripts/utils/schema_meta.py`
  (`detect_policy`, kalla frå `detect-validation-policy.py`) returnerer
  **`bronze`** som dokumentert default når `build.yaml` manglar —
  ingen kodeendring naudsynt.
- `mkdocs/lib/utils/metadata_parsers.sh` (delt av `badges.sh`,
  `om_denne_modellen.sh`, `generated_artifacts.sh` m.fl.) sjekkar
  eksplisitt `[ ! -f "$manifest" ] && return` (eller `&& echo "bronze"`)
  for kvart felt — docssida degraderer allereie grasiøst (viser
  ingenting/bronse-merke) i staden for å feile.
- `description.md`, `CHANGELOG.md` er alt behandla som valfrie overalt
  dei vert lesne (`domene_beskrivelse.sh`, `om_denne_modellen.sh`:
  «dersom den finst»).
- `make validate`/`make lint` (`make/40-validation.mk`) køyrer på
  `$(SCHEMAS)` (skjemaoppdaginga), **ikkje** på `build.yaml`-oppdaginga
  — grunnleggjande LinkML-korrektskapskontroll ville difor framleis
  gjelde delmodell-skjema utan manifest, uendra.

**Det eine staden som IKKJE degraderer grasiøst — og må hardkodast
eksplisitt, slik brukar føreslår:**
`src/assets/scripts/makefile/batch-generate.py` sin
`read_build_yaml_flag()` (linje 236-241) returnerer **`False`** for
**alle** generator-flagg (inkl. `docs`) når `build.yaml` manglar heilt —
i dag ville eit skjema utan manifest få **ingenting** generert, ikkje
engang dokumentasjon. For å oppnå det brukar spør om, må denne
funksjonen (eller eit kall rundt henne) endrast til å kjenne att eit
delmodell-skjema (t.d. via stidjupn — jf. førre seksjon sin
depth-deteksjon) og hardkode `docs`/`erdiagram`/`plantuml` = true,
alt anna = false, **utan** å slå opp i noka `build.yaml`. Dette er éin
konkret, avgrensa kodeendring — ikkje 8.

### Kva dette faktisk sparer — og kva det ikkje gjer

**Sparer:** at nokon må forfatte og vedlikehalde 7 nye
`build.yaml`-filer (generator-flagg, `validation_policy`,
`publish_external`) — hardkodinga fjernar denne
forfattaroppgåva heilt, og garanterer samstundes at ALLE
delmodell-skjema får identisk, korrekt oppsett (ingen risiko for at
nokon gløymer å skru av `rdf`/`owl` for eit skjema som ikkje skal ha
det).

**Løyser IKKJE, og må avklarast eksplisitt:**

1. **`release-please`-pakketalet er eit SEPARAT spørsmål frå
   `build.yaml`.** Uavhengig versjonering (unngå
   `submodels:`-fjerninga sitt versjoneringsproblem på nytt) krev at
   kvar delmodell-katalog er registrert som eigen pakke i
   `release-please-config.json`/`-manifest.json` — dette er
   **katalogsti-basert**, ikkje avhengig av `build.yaml`. Å droppe
   `build.yaml` **treng ikkje** bety å droppe uavhengig versjonering —
   men det er eit **eige, separat vedtak** brukar må ta eksplisitt,
   ikkje noko som fell ut automatisk av å droppe manifestet. Dersom
   uavhengig versjonering vert halden ved lag, står punkt 1-3 i
   «Negative konsekvensar» (pakketal, governance-overhead,
   release-please-støy) **framleis uendra** — hardkodinga sparer
   forfattararbeid, ikkje pakke-/governance-talet.
2. **Ny CI-valideringshòl, må gjerast eksplisitt (ikkje stille) dersom
   akseptert:** `valider-og-analyser`-jobben i `generate.yml`
   (~linje 324) oppdagar valideringsmål ved å søkje etter
   `build.yaml`-filer med ein `generators:`-seksjon
   (`find ... -name build.yaml | ... grep generators:`). Eit
   delmodell-skjema utan `build.yaml` ville difor **aldri** verte
   policy-validert i CI i det heile — ikkje "validert som bronse", men
   **aldri kalla**. Dette er eit anna, i praksis strengare utfall enn
   det `detect_policy` sin bronse-fallback isolert gir inntrykk av
   (den fallbacken gjeld berre når nokon eksplisitt køyrer
   `SCHEMA=<delmodell>` lokalt). Jf. CLAUDE.md § «Ingen stille feil»:
   dersom dette unntaket vert vedteke, må det dokumenterast eksplisitt
   som eit medvite val (t.d. i ein kommentar ved `find`-kallet), ikkje
   berre oppstå som eit biprodukt av manglande fil.
3. **Fastlåst til bronse, permanent.** Utan `build.yaml` er det ingen
   veg til å seinare heve eit delmodell-skjema til silver/gold dersom
   behovet skulle endre seg, utan å då leggje til eit `build.yaml`
   likevel — truleg akseptabelt for reint interne lagdelings-skjema,
   men verdt å seie eksplisitt.

### Revidert biletet

Å droppe `build.yaml` + hardkode dokumentasjon-berre generering er ein
**gjennomførbar, avgrensa presiseringstiltak** (éin kodestad, ikkje 8)
som fjernar forfattar-/vedlikehaldsbyrda av 7 manifestfiler. Det
**endrar likevel ikkje** kjernekonklusjonen frå dei to førre
seksjonane med mindre brukar **også** vel å droppe uavhengig
release-please-versjonering for delmodell-skjemaa (eit separat val) —
og **det** valet ville reintrodusere nøyaktig det
versjoneringsproblemet `submodels:`-fjerninga løyste for 10 dagar
sidan. Kombinasjonen «eige katalognivå + eiga release-please-pakke
(behald uavhengig versjon) + hardkoda dokumentasjon-berre generering
(drop `build.yaml`)» er den kombinasjonen som fjernar mest kostnad utan
å reintrodusere kjende, allereie løyste problem — men ho løyser
framleis ikkje nav-clutter (punkt 4) eller governance-klassifiseringa
(punkt 2) i «Negative konsekvensar», sidan begge er uavhengige av
`build.yaml` sin eksistens.

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

1. **Brukarvedtak (utvida etter kostnadsutreiinga over):** godkjenn/juster
   tilrådd lagdeling (alternativ 1+3+4), **og** vel eksplisitt mellom
   (a) godta full pakke-/governance-kostnaden (10 → 17 formelt styrte
   AP-NO-pakkar) eller (b1) reintrodusere delt-katalog/manifest for
   denne splittinga — sjå «Negative konsekvensar» over. **Eit nytt
   katalognivå (b2) er forkasta** (sjå eigen seksjon over) og krev
   ikkje eit separat vedtakspunkt. Utan vedtak 1 kan ikkje steg 4-6
   startast.
2. Verifiser klasse-til-lag-tilordning mot alle 19 konsumentskjema (jf.
   opne spørsmål punkt 2)
3. Avklar/rett silver/gull sitt `container_*`-krav (opne spørsmål punkt 1)
   — truleg eiga, mindre spec før modul-migrering kan reknast som
   sølv-konform for smalare lag
4. Dersom vedtak 1(a): registrer 7 nye pakkar i
   `.github/release-please-config.json` og
   `.github/release-please-manifest.json` (component/release-type +
   startversjon), opprett katalogstruktur (`build.yaml`,
   `description.md`, `CHANGELOG.md`) for kvar, **før** sjølve
   fil-splittinga. Dersom vedtak 1(b1): merk at dette reintroduserer
   nøyaktig den `submodels:`-mekanismen og dei versjonerings-/
   spesialkode-problema `specs/done/submodels-eigne-modellkatalogar-vurdering.md`
   nettopp fjerna — krev eksplisitt grunngjeving for kvifor unntaket
   er verdt det denne gongen.
5. Implementer sjølve fil-splittinga (`dcat-ap-no-*-schema.yaml`,
   `dqv-slots-schema.yaml`, `dqv-vokabular-schema.yaml`) + facade-import
   i eksisterande `dcat-ap-no-schema.yaml`/`dqv-core-schema.yaml`
6. Oppdater `modelldcat-katalog-schema.yaml` til å importere
   `dcat-ap-no-ressurs-schema` i staden for full `dcat-ap-no-schema`
7. Oppdater `new-modell.sh` til å spørje om AP-NO-lag i staden for å
   hardkode full `dcat-ap-no`-import
8. Migrer identifiserte lette konsumentar
   (`javazonetalk`, `bvrbekreftelse`, `bvrettersendingavvedlegg`,
   `bvrstiftelsesdokument`, `bvrinnfelles`, `frivilligorganisasjonapi`)
   til minimale importar, fjern «TODO: endre/legg til imports etter
   behov»-kommentaren
9. Mål faktisk `make lint`/`make validate`/`generate.yml`
   `merge`-steg-tidsgevinst i CI for migrerte konsument-domene **og**
   den motsette effekten for `ap-no`-domenet sin eigen
   `generate`/`valider-og-analyser`-køyring (jf. «Negative
   konsekvensar» punkt 6), koordiner med
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
- [x] Utreidd negative konsekvensar/kostnader ved oppdeling, verifisert
      mot `CONVENTIONS.md` («éin modell per katalog»-regelen),
      `GOVERNANCE.md` (felles infrastruktur-status, RFC-terskel),
      `release-please`-konfigurasjonen (pakketal), `mkdocs/publish.sh`
      (nav-generering) og `ap-no` sin status som eige CI-domene
- [x] Utreidd om eit nytt katalognivå under `<modell>/` kunne brukast til
      å samle delmodellar — same konklusjon som
      `specs/done/modellkatalog-fleire-skjema-evaluering.md` (2026,
      spørsmål 3) og `specs/done/submodels-eigne-modellkatalogar-vurdering.md`
      (2026-08-17): ikkje tilrådd
- [x] Utreidd om **målretta** (ikkje systemiske) tiltak kunne fått eit nytt
      katalognivå til å fungere — stadfesta **teknisk gjennomførbart**
      (dei fleste av dei 8 stadene er alt djupn-agnostiske, berre 3
      reelle enkeltlinje-logikkfiksar identifiserte:
      `gen-config.sh:23`, `mkdocs/publish.sh:336`,
      `find-similar-names.py:263`), men gevinsten samanlikna med flate
      søskenkatalogar er reint kosmetisk — løyser ikkje versjonerings-,
      governance- eller nav-clutter-kostnaden frå «Negative
      konsekvensar». Ikkje tilrådd åleine for den gevinsten.
- [x] Utreidd om `build.yaml` kan droppast per delmodell-skjema til
      fordel for hardkoda dokumentasjon-berre generering — stadfesta
      **gjennomførbart** med éin konkret kodeendring
      (`batch-generate.py` sin `read_build_yaml_flag()`), sidan
      fråvær av `build.yaml` alt er grasiøst handtert dei fleste andre
      stader (`detect_policy` → bronse-default,
      `metadata_parsers.sh` → tomme/bronse-fallbackar,
      `description.md`/`CHANGELOG.md` alt valfrie). Sparer
      forfattararbeidet med 7 manifestfiler, men løyser **ikkje**
      pakketal/governance/nav-kostnaden med mindre uavhengig
      release-please-versjonering **også** droppast — noko som ville
      reintrodusere versjoneringsproblemet frå
      `submodels:`-fjerninga. Identifiserte eit nytt, eksplisitt
      CI-valideringshòl (delmodell-skjema utan `build.yaml` ville aldri
      verte policy-validert i `valider-og-analyser`) som må
      dokumenterast medvite, ikkje stille, dersom vedteke.
- [ ] Brukarvedtak om kva alternativ som skal implementerast, **inkludert**
      vedtak om pakke-/governance-kostnaden i «Negative konsekvensar» er
      akseptabel, om eit unntak frå «éin modell per katalog» skal
      forfølgjast, og om `build.yaml`/uavhengig versjonering skal
      droppast for delmodell-skjema — **ikkje gjort, krev brukarinput**.
      Specen vert verande i `specs/backlog/` til vedtak er gjort.

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
- `CONVENTIONS.md` (linje 17-24) — «éin modell per katalog»-regelen som
  gjer kvart nytt lag til ein eigen release-please-pakke (kjelde til
  «Negative konsekvensar» punkt 1)
- `GOVERNANCE.md` (linje 84-103, 269-334) — governance-status og
  RFC-terskel for «felles infrastruktur» (`src/linkml/ap-no/`), grunnlag
  for «Negative konsekvensar» punkt 2
- `.github/release-please-config.json`,
  `.github/release-please-manifest.json` — dagens 37 manuelt registrerte
  pakkar, grunnlag for «Negative konsekvensar» punkt 3
- `mkdocs/publish.sh` (linje 268-275) — nav-generering per skjemakatalog,
  grunnlag for «Negative konsekvensar» punkt 4
- `src/linkml/ap-no/dcat-ap-no/build.yaml`
  (`external_spec_url`/`external_spec_label`),
  `src/linkml/ap-no/dcat-ap-no/description.md` — kopling til den
  eksterne Digdir-spesifikasjonen, grunnlag for «Negative konsekvensar»
  punkt 5
- `make/02-schema-discovery.mk` (`print-domains`),
  `.github/actions/discover-domains/action.yml` — stadfestar at `ap-no`
  er eit eige CI-matrise-domene, grunnlag for «Negative konsekvensar»
  punkt 6
- `specs/done/modellkatalog-fleire-skjema-evaluering.md`,
  `specs/done/submodels-eigne-modellkatalogar-vurdering.md` — dei to
  tidlegare vurderingane av eit tredje grupperingsnivå/delt katalog,
  grunnlag for «Kunne eit nytt katalognivå under modell løyst dette?»
- `make/02-schema-discovery.mk:13,22-25`, `make/40-validation.mk:113`,
  `src/assets/scripts/makefile/gen-config.sh:18,22-23`,
  `src/assets/scripts/makefile/{check-iri-resolution,find-similar-names,find-unused-local-definitions,update-modellkatalog}.py`,
  `mkdocs/publish.sh:272,275,334-339` — dei 8 stadene med hardkoda
  2-nivå katalogdjupn, og (etter grundigare gjennomgang) grunnlaget for
  kvifor dei fleste er djupn-agnostiske i logikken sin medan tre
  (`gen-config.sh:23`, `mkdocs/publish.sh:336`,
  `find-similar-names.py:263`) krev reelle enkeltlinje-fiksar
- `mkdocs/lib/sections/delmodellar.sh` — dormant spesialkode frå den
  fjerna `submodels:`-mekanismen, stadfesta framleis til stades
- `.github/workflows/generate.yml:271,519` — cache-nøklane sin
  `hashFiles(format('src/linkml/{0}/**', ...))` er alt rekursiv og
  krev ingen endring for nøsta skjema
- `src/assets/scripts/makefile/batch-generate.py:236-241`
  (`read_build_yaml_flag`) — den eine staden som *ikkje* degraderer
  grasiøst ved manglande `build.yaml` (returnerer `False` for alle
  flagg, inkl. `docs`); grunnlag for kvar hardkodinga må gjerast
- `src/assets/scripts/utils/schema_meta.py` (`detect_policy`),
  `mkdocs/lib/utils/metadata_parsers.sh`,
  `mkdocs/lib/sections/{om_denne_modellen,domene_beskrivelse}.sh` —
  stadfestar at manglande `build.yaml`/`description.md` alt er
  grasiøst handtert (bronse-default, tomme felt) dei fleste andre
  stader
- `.github/workflows/generate.yml` (~linje 324, `valider-og-analyser`-
  jobben sitt `find ... -name build.yaml | grep generators:`) — kjelda
  til det nye, eksplisitte CI-valideringshòlet dersom `build.yaml`
  droppast for delmodell-skjema
