# FINT Arkiv

FINT-domenemodell for arkiv basert på Noark 5-standarden. Dekkjer sakshandtering, journalpostar, dokumenthandsaming, tilgangsstyring og spesialiserte saksmappe-typar.


URI: https://data.norge.no/linkml/fint-arkiv

Name: fint-arkiv



## Classes

| Class | Description |
| --- | --- |
| [AdministrativEnhet](administrativenhet.md) | Administrativ eining med ansvar for saksbehandling |
| [Adresse](adresse.md) | Fysisk adresse eller postadresse |
| [Aktoer](aktoer.md) | Abstrakt base for person eller eining vi samhandlar med |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Person](person.md) | Fysiske private personar |
| [ArkivContainer](arkivcontainer.md) | Rotcontainer for FINT Arkiv-instansar |
| [Arkivdel](arkivdel.md) | Ein vilkårleg definert del av eit arkiv |
| [Arkivressurs](arkivressurs.md) | Ansatt med rolle og rettar innanfor arkiv |
| [Autorisasjon](autorisasjon.md) | Siling av kva ein innlogga brukar får lov til å gjere i løysinga |
| [Avskrivning](avskrivning.md) | Avskriving av ein journalpost (markering som ferdigbehandla) |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fylke](fylke.md) | Liste over Norges fylker |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kommune](kommune.md) | Liste over Norges kommunar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |
| [Dokumentbeskrivelse](dokumentbeskrivelse.md) | Skildring av eit dokument tilknytt ein journalpost |
| [Dokumentfil](dokumentfil.md) | Sjølve dokumentfila med data og metadata |
| [Dokumentobjekt](dokumentobjekt.md) | Referanse til éin og berre éin dokumentfil |
| [DokumentStatus](dokumentstatus.md) | Status til eit dokument |
| [DokumentType](dokumenttype.md) | Type dokument |
| [Format](format.md) | Dokumentets filformat |
| [Identifikator](identifikator.md) | Unik identifikasjon til eit objekt |
| [JournalpostType](journalposttype.md) | Namn på type journalpost |
| [JournalStatus](journalstatus.md) | Status til journalposten |
| [Klasse](klasse.md) | Ein klasse i eit klassifikasjonssystem |
| [Klassifikasjonssystem](klassifikasjonssystem.md) | Overordna struktur for mappene i ein eller fleire arkivdelar |
| [Klassifikasjonstype](klassifikasjonstype.md) | Type klassifikasjonssystem |
| [Kontaktinformasjon](kontaktinformasjon.md) | Informasjon som kan brukast for å oppnå kontakt |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |
| [Korrespondansepart](korrespondansepart.md) | Verksemd eller person som arkivskapar mottek eller sender arkivdokument til |
| [KorrespondansepartType](korrespondanseparttype.md) | Type korrespondansepart |
| [Mappe](mappe.md) | Abstrakt basisklasse for alle mappetypar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Saksmappe](saksmappe.md) | Abstrakt spesialisering av Mappe som svarar til ei "sak" i Noark |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DispensasjonAutomatiskFredaKulturminne](dispensasjonautomatiskfredakulturminne.md) | Sak om søknad om dispensasjon for tiltak på automatisk freda kulturminne |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Personalmappe](personalmappe.md) | Saksmappe med opplysningar om ein arbeidstakars arbeidsforhold |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Sak](sak.md) | Generisk saksmappe (konkret Sak i Noark) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SoeknadDrosjeloeyve](soeknaddrosjeloeyve.md) | Sak om søknad om løyve til å køyre drosje |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TilskuddFartoy](tilskuddfartoy.md) | Sak om søknad om tilskudd til freda fartøy |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TilskuddFredaBygningPrivatEie](tilskuddfredabygningprivateie.md) | Sak om søknad om tilskudd til freda bygningar i privat eige (FRIP) |
| [Matrikkelnummer](matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |
| [Merknad](merknad.md) | Merknad knytt til mappe, registrering eller dokumentbeskrivelse |
| [Merknadstype](merknadstype.md) | Namn på type merknad |
| [Part](part.md) | Part til Mappe, Registrering eller Dokumentbeskrivelse |
| [PartRolle](partrolle.md) | Rolla til ein part |
| [Periode](periode.md) | Tidsperiode med obligatorisk start og valfri slutt |
| [Personnavn](personnavn.md) | Namn på ein person |
| [Registrering](registrering.md) | Abstrakt basisklasse — arkivets primære byggeklossar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Journalpost](journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |
| [Rolle](rolle.md) | Rolla til ein arkivressurs |
| [Saksmappetype](saksmappetype.md) | Type saksmappe — differensierer innhald og behandlingsrutine |
| [Saksstatus](saksstatus.md) | Status til saksmappa |
| [Skjerming](skjerming.md) | Skjerming av mappe, registrering eller dokument etter offentleglova |
| [Skjermingshjemmel](skjermingshjemmel.md) | Tilvising til heimel i offentleglova, tryggingslova eller tryggingsinstruksen |
| [Tilgang](tilgang.md) | Styring av kven som har tilgang til kva opplysningar |
| [Tilgangsgruppe](tilgangsgruppe.md) | Tilgangsgruppe for intern skjerming av innhald |
| [Tilgangsrestriksjon](tilgangsrestriksjon.md) | Angiving av at dokumenta ikkje er offentleg tilgjengelege |
| [TilknyttetRegistreringSom](tilknyttetregistreringsom.md) | Kva rolle dokumentet har i høve registreringa (t |
| [Valuta](valuta.md) | Valutakodar for offisielle valutaer |
| [Variantformat](variantformat.md) | Angiving av kva variant eit dokument førekjem i |



## Slots

| Slot | Description |
| --- | --- |
| [administrativeEiningar](administrativeeiningar.md) |  |
| [administrativEnhet](administrativenhet.md) | Administrativ eining som har ansvar for saksbehandlinga |
| [administrativenhet](administrativenhet.md) | Administrative einingar autorisasjonen er gyldig for |
| [adresse](adresse.md) | Adressen til korrespondanseparten |
| [adresselinje](adresselinje.md) | Adresseinformasjon |
| [antallVedlegg](antallvedlegg.md) | Antal fysiske vedlegg til eit fysisk hoveddokument |
| [arbeidssted](arbeidssted.md) | Referanse til Organisasjonselement som er arbeidstakarens arbeidsstad |
| [arkivdel](arkivdel.md) | Arkivdel mappa tilhøyrer |
| [arkivdelar](arkivdelar.md) |  |
| [arkivertAv](arkivertav.md) | Person som arkiverte arkivenheten |
| [arkivertDato](arkivertdato.md) | Dato og klokkeslett alle dokument knytt til registreringa vart arkivert |
| [arkivressurs](arkivressurs.md) | Arkivressursar som har fått autorisasjonen |
| [arkivressursar](arkivressursar.md) |  |
| [autorisasjon](autorisasjon.md) | Autorisasjonar gjevne til arkivressursen |
| [autorisasjonar](autorisasjonar.md) |  |
| [avskrevetAv](avskrevetav.md) | Person som avskriva journalposten |
| [avskrivning](avskrivning.md) | Avskriving av journalposten |
| [avskrivningsdato](avskrivningsdato.md) | Dato og klokkeslett for avskrivinga |
| [avskrivningsmate](avskrivningsmate.md) | Korleis journalposten er avskriven |
| [avsluttetAv](avsluttetav.md) | Person som avslutta/lukka arkivenheten |
| [avsluttetDato](avsluttetdato.md) | Dato og klokkeslett når arkivenheten vart avslutta/lukka |
| [beskrivelse](beskrivelse.md) | Tekstleg skildring av arkivenheten |
| [bilde](bilde.md) | HTTP(S)-lenkje til eit bilete av personen |
| [bokstavkode](bokstavkode.md) | Bokstavkode for aktuell valuta |
| [bostedsadresse](bostedsadresse.md) | Folkeregistrert adresse til personen |
| [bruksnummer](bruksnummer.md) | Fortløpande nummerering av bruk under gårdsnummer |
| [bygningsnavn](bygningsnavn.md) | Bygningens namn |
| [data](data.md) | Dokumentfilens data, koda som Base64 |
| [dispensasjonAutomatiskFredaKulturminne](dispensasjonautomatiskfredakulturminne.md) |  |
| [dokumentbeskrivelsar](dokumentbeskrivelsar.md) |  |
| [dokumentbeskrivelse](dokumentbeskrivelse.md) | Dokumentbeskrivelsar til ei registrering |
| [dokumentetsDato](dokumentetsdato.md) | Dato påført sjølve dokumentet |
| [dokumentfiler](dokumentfiler.md) |  |
| [dokumentnummer](dokumentnummer.md) | Identifikasjon av dokumenta innanfor ei registrering |
| [dokumentobjekt](dokumentobjekt.md) | Dokumentobjekt tilhøyrande dokumentbeskrivelsa |
| [dokumentstatus](dokumentstatus.md) | Status til dokumentet |
| [dokumentstatuskodar](dokumentstatuskodar.md) |  |
| [dokumenttypar](dokumenttypar.md) |  |
| [dokumentType](dokumenttype.md) | Namn på type dokument |
| [elev](elev.md) | Referanse til Elev (Utdanning) |
| [epostadresse](epostadresse.md) | Namngitt elektronisk adresse for mottak av e-post |
| [etternavn](etternavn.md) | Etternamn til personen |
| [fartoyNavn](fartoynavn.md) | Fartøyets namn |
| [festenummer](festenummer.md) | Fortløpande nummerering av festar under gårdsnummer/bruksnummer |
| [filformat](filformat.md) | Dokumentets format |
| [filnavn](filnavn.md) | Dokumentfilens namn |
| [filstorrelse](filstorrelse.md) | Storleiken på fila i antal bytes |
| [fodselsdato](fodselsdato.md) | Dato for fødsel |
| [fodselsnummer](fodselsnummer.md) | Fødselsnummer eller ein av dei fiktive variantane |
| [foedselsnummer](foedselsnummer.md) | Fødselsnummer til korrespondanseparten |
| [foreldre](foreldre.md) | Den/dei som har foreldreansvar til personen |
| [foreldreansvar](foreldreansvar.md) | Personar denne personen har foreldreansvar for |
| [forfallsDato](forfallsdato.md) | Frist for å svare på eit inngåande dokument |
| [forfatter](forfatter.md) | Namn på person eller organisasjon som skapte dokumentet |
| [format](format.md) | Format på dokumentfil, som IANA Media Type |
| [formatar](formatar.md) |  |
| [formatDetaljer](formatdetaljer.md) | Nærare spesifikasjon av dokumentets format |
| [fornavn](fornavn.md) | Fornamn til personen |
| [forretningsadresse](forretningsadresse.md) | Besøksadresse til ein organisasjonseining i einingsregisteret |
| [fylke](fylke.md) | Fylket kommunen høyrer til |
| [gaardsnummer](gaardsnummer.md) | Nummerering av gårdseiging i matrikkelen, unik innanfor kommune |
| [gyldighetsperiode](gyldighetsperiode.md) | Periode der den administrative eininga er gyldig |
| [id](id.md) | URI-identifikator for ressursen |
| [identifikatorverdi](identifikatorverdi.md) | Ein konkret kombinasjon av teikn og/eller bokstavar som utgjer ein bestemt id... |
| [journalAr](journalar.md) | Året journalposten vart oppretta |
| [journalDato](journaldato.md) | Datoen journalposten er oppretta/arkivert |
| [journalenhet](journalenhet.md) | Eining med arkivmessig ansvar for saksmappa |
| [journalpost](journalpost.md) | Journalpostar knytt til saksmappa |
| [journalpostar](journalpostar.md) |  |
| [journalPostnummer](journalpostnummer.md) | Rekkjefølgja journalpostane vart oppretta innanfor saksmappa |
| [journalposttypar](journalposttypar.md) |  |
| [journalposttype](journalposttype.md) | Namn på type journalpost |
| [journalSekvensnummer](journalsekvensnummer.md) | Rekkjefølgja journalposten vart oppretta under året |
| [journalstatus](journalstatus.md) | Status til journalposten |
| [journalstatuskodar](journalstatuskodar.md) |  |
| [kallesignal](kallesignal.md) | Fartøyets kallesignal |
| [kildesystemId](kildesystemid.md) | Kildesystemets identifikator for arkivressursen |
| [kjonn](kjonn.md) | Kjønn for personen |
| [klasse](klasse.md) | Klassifisering av mappe |
| [klasseId](klasseid.md) | Eintydig identifikasjon av klassen innanfor klassifikasjonssystemet |
| [klassifikasjonssystem](klassifikasjonssystem.md) |  |
| [klassifikasjonstypar](klassifikasjonstypar.md) |  |
| [klassifikasjonstype](klassifikasjonstype.md) | Type klassifikasjonssystem |
| [kode](kode.md) |  |
| [kommune](kommune.md) | Alle kommunar som inngår i fylket |
| [kommunenummer](kommunenummer.md) | Nummerering av kommunen i høve til SSB si offisielle liste |
| [kontaktinformasjon](kontaktinformasjon.md) | Kontaktinformasjon til korrespondanseparten |
| [kontaktperson](kontaktperson.md) | Kontaktperson hos ein organisasjon som er avsender eller mottakar |
| [korrespondansepart](korrespondansepart.md) | Mottakar eller sendar av arkivdokument |
| [korrespondansepartNavn](korrespondansepartnavn.md) | Namn på person eller organisasjon som er avsender eller mottakar |
| [korrespondanseparttypar](korrespondanseparttypar.md) |  |
| [korrespondanseparttype](korrespondanseparttype.md) | Type korrespondansepart |
| [kulturminneId](kulturminneid.md) | Kulturminnets ID i Askeladden |
| [laerling](laerling.md) | Referanse til Laerling (Utdanning) |
| [land](land.md) | Land der adressa befinn seg |
| [leder](leder.md) | Referanse til Personalressurs som er arbeidstakarens leiar |
| [maalform](maalform.md) | Målform personen føretrekkjer |
| [mappeId](mappeid.md) | Eintydig identifikasjon av mappa innanfor arkivet |
| [matrikkelnummer](matrikkelnummer.md) | Kulturminnets identifikator i Matrikkelen |
| [mellomnavn](mellomnavn.md) | Mellomnamn |
| [merknad](merknad.md) | Merknader knytt til mappe |
| [merknadRegistrertAv](merknadregistrertav.md) | Person som registrerte merknaden |
| [merknadsdato](merknadsdato.md) | Dato og klokkeslett merknaden vart registrert |
| [merknadstekst](merknadstekst.md) | Merknad frå saksbehandlar, leiar eller arkivpersonale |
| [merknadstypar](merknadstypar.md) |  |
| [merknadstype](merknadstype.md) | Type merknad |
| [mobiltelefonnummer](mobiltelefonnummer.md) | Mobiltelefonnummer |
| [morsmaal](morsmaal.md) | Morsmål til personen |
| [mottattDato](mottattdato.md) | Dato eit eksternt dokument vart motteke |
| [navn](navn.md) | Namn på administrativ eining |
| [nettsted](nettsted.md) | Adresse til eit nettstad |
| [noekkelord](noekkelord.md) | Nøkkelord som skildrar innhaldet |
| [nokkelord](nokkelord.md) | Nøkkelord som skildrar innhaldet |
| [nummerkode](nummerkode.md) | Nummerkode for aktuell valuta |
| [offentlighetsvurdertDato](offentlighetsvurdertdato.md) | Datoen offentlegheitsvurdering vart gjennomført |
| [offentligTittel](offentligtittel.md) | Offentleg tittel der skjerma ord er fjerna |
| [opprettetAv](opprettetav.md) | Person som oppretta/registrerte arkivenheten |
| [opprettetDato](opprettetdato.md) | Dato og klokkeslett arkivenheten vart oppretta/registrert |
| [organisasjonselement](organisasjonselement.md) | Referanse til Organisasjonselement i Administrasjon-domenet |
| [organisasjonsnavn](organisasjonsnavn.md) | Organisasjonsnamn til føretaket som søkte om drosjeløyve |
| [organisasjonsnummer](organisasjonsnummer.md) | Organisasjonsnummer til føretaket som søkte om drosjeløyve |
| [otungdom](otungdom.md) | Referanse til OtUngdom (Utdanning) |
| [parorende](parorende.md) | Pårørande kontaktperson til personen |
| [part](part.md) | Partar til mappe |
| [partNavn](partnavn.md) | Namn på verksemd eller person som er part |
| [partRollar](partrollar.md) |  |
| [partRolle](partrolle.md) | Rolla til parten |
| [passiv](passiv.md) |  |
| [person](person.md) | Referanse til Person i Administrasjon-domenet |
| [personalmappe](personalmappe.md) |  |
| [personalressurs](personalressurs.md) | Referanse til Personalressurs i Administrasjon-domenet |
| [postadresse](postadresse.md) | Informasjon om postadresse til ein aktør |
| [postnummer](postnummer.md) | Postnummer |
| [poststed](poststed.md) | Poststad |
| [referanseArkivDel](referansearkivdel.md) | Referanse til arkivdelen denne arkivenheten er tilknytt |
| [referanseArkivdel](referansearkivdel.md) | Referanse til arkivdelen denne arkivenheten er tilknytt |
| [referanseDokumentfil](referansedokumentfil.md) | Referanse til fila som inneheld det elektroniske dokumentet |
| [registreringsId](registreringsid.md) | Inngår i M004 journalpostID |
| [rekkefølge](rekkefølge.md) | Rekkjefølgje for klassifiseringar |
| [rollar](rollar.md) |  |
| [rolle](rolle.md) | Rolle tilknytt tilgangen |
| [sakar](sakar.md) |  |
| [saksaar](saksaar.md) | Inngår i M003 mappeID — viser året saksmappa vart oppretta |
| [saksansvarlig](saksansvarlig.md) | Person som er saksansvarleg |
| [saksbehandler](saksbehandler.md) | Person som er saksbehandlar |
| [saksdato](saksdato.md) | Datoen saka er oppretta |
| [saksmappetypar](saksmappetypar.md) |  |
| [saksmappetype](saksmappetype.md) | Type saksmappe |
| [sakssekvensnummer](sakssekvensnummer.md) | Inngår i M003 mappeID — viser rekkjefølgja saksmappene vart oppretta |
| [saksstatus](saksstatus.md) | Status til saksmappa |
| [sakstatuskodar](sakstatuskodar.md) |  |
| [seksjonsnummer](seksjonsnummer.md) | Fortløpande nummerering av seksjonar under gårdsnummer/bruksnummer |
| [sendtDato](sendtdato.md) | Dato eit internt produsert dokument vart sendt/ekspedert |
| [sip](sip.md) | SIP-protokoll for VoIP (IP-telefoni) |
| [sjekksum](sjekksum.md) | Verdi som gir integritetssikring til dokumentets innhald |
| [sjekksumAlgoritme](sjekksumalgoritme.md) | Algoritme nytta for å berekne sjekksummen |
| [skjerming](skjerming.md) | Skjerming av mappe |
| [skjermingsheimlar](skjermingsheimlar.md) |  |
| [skjermingshjemmel](skjermingshjemmel.md) | Skjermingsheimelen |
| [slutt](slutt.md) | Til tidspunkt |
| [soeknadDrosjeloeyve](soeknaddrosjeloeyve.md) |  |
| [soeknadsnummer](soeknadsnummer.md) | Søknadsnummer frå Digisak |
| [start](start.md) | Frå tidspunkt |
| [statsborgerskap](statsborgerskap.md) | Alle statsborgarskap personen har |
| [telefonnummer](telefonnummer.md) | Telefonnummer |
| [tilgang](tilgang.md) | Tilgangar gjevne til arkivressursen |
| [tilgangar](tilgangar.md) |  |
| [tilgangsgruppe](tilgangsgruppe.md) | Tilgangsgruppe som har tilgang til saksmappa |
| [tilgangsgrupper](tilgangsgrupper.md) |  |
| [tilgangsrestriksjon](tilgangsrestriksjon.md) | Tilgangsrestriksjonar autorisasjonen er gjeven for |
| [tilgangsrestriksjonar](tilgangsrestriksjonar.md) |  |
| [tilknyttetAv](tilknyttetav.md) | Person som knytte dokumentet til registreringa |
| [tilknyttetDato](tilknyttetdato.md) | Datoen eit dokument vart knytt til ei registrering |
| [tilknyttetRegistreringSom](tilknyttetregistreringsom.md) | Rolle dokumentet har i høve registreringa |
| [tilknyttetRegistreringSomKodar](tilknyttetregistreringsomkodar.md) |  |
| [tilskuddFartoy](tilskuddfartoy.md) |  |
| [tilskuddFredaBygningPrivatEie](tilskuddfredabygningprivateie.md) |  |
| [tiltak](tiltak.md) | Skildrar kva tiltak som skal utførast på eigedommen |
| [tittel](tittel.md) | Tittel eller namn på arkivenheten |
| [type](type.md) | Beskriv kva slags type kontaktperson |
| [utlaantDato](utlaantdato.md) | Dato ein fysisk saksmappe eller journalpost vart utlånt |
| [variantFormat](variantformat.md) | Kva variant dokumentet førekjem i |
| [variantformatar](variantformatar.md) |  |
| [versjonsnummer](versjonsnummer.md) | Identifikasjon av versjonar innanfor same dokument |
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
