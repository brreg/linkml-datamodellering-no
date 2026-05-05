# FINT Personvern

FINT-domenemodell for personvern. Dekkjer behandling av personopplysningar, samtykke, tenester og kodeverk for behandlingsgrunnlag og personopplysningstypar.


URI: https://data.norge.no/linkml/fint-personvern

Name: fint-personvern



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
| [Behandling](behandling.md) | All bruk av personopplysningar (behandlingsaktivitet) |
| [Behandlingsgrunnlag](behandlingsgrunnlag.md) | Rettsleg grunnlag for behandling av personopplysningar |
| [Identifikator](identifikator.md) | Unik identifikasjon til eit objekt |
| [Kontaktinformasjon](kontaktinformasjon.md) | Informasjon som kan brukast for å oppnå kontakt |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |
| [Matrikkelnummer](matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |
| [Periode](periode.md) | Tidsperiode med obligatorisk start og valfri slutt |
| [Personnavn](personnavn.md) | Namn på ein person |
| [Personopplysning](personopplysning.md) | Opplysningar og vurderingar som kan knytast til enkeltpersonar |
| [PersonvernContainer](personverncontainer.md) | Rotcontainer for FINT Personvern-instansar |
| [Samtykke](samtykke.md) | Tillating til behandling av personopplysning |
| [Tjeneste](tjeneste.md) | Teneste eller system som behandlar personopplysningar |
| [Valuta](valuta.md) | Valutakodar for offisielle valutaer |



## Slots

| Slot | Description |
| --- | --- |
| [adresse](adresse.md) | Adresse til matrikkeleining |
| [adresselinje](adresselinje.md) | Adresseinformasjon |
| [aktiv](aktiv.md) | Status på behandling |
| [behandling](behandling.md) | Behandling som vert omfatta av samtykket |
| [behandlingar](behandlingar.md) |  |
| [behandlingsgrunnlag](behandlingsgrunnlag.md) |  |
| [beskrivelse](beskrivelse.md) | Beskriven namn på perioden |
| [bilde](bilde.md) | HTTP(S)-lenkje til eit bilete av personen |
| [bokstavkode](bokstavkode.md) | Bokstavkode for aktuell valuta |
| [bostedsadresse](bostedsadresse.md) | Folkeregistrert adresse til personen |
| [bruksnummer](bruksnummer.md) | Fortløpande nummerering av bruk under gårdsnummer |
| [elev](elev.md) | Referanse til Elev (Utdanning) |
| [epostadresse](epostadresse.md) | Namngitt elektronisk adresse for mottak av e-post |
| [etternavn](etternavn.md) | Etternamn til personen |
| [festenummer](festenummer.md) | Fortløpande nummerering av festar under gårdsnummer/bruksnummer |
| [fodselsdato](fodselsdato.md) | Dato for fødsel |
| [fodselsnummer](fodselsnummer.md) | Fødselsnummer eller ein av dei fiktive variantane |
| [foreldre](foreldre.md) | Den/dei som har foreldreansvar til personen |
| [foreldreansvar](foreldreansvar.md) | Personar denne personen har foreldreansvar for |
| [formal](formal.md) | Grunngjeving for behandling av personopplysning |
| [fornavn](fornavn.md) | Fornamn til personen |
| [forretningsadresse](forretningsadresse.md) | Besøksadresse til ein organisasjonseining i einingsregisteret |
| [fylke](fylke.md) | Fylket kommunen høyrer til |
| [gaardsnummer](gaardsnummer.md) | Nummerering av gårdseiging i matrikkelen, unik innanfor kommune |
| [gyldighetsperiode](gyldighetsperiode.md) | Tidsrom samtykket er gyldig |
| [id](id.md) | URI-identifikator for ressursen |
| [identifikatorverdi](identifikatorverdi.md) | Ein konkret kombinasjon av teikn og/eller bokstavar som utgjer ein bestemt id... |
| [kjonn](kjonn.md) | Kjønn for personen |
| [kode](kode.md) | Verdi som identifiserer omgrepet |
| [kommune](kommune.md) | Alle kommunar som inngår i fylket |
| [kommunenummer](kommunenummer.md) | Nummerering av kommunen i høve til SSB si offisielle liste |
| [kontaktinformasjon](kontaktinformasjon.md) | Den føretrekte måten å kome i kontakt med ein aktør |
| [kontaktperson](kontaktperson.md) | Personar kontaktpersonen er pårørande for |
| [laerling](laerling.md) | Referanse til Laerling (Utdanning) |
| [land](land.md) | Land der adressa befinn seg |
| [maalform](maalform.md) | Målform personen føretrekkjer |
| [mellomnavn](mellomnavn.md) | Mellomnamn |
| [mobiltelefonnummer](mobiltelefonnummer.md) | Mobiltelefonnummer |
| [morsmaal](morsmaal.md) | Morsmål til personen |
| [navn](navn.md) | Tittel på tenesta |
| [nettsted](nettsted.md) | Adresse til eit nettstad |
| [nummerkode](nummerkode.md) | Nummerkode for aktuell valuta |
| [opprettet](opprettet.md) | Dato då samtykket vart oppretta |
| [organisasjonselement](organisasjonselement.md) | Referanse til Organisasjonselement (Administrasjon) tilknytt samtykket |
| [organisasjonsnavn](organisasjonsnavn.md) | Namn på eining registrert i Einingsregisteret |
| [organisasjonsnummer](organisasjonsnummer.md) | Niisifra nummer som eintydleg identifiserer einingar i Einingsregisteret |
| [otungdom](otungdom.md) | Referanse til OtUngdom (Utdanning) |
| [parorende](parorende.md) | Pårørande kontaktperson til personen |
| [passiv](passiv.md) | Angir at koden er passiv og ikkje kan veljast |
| [person](person.md) | Referanse til Person (Administrasjon) som har gjeve samtykke |
| [personalressurs](personalressurs.md) | Referanse til Personalressurs (Administrasjon) |
| [personopplysning](personopplysning.md) | Opplysning eller vurdering som kan knytast til ein enkeltperson |
| [personopplysningar](personopplysningar.md) |  |
| [postadresse](postadresse.md) | Informasjon om postadresse til ein aktør |
| [postnummer](postnummer.md) | Postnummer |
| [poststed](poststed.md) | Poststad |
| [samtykke](samtykke.md) | Samtykker tilknytt ei behandling |
| [samtykker](samtykker.md) |  |
| [seksjonsnummer](seksjonsnummer.md) | Fortløpande nummerering av seksjonar under gårdsnummer/bruksnummer |
| [sip](sip.md) | SIP-protokoll for VoIP (IP-telefoni) |
| [slettet](slettet.md) | Tidspunkt behandlinga er sletta |
| [slutt](slutt.md) | Til tidspunkt |
| [start](start.md) | Frå tidspunkt |
| [statsborgerskap](statsborgerskap.md) | Alle statsborgarskap personen har |
| [telefonnummer](telefonnummer.md) | Telefonnummer |
| [tenester](tenester.md) |  |
| [tjeneste](tjeneste.md) | Tenesta som behandlinga tilhøyrer |
| [type](type.md) | Beskriv kva slags type kontaktperson |
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
