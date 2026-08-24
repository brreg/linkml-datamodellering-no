# Kartlegging: Repoet mot Digdirs Rammeverk for informasjonsforvaltning

**Kjelde:** [digdir.no/informasjonsforvaltning/rammeverk-informasjonsforvaltning/3626](https://www.digdir.no/informasjonsforvaltning/rammeverk-informasjonsforvaltning/3626)
**Målgruppe for rammeverket:** Arkitektar og ansvarlege for informasjonsforvaltning i offentlege verksemder
**Formål med rammeverket:** «Skal gi tilstrekkelige føringer og støtte slik at offentlige virksomheter kan utveksle og dele data og beskrivelser av data, også maskinelt.»

---

## Bakgrunn

Eit av måla med `linkml-datamodellering-no` er å realisere Digdirs Rammeverk for
informasjonsforvaltning som eit nasjonalt verktøy (jf. `SCOPE.md`: «eit felles
grunnlag — ein stad der norske offentlege verksemder kan hente og gjenbruke
modellar»). Rammeverket er strukturert i tre pilarar pluss fire kjerneprinsipp:

| Pilar | Tal ressursar | Innhald |
|---|---|---|
| **Veiledere** | 7 | Prosess- og metoderettleiarar (orden i eget hus, opne data, datakvalitet, informasjonssikkerheit, språkdata) |
| **Standarder og spesifikasjoner** | 11 | Tekniske applikasjonsprofilar og vokabular (DCAT-AP-NO, SKOS-AP-NO, ModelDCAT-AP-NO, DQV-AP-NO, XKOS-AP-NO, Los, URI-standard, Termlosen, TBX, begrepsharmonisering, retningslinjer opne data) |
| **Informasjonsmodellar** | 5 | Modelleringsprinsipp, -reglar og to felles domenemodellar (Person og Enhet, Adresse) |

**Kjerneprinsipp:** Orden i eget hus · «Kun én gang»-prinsippet · Maskinell
datautveksling · Felles standardar.

Repoet har **allereie 17 detaljerte `avvik-*.md`-kartlegginger** i
`specs/done/` mot enkeltelement i rammeverket (dei fleste er `Utført`), pluss
éin open i `specs/backlog/` (`avvik-peikarar-til-offentlege-ressursar.md`,
3 av 5 tiltak attståande). Denne spesifikasjonen har difor to jobbar:

1. **Syntetisere** dei eksisterande kartleggingane til éi samla oversikt
   strukturert etter rammeverket sjølv (§ Rammeverksdekning nedanfor), med
   status og kryssreferanse per ressurs.
2. **Fylle dei attverande gapa** — sju rammeverkselement som aldri har vore
   kartlagt mot repoet: Modenhetsmodell for orden i eget hus, Internkontroll
   i praksis, Veileder for høsting og deling av språkdata, Forvaltningsstandard
   for begrepsharmonisering/-differensiering, TBX-AP-NO, Person og Enhet, og
   Adresse (dei to siste sett mot `ngr-person`/`ngr-adresse` og
   `enhetsregisteret-bvrinn`).

---

## Metode / steg

1. Hent offisiell struktur for rammeverksida og fulltekst for dei sju udekte
   delressursane (kjeldene er lista i kvar delseksjon nedanfor).
2. Les status/konklusjon i alle 17 eksisterande `avvik-*.md`-spesifikasjonar
   i `specs/done/` og den opne i `specs/backlog/`.
3. Samanlikn `ngr-adresse-schema.yaml`, `ngr-person-schema.yaml` og
   `enhetsregisteret-bvrinn-schema.yaml` mot Digdirs Person/Enhet- og
   Adresse-modellar klasse for klasse.
4. Bygg rammeverk-strukturtabell: pilar → ressurs → status → kjelde.
5. Vurder dei fire kjerneprinsippa på arkitekturnivå (ikkje per-skjema).
6. Skriv nye korte delkartlegginger for dei sju udekte elementa.
7. Samle attverande gap i éi prioritert handlingsliste.
8. Skriv heilskapleg konklusjon.

Steg 1-3 er gjennomførte som grunnlag for innhaldet under. Steg 4-8 er
resultatet, presentert nedanfor.

---

## Rammeverksdekning — samla tabell

### Pilar 1: Veiledere (7)

| Ressurs | Status | Kjelde/kryssreferanse |
|---|---|---|
| Orden i eget hus | ✅ Kartlagt, i hovudsak utført | `specs/done/avvik-veileder-orden-i-eget-hus.md` |
| Modenhetsmodell for orden i eget hus | ⚪ Kartlagt no (§ nedanfor) — organisatorisk sjølvvurdering, avgrensa direkte relevans | Ny, sjå under |
| Tilgjengeliggjøring av åpne data | ✅ Kartlagt, delvis utført (nokre tiltak krev fagkunnskap frå codeowners) | `specs/done/avvik-veileder-apne-data.md` |
| Beskrivelse av kvalitet på datasett (kvantifiserbar) | ✅ Kartlagt, utført | `specs/done/avvik-veileder-kvantifiserbar-kvalitet.md` |
| Internkontroll i praksis for informasjonssikkerheit | ⚪ Kartlagt no (§ nedanfor) — organisatorisk, avgrensa teknisk relevans | Ny, sjå under |
| Veileder for informasjonsmodellar (ModellDCAT-AP-NO) | ✅ Kartlagt, i hovudsak utført | `specs/done/avvik-veileder-modelldcat-ap-no.md` |
| Veileder for høsting og deling av språkdata | ⚪ Kartlagt no (§ nedanfor) — relevant, ingen tiltak tilrådd enno | Ny, sjå under |

### Pilar 2: Standarder og spesifikasjoner (11)

| Ressurs | Status | Kjelde/kryssreferanse |
|---|---|---|
| DCAT-AP-NO | ✅ Kartlagt, utført | `specs/done/avvik-dcat-ap-no.md` |
| SKOS-AP-NO Begrep | ✅ Kartlagt, i hovudsak utført | `specs/done/avvik-skos-ap-no.md` |
| Termlosen (omgrepsanalyse) | ✅ Kartlagt, i hovudsak utført | `specs/done/avvik-termlosen.md` |
| Forvaltningsstandard for begrepsharmonisering/-differensiering | ⚪ Kartlagt no (§ nedanfor) — samsvar via SKOS-AP-NO sine relasjonsklasser | Ny, sjå under |
| TBX-basert tilgjengeliggjøring (TBX-AP-NO) | ⚪ Kartlagt no (§ nedanfor) — **reelt gap identifisert** | Ny, sjå under |
| Retningslinjer ved tilgjengeliggjøring av offentlege data | ✅ Kartlagt, utført | `specs/done/avvik-retningslinjer-apne-data.md` |
| DQV-AP-NO | ✅ Kartlagt, løyst | `specs/done/avvik-dqv-ap-no.md` |
| ModelDCAT-AP-NO | ✅ Kartlagt, utført (delt i modell/katalog-skjema) | `specs/done/avvik-modelldcat-ap-no.md` |
| Los (klassifiseringsvokabular) | ✅ Kartlagt, utført | `specs/done/avvik-los.md` |
| Standarder for URI-peikarar til offentlege ressursar | 🟡 Kartlagt, **delvis utført** (2/5 tiltak ope) | `specs/backlog/avvik-peikarar-til-offentlege-ressursar.md` |
| XKOS-AP-NO | ✅ Kartlagt, i hovudsak utført | `specs/done/avvik-xkos-ap-no.md`, `specs/done/xkos-ap-no-resterande-avvik.md` |

*(Repoet implementerer i tillegg CPSV-AP-NO, som ikkje er lista på
rammeverksida, men høyrer til same standardfamilie — sjå
`specs/done/avvik-cpsv-ap-no.md`, utført.)*

### Pilar 3: Informasjonsmodellar (5)

| Ressurs | Status | Kjelde/kryssreferanse |
|---|---|---|
| Introduksjon til informasjonsmodellar (PPT) | N/A — informasjonsmateriell, ingen teknisk motpart å kartleggje | — |
| Ni designprinsipper for informasjonsmodellar | ✅ Kartlagt, i hovudsak utført | `specs/done/avvik-prinsipper-informasjonsmodeller.md` |
| Felles modelleringsregler for offentleg forvaltning (15 reglar) | ✅ Kartlagt, alle 15 reglar dekt av MCP-validator | `specs/done/avvik-felles-modelleringsregler.md` |
| Person og Enhet — felles informasjonsmodell | ⚪ Kartlagt no (§ nedanfor) — sterkt samsvar i sak, ingen 1:1-mapping | Ny, sjå under |
| Adresse — felles informasjonsmodell | ⚪ Kartlagt no (§ nedanfor) — sterkt samsvar, 1 mindre avvik | Ny, sjå under |

### Kjerneprinsipp

| Prinsipp | Vurdering |
|---|---|
| **Orden i eget hus** | Repoet gir *verktøya* (skjemabibliotek, validering, publisering) som steg 3 og 5 i veilederen (kartlegge/beskrive) treng, men kan ikkje utføre steg 1/2/4/6/7 (forankring, prioritering, tilgangsvurdering, endeleg tilgjengeleggjering) for ei einskild verksemd — det er per design (repoet er eit delt verktøy, ikkje ei verksemds eiga kartlegging, jf. `SCOPE.md`). Sterk *støtte*, ikkje sjølve *gjennomføringa*. |
| **«Kun én gang»-prinsippet** | Sterkt implementert på modelleringsnivå gjennom import-hierarkiet (klasser/slots definert éin stad, importert nedover, jf. `PRINCIPLES.md`) og gjennom lenkingsprinsippet (URI-referansar mellom instansar i staden for duplisering/inlining). Dette er strukturelt likt DRY-prinsippet CLAUDE.md handhevar for koden sjølv. |
| **Maskinell datautveksling** | Kjernen i verktøykjeda: LinkML genererer RDF/TTL, JSON-LD, JSON Schema, SHACL, OWL, PlantUML/ER-diagram og protobuf frå éi kjelde. Sterkast dekte prinsippet i repoet. |
| **Felles standardar** | Repoet *er* i stor grad ein samling implementasjonar av felles standardar (DCAT-AP-NO, SKOS-AP-NO, ModelDCAT-AP-NO, DQV-AP-NO, XKOS-AP-NO, CPSV-AP-NO, Los) — den andre sterkast dekte pilaren. |

---

## Nye delkartlegginger

### Modenhetsmodell for orden i eget hus

**Kjelde:** [digdir.no/.../modenhetsmodell-orden-i-eget-hus/2124](https://www.digdir.no/informasjonsforvaltning/modenhetsmodell-orden-i-eget-hus/2124)

Modellen er eit **sjølvvurderingsverktøy** ei einskild verksemd fyller ut for
å måle eiga modenheit i informasjonsforvaltning — sjølve
vurderingsskjemaet ligg bak eit interaktivt verktøy på data.norge.no, ikkje
som ein nedlastbar teknisk spesifikasjon. Repoet kan difor ikkje «kartleggjast
mot» modellen på same måte som eit dataformat.

**Vurdering:** Ikkje direkte aktuelt for eit delt verktøyrepo (repoet er
ikkje éi verksemd som skal sjølvvurderast). Repoet fungerer derimot som
*infrastruktur* som hevar modenheita for verksemder som tar det i bruk —
dei får eit ferdig skjemabibliotek, valideringsrøyrsle og
publiseringsmekanisme utan å byggje det sjølv. Ingen tiltak tilrådd.

### Internkontroll i praksis for informasjonssikkerheit

**Kjelde:** [digdir.no/.../internkontroll-i-praksis-informasjonssikkerhet/2601](https://www.digdir.no/informasjonssikkerhet/internkontroll-i-praksis-informasjonssikkerhet/2601)

Rettleiaren er **organisatorisk** — styringsaktivitetar, risikovurdering og
fellessikring for leiinga i ei verksemd. Ikkje eit teknisk dataformat.

**Vurdering:** Avgrensa direkte relevans for eit skjemabibliotek. Repoet har
likevel tilstøytande infrastruktur som understøttar tilsvarande mål:
`dct:accessRights`/trafikklyssystem-mappinga (jf.
`avvik-veileder-orden-i-eget-hus.md`), CODEOWNERS-basert
gjennomgangsplikt, og `specs/done/security-pipeline-og-sbom.md` (SBOM/
sikker CI-pipeline). Ingen nye tiltak tilrådd — dette er organisatorisk
ansvar hos verksemder som bruker repoet, ikkje eit repo-arkitekturspørsmål.

### Veileder for høsting og deling av språkdata

**Kjelde:** [digdir.no/.../sprakdata-korleis-kan-vi-hauste-og-dele/2367](https://www.digdir.no/datadeling/sprakdata-korleis-kan-vi-hauste-og-dele/2367)

Rettleiaren tilrår at offentleg sektor deler språkdata (m.a. **omgrepsapparat
og termlister**) med Språkbanken ved Nasjonalbiblioteket, for å styrkje norsk
språkteknologi.

**Vurdering:** Reelt relevant — `brreg-begrepskatalog` (SKOS-AP-NO) er
nettopp eit termlister-liknande omgrepsapparat, og publiserast alt til
Felles datakatalog/begrepskatalog via pull-arkitektur. Eit eksplisitt bidrag
til Språkbanken ville derimot krevje ein push mot eit *nytt* eksternt system,
som bryt `SCOPE.md` sitt pull-prinsipp («Repoet initierer aldri push til
eksterne katalogar»). Ingen tiltak tilrådd i repoet sjølv — dette er ei
publiseringsavgjerd for codeowners av begrepskatalog-data (Brreg/andre), ikkje
eit arkitekturgap.

### Forvaltningsstandard for begrepsharmonisering og begrepsdifferensiering

**Kjelde:** [digdir.no/.../forvaltningsstandard-omgrepsharmonisering-og-omgrepsdifferensiering/1683](https://www.digdir.no/standarder/forvaltningsstandard-omgrepsharmonisering-og-omgrepsdifferensiering/1683)

Ein **prosessuell** standard for korleis verksemder skal koordinere
omgrepsbruk seg imellom — ikkje ein RDF-spesifikasjon med eigne eigenskapar.

**Vurdering:** `skos-ap-no-schema.yaml` har alt ein `GeneriskRelasjon`-klasse
(jf. `avvik-skos-ap-no.md`) som kan uttrykkje relasjonar mellom omgrep frå
ulike kjelder — den tekniske føresetnaden for harmonisering/differensiering
er difor på plass. Ingen teknisk gap identifisert utover det SKOS-AP-NO
allereie dekkjer. Ingen tiltak tilrådd.

### TBX-basert tilgjengeliggjøring av begrep (TBX-AP-NO)

**Kjelde:** [digdir.no/.../tbx-ap-no-forvaltningsstandard-tilgjengeleggjering-av-omgrepsbeskrivingar-basert-pa-tbx/1684](https://www.digdir.no/standarder/tbx-ap-no-forvaltningsstandard-tilgjengeleggjering-av-omgrepsbeskrivingar-basert-pa-tbx/1684)

TBX (Term Base eXchange) er ein ISO-standard for maskinlesbar
terminologiutveksling. Standarden krev at omgrep alt beskrivne etter
SKOS-AP-NO-Begrep kapittel 2 **også** gjerast tilgjengelege i TBX-format — eit
**supplerande**, ikkje eit alternativt, format.

**Vurdering — reelt gap:** Repoet genererer i dag RDF/TTL, JSON-LD, JSON
Schema, OWL og SHACL for `brreg-begrepskatalog`, men **ingen TBX-eksport**
finst i generator-flagga (`build.yaml`) eller i LinkML-verktøykjeda. TBX er
tilrådd (ikkje obligatorisk), så dette er ikkje eit brot, men eit reelt
utvidingspunkt for begrepskatalog-domenet. Krev anten ein ny
transformasjonsgenerator (SKOS-RDF → TBX-XML) eller eit eige script i
`mkdocs/lib/scripts/` — ut over LinkML sine innebygde generatorar, som ikkje
har TBX-støtte. Sett som eige, avgrensa element i prioritert handlingsliste.

### Person og Enhet — felles informasjonsmodell

**Kjelde:** [digdir.no/.../person-og-enhet-felles-informasjonsmodell/2018](https://www.digdir.no/informasjonsforvaltning/person-og-enhet-felles-informasjonsmodell/2018)

Digdirs modell er ei **forenkla** referansemodell med 9 klasser (Aktør,
Kontaktinformasjon, Identifikator, Person, Personnavn, Kjønn, Sivilstand,
Enhet, Adresse-referanse) — kjernefelt for navn, kjønn, statsborgerskap,
fødsel/død, sivilstand, organisasjonsnummer/-form.

Repoet dekkjer domenet med to **fullverdige registermodellar** i staden for
éin forenkla fellesmodell:

| Digdir-klasse | Repoets motstykke | Merknad |
|---|---|---|
| Person | `ngr-person.Person` | Overgår Digdir-modellen — inkluderer identitetsgrunnlag, familierelasjonar, vergemål, folkeregisterstatus m.m. |
| Personnavn | `ngr-person.Personnavn` | Same struktur (for-/mellom-/etternavn) |
| Kjønn (kodeliste) | `ngr-person.KjoennKode`-enum | Direkte samsvar |
| Sivilstand (kodeliste) | `ngr-person.SivilstandType`-enum | Repoet har fleire verdiar (m.a. partnarskap-variantar) |
| Adresse (referert) | `ngr-person.Bostedsadresse`/`Postadresse`/`Oppholdsadresse` | Tre spesialiserte typar i staden for éin generisk referanse |
| Enhet | `enhetsregisteret-bvrinn` (Organisasjonsnummer, Virksomhetsnavn, Organisasjonsform, Virksomhetstype) | Separat skjema, silver-policy, Brønnøysund-detaljert |

**Vurdering:** Sterkt samsvar *i sak* (alle Digdir sine kjernefelt er
representerte, ofte med større presisjon), men **ingen direkte 1:1-mapping**
sidan repoet sine modellar er kjeldespesifikke registermodellar
(Folkeregisteret/Brønnøysundregistra), ikkje implementasjonar av den
forenkla fellesmodellen. Dette er venta og tilsikta — «Nasjonale grunndata»
er meint å vere autoritative kjeldemodellar, ikkje ei forenkling. Einaste
identifiserte gap: **ingen eksplisitt dokumentert kryssreferanse** mellom
`ngr-person`/`enhetsregisteret-bvrinn` og Digdirs felles modell i
skjemaas `description.md`. Tilrådd tiltak: legg til ei kort tilvising i
`description.md` for begge skjema (ikkje bygg ein ny, forenkla modell —
det ville vere duplisering av det som alt finst).

### Adresse — felles informasjonsmodell

**Kjelde:** [digdir.no/.../adresse-felles-informasjonsmodell/2019](https://www.digdir.no/informasjonsforvaltning/adresse-felles-informasjonsmodell/2019)

Digdirs modell: `Adresse` (grunnklasse) → `GeografiskAdresse` →
`Offisielladresse` → {`Vegadresse`, `Matrikkeladresse`}, pluss
`Postboksadresse`, `Poststed` og ein geometritype `Punkt` (ISO TC211).

Repoets `ngr-adresse-schema.yaml`: `GeografiskAdresse` (abstrakt) →
{`OffisiellAdresse`, `Postboksadresse`}, der `OffisiellAdresse` slår saman
veg- og matrikkeladresse-felt i éin klasse med valfrie felt per variant
(`adressenavn_ref`+`husnummer_ref` for vegadresse,
`matrikkelnummer` for matrikkeladresse) i staden for Digdirs to separate
underklasser. `Poststed` finst som eiga `GeografiskOmrade`-underklasse og
samsvarer direkte. `Representasjonspunkt` tilsvarar Digdirs `Punkt`.

**Vurdering:** Sterkt strukturelt og semantisk samsvar — venta, sidan begge
modellane har same autoritative kjelde (Kartverket/Matrikkelen/Posten). Eitt
identifisert avvik: `Representasjonspunkt` manglar eksplisitt `class_uri`
til eit geometrivokabular (skjemaet importerer `geo:`-prefikset, men brukar
det ikkje på klassen), sjølv om Digdir-modellen skil `Punkt` ut som eigen
RDF-typa geometritype. Tilrådd tiltak: legg til
`class_uri: locn:geometry` (eller tilsvarande) på `Representasjonspunkt` i
`ngr-adresse-schema.yaml`. Låg prioritet — påverkar ikkje funksjonell
korrekthet, berre presisjonen i RDF-typinga.

---

## Prioritert handlingsliste (attverande gap)

| # | Tiltak | Fil(ar) | Kjelde | Prioritet |
|---|---|---|---|---|
| 1 | Fullfør PO2-PO4: avklar `begrep.brreg.no`/`brreg.no/modellkatalogar/`-URI-ar og dokumenter URI-konstruksjonspolicy i `CLAUDE.md` | `specs/backlog/avvik-peikarar-til-offentlege-ressursar.md` | Standarder for URI-peikarar | Ope frå før — uendra av denne kartlegginga |
| 2 | Vurder TBX-eksport for `brreg-begrepskatalog` (ny generator/script) | `src/linkml/begrepskatalog/brreg-begrepskatalog/build.yaml` + ny transformasjon | TBX-AP-NO | Middels — reelt, men valfritt format |
| 3 | Legg til `class_uri` på `Representasjonspunkt` | `src/linkml/ngr/ngr-adresse/ngr-adresse-schema.yaml` | Adresse — felles informasjonsmodell | Låg — presisjonsfiks |
| 4 | Dokumenter kryssreferanse til Digdirs Person/Enhet-modell | `src/linkml/ngr/ngr-person/description.md`, `src/linkml/oreg/enhetsregisteret-bvrinn/description.md` | Person og Enhet — felles informasjonsmodell | Låg — dokumentasjon, ingen strukturendring |

Tiltak 1 er allereie planlagt i eksisterande backlog-spec og vert ikkje
duplisert her. Tiltak 2-4 er nye funn frå denne kartlegginga og ligg ikkje i
nokon annan spec — dei er kandidatar for eigne, avgrensa specs når/om
brukaren prioriterer dei.

---

## Samandrag

Repoet realiserer kjernen i Digdirs rammeverk **sterkt**, og har gjort det
gjennom systematisk, dokumentert kartleggingsarbeid over tid — 17 av 23
navngjevne ressursar var alt kartlagde og i hovudsak utbetra før denne
spesifikasjonen. Dei to sterkast dekte pilarane er **Standarder og
spesifikasjoner** (10/11 element kartlagt og i hovudsak utført, det siste
delvis) og **Informasjonsmodellar** (begge tekniske ressursar — 15
modelleringsreglar og 9 designprinsipp — fullt dekt av MCP-validatoren).
Dei to felles domenemodellane (Person/Enhet, Adresse) er ikkje direkte
implementerte, men overgåtte av meir detaljerte, kjeldeautoritative
registermodellar (`ngr-person`, `ngr-adresse`, `enhetsregisteret-bvrinn`) —
eit medvite og rimeleg avvik, ikkje eit gap.

**Veiledere**-pilaren har ei naturleg grense: dei tre elementa som er reint
organisatoriske/prosessretta og gjeld *éi einskild verksemd* (Modenhetsmodell,
Internkontroll, delvis Orden i eget hus) kan eit delt verktøyrepo støtte, men
ikkje sjølv «oppfylle» — det ligg utanfor kva eit skjemabibliotek kan vere
ansvarleg for, i tråd med `SCOPE.md` sine eksplisitte avgrensingar.

**Kjerneprinsippa** er godt realiserte: «Kun én gang» gjennom import-hierarki
og lenkingsprinsippet, maskinell datautveksling gjennom heile
LinkML-generatorkjeda, og felles standardar gjennom sjølve
skjemabiblioteket. Orden i eget hus er understøtta, men ikkje sjølv utført av
repoet, sidan det per design er ei verksemds eigen prosess.

**Éin reell teknisk mangel** vart identifisert i denne kartlegginga: manglande
TBX-AP-NO-eksport for begrepskatalog-data. To mindre presisjonsfiksar
(`Representasjonspunkt` sin `class_uri`, kryssreferanse-dokumentasjon for
Person/Enhet) er også identifiserte. Alle tre er nye funn, ikkje del av
noka tidlegare kartlegging, og er lista i prioritert handlingsliste over.

---

## Utført

Kartlegging fullført 2026-08-11. Dette er eit rein syntese-/analysedokument
— ingen kodeendringar er gjort som del av denne spesifikasjonen. Resultat:

- Bygd samla rammeverksdekning-tabell for alle 23 navngjevne ressursar +
  4 kjerneprinsipp, med status og kryssreferanse til dei 17 eksisterande
  `avvik-*.md`-kartleggingane i `specs/done/` og den opne i `specs/backlog/`.
- Skrive 7 nye delkartlegginger for dei rammeverkselementa som aldri før var
  vurderte mot repoet: Modenhetsmodell for orden i eget hus, Internkontroll i
  praksis, Veileder for høsting og deling av språkdata, Forvaltningsstandard
  for begrepsharmonisering/-differensiering, TBX-AP-NO, Person og Enhet, og
  Adresse (dei to siste ved klasse-for-klasse-samanlikning av `ngr-person`,
  `ngr-adresse` og `enhetsregisteret-bvrinn` mot Digdirs felles modellar).
- Identifisert 3 nye, avgrensa gap (TBX-eksport, `Representasjonspunkt`
  `class_uri`, Person/Enhet-kryssreferanse) som ikkje var fanga av tidlegare
  kartlegginger — lista i prioritert handlingsliste, ikkje utført her.
- Konklusjon: repoet realiserer rammeverkets tekniske pilarar (Standarder og
  spesifikasjoner, Informasjonsmodellar) og alle fire kjerneprinsipp sterkt;
  Veiledere-pilaren har ei naturleg grense mot dei elementa som gjeld éi
  einskild verksemds eigne organisatoriske prosessar.
