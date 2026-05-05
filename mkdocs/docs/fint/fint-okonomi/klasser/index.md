# FINT Økonomi

FINT-domenemodell for økonomi. Dekkjer tre sub-pakkar: okonomi.faktura (faktura, fakturagrunnlag, fakturautsteder), okonomi.regnskap (transaksjonar, posteringar, bilag, leverandørar) og okonomi.kodeverk (vare, merverdiavgift, valuta).


URI: https://data.norge.no/linkml/fint-okonomi

Name: fint-okonomi



## Classes

| Class | Description |
| --- | --- |
| [Adresse](adresse.md) | Fysisk adresse eller postadresse |
| [Aktoer](aktoer.md) | Abstrakt base for person eller eining vi samhandlar med |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Person](person.md) | Fysiske private personar |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fylke](fylke.md) | Liste over Norges fylker |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kommune](kommune.md) | Liste over Norges kommunar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |
| [Bilag](bilag.md) | Dokumentasjon til ein transaksjon (kompleks datatype) |
| [Faktura](faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |
| [Fakturagrunnlag](fakturagrunnlag.md) | Grunnlag for fakturering |
| [Fakturalinje](fakturalinje.md) | Del av Fakturagrunnlag som skildrar ei enkelt vare (kompleks datatype) |
| [Fakturamottaker](fakturamottaker.md) | Aktør som skal betale faktura (kompleks datatype) |
| [Fakturautsteder](fakturautsteder.md) | Eining som utformar og oversender faktura og mottar betaling |
| [Identifikator](identifikator.md) | Unik identifikasjon til eit objekt |
| [Kontaktinformasjon](kontaktinformasjon.md) | Informasjon som kan brukast for å oppnå kontakt |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |
| [Kontostreng](kontostreng.md) | Kontodimensjonar for ei postering (kompleks datatype) |
| [Leverandor](leverandor.md) | Person eller verksemd som leverer produkt eller tenester (Leverandør) |
| [Leverandorgruppe](leverandorgruppe.md) | Gruppering av leverandørar (Leverandørgruppe) |
| [Matrikkelnummer](matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |
| [Merverdiavgift](merverdiavgift.md) | Kodeverk for merverdiavgifter |
| [OkonomiContainer](okonomicontainer.md) | Rotcontainer for FINT Økonomi-instansar |
| [OkonomiValuta](okonomivaluta.md) | Valuta for transaksjonsbeløp |
| [Periode](periode.md) | Tidsperiode med obligatorisk start og valfri slutt |
| [Personnavn](personnavn.md) | Namn på ein person |
| [Postering](postering.md) | Føring på ein konto i rekneskapet |
| [Transaksjon](transaksjon.md) | Overføring av pengar til eller frå eksterne partar |
| [Valuta](valuta.md) | Valutakodar for offisielle valutaer |
| [Vare](vare.md) | Vare eller teneste som kan leverast og fakturerast |



## Slots

| Slot | Description |
| --- | --- |
| [adresse](adresse.md) | Adresse til mottakar |
| [adresselinje](adresselinje.md) | Adresseinformasjon |
| [ansvar](ansvar.md) | Ansvarsomrade |
| [ansvarlig](ansvarlig.md) | Referanse til Personalressurs (Administrasjon) som er ansvarleg for å godkjen... |
| [antall](antall.md) | Mengd av varen levert |
| [art](art.md) | Artskonto (type utgift/inntekt) |
| [avgiftsbelop](avgiftsbelop.md) | Del av totalbeløp som er avgifter, i øre (avgiftsbeløp) |
| [belop](belop.md) | Beløp mottakar skal betale, i øre (beløp) |
| [beskrivelse](beskrivelse.md) | Skildring av transaksjonen |
| [betalt](betalt.md) | Status på betaling |
| [bilag](bilag.md) | Bilag til transaksjonen |
| [bilagsdato](bilagsdato.md) | Dato bilaget er registrert |
| [bilagsnummer](bilagsnummer.md) | Nummer på bilaget |
| [bilde](bilde.md) | HTTP(S)-lenkje til eit bilete av personen |
| [bokstavkode](bokstavkode.md) | Bokstavkode for aktuell valuta |
| [bostedsadresse](bostedsadresse.md) | Folkeregistrert adresse til personen |
| [bruksnummer](bruksnummer.md) | Fortløpande nummerering av bruk under gårdsnummer |
| [data](data.md) | Bilagets fil, koda som Base64 |
| [dato](dato.md) | Dato for utferding av faktura |
| [debet](debet.md) | Angir om posteringa er debet eller kredit |
| [elev](elev.md) | Referanse til Elev (Utdanning) |
| [enhet](enhet.md) | Namn på mengdeeininga varen leverast i |
| [epostadresse](epostadresse.md) | Namngitt elektronisk adresse for mottak av e-post |
| [etternavn](etternavn.md) | Etternamn til personen |
| [faktura](faktura.md) | Utferdigde fakturaer for fakturagrunnlaget |
| [fakturaer](fakturaer.md) |  |
| [fakturagrunnlag](fakturagrunnlag.md) |  |
| [fakturalinjer](fakturalinjer.md) | Linjer av varer eller tenester som skal fakturerast |
| [fakturanummer](fakturanummer.md) | Identifikator oppretta i fakturaprogrammet |
| [fakturautsteder](fakturautsteder.md) | Utstedar av faktura og mottakar av betaling |
| [fakturautstederear](fakturautstederear.md) |  |
| [fakturert](fakturert.md) | Status på utsending |
| [festenummer](festenummer.md) | Fortløpande nummerering av festar under gårdsnummer/bruksnummer |
| [filnavn](filnavn.md) | Namn på bilagets fil |
| [fodselsdato](fodselsdato.md) | Dato for fødsel |
| [fodselsnummer](fodselsnummer.md) | Fødselsnummer eller ein av dei fiktive variantane |
| [foreldre](foreldre.md) | Den/dei som har foreldreansvar til personen |
| [foreldreansvar](foreldreansvar.md) | Personar denne personen har foreldreansvar for |
| [forfallsdato](forfallsdato.md) | Frist for betaling |
| [fornavn](fornavn.md) | Fornamn til personen |
| [forretningsadresse](forretningsadresse.md) | Besøksadresse til ein organisasjonseining i einingsregisteret |
| [fritekst](fritekst.md) | Fritekst som skildrar varen slik han er levert |
| [funksjon](funksjon.md) | Funksjonskode (KOSTRA) |
| [fylke](fylke.md) | Fylket kommunen høyrer til |
| [gaardsnummer](gaardsnummer.md) | Nummerering av gårdseiging i matrikkelen, unik innanfor kommune |
| [gyldighetsperiode](gyldighetsperiode.md) | Angir gyldighetsperioden for omgrepet/koden |
| [id](id.md) | URI-identifikator for ressursen |
| [identifikatorverdi](identifikatorverdi.md) | Ein konkret kombinasjon av teikn og/eller bokstavar som utgjer ein bestemt id... |
| [kjonn](kjonn.md) | Kjønn for personen |
| [kode](kode.md) | Verdi som identifiserer omgrepet |
| [kommune](kommune.md) | Alle kommunar som inngår i fylket |
| [kommunenummer](kommunenummer.md) | Nummerering av kommunen i høve til SSB si offisielle liste |
| [kontaktinformasjon](kontaktinformasjon.md) | Den føretrekte måten å kome i kontakt med ein aktør |
| [kontaktperson](kontaktperson.md) | Personar kontaktpersonen er pårørande for |
| [kontering](kontering.md) | Kontodimensjonar for posteringa |
| [kontonummer](kontonummer.md) | Kontonummer til leverandøren |
| [kreditert](kreditert.md) | Status på kreditering |
| [laerling](laerling.md) | Referanse til Laerling (Utdanning) |
| [land](land.md) | Land der adressa befinn seg |
| [leverandor](leverandor.md) | Leverandør knytt til transaksjonen (leverandor) |
| [leverandorar](leverandorar.md) |  |
| [leverandorgruppe](leverandorgruppe.md) | Gruppe av leverandørar leverandøren tilhøyrer (leverandørgruppe) |
| [leverandorgrupper](leverandorgrupper.md) |  |
| [leverandornummer](leverandornummer.md) | Nummer som identifiserer ein leverandør (leverandørnummer) |
| [leveringsdato](leveringsdato.md) | Dato varer eller tenester vart leverte |
| [maalform](maalform.md) | Målform personen føretrekkjer |
| [mellomnavn](mellomnavn.md) | Mellomnamn |
| [merverdiavgift](merverdiavgift.md) | Varens avgiftsklasse og -sats |
| [merverdiavgifter](merverdiavgifter.md) |  |
| [mobiltelefonnummer](mobiltelefonnummer.md) | Mobiltelefonnummer |
| [morsmaal](morsmaal.md) | Morsmål til personen |
| [mottaker](mottaker.md) | Namn på mottakar |
| [navn](navn.md) | Juridisk namn på fakturutstedar |
| [nettobelop](nettobelop.md) | Del av totalbeløp som utgjer summen av fakturalinjene, i øre (nettobeløp) |
| [nettsted](nettsted.md) | Adresse til eit nettstad |
| [nummerkode](nummerkode.md) | Nummerkode for aktuell valuta |
| [oppdateringstidspunkt](oppdateringstidspunkt.md) | Tidspunkt for siste endring i transaksjonen |
| [ordrenummer](ordrenummer.md) | Unik identifikator for ordren det skal utferdigast faktura på |
| [organisasjonselement](organisasjonselement.md) | Referanse til Organisasjonselement (Administrasjon) som kan utstede faktura |
| [organisasjonsnavn](organisasjonsnavn.md) | Namn på eining registrert i Einingsregisteret |
| [organisasjonsnummer](organisasjonsnummer.md) | Niisifra nummer som eintydleg identifiserer einingar i Einingsregisteret |
| [otungdom](otungdom.md) | Referanse til OtUngdom (Utdanning) |
| [parorende](parorende.md) | Pårørande kontaktperson til personen |
| [passiv](passiv.md) | Angir at koden er passiv og ikkje kan veljast |
| [person](person.md) | Referanse til Person (Administrasjon) som skal betale faktura |
| [personalressurs](personalressurs.md) | Referanse til Personalressurs (Administrasjon) |
| [postadresse](postadresse.md) | Informasjon om postadresse til ein aktør |
| [postering](postering.md) | Posteringar tilhøyrande transaksjonen |
| [posteringar](posteringar.md) |  |
| [posteringsId](posteringsid.md) | Intern unik identifikator i økonomisystemet |
| [postnummer](postnummer.md) | Postnummer |
| [poststed](poststed.md) | Poststad |
| [pris](pris.md) | Pris per eining levert, i øre |
| [prosjekt](prosjekt.md) | Prosjektkode |
| [referanse](referanse.md) | Ekstern referanse, t |
| [restbelop](restbelop.md) | Gjenståande beløp å betale, i øre (restbeløp) |
| [sats](sats.md) | Sats for merverdiavgift |
| [seksjonsnummer](seksjonsnummer.md) | Fortløpande nummerering av seksjonar under gårdsnummer/bruksnummer |
| [sip](sip.md) | SIP-protokoll for VoIP (IP-telefoni) |
| [slutt](slutt.md) | Til tidspunkt |
| [start](start.md) | Frå tidspunkt |
| [statsborgerskap](statsborgerskap.md) | Alle statsborgarskap personen har |
| [telefonnummer](telefonnummer.md) | Telefonnummer |
| [totalbelop](totalbelop.md) | Totalt beløp på faktura inkl |
| [transaksjon](transaksjon.md) | Transaksjonen posteringa tilhøyrer |
| [transaksjonar](transaksjonar.md) |  |
| [transaksjonsId](transaksjonsid.md) | Intern unik identifikator i økonomisystemet |
| [transaksjonstidspunkt](transaksjonstidspunkt.md) | Tidspunkt for registrering av transaksjonen |
| [type](type.md) | Beskriv kva slags type kontaktperson |
| [url](url.md) | URL til eksternt dokument |
| [valuta](valuta.md) | Valuta for oppgjeve beløp |
| [valutaer](valutaer.md) |  |
| [vare](vare.md) | Alle varer i vareregisteret til fakturutstedaren |
| [varer](varer.md) |  |
| [virksomhet](virksomhet.md) | Referanse til Virksomhet som er leverandør |
| [virksomhetsId](virksomhetsid.md) | Intern unik identifikator i økonomisystemet |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |
| [Boolean](boolean.md) | A binary (true or false) value |
| [Curie](curie.md) | a compact URI |
| [Date](date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](dateordatetime.md) | Either a date or a datetime |
| [Datetime](datetime.md) | The combination of a date and time |
| [Decimal](decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](double.md) | A real number that conforms to the xsd:double specification |
| [Float](float.md) | A real number that conforms to the xsd:float specification |
| [Integer](integer.md) | An integer |
| [Jsonpath](jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](string.md) | A character string |
| [Time](time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](uri.md) | a complete URI |
| [Uriorcurie](uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
| [Anbefalt](anbefalt.md) | Anbefalt eigensskap |
| [Obligatorisk](obligatorisk.md) | Obligatorisk eigensskap |
| [Valgfri](valgfri.md) | Valfri eigensskap |
