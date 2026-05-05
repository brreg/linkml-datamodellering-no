# FINT Ressurs

FINT-domenemodell for ressursstyring. Dekkjer tre sub-pakkar: ressurs.eiendel (applikasjonar og lisensressursar), ressurs.datautstyr (digitale einingar og einingsgrupper) og ressurs.tilgang (identitetar og rettigheiter).


URI: https://data.norge.no/linkml/fint-ressurs

Name: fint-ressurs



## Classes

| Class | Description |
| --- | --- |
| [Adresse](adresse.md) | Fysisk adresse eller postadresse |
| [Aktoer](aktoer.md) | Abstrakt base for person eller eining vi samhandlar med |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Person](person.md) | Fysiske private personar |
| [Applikasjon](applikasjon.md) | Ein applikasjon med tilhøyrande ressursar |
| [Applikasjonskategori](applikasjonskategori.md) | Kategori av applikasjonar |
| [Applikasjonsressurs](applikasjonsressurs.md) | Informasjon om kor ein applikasjon kan nyttast (lisensressurs) |
| [Applikasjonsressurstilgjengelighet](applikasjonsressurstilgjengelighet.md) | Kva organisasjonselements brukarar som har tilgang til ein ressurs |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fylke](fylke.md) | Liste over Norges fylker |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kommune](kommune.md) | Liste over Norges kommunar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |
| [Brukertype](brukertype.md) | Dei ulike brukartypane som kan nytte lisensen (t |
| [DigitalEnhet](digitalenhet.md) | Ei digital eining som t |
| [Enhetsgruppe](enhetsgruppe.md) | Ei gruppering av einsarta digitale einingar (t |
| [Enhetsgruppemedlemskap](enhetsgruppemedlemskap.md) | Medlemskap mellom ei digital eining og ei einingsgruppe |
| [Enhetstype](enhetstype.md) | Type digital eining (t |
| [Handhevingstype](handhevingstype.md) | Korleis ulike lisensmodellar kan handhevast (Håndhevingstype) |
| [Identifikator](identifikator.md) | Unik identifikasjon til eit objekt |
| [Identitet](identitet.md) | Identitet som identifiserer innehavaren av rettigheiter i organisasjonen |
| [Kontaktinformasjon](kontaktinformasjon.md) | Informasjon som kan brukast for å oppnå kontakt |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |
| [Lisensmodell](lisensmodell.md) | Lisensmodellar som kan knytast til ein lisens |
| [Matrikkelnummer](matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |
| [Periode](periode.md) | Tidsperiode med obligatorisk start og valfri slutt |
| [Personnavn](personnavn.md) | Namn på ein person |
| [Plattform](plattform.md) | Plattforma tenesta kan leverast på (t |
| [Produsent](produsent.md) | Produsent av ei digital eining |
| [RessursContainer](ressurscontainer.md) | Rotcontainer for FINT Ressurs-instansar |
| [Rettighet](rettighet.md) | Ei namngitt rettighet |
| [Status](status.md) | Status på ei digital eining i fagsystemet |
| [Valuta](valuta.md) | Valutakodar for offisielle valutaer |



## Slots

| Slot | Description |
| --- | --- |
| [administrator](administrator.md) | Referanse til Organisasjonselement som administrerer eininga |
| [adresse](adresse.md) | Adresse til matrikkeleining |
| [adresselinje](adresselinje.md) | Adresseinformasjon |
| [applikasjon](applikasjon.md) | Applikasjonen denne ressursen (lisensen) er knytt til |
| [applikasjonar](applikasjonar.md) |  |
| [applikasjonskategori](applikasjonskategori.md) | Kategoriar av applikasjonar |
| [applikasjonskategoriar](applikasjonskategoriar.md) |  |
| [applikasjonsressursar](applikasjonsressursar.md) |  |
| [applikasjonsressurstilgjengelegheit](applikasjonsressurstilgjengelegheit.md) |  |
| [beskrivelse](beskrivelse.md) |  |
| [bilde](bilde.md) | HTTP(S)-lenkje til eit bilete av personen |
| [bokstavkode](bokstavkode.md) | Bokstavkode for aktuell valuta |
| [bostedsadresse](bostedsadresse.md) | Folkeregistrert adresse til personen |
| [brukertypar](brukertypar.md) |  |
| [brukertype](brukertype.md) | For kva brukertypar denne lisensen er gyldig |
| [bruksnummer](bruksnummer.md) | Fortløpande nummerering av bruk under gårdsnummer |
| [dataobjektId](dataobjektid.md) | Einingsens ID i datakatalogen (t |
| [digitaleEiningar](digitaleeiningar.md) |  |
| [digitalEnhet](digitalenhet.md) | Den digitale eininga dette medlemskapet tilhøyrer |
| [eier](eier.md) | Referanse til Organisasjonselement som har eigarskap til lisensen |
| [einingsgruppedmedlemskap](einingsgruppedmedlemskap.md) |  |
| [einingsgrupper](einingsgrupper.md) |  |
| [einingstypar](einingstypar.md) |  |
| [elev](elev.md) | Referanse til Elev (Utdanning) som nyttar eininga |
| [enhetsgruppe](enhetsgruppe.md) | Einingsgruppen dette medlemskapet tilhøyrer |
| [enhetsgruppemedlemskap](enhetsgruppemedlemskap.md) | Einingsgruppene eininga er medlem av |
| [enhetskostnad](enhetskostnad.md) | Kostnad per ressurs |
| [enhetstype](enhetstype.md) | Type digital eining: Mobiltelefon, datamaskin, nettbrett |
| [epostadresse](epostadresse.md) | Namngitt elektronisk adresse for mottak av e-post |
| [etternavn](etternavn.md) | Etternamn til personen |
| [festenummer](festenummer.md) | Fortløpande nummerering av festar under gårdsnummer/bruksnummer |
| [flerbrukerenhet](flerbrukerenhet.md) | Kvifor eininga er ein- eller flerbrukarenheit |
| [fodselsdato](fodselsdato.md) | Dato for fødsel |
| [fodselsnummer](fodselsnummer.md) | Fødselsnummer eller ein av dei fiktive variantane |
| [foreldre](foreldre.md) | Den/dei som har foreldreansvar til personen |
| [foreldreansvar](foreldreansvar.md) | Personar denne personen har foreldreansvar for |
| [fornavn](fornavn.md) | Fornamn til personen |
| [forretningsadresse](forretningsadresse.md) | Besøksadresse til ein organisasjonseining i einingsregisteret |
| [fylke](fylke.md) | Fylket kommunen høyrer til |
| [gaardsnummer](gaardsnummer.md) | Nummerering av gårdseiging i matrikkelen, unik innanfor kommune |
| [gyldighetsperiode](gyldighetsperiode.md) | Start- og sluttdato for gyldighetsperioden til applikasjonen |
| [handhaevingstypar](handhaevingstypar.md) |  |
| [handhevingstype](handhevingstype.md) | Korleis det skal handhevast når lisensantall vert overskredet (Håndhevingstyp... |
| [id](id.md) | URI-identifikator for ressursen |
| [identifikatorverdi](identifikatorverdi.md) | Ein konkret kombinasjon av teikn og/eller bokstavar som utgjer ein bestemt id... |
| [identitet](identitet.md) | Identitetar knytt til rettigheta |
| [identitetar](identitetar.md) |  |
| [kjonn](kjonn.md) | Kjønn for personen |
| [kode](kode.md) | Verdi som identifiserer omgrepet |
| [kommune](kommune.md) | Alle kommunar som inngår i fylket |
| [kommunenummer](kommunenummer.md) | Nummerering av kommunen i høve til SSB si offisielle liste |
| [konsument](konsument.md) | Referanse til Organisasjonselement som har tilgang til denne ressursen |
| [kontaktinformasjon](kontaktinformasjon.md) | Den føretrekte måten å kome i kontakt med ein aktør |
| [kontaktperson](kontaktperson.md) | Personar kontaktpersonen er pårørande for |
| [kreverGodkjenning](krevergodkjenning.md) | True dersom tildeling av ressursen krev godkjenning av leiar/tenestteforvalta... |
| [laerling](laerling.md) | Referanse til Laerling (Utdanning) |
| [land](land.md) | Land der adressa befinn seg |
| [lisensantall](lisensantall.md) | Totalt tal på lisensar |
| [lisensmodell](lisensmodell.md) | Kva lisensmodell applikasjonsressursen har |
| [lisensmodellar](lisensmodellar.md) |  |
| [maalform](maalform.md) | Målform personen føretrekkjer |
| [mellomnavn](mellomnavn.md) | Mellomnamn |
| [mobiltelefonnummer](mobiltelefonnummer.md) | Mobiltelefonnummer |
| [morsmaal](morsmaal.md) | Morsmål til personen |
| [navn](navn.md) |  |
| [nettsted](nettsted.md) | Adresse til eit nettstad |
| [nummerkode](nummerkode.md) | Nummerkode for aktuell valuta |
| [organisasjonsenhet](organisasjonsenhet.md) | Referanse til Organisasjonselement grupperinga er tilknytt |
| [organisasjonsnavn](organisasjonsnavn.md) | Namn på eining registrert i Einingsregisteret |
| [organisasjonsnummer](organisasjonsnummer.md) | Niisifra nummer som eintydleg identifiserer einingar i Einingsregisteret |
| [otungdom](otungdom.md) | Referanse til OtUngdom (Utdanning) |
| [parorende](parorende.md) | Pårørande kontaktperson til personen |
| [passiv](passiv.md) | Angir at koden er passiv og ikkje kan veljast |
| [personalressurs](personalressurs.md) | Referanse til Personalressurs (Administrasjon) som nyttar eininga |
| [plattform](plattform.md) | Den eller dei plattformane applikasjonen kan køyre på |
| [plattformar](plattformar.md) |  |
| [postadresse](postadresse.md) | Informasjon om postadresse til ein aktør |
| [postnummer](postnummer.md) | Postnummer |
| [poststed](poststed.md) | Poststad |
| [privateid](privateid.md) | Angir om eininga er eigd av organisasjonen eller privatperson |
| [produsent](produsent.md) | Namn på produsenten av eininga |
| [produsentar](produsentar.md) |  |
| [ressurs](ressurs.md) | Ulike ressursar (lisensar) knytt til denne applikasjonen |
| [ressurstilgjengelighet](ressurstilgjengelighet.md) | Angir kva organisasjonseining og kor mange ressursar som skal tilordnast |
| [rettigheiter](rettigheiter.md) |  |
| [rettighet](rettighet.md) | Rettigheiter knytt til identiteten |
| [seksjonsnummer](seksjonsnummer.md) | Fortløpande nummerering av seksjonar under gårdsnummer/bruksnummer |
| [serienummer](serienummer.md) | Unikt serienummer frå einingsprodusentens |
| [sip](sip.md) | SIP-protokoll for VoIP (IP-telefoni) |
| [slutt](slutt.md) | Til tidspunkt |
| [start](start.md) | Frå tidspunkt |
| [statsborgerskap](statsborgerskap.md) | Alle statsborgarskap personen har |
| [status](status.md) | Status på eininga i fagsystemet |
| [statusar](statusar.md) |  |
| [telefonnummer](telefonnummer.md) | Telefonnummer |
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
