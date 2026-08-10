# Gap-analyse: repoet mot Digdir sin veileder "Orden i eget hus"

**Opprett:** 2026-08-10
**Status:** Utført

## Bakgrunn

Brukaren ba om å evaluere gapet mellom dette repoet og Digdir sin veileder
[«Orden i eget hus»](https://www.digdir.no/informasjonsforvaltning/veileder-orden-i-eget-hus/2716).
Veilederen er skriven for **ei enkelt offentleg verksemd** som skal skaffe
seg oversikt over eigne data, og er strukturert i sju steg:

1. Planlegge — forankring og mål i verksemda
2. Prioritere — kva data skal kartleggjast først
3. Kartlegge — dokumentere datasett og omgrep i ei oversikt
4. Vurdere tilgangsnivå — klassifisere tilgang (trafikklyssystemet) og lovheimel
5. Beskrive — metadatafelt for datasett og omgrep
6. Tilgjengeliggjøre — publisere oversikta internt og eksternt (Felles datakatalog/begrepskatalog)
7. Styre og forvalte — kontinuerleg forvaltning av oversikta

Alle sju steg-sidene er henta og analyserte, i tillegg til hovudsida.
Samanlikninga er gjort mot `SCOPE.md`, `PRINCIPLES.md`, `GOVERNANCE.md`,
`src/mcp-linkml-validator/policies/README.md`,
`src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`,
`src/linkml/ap-no/skos-ap-no/skos-ap-no-schema.yaml`, og
`mkdocs/docs/kom-i-gang/ny-domenemodell.md`.

## Samandrag

Veilederen dekkjer heile prosessen ei verksemd må gjennom for å få oversikt
over eigne data — frå organisatorisk forankring til teknisk publisering.
Dette repoet er **eit verktøyrepo for informasjonsmodellering**
([SCOPE.md](../../SCOPE.md)), ikkje eit verktøy for heile
"orden i eget hus"-prosessen. Repoet sin funksjonalitet fell difor naturleg
inn i berre tre av dei sju stega:

| Steg | Relevans for repoet |
|---|---|
| 1. Planlegge | Utanfor scope — organisatorisk forankring i den enkelte verksemda |
| 2. Prioritere | Utanfor scope — organisatorisk prioritering før modellering startar |
| 3. Kartlegge | **I scope** — LinkML-modellering og begrep-verktøy (`mcp-linkml-modell-utkast`, `mcp-linkml-begrep-utkast`) er sjølve dokumentasjonsmekanismen |
| 4. Vurdere tilgangsnivå | **Delvis i scope** — feltet finst i skjemaet, men er ikkje handheva av policy-hierarkiet (sjå Gap 1) |
| 5. Beskrive | **I scope** — kjernefunksjonen til repoet: DCAT-AP-NO/SKOS-AP-NO/ModellDCAT-AP-NO/DQV-AP-NO-skjema dekkjer metadatafelta veilederen etterspør |
| 6. Tilgjengeliggjøre | **I scope** — pull-basert publisering til Felles datakatalog/begrepskatalog er sjølve arkitekturprinsippet ([PRINCIPLES.md § 6](../../PRINCIPLES.md#6-pull-ikkje-push)) |
| 7. Styre og forvalte | Delvis i scope — `GOVERNANCE.md` dekkjer roller, eigarskap, RFC-prosess og utmelding grundig, men for repoet sin infrastruktur, ikkje for den enkelte verksemda si løpande datastyring |

Dei tre stega repoet faktisk dekkjer (3, 5, 6) er **godt implementerte**.
Det eine identifiserte strukturelle gapet er at steg 4 (tilgangsnivå) har eit
felt i skjemaet, men ingen handheving i valideringspolicyane — resten av
funna er dokumentasjons- og kryssreferansegap.

## Identifiserte gap

### Gap 1: Tilgangsnivå og lovheimel er ikkje del av noka valideringspolicy

Digdir steg 4 sitt kjernekrav er at kvart kartlagt datasett skal ha eit
**vurdert og dokumentert tilgangsnivå** (trafikklyssystemet: grøn/gul/raud)
og ei **oppgitt lovheimel**. Repoet har begge felta i
`dcat-ap-no-schema.yaml`:

- `tilgangsrettigheter` → `dct:accessRights`, med kontrollert vokabular EU
  Access Right (`PUBLIC`/`RESTRICTED`/`NON_PUBLIC` — funksjonelt tilsvarande
  grøn/gul/raud), markert `Anbefalt` på `Datasett`
- `gjeldende_lovgivning` → `dcatap:applicableLegislation`, markert
  `Anbefalt` på `Datasett`

Men ingen av felta er sjekka i bronze-, silver- eller gold-policyen
(`src/mcp-linkml-validator/policies/README.md`). Ein katalogeigar kan difor
validere eit skjema på `gold`-nivå — repoets høgaste kvalitetsnivå — utan at
tilgangsnivå eller lovheimel nokon gong er vurdert eller dokumentert for eit
einaste datasett. Dette er eit gap mot Digdir-regel 12 (Rettar/tilgang) og
steg 4 spesifikt.

**Forslag:**
1. Legg til ein `warning`-sjekk på `silver`-nivå i
   `src/mcp-linkml-validator/policies/silver.yaml` (eller tilsvarande) som
   flaggar `Datasett`-instansar/klassar utan `tilgangsrettigheter` i
   `slot_usage`, tilsvarande mønsteret for `dcat:theme`/`dct:publisher`.
2. Legg til ei kort forklarande kryssreferanse i policy-READMEen som koplar
   `dct:accessRights`-verdiane til Digdir sitt trafikklyssystem
   (PUBLIC≈grøn, RESTRICTED≈gul, NON_PUBLIC≈raud), med lenke til
   [steg 4](https://www.digdir.no/informasjonsforvaltning/steg-4-vurdere-tilgangsniva/2723),
   slik at brukarar som kjenner veilederen kjenner igjen omgrepet att i
   repoet.

### Gap 2: Ingen kopling mellom repoets inngangspunkt og steg 1-4 i veilederen

`mkdocs/docs/kom-i-gang/ny-domenemodell.md` forklarer **korleis** ein
modellerer eit domene i LinkML, men føreset implisitt at organisasjonen
allereie har gjennomført kartlegging, prioritering og
tilgangsnivå-vurdering (steg 1-4 i veilederen) — utan å seie det eksplisitt
eller lenkje vidare til veilederen for organisasjonar som ikkje har gjort
dette enno. Ein ny brukar som kjem rett frå Digdir sin veileder (t.d. etter
å ha lese steg 5 "Beskrive") får dermed ikkje nokon peikepinn om at repoet
tek over frå og med steg 3/5, eller at steg 1, 2 og 4 bør vere avklarte
først.

**Forslag:** Legg til ei kort innleiingsboks øvst i `ny-domenemodell.md` som
seier at repoet dekkjer steg 3 (kartlegge → modellere), 5 (skildre →
LinkML-skjema) og 6 (tilgjengeleggjere → publisere) i Digdir sin
"orden i eget hus"-veileder, med lenke til veilederen for organisasjonar som
treng å gjennomføre steg 1, 2 og 4 først.

### Gap 3: Kjeldetype (autoritativ vs. avleidd) er ikkje eksplisitt dokumentert som bruksområde for provenance-felta

Digdir steg 5 tilrår å dokumentere om eit datasett er sjølvinnsamla
("autoritativt") eller kopiert/samanstilt frå andre kjelder ("avleidd").
Repoet har `dct:provenance`, `prov:wasGeneratedBy` og
`prov:qualifiedAttribution` i `dcat-ap-no-schema.yaml` som kan uttrykkje
dette, men felta er generiske proveniens-felt — det er ikkje dokumentert
nokon stad at dei bør brukast til nettopp autoritativ/avleidd-skiljet
veilederen etterspør.

**Forslag:** Legg til éin setning i `dct:provenance`-slotens `description`
eller i policy-READMEen som viser korleis feltet kan nyttast til å skildre
kjeldetype, jf. steg 5. Lågt prioritert — dette er eit presiseringsgap, ikkje
eit strukturelt hol (feltet finst og valideringspolicyen presser ikkje på
temaet).

## Ikkje-gap (vurdert, men ingen tiltak)

- **Steg 1 (Planlegge) og steg 2 (Prioritere):** Reint organisatoriske steg
  som skjer i den einskilde verksemda før dei tek i bruk repoet. `SCOPE.md`
  er allereie eksplisitt på at repoet er eit verktøyrepo, ikkje eit
  styringsverktøy for heile datalandskapet til ei verksemd. Ingen tiltak.
- **Steg 3 (Kartlegge) — dataset-granularitet:** Veilederen åtvarar mot
  «uendeleg mange små» eller «for få, breie» datasett.
  `PRINCIPLES.md` sitt importhierarki og éin-klasse-per-domeneomgrep-mønster
  gir allereie tilsvarande rettleiing for LinkML-modellering. Ingen tiltak.
- **Steg 3 — begrepskartlegging:** Dekt av `mcp-linkml-begrep-utkast` og
  SKOS-AP-NO-skjemaet (`definisjon`, `gyldig_fra`/`gyldig_til`,
  `tillate_term`/`forkasta_term`, `fagomrade`, `kontaktpunkt_vcard`). Ingen
  tiltak.
- **Steg 5 — minimumsfelt (eigar, tittel, tema, innhaldsskildring,
  lovheimel):** Dekt av `utgiver`/`dct:publisher`, `tittel`, `dcat:theme`
  (Los), `dct:description` og `gjeldende_lovgivning` — alle handheva som
  `error` på `silver`-nivå (unnateke lovheimel, sjå Gap 1). Ingen tiltak.
- **Steg 5 — datakvalitet (relevans, fullstendigheit, nøyaktigheit,
  tilgjengelegheit):** Dekt av `dqv-ap-no-schema.yaml`
  (`Kvalitetsdimensjon`, `Kvalitetsmaaling`, `Kvalitetsmerknad`), som er ein
  av AP-NO-profilene repoet allereie implementerer og handhevar på
  `silver`-nivå. Ingen tiltak.
- **Steg 5 — kontaktperson/ansvarleg på detaljert nivå:** Dekt av
  `dcat:contactPoint`/vCard-strukturen, som kan peike til
  seksjon/avdeling/enkeltperson. Ingen tiltak.
- **Steg 6 — ekstern tilgjengeleggjering via Felles datakatalog/
  begrepskatalog:** Repoet sin heile publiseringsarkitektur
  (`publish_external: true`, `felles-datakatalog`/`felles-begrepskatalog`-
  policyane, GitHub Pages som haustingsendepunkt) er direkte bygd for dette
  steget, og er allereie handsama grundig i
  `specs/done/gap-sharing-data-norge-no.md`. Ingen nye tiltak.
- **Steg 6 — intern tilgjengeleggjering:** Gjeld verksemda sitt interne
  intranett/fildeling, utanfor repoets virkeområde. Ingen tiltak.
- **Steg 7 (Styre og forvalte):** `GOVERNANCE.md` dekkjer roller,
  eigarskap, RFC-prosess for brytande endringar, utmeldingsprosedyre og
  konflikthandtering svært grundig for repoets eiga infrastruktur. Dette
  er ikkje det same som ei verksemd si løpande forvaltning av eiga
  datainventar (som er utanfor scope), men repoet sin eigen governance-modell
  følgjer prinsippa i steg 7 (tydelege roller, byggjer på eksisterande
  strukturar, jamleg revurdering via RFC). Ingen tiltak.

## Handlingsliste

- [x] Legg til warning-sjekk for manglande `tilgangsrettigheter` på
      `Datasett` i silver-policyen, og kryssreferanse til Digdir sitt
      trafikklyssystem i `src/mcp-linkml-validator/policies/README.md`
      (Gap 1)
- [x] Legg til innleiingsboks i `mkdocs/docs/kom-i-gang/ny-domenemodell.md`
      som koplar repoet til steg 3/5/6 i veilederen, med lenke til
      veilederen for steg 1/2/4 (Gap 2)
- [x] Legg til presisering om kjeldetype (autoritativ/avleidd) ved
      `dct:provenance`-slotens `description` eller i policy-READMEen
      (Gap 3)

Alle tre tiltak er reint dokumentasjons-/policyarbeid (Gap 1 krev ei
policy-YAML-endring, Gap 2 og 3 er rein Markdown) og kan gjerast uavhengig
av kvarandre. Ingen av tiltaka krev skjemabrytande endringar.

## Utført

- `src/mcp-linkml-validator/policies/silver.yaml`: nye sjekkar
  `datasett_tilgangsrettigheter` (`dct:accessRights`, warning) og
  `datasett_lovgivning` (`dcatap:applicableLegislation`, warning) på
  `Datasett`
- `src/mcp-linkml-validator/policies/gold.yaml`: same to sjekkane
  oppgraderte til `error` (følgjer mønsteret til `distribusjon_lisens`)
- `src/mcp-linkml-validator/policies/README.md`: nye rader i silver- og
  gold-tabellane, pluss ein forklarande merknad som koplar
  `dct:accessRights`-verdiane (PUBLIC/RESTRICTED/NON_PUBLIC) til Digdir sitt
  trafikklyssystem (grøn/gul/raud) og `dcatap:applicableLegislation` til
  lovheimel-kravet i steg 4
- `mkdocs/docs/kom-i-gang/ny-domenemodell.md`: ny innleiingsboks som
  koplar rettleiinga til steg 3/5/6 i veilederen, med lenkjer til steg
  1/2/4 for organisasjonar som ikkje har gjennomført desse enno
- `src/linkml/ap-no/dcat-ap-no/dcat-ap-no-schema.yaml`: presisert
  `description` på `eierskapshistorikk`-sloten (`dct:provenance`) med
  kjeldetype-bruk (autoritativ/avleidd), jf. steg 5
- Verifisert: dei to nye sjekkane gir warning på
  `referansemodell-silver-schema.yaml` (manglar felta) og ingen falske
  positive på `dcat-ap-no-schema.yaml` sjølv (har felta frå før).
  `make lint`/`make roundtrip` på `dcat-ap-no-schema.yaml` framleis grøne
  (lint-åtvaringane er kjende, urelaterte `canonical_prefixes`-varsel)
