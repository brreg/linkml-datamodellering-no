# Mange små brreg-felles-*-modellar for enhetsregisteret-*, utleia frå BR sine interne referansekatalogar

## Bakgrunn

Brukaren la 31.08.2026 fire filer i `src/tmp/`, eksportert frå Brønnøysundregistrene
(BR) sitt MagicDraw-verktøy (UML/XMI, `2024x v6`), og bad om ei vurdering av om
desse kan brukast til å lage felles-modellar som handhevar DRY-prinsippet i
`oreg`-domenet sine `enhetsregisteret-*`-modellar:

- `BRProfilV2.xml` (225 KB) — BR sin **UML-modelleringsprofil**: stereotypar
  (`Forretningsobjekt`, `Løsningsmodell`, `Strukturmodell`, `Kode`,
  `Primitivtype`, `Rotelement`, `Nullbar`, `MinstEn`, `EnAv` m.fl.) og
  tagged-value-enum-ar (`Statustype`, `Modellstatus`, `Tjenesteområde`).
  Dette er verktøymetadata for korleis BR klassifiserer eigne modellelement —
  **ikkje** domeneinnhald som kan importerast i ein LinkML-skjema.
- `BRReferansemodell_v3.xml` (4,4 MB, men berre 39 `uml:Class`/7 `uml:DataType`
  — resten er MagicDraw-diagram-binærdata) — BR sin **referansemodell**:
  kjernedomeneklassar for Aktør/Virksomhet/Person/Rolle og eit fullt
  Adresse-hierarki (geografisk og digital adresse).
- `Løsningstypekatalog_v1.xml` (574 KB, 59 `uml:PrimitiveType`) — BR sin
  **katalog over gjenbrukbare primitivtypar**: `Enkeltyper` (t.d.
  `Organisasjonsnummer`, `Virksomhetsnavn`, `Fødselsnummer`, `UUID`,
  `Kontonummer`) og `Kodetyper` (t.d. `Postnummer`, `Kommunenummer`,
  `Landkode`, `Organisasjonsform`).
- `Strukturtypekatalog_v1.xml` (365 KB, 27 `uml:PrimitiveType` + 12
  `uml:DataType` + 2 `uml:Enumeration`) — BR sin **katalog over
  samansette/strukturerte typar**: `Komplekstyper` (t.d. `BeløpIValuta`,
  `Matrikkelnummer`, `Poststed`, `Personnavn`, `Tidsperiode`) og ein
  `Identifikator`/`Tid`-basistype-hierarki dei andre typane arvar frå.

Namnestrukturen stadfestar seg sjølv: `BRProfilV2` sine stereotypar
(`Forretningsobjektmodell`, `Løsningsmodell`, `Strukturmodell`) er nett dei
tre modelltypane dei tre andre filene representerer. Filene er altså BR sin
**autoritative, interne kjelde** — og alt tyder på at dei eksisterande
`enhetsregisteret-*`-skjemaa i dette repoet er handmodellerte/generert
**uavhengig av** denne kjelda, med namnedrift og duplisering som resultat
(sjå «Funn» under).

## Metode

Dei fire XMI-filene vart parsa med eit eingongs Python-script
(`xml.etree.ElementTree`, ingen eksterne avhengigheiter) som gjekk gjennom
`packagedElement`-treet under `uml:Model` og henta ut namn, `ownedAttribute`
(namn + type-referanse), `ownedLiteral` (enum-verdiar) og `generalization`
for kvar `uml:Class`/`uml:Enumeration`/`uml:PrimitiveType`/`uml:DataType` —
og hoppa dermed over all diagram-/layout-støy (`ownedDiagram`,
`diagramRepresentation` osv.), som utgjer størstedelen av filstorleiken.
Resultatet vart kryssa mot dei sju eksisterande
`src/linkml/oreg/enhetsregisteret-*/enhetsregisteret-*-schema.yaml`-filene
(`grep`/`awk` over `types:`- og `classes:`-blokkene).

## Funn 1: massiv, alt eksisterande DRY-brot i `enhetsregisteret-*`

**`enhetsregisteret-bvrinn` og `enhetsregisteret-bvrinnfelles` er praktisk
tala identiske** (2091 vs. 2087 linjer, `diff` gjev 794 linjer skilnad —
nesten utelukkande metadata). Dette er sannsynlegvis eit uforløyst
scaffolding-resultat, men er **heilt uavhengig av** BR-katalogane (§ Funn
2-4). Brukaren har bestemt (avklaring 31.08.2026, punkt 8) at saneringa
av dette høyrer heime i ein **eigen spec** —
sjå `specs/done/enhetsregisteret-bvrinn-bvrinnfelles-duplikat.md` for
full utgreiing og handlingsliste. Resten av denne specen handterer berre
BR-katalog-avleidde felles-modellar.

**Lokalt definerte `types:` gjentek seg på tvers av dei sju skjemaa** —
utan import, kvar med eiga (og stundom avvikande) `uri: xsd:string` /
`base: str`-deklarasjon:

| Type | Finst lokalt i (tal skjema) |
|---|---|
| `Organisasjonsnummer` | Alle 7 skjema |
| `Dato` | 5 (`bekreftelse`, `bvrinn`, `bvrinnfelles`, `stiftelsesdokument`, `frivilligorganisasjonapi`) |
| `Virksomhetsnavn`, `Tekst50` | 4 kvar |
| `Versjonsnummer`, `InnsendertjenesteType`, `DatoKlokkeslett`, `Tjenestevariant`, `NasjonaltNummer`, `FagsystemId`, `Postnummer`, `Landkode`, `URL`, `InternasjonaltPrefiks`, `PersonMappingId` | 3 kvar (nesten alltid `bvrinn` + `bvrinnfelles` + éin til) |
| `Foedselsnummer`, `Kontonummer`, `ICNPOKategori`, `Organisasjonsform`, `Kommunenummer`, `Bruksenhetsnummer`, `Husnummer`, `Husbokstav`, `Postboksnummer`, `Aktivitetskode`, `Tekst1000` | 2 kvar |

**Klassenamn frå BR sitt Adresse-/Aktør-hierarki går att som lokale
klassar** i fleire skjema utan felles kjelde: `Stedsadresse`, `Vegadresse`,
`Postboksadresse`, `InternasjonalAdresse`, `GeografiskAdresse`,
`Telefonnummer`, `Matrikkelnummer`, `Personnavn`, `Poststed`, `Rolle`,
`Virksomhet`, `Person` — kvar med sine eigne, lett ulike felt (t.d.
`bvrinn`/`bvrinnfelles` sin `Vegadresse` har 9 felt inkl. `fylke`, medan
`bvrstiftelsesdokument` sin har berre nokre av desse).

## Funn 2: BR-katalogane er den manglande felles kjelda

Kryss-referansen mot Løsningstypekatalog_v1/Strukturtypekatalog_v1 stadfestar
at dei fleste lokale ad-hoc-typane over faktisk **finst i BR sin offisielle
katalog**, men med små, usystematiske namneavvik mellom denne repoen og
katalogen — og til og med **internt i BR sine to katalog-filer**:

| Lokal type i repoet | BR-katalog (kjelde) | Merknad |
|---|---|---|
| `Organisasjonsnummer` | `Organisasjonsnummer` (begge katalogar) | Eksakt treff |
| `Virksomhetsnavn` | `Virksomhetsnavn` (Løysingstypekatalog) | Eksakt treff |
| `Foedselsnummer` | `Fødselsnummer` (begge katalogar) | Berre translitterering (korrekt jf. CONVENTIONS.md) |
| `Kontonummer`, `Aktivitetskode`, `Postboksnummer`, `Husnummer`, `Husbokstav`, `Bruksenhetsnummer`, `NasjonaltNummer` | Same namn i Løysingstypekatalog | Eksakt treff |
| `URL` | `URL` (Løysingstypekatalog har òg separat `URI`) | Eksakt treff |
| `Tekst50`/`Tekst100`/`Tekst1000` | `Tekst50`/`Tekst100`/`Tekst1000` (katalogen har òg `Tekst175`, `Tekst255` — ikkje i bruk lokalt enno) | Eksakt treff |
| `Postnummer`, `Kommunenummer`, `Landkode`, `Organisasjonsform` | Same namn i `Kodetyper` (begge katalogar) | Eksakt treff |
| `UUID` (kun i `bvrettersendingavvedlegg`) | `UUID` (Løysingstypekatalog) **men** `GUID` (Strukturtypekatalog) | **Katalogane er ueinige med seg sjølve** — treng avklaring frå BR, ikkje berre frå repoet |
| `InternasjonaltPrefiks` | `PrefiksMedNasjonalKode` | Namnedrift — same omgrep, ulikt namn |
| `DatoKlokkeslett` | `DatoOgKlokkeslett` (Strukturtypekatalog, arvar frå `Tid`) | Namnedrift |
| `AArstall` (frivilligorganisasjonapi) | `Årstall` (Strukturtypekatalog, arvar frå `Tid`) | Berre translitterering |
| `Dato` | `Dato` (Strukturtypekatalog, arvar frå `Tid`) | Eksakt treff |
| `Beloep`/`BeloepFriDesimal` | `Beløp` (begge katalogar); Strukturtypekatalog har òg samansett `BeløpIValuta` (beløp + `Valutakode`) | Delvis treff — komplekstypen `BeløpIValuta` finst ikkje lokalt enno |

Typar som **ikkje** finst i nokon av katalogane (truleg interne
saksbehandlings-/skjemakodar, ikkje del av BR sin gjenbrukbare
type-katalog): `InnsendertjenesteType`, `Tjenestevariant`, `Virksomhetstype`,
`Ansvarsform`, `ValgtAv`, `SignaturrettEllerProkuraregel`,
`Mengdeangivelse`, `TilknyttetRegistertype`, `FagsystemId`,
`PersonMappingId`, `ICNPOKategori`, `ICNPOKategorinummer`,
`FrivilligOrganisasjonsstatus`, `IdentifikatorInformasjonstype`,
`Rolletype`, `AntallAksjer`, `Tekst5000`, `DagMaaned`. Desse er ikkje
kandidatar for felles-modellen.

> **Revidert 31.08.2026:** Brukaren bad om (1) å ta med **alt** innhaldet
> i Løsningstypekatalog_v1 (ikkje berre dei ~20 med lokalt treff), (2) å
> undersøkje om `BRReferansemodell_v3` sine klassar kan delast opp i
> fleire små, sjølvstendige felles-modellar, (3) ei eiga vurdering av
> gjenbrukbarheita til dei 12 komplekstypane i Strukturtypekatalog_v1, og
> (4) ei utgreiing av om `make new-modell` kan utvidast med eit
> XML/XMI-input-flagg. «Funn 3», «Funn 4» og «Evaluering» under svarer på
> punkt 2-3, og «Vurdering»/«Nummererte steg» er omskrivne til å
> reflektere prinsippet om **mange små, målretta felles-modellar** framfor
> éin stor. Alle opne spørsmål frå dette utkastet er sidan avklara med
> brukaren — sjå «Avklaringar frå brukaren» heilt nedst, som no er
> fasiten for kva som skal byggjast.

## Funn 3: BRReferansemodell_v3 hentar typane sine frå Strukturtypekatalog_v1 — ikkje frå Løsningstypekatalog_v1

Kryssreferansen (§ Metode, utvida til å slå saman id→namn-tabellane frå
alle fire XMI-filene og følgje `<type href='<fil>#<id>'>`-referansane på
tvers av filer) avdekte at BR sjølv har **to parallelle, delvis
overlappande type-katalogar** — ikkje eitt lagdelt hierarki:

- **Løsningstypekatalog_v1** — flate `PrimitiveType`-ar utan arv
  (`Organisasjonsnummer` er ein sjølvstendig type).
- **Strukturtypekatalog_v1** — ein eigen, **arva** `Enkeltyper`-hierarki
  rota i `Identifikator` (`Organisasjonsnummer extends Identifikator`,
  `Fødselsnummer extends Identifikator`, `AktørId extends Identifikator`
  osv.), pluss eit `Tid`-hierarki (`Dato`/`DatoOgKlokkeslett`/
  `MånedOgÅr`/`Årstall` extends `Tid`).

**Alle** `ownedAttribute`-typereferansane i `BRReferansemodell_v3` (stadfesta
ved å følgje `referenceExtension referentPath=`-attributtet i rå-XML-en,
t.d. `Virksomhet.organisasjonsnummer` → `referentPath='Strukturtypekatalog_v1::
Enkeltyper::Organisasjonsnummer'`) peikar til **Strukturtypekatalog_v1**
sin versjon — aldri til Løsningstypekatalog_v1 sin, sjølv der begge
katalogane har ein type med identisk namn. Dette stemmer med
`BRProfilV2` sine stereotypar (Funn i «Bakgrunn»): `BRReferansemodell_v3`
er ein «Forretningsobjektmodell» bygd på «Strukturmodell»
(Strukturtypekatalog_v1), medan Løsningstypekatalog_v1 høyrer til
«Løsningsmodell»-laget — nett det laget dei sju eksisterande
`enhetsregisteret-*`-skjemaa (som **er** løysingsmodellar, jf. `BVR-inn`
m.fl.) alt viste seg å samsvare med i Funn 2.

> **Avklaring 31.08.2026 (punkt 3):** Brukaren har bestemt at ein eigen
> `brreg-felles-struktur-typer` **ikkje** skal opprettast i første omgang.
> Konsekvens: `brreg-felles-adresse`/`brreg-felles-aktoer` (§ Funn 4) kan
> **ikkje** vere byte-for-byte tru mot Strukturtypekatalog_v1 sine
> typereferansar. Løysinga vert difor:
> - Der Løsningstypekatalog_v1 har ein type med **same namn** som
>   Strukturtypekatalog_v1 sin (t.d. `Organisasjonsnummer`,
>   `Fødselsnummer`/`Foedselsnummer`, `Beløp`, `NasjonaltNummer`,
>   `BRAdresseId`, `BRPersonId`) — bruk `brreg-felles-typer` sin versjon
>   direkte. Dette dekkjer dei fleste konkrete felta.
> - Der eit felt er typa generisk til den abstrakte basen `Identifikator`
>   (t.d. `GeografiskAdresse.brAdresseId`, `DigitalAdresse.identifikator`,
>   `Aktør.identifikator`) og ingen namnelik Løsningstypekatalog-type
>   finst — forenkl til LinkML sin innebygde `string` med ein
>   `# TODO: vurder felles-type når/dersom brreg-felles-struktur-typer
>   vert oppretta`-kommentar, løyst felt for felt ved implementering
>   (steg 3-4).
> - `Tid`-basisen (`Dato`/`DatoOgKlokkeslett`/`MånedOgÅr`/`Årstall`)
>   handterast tilsvarande: bruk dei rå XSD-primitivtypane frå
>   `brreg-felles-typer` sitt `Primitivtyper`-utval (`date`, `dateTime`,
>   `gYearMonth`, `gYear`) i staden for dei namngjevne
>   Strukturtypekatalog-variantane.
>
> Dette er ei medviten, dokumentert forenkling — ikkje eit tap av
> informasjon frå BR-kjelda, berre eit val om å ikkje byggje eit femte
> skjema for eit lag som i dag har få unike, namnelause omgrep att etter
> at dei namnelike typane er dekte av `brreg-felles-typer`.

**Kodetyper-pakken er eit reelt duplikat mellom katalogane** (same
konklusjon, no enda meir relevant sidan `brreg-felles-struktur-typer`
uansett ikkje vert oppretta): alle 11 `Kodetyper` i Strukturtypekatalog_v1
(`Organisasjonsform`, `Næringskode`, `Valutakode`, `Landkode`,
`Postnummer`, `Kommunenummer`, `Fylkesnummer`, `Språkkode`,
`InstitusjonellSektorkode`, `Virksomhetsstatus`, `PersonstatusType`) er
ein rein delmengd av dei 13 i Løsningstypekatalog_v1, namn-for-namn.
Klassar som treng desse (t.d. `Vegadresse.fylke`/`.kommune`) importerer
`brreg-felles-typer` for dei.

## Funn 4: BRReferansemodell_v3 sine klassar kan delast i tre naturlege, nesten sirkelfrie delar

Med full kryssreferanse-oppløysing (§ Metode) vart det bygd ein
avhengigheitsgraf mellom alle 39 klassane. Grafen fell nesten perfekt
saman med BR sine eigne pakkenamn, med **éin** avvikande kant:

**Del 1 — `Adresse`-pakken (13 av 14 klassar, ekskl. `Aksesspunkt`):**
`GeografiskAdresse`-hierarkiet (`GeografiskAdresse` → `Postboksadresse`,
`Stedsadresse`, `Vegadresse`, `Matrikkeladresse`, `InternasjonalAdresse`)
og `DigitalAdresse`-hierarkiet (`DigitalAdresse` → `IPAdresse`,
`EPostadresse`, `Nettadresse`, `Meldingsboks`, `Mobiltelefonnummer`,
`Telefonnummer`). Avheng berre av primitiv-/komplekstypar (§ Funn 3,
Evaluering under) — **ingen** avhengigheit til Aktør-pakken, med eitt
unntak:

**Avvikande kant:** `Aksesspunkt` (extends `Nettadresse`) har feltet
`aksesspunktoperatør: Virksomhet` — ein peikar **frå** Adresse-pakken
**til** Aktør-pakken. Dette er den einaste sirkulære referansen mellom
dei to pakkane i heile modellen.

> **Avklaring 31.08.2026 (punkt 2):** Brukaren har bestemt å **utelate**
> `Aksesspunkt` heilt frå `brreg-felles-adresse` (ikkje flytte han til
> `brreg-felles-aktoer`, slik første utkast av denne specen føreslo).
> Skriv ein eksplisitt kommentar i `brreg-felles-adresse-schema.yaml` der
> `Nettadresse` (foreldreklassen hans) er definert, t.d.: `# BR sin
> Nettadresse-undertype "Aksesspunkt" er medvite utelaten her —
> aksesspunktoperatør-feltet peikar til Virksomhet (Aktør-pakken) og
> ville gjort importgrafen sirkulær. Sjå specs/backlog/felles-typar-
> enhetsregisteret-fra-br-katalogar.md § Funn 4.` Dette held
> importgrafen asyklisk med minimalt tap (éin smal, spesialisert klasse).

**Del 2 — `Aktør`-pakken (7 klassar):** `Aktør`, `Kontaktinformasjon`,
`Rolle`, `Rolletypegruppe`, `Relasjon`, `Virksomhet`, `Person`
(`Aksesspunkt` er **utelaten**, ikkje flytta hit — sjå avklaring over).
Avheng av del 1 (`Aktør.geografiskAdresse`/`digitalAdresse`, `Rolle`
same), av dei namnelike typane i `brreg-felles-typer` som stand-in for
Strukturtypekatalog_v1 sitt `Enkeltyper`-lag (§ Funn 3-boksen), og av eit
utval Komplekstyper (§ Evaluering under: `Personnavn`,
`Personidentifikator`, `Virksomhetsidentifikator`). **Éin retning:** del
2 importerer del 1, aldri omvendt.

**Ikkje kandidat — `DigdirStandard`-pakken (16 klassar/typar):** ein
tydeleg **utkast-/tilpassingsområde**, ikkje del av BR sin autoritative
kjerne. Inneheld klassar med **same namn som** del 1/del 2 sine
(`Adresse`, `Postboksadresse`, `Matrikkeladresse`, `Vegadresse`,
`GeografiskAdresse`, `Aktør`, `Person`, `Kontaktinformasjon`,
`Identifikator`) men **andre felt** (t.d. denne pakken sin `Person` har
`fulltNavn`/`kjønn` i staden for del 2 sin `navn`/`identifikator`-struktur),
pluss fire tomme placeholder-klassar (`X3`, `X4`, `X5`, ein namnlaus
`uml:DataType x`) som ikkje har noka openbar tolking. Tilråding: **ekskluder
heile denne pakken** frå felles-modellane no — namnekollisjonen mot del
1/del 2 (same klassenamn, ulikt innhald) ville uansett gjort samtidig
import umogleg utan omdøyping. Avklaring 31.08.2026 (punkt 6): brukaren
har stadfesta at pakken skal utelatast og dokumenterast som eit utkast/
ikkje-autoritativt område (denne seksjonen er dokumentasjonen).

## Evaluering: gjenbrukbarheit av dei 12 komplekstypane i Strukturtypekatalog_v1

`Komplekstyper`-pakken i Strukturtypekatalog_v1 har 12 `uml:DataType`
(+ 2 `uml:Enumeration`, + 1 `uml:Class Telefonnummer` som er eit
duplikat/alternativ til `BRReferansemodell_v3` sin eigen
`Telefonnummer`-klasse i Adresse-pakken — tilråding: bruk
`BRReferansemodell_v3` sin versjon, sidan han alt er ein `DigitalAdresse`-
undertype og dermed høyrer naturleg heime i del 1). Kvar av dei 12 vart
kryssjekka feltvis mot **faktiske** klassar i dei sju
`enhetsregisteret-*`-skjemaa (ikkje berre namnetreff):

**Høg gjenbrukbarheit — 6 av 12 finst allereie, feltidentiske eller
nesten feltidentiske, uavhengig oppfunne lokalt:**

| Komplekstype (Strukturtypekatalog) | Felt i katalogen | Finst lokalt som | Lokale felt | Treff |
|---|---|---|---|---|
| `Adressenummer` | `nummer`, `bokstav` | `Adressenummer`-klasse i `bvrinn`/`bvrinnfelles` | `nummer`, `bokstav` | **100 %** |
| `Personnavn` | `fornavn`, `mellomnavn`, `etternavn` | `Personnavn`-klasse i `bvrstiftelsesdokument` | `fornavn`, `mellomnavn`, `etternavn` | **100 %** |
| `Poststed` | `navn`(/`poststedsnavn`), `postnummer` | `Poststed`-klasse i `bvrstiftelsesdokument` | `navn`, `postnummer` | **100 %** |
| `Tidsperiode` | `fraDato`, `tilDato` | `Tidsperiode`-klasse i `frivilligorganisasjonapi` (`class_uri: dct:PeriodOfTime`) | `fraDato`, `tilDato` | **100 %** (behald `dct:PeriodOfTime`-mappinga ved migrering) |
| `Matrikkelnummer` | `kommunenummer`, `gårdsnummer`, `bruksnummer`, `festenummer`, `seksjonsnummer` | `Matrikkelnummer`-klasse i `bvrinn`/`bvrinnfelles` | `kommunenummer`, `gaardsnummer`, `bruksnummer`, `festenummer` (manglar `seksjonsnummer`) | **80 %** |
| `Telefonnummer` (klassevarianten i `BRReferansemodell_v3`, sjå over) | `prefiksMedNasjonalKode`, `nasjonaltNummer` | `Telefonnummer`-klasse i `bvrinn`/`bvrinnfelles` | `internasjonaltPrefiks` (namnedrift), `nasjonaltNummer` | **~90 %** |

**Låg/inga gjenbrukbarheit i dag — 0 treff i noka av dei sju skjemaa:**
`Beløpsintervall`, `BeløpIValuta`, `Fylke`, `Kommune`,
`Personidentifikator` (+ enum `PersonidentifikatorType`),
`Virksomhetsidentifikator` (+ enum `VirksomhetsidentifikatorType`),
`TidsperiodeDatoKlokkeslett`. Merk at `Fylke`/`Kommune` og
`Personidentifikator`/`Virksomhetsidentifikator` likevel er **strukturelt
kravde** dersom del 2 (Aktør-modellen, § Funn 4) skal vere tru mot
`BRReferansemodell_v3` (`Vegadresse.fylke`/`.kommune`,
`Person.identifikator: Personidentifikator`,
`Virksomhet.identifikator: Virksomhetsidentifikator`) — dei er difor ikkje
reint spekulative, men har **ingen ekstern etterspurnad frå dagens
skjema** enno. Avklaring 31.08.2026 (punkt 4, nedanfor «Konklusjon»):
tekne med likevel, for å vere tru mot kjelda.

**Konklusjon (avklaring 31.08.2026, punkt 4):** brukaren har bestemt å ta
med **alle** 12 komplekstypane, ikkje berre dei 6 med provd lokal
gjenbruk — for å vere tru mot `BRReferansemodell_v3` sin faktiske
klassestruktur (`Vegadresse.fylke`/`.kommune`,
`Person.identifikator: Personidentifikator`,
`Virksomhet.identifikator: Virksomhetsidentifikator` osv. er reelle felt
i kjelda, ikkje spekulative). Reusability-tabellen over står likevel att
som verdifull dokumentasjon: han viser **kva for 6** av dei 12 som alt
har eit sjølvstendig, uavhengig oppfunne motstykke lokalt (høg
migreringsprioritet i steg 6), og kva for 6 som er nye for repoet (lågare
prioritet, men no likevel med frå dag éin). Alle 12 vert fordelte etter
kva del dei høyrer naturleg til (§ Vurdering) — ikkje samla i éin stor
struktur-modell.

## Vurdering

Ja, eit solid, evidensbasert grunnlag — bygd opp som **mange små,
målretta felles-modellar som kan importerast ved behov, framfor éin
stor**, jf. brukaren sitt eksplisitte prinsipp. Dette minimerer
modellbloat på same måte som `del-opp-ap-no-profilar-i-moduler.md`
åtvarar mot for AP-NO-importa (eit skjema som berre treng
`Organisasjonsnummer` skal ikkje måtte importere heile
Aktør-/Adresse-klassehierarkiet, og omvendt).

**Domeneplassering (avklaring 31.08.2026, punkt 1):** brukaren bad om ei
vurdering av eit nytt, eige `felles`-domene som samlar alle
felles-modellar (i staden for å plassere dei under `oreg`). Undersøkinga
stadfestar at dette er **trygt og godt støtta**: `DOMAINS` i byggsystemet
er **fullstendig dynamisk oppdaga**, ikkje hardkoda —
`make/02-schema-discovery.mk` avleier domenelista frå 3. stikomponent i
`find src/linkml -mindepth 3 -maxdepth 3 -name '*-schema.yaml'`, og
`make print-domains` (brukt av CI for dynamisk matrise-generering) og
`mkdocs/publish.sh` sin domene-gjennomgang følgjer same mønster. Ei ny
mappe `src/linkml/felles/` vert dermed automatisk plukka opp av CI,
`make domain-felles`, og mkdocs-portalen **utan kodeendringar**. Einaste
manuelle steget er å leggje ein ny rad i CONVENTIONS.md sin
URI-segment-tabell (jf. `fair`, som same stad er skildra som eit
frittståande, tverrgåande domene «kan kombinerast med AP-NO, FINT og
oreg» — akkurat den rolla eit `felles`-domene for BR sine eigne
tverrgåande typar/klassar ville spele). **Tilråding: opprett
`felles`-domenet.** Alle fire modellane under ligg difor i
`src/linkml/felles/`, ikkje `src/linkml/oreg/`.

**Forslag til modellsett** (alle under `src/linkml/felles/`):

| Modell | Kjelde | Innhald | Importerer |
|---|---|---|---|
| `brreg-felles-typer` | Løsningstypekatalog_v1 (heile) | Alle 59 typar: 20 XSD-baserte `Primitivtyper`, 13 `Kodetyper`, 26 `Enkeltyper` | `linkml:types` |
| `brreg-felles-adresse` | `BRReferansemodell_v3`/Adresse (§ Funn 4, del 1, `Aksesspunkt` utelaten og dokumentert) + alle 5 adresse-relaterte Komplekstyper (§ Evaluering: `Poststed`, `Kommune`, `Fylke`, `Matrikkelnummer`, `Adressenummer`) | 13 klassar + 5 datatypar | `brreg-felles-typer` |
| `brreg-felles-aktoer` | `BRReferansemodell_v3`/Aktør (§ Funn 4, del 2) + alle Aktør-relaterte Komplekstyper (`Personnavn`, `Personidentifikator`+enum, `Virksomhetsidentifikator`+enum) | 7 klassar + 3 datatypar/enum | `brreg-felles-adresse` (transitivt òg `brreg-felles-typer`) |
| `brreg-felles-tid` | Strukturtypekatalog_v1 Komplekstyper (`Tidsperiode`, `TidsperiodeDatoKlokkeslett`) | 2 datatypar | `brreg-felles-typer` |

`Beløpsintervall`/`BeløpIValuta` er dei einaste to av dei 12 komplekstypane
utan noko naturleg heim i tabellen over (verken adresse-, aktør- eller
tid-relaterte) — dei høyrer ikkje til nokon av dei fire modellane sitt
tematiske omfang. Sidan brukaren sitt punkt 4 gjaldt spesifikt dei
strukturelt kravde typane frå `BRReferansemodell_v3` (som desse to
**ikkje** er — dei er ikkje referert av noka klasse i modellen), stend
tilrådinga frå første utkast ved lag for akkurat desse to: legg dei til
seinare, i den modellen som passar best, når eit konkret skjema treng dei.

Ein konsument som berre treng `Organisasjonsnummer` importerer no berre
`brreg-felles-typer` (59 typar, ingen klassar). Eit skjema som treng
fullt Adresse-hierarki, men ikkje Aktør/Rolle, importerer
`brreg-felles-adresse` og dreg **ikkje** med seg `Virksomhet`/`Person`/
`Rolle`. Dette er nett den granulariteten brukaren bad om.

## Nummererte steg

1. **Legg til `felles`** som ny rad i CONVENTIONS.md sin
   URI-segment-tabell (§ Vurdering) — einaste manuelle registreringssteget
   for det nye domenet.
2. **Opprett `brreg-felles-typer`** (`src/linkml/felles/brreg-felles-typer/`):
   eige `build.yaml` (`publish_external: false`), `description.md`, og
   `brreg-felles-typer-schema.yaml` med **alle** 59 typane frå
   Løsningstypekatalog_v1, translitterert etter CONVENTIONS.md §
   Klassenavn, med **éi kjeldekommentarlinje per type** (avklaring punkt
   10), t.d. `# Kjelde: BR Løsningstypekatalog_v1 (Enkeltyper)`. Brukar
   namnet `UUID` konsekvent (avklaring punkt 9). Importerer berre
   `linkml:types`.
3. **Opprett `brreg-felles-adresse`**: dei 13 Adresse-klassane (§ Funn 4,
   del 1) + dei 5 adresse-relaterte Komplekstypane (§ Evaluering, alle
   tekne med jf. avklaring punkt 4). `Aksesspunkt` utelates med
   kommentar (§ Funn 4). Generiske `Identifikator`-typa felt utan
   namnelik `brreg-felles-typer`-motpart forenklast til `string` med
   TODO-kommentar (§ Funn 3-boksen). Importerer steg 2.
4. **Opprett `brreg-felles-aktoer`**: dei 7 Aktør-klassane (§ Funn 4, del
   2) + `Personnavn`/`Personidentifikator`(+enum)/
   `Virksomhetsidentifikator`(+enum), alle tekne med (avklaring punkt 4).
   Importerer steg 3 (transitivt steg 2).
5. **Opprett `brreg-felles-tid`**: `Tidsperiode` (behald
   `class_uri: dct:PeriodOfTime`-mappinga, § Evaluering) og
   `TidsperiodeDatoKlokkeslett`. Opprettast no (avklaring punkt 5), ikkje
   utsett. Importerer steg 2.
6. **Migrer dei sju `enhetsregisteret-*`-skjemaa til `brreg-felles-typer`**
   éin om gongen: fjern den lokale `types:`-duplikaten som har
   eksakt/nesten-eksakt treff (§ Funn 2), legg til import, køyr
   `make lint SCHEMA=... && make roundtrip SCHEMA=...` for kvart skjema.
7. **Vurder klassemigrering til `brreg-felles-adresse`/`-aktoer`/`-tid`
   separat, skjema for skjema** (kan vere eiga oppfølgings-spec): for
   kvart av dei 6 høg-gjenbrukbarheit-treffa i § Evaluering, samanlikn
   feltsettet nøye (t.d. `Matrikkelnummer` manglar `seksjonsnummer`
   lokalt — avgjer om det skal leggjast til eller om felles-typen skal ha
   feltet som valfritt) før import erstattar den lokale
   klassedefinisjonen.
8. **`Beløpsintervall`/`BeløpIValuta`** vurderast **berre** når eit
   konkret skjema treng dei (jf. terskelen i steg 7).
9. **Etter kvart steg:** oppdater denne specen sin «Utført»-seksjon,
   generer commit-melding, og flytt specen til `specs/done/` når alle
   tiltak er gjennomførte.

## Utgreiing: `make new-modell` med XML/XMI-input

**Avklaring 31.08.2026 (punkt 11):** flytta til eigen spec —
sjå `specs/done/make-new-modell-xmi-input-utgreiing.md` for full
utgreiing (korleis JSON_SCHEMA-vegen fungerer i dag, kva som er
lettare/vanskelegare med XMI enn JSON Schema, og konklusjon/tilråding).

## Avklaringar frå brukaren (31.08.2026)

Alle punkt under er avgjorde — ingen opne spørsmål står att før
implementering (steg 1-9) kan starte:

1. **Domeneplassering:** nytt `felles`-domene (§ Vurdering) — alle fem
   modellane ligg i `src/linkml/felles/`, ikkje `src/linkml/oreg/`.
2. **`Aksesspunkt`:** utelaten heilt frå `brreg-felles-adresse`, med
   kommentar i skjemaet (§ Funn 4).
3. **`brreg-felles-struktur-typer`:** droppa i første omgang. Generiske
   `Identifikator`-typa felt utan namnelik motpart i `brreg-felles-typer`
   forenklast til `string` med TODO-kommentar (§ Funn 3-boksen).
4. **Dei 12 komplekstypane:** alle tekne med (§ Evaluering), fordelt på
   `brreg-felles-adresse`/`-aktoer`/`-tid` etter tema, unntatt
   `Beløpsintervall`/`BeløpIValuta` som ikkje høyrer naturleg til nokon
   (§ Vurdering).
5. **`brreg-felles-tid`:** opprettast no, ikkje utsett.
6. **`DigdirStandard`-pakken:** utelaten heilt, dokumentert som utkast/
   ikkje-autoritativ (§ Funn 4).
7. **Kjeldefiler i `src/tmp/`:** vert liggjande der — inga flytting til
   `docs/kjeldemateriale/` eller liknande.
8. **`bvrinn`/`bvrinnfelles`-duplikatet:** utskilt til eigen spec —
   `specs/done/enhetsregisteret-bvrinn-bvrinnfelles-duplikat.md`.
9. **`UUID`/`GUID`:** `brreg-felles-typer` brukar `UUID` konsekvent
   (Strukturtypekatalog sin `GUID` er ikkje teken med, sidan
   `brreg-felles-struktur-typer` er droppa, jf. punkt 3).
10. **Kjeldehenvisning:** éi kommentarlinje per type i
    `brreg-felles-typer-schema.yaml`.
11. **`make new-modell XML=`-utgreiing:** utskilt til eigen spec —
    `specs/done/make-new-modell-xmi-input-utgreiing.md`.

## Akseptansekriterium

- Alle fire `brreg-felles-*`-skjemaa (`brreg-felles-typer`,
  `brreg-felles-adresse`, `brreg-felles-aktoer`, `brreg-felles-tid`) finst
  under `src/linkml/felles/`, validerer kvar for seg med `make lint`, og
  har eit asyklisk importhierarki (§ Funn 4, § Vurdering).
- `felles` er lagt til som rad i CONVENTIONS.md sin URI-segment-tabell.
- `brreg-felles-typer` inneheld alle 59 typane frå Løsningstypekatalog_v1
  (ikkje berre dei med lokalt treff), kvar med éi kjeldekommentarlinje,
  og brukar `UUID` (ikkje `GUID`).
- Alle sju `enhetsregisteret-*`-skjema importerer `brreg-felles-typer` og
  har null lokale duplikat av dei migrerte typane (verifiserbart med same
  `awk`-søk som vart brukt i «Metode»).
- `make analyse-similar-slots-domain DOMAIN=oreg` og
  `make analyse-similar-classes-domain DOMAIN=oreg` viser färre/ingen
  100 %-treff for dei migrerte typenamna/klassenamna.

## Relaterte filer

- `src/tmp/BRProfilV2.xml`, `src/tmp/BRReferansemodell_v3.xml`,
  `src/tmp/Løsningstypekatalog_v1.xml`, `src/tmp/Strukturtypekatalog_v1.xml`
  — kjeldemateriale, vert liggjande i `src/tmp/` (avklaring punkt 7)
- `specs/done/enhetsregisteret-bvrinn-bvrinnfelles-duplikat.md` —
  utskilt spec for Funn 1 (avklaring punkt 8)
- `specs/done/make-new-modell-xmi-input-utgreiing.md` — utskilt spec
  for XML/XMI-input-utgreiinga (avklaring punkt 11)
- `make/02-schema-discovery.mk` — dynamisk domene-oppdaging, grunngjev
  tilrådinga i § Vurdering om å opprette `felles`-domenet
- `CONVENTIONS.md` § URI-segment-konvensjon — treng ny rad for `felles`
  (steg 1)
- `specs/backlog/del-opp-ap-no-profilar-i-moduler.md` — åtvaringa mot
  importoppblåsing § Vurdering byggjer vidare på
- `mkdocs/docs/arkitektur/importhierarki.md` — mønsteret denne specen
  følgjer (`common-ap-no-schema`, `fint-common-schema`)
- `src/tmp/analyse-similar-classes-domain-oreg.md`,
  `src/tmp/analyse-similar-slots-domain-oreg.md` — tidlegare
  duplikat-analyse i domenet (avgrensa treff fordi han berre samanliknar
  skjema mot kvarandre, ikkje mot BR-katalogane)

## Utført (31.08.2026)

**Steg 1-6 gjennomførte.** Steg 7 (feltvis samanlikning før klassemigrering)
og steg 8 (`Beløpsintervall`/`BeløpIValuta`) er **medvite utsette**, som
planlagt — begge krev eit konkret forbrukande skjema/behov først.

1. **`felles`-domenet** lagt til i CONVENTIONS.md § URI-segment-konvensjon.
2. **`brreg-felles-typer`** oppretta i `src/linkml/felles/brreg-felles-typer/`
   med alle 59 typane frå Løsningstypekatalog_v1 (53 deklarerte, 6 medvite
   utelatne som kollisjonar med `linkml:types`-builtinane, dokumentert i
   skjemaet). To av dei 14 XSD-primitivtypane (`GYear`, `NonNegativeInteger`)
   vart under arbeidet oppdaga å kollidere med typar i `common-ap-no-schema`
   òg (ikkje fanga opp i den opphavlege analysen, sidan ho ikkje kryssjekka
   mot AP-NO-importkjeda) — løyst med `Brreg`-prefiks
   (`BrregGYear`/`BrregNonNegativeInteger`) og dokumentert i skjemaet.
   `URI`/`URL`/`UUID` brukar stor forbokstav-forkorting (ikkje `Uri`/`Url`/
   `Uuid`) for å samsvare med både BR sitt eige kjeldenamn og eksisterande
   lokal konvensjon.
3. **`brreg-felles-adresse`** oppretta med 13 adresseklassar (`Aksesspunkt`
   utelaten og dokumentert, jf. avklaring punkt 2) + 5 adresse-relaterte
   komplekstypar frå Strukturtypekatalog_v1. Importerer `brreg-felles-typer`.
4. **`brreg-felles-aktoer`** oppretta med 7 aktørklassar + 3
   komplekstypar/enum-par frå Strukturtypekatalog_v1 (alle tekne med, jf.
   avklaring punkt 4). Importerer `brreg-felles-adresse`.
5. **`brreg-felles-tid`** oppretta med `Tidsperiode`
   (`class_uri: dct:PeriodOfTime` behalde) og `TidsperiodeDatoKlokkeslett`.
   Importerer `brreg-felles-typer`.
6. **Alle sju `enhetsregisteret-*`-skjema migrerte** til å importere
   `brreg-felles-typer` og fjerne dei lokale typedublettane som hadde
   eksakt/nesten-eksakt treff. To ekstra namnetreff (`E_postadresse` i
   `bvrfriv`/`bvrinn`/`bvrinnfelles`) vart oppdaga undervegs (ikkje fanga
   opp av den opphavlege `awk`-baserte analysen, sidan regexen ikkje
   matcha understrek) og migrert til `Epostadresse`. To **namnekollisjonar
   utan semantisk treff** vart oppdaga og løyst ved omdøyping av det
   lokale elementet (behalde lokal semantikk, unngå importkollisjon):
   - `bvrinn`/`bvrinnfelles` sin `Aktivitetskode` (eit heiltal,
     `uri: xsd:integer`) → omdøypt til `AktivitetskodeTal`, sidan
     `brreg-felles-typer` sin `Aktivitetskode` er ein tekstleg
     BR-forretningskode.
   - `bvrstiftelsesdokument` sin `Beloep` (ein streng med desimalmønster,
     `uri: xsd:string`) → omdøypt til `BeloepStreng`, sidan
     `brreg-felles-typer` sin `Beloep` er `uri: xsd:decimal`.

**Verifisering:** alle 4 nye + 7 migrerte skjema (`make lint`,
`make check-import-duplicates`) er reine — stadfesta både enkeltvis og
samla (`DOMAIN=felles`, `DOMAIN=oreg`, 13 skjema totalt, 0 kollisjonar).
`make roundtrip` køyrde grønt for `brreg-felles-typer`, `brreg-felles-adresse`,
`brreg-felles-aktoer`, `brreg-felles-tid`, og 4 av 7 migrerte
`enhetsregisteret-*`-skjema (`bvrbekreftelse`, `bvrettersendingavvedlegg`,
`bvrinn`, `bvrstiftelsesdokument`). For dei attverande tre
(`bvrfriv`, `bvrinnfelles`, `frivilligorganisasjonapi`) feila
`make roundtrip` gjentekne gonger med `<urlopen error [Errno -3] Try again>`
— DNS-oppløysingsfeil i podman-containeren ved henting av det
versjonslåste `dcat-ap-no-schema`-importet, stadfesta **uavhengig av
innhaldet i denne endringa** (same feilmønster oppstod også ved gjentekne
forsøk, og forsvann delvis/kom tilbake tilfeldig — typisk nettverksflakse,
ikkje eit deterministisk skjemaproblem). Desse tre bør roundtrip-testast på
nytt når nettverkstilgangen i miljøet er stabil.

**Ikkje utført i denne omgangen** (krev brukarstadfesting før dei kan
utførast, jf. dei to utskilte spesifikasjonane):
- `specs/done/enhetsregisteret-bvrinn-bvrinnfelles-duplikat.md` — steg 1
  der (avklar kjend bruk av `bvrinnfelles`) er ikkje gjort, sidan det kan
  leie til sletting av eit heilt skjema — ei destruktiv handling som krev
  eksplisitt brukarstadfesting.
- `specs/done/make-new-modell-xmi-input-utgreiing.md` — spec sin eigen
  konklusjon var å **ikkje** implementere `XML=`-flagget no; sjølve
  utgreiinga (leveransemålet for den specen) er fullført ved oppretting.
