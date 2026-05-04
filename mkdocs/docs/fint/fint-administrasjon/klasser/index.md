# FINT Administrasjon

FINT-domenemodell for administrasjon og HR. Dekkjer personalressursar, arbeidsforhold, fullmakter og organisasjonsstruktur.


URI: https://data.norge.no/linkml/fint-administrasjon

Name: fint-administrasjon



## Classes

| Class | Description |
| --- | --- |
| [AdministrasjonContainer](AdministrasjonContainer.md) | Rotcontainer for FINT Administrasjon-instansar |
| [Adresse](Adresse.md) | Fysisk adresse eller postadresse |
| [Aktoer](Aktoer.md) | Abstrakt base for person eller eining vi samhandlar med |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Enhet](Enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Virksomhet](Virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Person](Person.md) | Fysiske private personar |
| [Arbeidsforhold](Arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |
| [Arbeidslokasjon](Arbeidslokasjon.md) | Fysisk lokasjon der ein tilsett har sitt arbeidsstad |
| [Begrep](Begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Aktivitet](Aktivitet.md) | Del av kontostrengen og detaljering av funksjon |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Anlegg](Anlegg.md) | Del av kontostrengen; objekt som skal aktiverast eller avskrivast |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Ansvar](Ansvar.md) | Del av kontostrengen som beskriv kven som har ansvaret for ei utgift eller in... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Arbeidsforholdstype](Arbeidsforholdstype.md) | Viser kva behov hos arbeidsgjevar arbeidsforholdet dekkjer |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Art](Art.md) | Del av kontostrengen som beskriv kva slags inntekter og utgifter det gjeld |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Diverse](Diverse.md) | Del av kontostrengen; supplement til øvrige dimensjonar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Formaal](Formaal.md) | Del av kontostrengen som detaljerer inntekter og utgifter ved drift |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fravaersgrunn](Fravaersgrunn.md) | Grunn til fråvær |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fravaerstype](Fravaerstype.md) | Type fråvær |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Funksjon](Funksjon.md) | Del av kontostrengen som beskriv kva som vert produsert |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fylke](Fylke.md) | Liste over Norges fylker |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kjonn](Kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kommune](Kommune.md) | Liste over Norges kommunar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kontrakt](Kontrakt.md) | Kontrakt transaksjonen er knytt til |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Landkode](Landkode.md) | Landskode i ISO 3166-1 alpha-2 format |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Lonsart](Lonsart.md) | Type ytelse |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Lopenummer](Lopenummer.md) | Løpenummer i ei nummerserie |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Objekt](Objekt.md) | Eit bygg, ein veg eller ein mottakar av ei teneste eller eit tilskott |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Organisasjonstype](Organisasjonstype.md) | Typen til eit organisasjonselement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Personalressurskategori](Personalressurskategori.md) | Ansettelsesform til eit arbeidsforhold |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Prosjekt](Prosjekt.md) | Del av kontostrengen som peikar på løpande prosjekt |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Prosjektart](Prosjektart.md) | Element i ei prosjektnedbrytningsstruktur eller arbeidsnedbrytningsstruktur |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Ramme](Ramme.md) | Del av kontostrengen som viser kva budsjettramme som skal bere kostnadane |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Spraak](Spraak.md) | Verdiar for språk (2 bokstavar) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Stillingskode](Stillingskode.md) | Felles kodeverk for stillingar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Uketimetall](Uketimetall.md) | Timer per veke i 100 % stilling |
| [Fravaer](Fravaer.md) | Fråvær frå eit arbeidsforhold |
| [Fullmakt](Fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |
| [Identifikator](Identifikator.md) | Unik identifikasjon til eit objekt |
| [Kontaktinformasjon](Kontaktinformasjon.md) | Informasjon som kan brukast for å oppnå kontakt |
| [Kontaktperson](Kontaktperson.md) | Kontaktperson (pårørande) til ein person |
| [Kontostreng](Kontostreng.md) | Sammensetning av kontodimensjonar for bokføring |
| [Lonn](Lonn.md) | Informasjon om lønn for eit arbeidsforhold (abstrakt base) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fastlonn](Fastlonn.md) | Informasjon om fast lønnsbeordring |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fasttillegg](Fasttillegg.md) | Faste tillegg til utbetaling |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Variabellonn](Variabellonn.md) | Informasjon om variabel lønn |
| [Matrikkelnummer](Matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |
| [Organisasjonselement](Organisasjonselement.md) | Eit element i organisasjonsstrukturen |
| [Periode](Periode.md) | Tidsperiode med obligatorisk start og valfri slutt |
| [Personalressurs](Personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |
| [Personnavn](Personnavn.md) | Namn på ein person |
| [Rolle](Rolle.md) | Rettighet eller type fullmakt |
| [Valuta](Valuta.md) | Valutakodar for offisielle valutaer |



## Slots

| Slot | Description |
| --- | --- |
| [aarslonn](aarslonn.md) | Årslønn/grunnlønn i 100 % stilling |
| [adresse](adresse.md) | Adresse til matrikkeleining |
| [adresselinje](adresselinje.md) | Adresseinformasjon |
| [aktivitet](aktivitet.md) | Detaljering av funksjon |
| [aktivitetar](aktivitetar.md) |  |
| [anlegg](anlegg.md) |  |
| [ansattnummer](ansattnummer.md) | Unik identifikator for den tilsette i HR-systemet |
| [ansettelsesperiode](ansettelsesperiode.md) | Perioden personalressursen er i eit tilhøve til organisasjonen |
| [ansettelsesprosent](ansettelsesprosent.md) | Prosenten personalressursen eig i høve til arbeidsavtalen |
| [ansiennitet](ansiennitet.md) | Ansiennitet for personalressurs hos arbeidsgjevar |
| [ansvar](ansvar.md) |  |
| [antall](antall.md) | Mengde som vert beskriven av tillegget, i hundredeler |
| [anviser](anviser.md) | Personalressurs som har anvist lønsmeldinga etter fullmakt |
| [anvist](anvist.md) | Tidspunkt då lønn vart anvist |
| [arbeidsforhold](arbeidsforhold.md) |  |
| [arbeidsforholdsperiode](arbeidsforholdsperiode.md) | Periode for ei gjeven stilling |
| [arbeidsforholdstypar](arbeidsforholdstypar.md) |  |
| [arbeidsforholdstype](arbeidsforholdstype.md) | Beskriven kode som kategoriserer kva funksjon stillinga er gruppert til |
| [arbeidslokasjon](arbeidslokasjon.md) | Fysisk lokasjon der den tilsette har sitt arbeidsstad |
| [arbeidslokasjoner](arbeidslokasjoner.md) |  |
| [arbeidssted](arbeidssted.md) | Tilhøyrsle til organisasjonsstrukturen |
| [art](art.md) | Type inntekt eller utgift |
| [artar](artar.md) |  |
| [attestant](attestant.md) | Personalressurs som har attestert lønsmeldinga etter fullmakt |
| [attestert](attestert.md) | Tidspunkt då lønn vart attestert |
| [belop](belop.md) | Beløp i øre |
| [beskrivelse](beskrivelse.md) | Beskriving av lønn til føring på lønnslipp |
| [bilde](bilde.md) | HTTP(S)-lenkje til eit bilete av personen |
| [bokstavkode](bokstavkode.md) | Bokstavkode for aktuell valuta |
| [bostedsadresse](bostedsadresse.md) | Folkeregistrert adresse til personen |
| [brukernavn](brukernavn.md) | Brukarnamn til den tilsette |
| [bruksnummer](bruksnummer.md) | Fortløpande nummerering av bruk under gårdsnummer |
| [diverse](diverse.md) |  |
| [elev](elev.md) | Referanse til Elev (Utdanning) |
| [epostadresse](epostadresse.md) | Namngitt elektronisk adresse for mottak av e-post |
| [etternavn](etternavn.md) | Etternamn til personen |
| [fastlonn](fastlonn.md) |  |
| [fasttillegg](fasttillegg.md) |  |
| [festenummer](festenummer.md) | Fortløpande nummerering av festar under gårdsnummer/bruksnummer |
| [fodselsdato](fodselsdato.md) | Dato for fødsel |
| [fodselsnummer](fodselsnummer.md) | Fødselsnummer eller ein av dei fiktive variantane |
| [forelder](forelder.md) | For å byggje hierarki av Arbeidsforholdstype |
| [foreldre](foreldre.md) | Den/dei som har foreldreansvar til personen |
| [foreldreansvar](foreldreansvar.md) | Personar denne personen har foreldreansvar for |
| [formaal](formaal.md) |  |
| [fornavn](fornavn.md) | Fornamn til personen |
| [forretningsadresse](forretningsadresse.md) | Besøksadresse til organisasjonseininga |
| [fortsettelse](fortsettelse.md) | Fortsetjande fråvær |
| [fortsetter](fortsetter.md) | Fråværet dette fråværet er fortsetjing av |
| [fravaer](fravaer.md) |  |
| [fravaersgrunn](fravaersgrunn.md) | Grunn til fråværet |
| [fravaersgrunnar](fravaersgrunnar.md) |  |
| [fravaerstypar](fravaerstypar.md) |  |
| [fravaerstype](fravaerstype.md) | Type fråvær |
| [fullmakt](fullmakt.md) | Alle fullmakter av denne typen |
| [fullmakter](fullmakter.md) |  |
| [fullmektig](fullmektig.md) | Personalressurs som har fått fullmakt til ei gjeven rolle |
| [funksjon](funksjon.md) | Det som vert produsert eller tenesta som vert levert |
| [funksjonar](funksjonar.md) |  |
| [fylke](fylke.md) |  |
| [gaardsnummer](gaardsnummer.md) | Nummerering av gårdseiging i matrikkelen, unik innanfor kommune |
| [godkjenner](godkjenner.md) | Personalressurs som har godkjent fråværsmeldinga |
| [godkjent](godkjent.md) | Tidspunkt då fråværet vart godkjent |
| [gyldighetsperiode](gyldighetsperiode.md) | Periode fullmakta er gyldig for |
| [hovedstilling](hovedstilling.md) | Angir kva arbeidsforhold som er hovudarbeidsforhold |
| [id](id.md) | URI-identifikator for ressursen |
| [identifikatorverdi](identifikatorverdi.md) | Ein konkret kombinasjon av teikn og/eller bokstavar som utgjer ein bestemt id... |
| [jobbtittel](jobbtittel.md) | Namn som beskriv jobben eller stillinga |
| [kategori](kategori.md) | Kategori lønnsart |
| [kildesystemId](kildesystemId.md) | Kjeldesystemets unike identifikator for lønn |
| [kjonn](kjonn.md) |  |
| [kode](kode.md) | Verdi som identifiserer omgrepet |
| [kommunar](kommunar.md) |  |
| [kommune](kommune.md) | Alle kommunar som inngår i fylket |
| [kommunenummer](kommunenummer.md) | Nummerering av kommunen i høve til SSB si offisielle liste |
| [kontaktinformasjon](kontaktinformasjon.md) | Kontaktinformasjon til arbeidslokasjonen |
| [kontaktperson](kontaktperson.md) | Personar kontaktpersonen er pårørande for |
| [kontaktpersonar](kontaktpersonar.md) |  |
| [konterer](konterer.md) | Personalressurs som har kontert lønsmeldinga etter fullmakt |
| [kontert](kontert.md) | Tidspunkt då lønn vart kontert |
| [kontostreng](kontostreng.md) | Kontering av lønn |
| [kontrakt](kontrakt.md) | Kontostrengens kontraktsegment |
| [kontrakter](kontrakter.md) |  |
| [kortnavn](kortnavn.md) | Forkorta namn som beskriv organisasjonselementet |
| [laerling](laerling.md) | Referanse til Laerling (Utdanning) |
| [land](land.md) | Land der adressa befinn seg |
| [landkodar](landkodar.md) |  |
| [leder](leder.md) | Ansvarleg leiar for organisasjonselementet |
| [lederFor](lederFor.md) | Organisasjonselement personalressursen er leiar for |
| [lokasjonskode](lokasjonskode.md) | Kode som identifiserer ein arbeidslokasjon |
| [lokasjonsnavn](lokasjonsnavn.md) | Namn som beskriv ein arbeidslokasjon |
| [lonnsprosent](lonnsprosent.md) | Prosent av årslønn den tilsette skal ha utbetalt |
| [lonsart](lonsart.md) | Lønnsart fråværstypen vert ført på |
| [lonsartar](lonsartar.md) |  |
| [lopenummer](lopenummer.md) |  |
| [maalform](maalform.md) | Målform personen føretrekkjer |
| [mellomnavn](mellomnavn.md) | Mellomnamn |
| [mobiltelefonnummer](mobiltelefonnummer.md) | Mobiltelefonnummer |
| [morsmaal](morsmaal.md) | Morsmål til personen |
| [navn](navn.md) | Namn på organisasjonselementet |
| [nettsted](nettsted.md) | Adresse til eit nettstad |
| [nummerkode](nummerkode.md) | Nummerkode for aktuell valuta |
| [objekt](objekt.md) |  |
| [opptjent](opptjent.md) | Periode der lønn vart opptent |
| [organisasjonselement](organisasjonselement.md) |  |
| [organisasjonsId](organisasjonsId.md) | Unikt internnummer for organisasjonselementet |
| [organisasjonsKode](organisasjonsKode.md) | Beskriven kode for organisasjonselementet |
| [organisasjonsnavn](organisasjonsnavn.md) | Namn på eining registrert i Einingsregisteret |
| [organisasjonsnummer](organisasjonsnummer.md) | Niisifra nummer som eintydleg identifiserer einingar i Einingsregisteret |
| [organisasjonstypar](organisasjonstypar.md) |  |
| [organisasjonstype](organisasjonstype.md) | Kva type organisasjonselement dette er |
| [otungdom](otungdom.md) | Referanse til OtUngdom (Utdanning) |
| [overfores](overfores.md) | Angir om fråvær av denne typen skal overførast til HR |
| [overordnet](overordnet.md) | Overordna ansvar |
| [parorende](parorende.md) | Pårørande kontaktperson til personen |
| [passiv](passiv.md) | Angir at koden er passiv og ikkje kan veljast |
| [periode](periode.md) | Periode lønn vert utbetalt |
| [person](person.md) | Person som er ein personalressurs |
| [personalansvar](personalansvar.md) | Arbeidsforhold der personalressursen har personalansvar |
| [personalleder](personalleder.md) | Personalleiar til arbeidsforholdet |
| [personalressurs](personalressurs.md) | Personalressurs til arbeidsforholdet |
| [personalressursar](personalressursar.md) |  |
| [personalressurskategori](personalressurskategori.md) | Kategori for personalressursen |
| [personalressurskategoriar](personalressurskategoriar.md) |  |
| [personar](personar.md) |  |
| [postadresse](postadresse.md) | Postadresse til arbeidslokasjonen |
| [postnummer](postnummer.md) | Postnummer |
| [poststed](poststed.md) | Poststad |
| [prosent](prosent.md) | Andel av lønnsprosent som vert beslaglagt |
| [prosjekt](prosjekt.md) |  |
| [prosjektart](prosjektart.md) | Deloppgåve eller delprosjekt |
| [prosjektartar](prosjektartar.md) |  |
| [ramme](ramme.md) | Budsjettramme som skal bere kostnadane |
| [rammer](rammer.md) |  |
| [rollar](rollar.md) |  |
| [rolle](rolle.md) | Kva type fullmakt |
| [rolleNavn](rolleNavn.md) | Namn på rolla; unik identifikator |
| [seksjonsnummer](seksjonsnummer.md) | Fortløpande nummerering av seksjonar under gårdsnummer/bruksnummer |
| [sip](sip.md) | SIP-protokoll for VoIP (IP-telefoni) |
| [skole](skole.md) | Referanse til Skole (Utdanning) |
| [skoleressurs](skoleressurs.md) | Referanse til Skoleressurs (Utdanning) |
| [slutt](slutt.md) | Til tidspunkt |
| [spraak](spraak.md) |  |
| [start](start.md) | Frå tidspunkt |
| [statsborgerskap](statsborgerskap.md) | Alle statsborgarskap personen har |
| [stedfortreder](stedfortreder.md) | Personalressurs som er stedfortredar for den fullmektige |
| [stillingskode](stillingskode.md) | Firesifra stillingskode frå KS, eventuelt utvida med to siffer |
| [stillingskoder](stillingskoder.md) |  |
| [stillingsnummer](stillingsnummer.md) | Løpenummer for stillinga |
| [stillingstittel](stillingstittel.md) | Arbeidstakarens stillingstittel i gjeldande stilling |
| [telefonnummer](telefonnummer.md) | Telefonnummer |
| [tilstedeprosent](tilstedeprosent.md) | Det personalressursen faktisk jobbar |
| [timerPerUke](timerPerUke.md) | Timer per veke i 100 % stilling |
| [type](type.md) | Beskriv kva slags type kontaktperson |
| [uketimetall](uketimetall.md) |  |
| [underordnet](underordnet.md) | Alle underansvar |
| [undervisningsforhold](undervisningsforhold.md) | Referanse til Undervisningsforhold (Utdanning) |
| [valuta](valuta.md) |  |
| [variabellonn](variabellonn.md) |  |
| [virksomhetar](virksomhetar.md) |  |
| [virksomhetsId](virksomhetsId.md) | Intern unik identifikator i økonomisystemet |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
| [Anbefalt](Anbefalt.md) | Anbefalt eigensskap |
| [Obligatorisk](Obligatorisk.md) | Obligatorisk eigensskap |
| [Valgfri](Valgfri.md) | Valfri eigensskap |
