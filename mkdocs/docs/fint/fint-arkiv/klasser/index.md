# FINT Arkiv

FINT-domenemodell for arkiv basert på Noark 5-standarden. Dekkjer sakshandtering, journalpostar, dokumenthandsaming, tilgangsstyring og spesialiserte saksmappe-typar.


URI: https://data.norge.no/linkml/fint-arkiv

Name: fint-arkiv



## Classes

| Class | Description |
| --- | --- |
| [AdministrativEnhet](AdministrativEnhet.md) | Administrativ eining med ansvar for saksbehandling |
| [Adresse](Adresse.md) | Fysisk adresse eller postadresse |
| [Aktoer](Aktoer.md) | Abstrakt base for person eller eining vi samhandlar med |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Enhet](Enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Virksomhet](Virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Person](Person.md) | Fysiske private personar |
| [ArkivContainer](ArkivContainer.md) | Rotcontainer for FINT Arkiv-instansar |
| [Arkivdel](Arkivdel.md) | Ein vilkårleg definert del av eit arkiv |
| [Arkivressurs](Arkivressurs.md) | Ansatt med rolle og rettar innanfor arkiv |
| [Autorisasjon](Autorisasjon.md) | Siling av kva ein innlogga brukar får lov til å gjere i løysinga |
| [Avskrivning](Avskrivning.md) | Avskriving av ein journalpost (markering som ferdigbehandla) |
| [Begrep](Begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fylke](Fylke.md) | Liste over Norges fylker |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kjonn](Kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kommune](Kommune.md) | Liste over Norges kommunar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Landkode](Landkode.md) | Landskode i ISO 3166-1 alpha-2 format |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Spraak](Spraak.md) | Verdiar for språk (2 bokstavar) |
| [Dokumentbeskrivelse](Dokumentbeskrivelse.md) | Skildring av eit dokument tilknytt ein journalpost |
| [Dokumentfil](Dokumentfil.md) | Sjølve dokumentfila med data og metadata |
| [Dokumentobjekt](Dokumentobjekt.md) | Referanse til éin og berre éin dokumentfil |
| [DokumentStatus](DokumentStatus.md) | Status til eit dokument |
| [DokumentType](DokumentType.md) | Type dokument |
| [Format](Format.md) | Dokumentets filformat |
| [Identifikator](Identifikator.md) | Unik identifikasjon til eit objekt |
| [JournalpostType](JournalpostType.md) | Namn på type journalpost |
| [JournalStatus](JournalStatus.md) | Status til journalposten |
| [Klasse](Klasse.md) | Ein klasse i eit klassifikasjonssystem |
| [Klassifikasjonssystem](Klassifikasjonssystem.md) | Overordna struktur for mappene i ein eller fleire arkivdelar |
| [Klassifikasjonstype](Klassifikasjonstype.md) | Type klassifikasjonssystem |
| [Kontaktinformasjon](Kontaktinformasjon.md) | Informasjon som kan brukast for å oppnå kontakt |
| [Kontaktperson](Kontaktperson.md) | Kontaktperson (pårørande) til ein person |
| [Korrespondansepart](Korrespondansepart.md) | Verksemd eller person som arkivskapar mottek eller sender arkivdokument til |
| [KorrespondansepartType](KorrespondansepartType.md) | Type korrespondansepart |
| [Mappe](Mappe.md) | Abstrakt basisklasse for alle mappetypar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Saksmappe](Saksmappe.md) | Abstrakt spesialisering av Mappe som svarar til ei "sak" i Noark |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DispensasjonAutomatiskFredaKulturminne](DispensasjonAutomatiskFredaKulturminne.md) | Sak om søknad om dispensasjon for tiltak på automatisk freda kulturminne |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Personalmappe](Personalmappe.md) | Saksmappe med opplysningar om ein arbeidstakars arbeidsforhold |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Sak](Sak.md) | Generisk saksmappe (konkret Sak i Noark) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SoeknadDrosjeloeyve](SoeknadDrosjeloeyve.md) | Sak om søknad om løyve til å køyre drosje |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TilskuddFartoy](TilskuddFartoy.md) | Sak om søknad om tilskudd til freda fartøy |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TilskuddFredaBygningPrivatEie](TilskuddFredaBygningPrivatEie.md) | Sak om søknad om tilskudd til freda bygningar i privat eige (FRIP) |
| [Matrikkelnummer](Matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |
| [Merknad](Merknad.md) | Merknad knytt til mappe, registrering eller dokumentbeskrivelse |
| [Merknadstype](Merknadstype.md) | Namn på type merknad |
| [Part](Part.md) | Part til Mappe, Registrering eller Dokumentbeskrivelse |
| [PartRolle](PartRolle.md) | Rolla til ein part |
| [Periode](Periode.md) | Tidsperiode med obligatorisk start og valfri slutt |
| [Personnavn](Personnavn.md) | Namn på ein person |
| [Registrering](Registrering.md) | Abstrakt basisklasse — arkivets primære byggeklossar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Journalpost](Journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |
| [Rolle](Rolle.md) | Rolla til ein arkivressurs |
| [Saksmappetype](Saksmappetype.md) | Type saksmappe — differensierer innhald og behandlingsrutine |
| [Saksstatus](Saksstatus.md) | Status til saksmappa |
| [Skjerming](Skjerming.md) | Skjerming av mappe, registrering eller dokument etter offentleglova |
| [Skjermingshjemmel](Skjermingshjemmel.md) | Tilvising til heimel i offentleglova, tryggingslova eller tryggingsinstruksen |
| [Tilgang](Tilgang.md) | Styring av kven som har tilgang til kva opplysningar |
| [Tilgangsgruppe](Tilgangsgruppe.md) | Tilgangsgruppe for intern skjerming av innhald |
| [Tilgangsrestriksjon](Tilgangsrestriksjon.md) | Angiving av at dokumenta ikkje er offentleg tilgjengelege |
| [TilknyttetRegistreringSom](TilknyttetRegistreringSom.md) | Kva rolle dokumentet har i høve registreringa (t |
| [Valuta](Valuta.md) | Valutakodar for offisielle valutaer |
| [Variantformat](Variantformat.md) | Angiving av kva variant eit dokument førekjem i |



## Slots

| Slot | Description |
| --- | --- |
| [administrativeEiningar](administrativeEiningar.md) |  |
| [administrativEnhet](administrativEnhet.md) | Administrativ eining som har ansvar for saksbehandlinga |
| [administrativenhet](administrativenhet.md) | Administrative einingar autorisasjonen er gyldig for |
| [adresse](adresse.md) | Adressen til korrespondanseparten |
| [adresselinje](adresselinje.md) | Adresseinformasjon |
| [antallVedlegg](antallVedlegg.md) | Antal fysiske vedlegg til eit fysisk hoveddokument |
| [arbeidssted](arbeidssted.md) | Referanse til Organisasjonselement som er arbeidstakarens arbeidsstad |
| [arkivdel](arkivdel.md) | Arkivdel mappa tilhøyrer |
| [arkivdelar](arkivdelar.md) |  |
| [arkivertAv](arkivertAv.md) | Person som arkiverte arkivenheten |
| [arkivertDato](arkivertDato.md) | Dato og klokkeslett alle dokument knytt til registreringa vart arkivert |
| [arkivressurs](arkivressurs.md) | Arkivressursar som har fått autorisasjonen |
| [arkivressursar](arkivressursar.md) |  |
| [autorisasjon](autorisasjon.md) | Autorisasjonar gjevne til arkivressursen |
| [autorisasjonar](autorisasjonar.md) |  |
| [avskrevetAv](avskrevetAv.md) | Person som avskriva journalposten |
| [avskrivning](avskrivning.md) | Avskriving av journalposten |
| [avskrivningsdato](avskrivningsdato.md) | Dato og klokkeslett for avskrivinga |
| [avskrivningsmate](avskrivningsmate.md) | Korleis journalposten er avskriven |
| [avsluttetAv](avsluttetAv.md) | Person som avslutta/lukka arkivenheten |
| [avsluttetDato](avsluttetDato.md) | Dato og klokkeslett når arkivenheten vart avslutta/lukka |
| [beskrivelse](beskrivelse.md) | Tekstleg skildring av arkivenheten |
| [bilde](bilde.md) | HTTP(S)-lenkje til eit bilete av personen |
| [bokstavkode](bokstavkode.md) | Bokstavkode for aktuell valuta |
| [bostedsadresse](bostedsadresse.md) | Folkeregistrert adresse til personen |
| [bruksnummer](bruksnummer.md) | Fortløpande nummerering av bruk under gårdsnummer |
| [bygningsnavn](bygningsnavn.md) | Bygningens namn |
| [data](data.md) | Dokumentfilens data, koda som Base64 |
| [dispensasjonAutomatiskFredaKulturminne](dispensasjonAutomatiskFredaKulturminne.md) |  |
| [dokumentbeskrivelsar](dokumentbeskrivelsar.md) |  |
| [dokumentbeskrivelse](dokumentbeskrivelse.md) | Dokumentbeskrivelsar til ei registrering |
| [dokumentetsDato](dokumentetsDato.md) | Dato påført sjølve dokumentet |
| [dokumentfiler](dokumentfiler.md) |  |
| [dokumentnummer](dokumentnummer.md) | Identifikasjon av dokumenta innanfor ei registrering |
| [dokumentobjekt](dokumentobjekt.md) | Dokumentobjekt tilhøyrande dokumentbeskrivelsa |
| [dokumentstatus](dokumentstatus.md) | Status til dokumentet |
| [dokumentstatuskodar](dokumentstatuskodar.md) |  |
| [dokumenttypar](dokumenttypar.md) |  |
| [dokumentType](dokumentType.md) | Namn på type dokument |
| [elev](elev.md) | Referanse til Elev (Utdanning) |
| [epostadresse](epostadresse.md) | Namngitt elektronisk adresse for mottak av e-post |
| [etternavn](etternavn.md) | Etternamn til personen |
| [fartoyNavn](fartoyNavn.md) | Fartøyets namn |
| [festenummer](festenummer.md) | Fortløpande nummerering av festar under gårdsnummer/bruksnummer |
| [filformat](filformat.md) | Dokumentets format |
| [filnavn](filnavn.md) | Dokumentfilens namn |
| [filstorrelse](filstorrelse.md) | Storleiken på fila i antal bytes |
| [fodselsdato](fodselsdato.md) | Dato for fødsel |
| [fodselsnummer](fodselsnummer.md) | Fødselsnummer eller ein av dei fiktive variantane |
| [foedselsnummer](foedselsnummer.md) | Fødselsnummer til korrespondanseparten |
| [foreldre](foreldre.md) | Den/dei som har foreldreansvar til personen |
| [foreldreansvar](foreldreansvar.md) | Personar denne personen har foreldreansvar for |
| [forfallsDato](forfallsDato.md) | Frist for å svare på eit inngåande dokument |
| [forfatter](forfatter.md) | Namn på person eller organisasjon som skapte dokumentet |
| [format](format.md) | Format på dokumentfil, som IANA Media Type |
| [formatar](formatar.md) |  |
| [formatDetaljer](formatDetaljer.md) | Nærare spesifikasjon av dokumentets format |
| [fornavn](fornavn.md) | Fornamn til personen |
| [forretningsadresse](forretningsadresse.md) | Besøksadresse til ein organisasjonseining i einingsregisteret |
| [fylke](fylke.md) | Fylket kommunen høyrer til |
| [gaardsnummer](gaardsnummer.md) | Nummerering av gårdseiging i matrikkelen, unik innanfor kommune |
| [gyldighetsperiode](gyldighetsperiode.md) | Periode der den administrative eininga er gyldig |
| [id](id.md) | URI-identifikator for ressursen |
| [identifikatorverdi](identifikatorverdi.md) | Ein konkret kombinasjon av teikn og/eller bokstavar som utgjer ein bestemt id... |
| [journalAr](journalAr.md) | Året journalposten vart oppretta |
| [journalDato](journalDato.md) | Datoen journalposten er oppretta/arkivert |
| [journalenhet](journalenhet.md) | Eining med arkivmessig ansvar for saksmappa |
| [journalpost](journalpost.md) | Journalpostar knytt til saksmappa |
| [journalpostar](journalpostar.md) |  |
| [journalPostnummer](journalPostnummer.md) | Rekkjefølgja journalpostane vart oppretta innanfor saksmappa |
| [journalposttypar](journalposttypar.md) |  |
| [journalposttype](journalposttype.md) | Namn på type journalpost |
| [journalSekvensnummer](journalSekvensnummer.md) | Rekkjefølgja journalposten vart oppretta under året |
| [journalstatus](journalstatus.md) | Status til journalposten |
| [journalstatuskodar](journalstatuskodar.md) |  |
| [kallesignal](kallesignal.md) | Fartøyets kallesignal |
| [kildesystemId](kildesystemId.md) | Kildesystemets identifikator for arkivressursen |
| [kjonn](kjonn.md) | Kjønn for personen |
| [klasse](klasse.md) | Klassifisering av mappe |
| [klasseId](klasseId.md) | Eintydig identifikasjon av klassen innanfor klassifikasjonssystemet |
| [klassifikasjonssystem](klassifikasjonssystem.md) |  |
| [klassifikasjonstypar](klassifikasjonstypar.md) |  |
| [klassifikasjonstype](klassifikasjonstype.md) | Type klassifikasjonssystem |
| [kode](kode.md) |  |
| [kommune](kommune.md) | Alle kommunar som inngår i fylket |
| [kommunenummer](kommunenummer.md) | Nummerering av kommunen i høve til SSB si offisielle liste |
| [kontaktinformasjon](kontaktinformasjon.md) | Kontaktinformasjon til korrespondanseparten |
| [kontaktperson](kontaktperson.md) | Kontaktperson hos ein organisasjon som er avsender eller mottakar |
| [korrespondansepart](korrespondansepart.md) | Mottakar eller sendar av arkivdokument |
| [korrespondansepartNavn](korrespondansepartNavn.md) | Namn på person eller organisasjon som er avsender eller mottakar |
| [korrespondanseparttypar](korrespondanseparttypar.md) |  |
| [korrespondanseparttype](korrespondanseparttype.md) | Type korrespondansepart |
| [kulturminneId](kulturminneId.md) | Kulturminnets ID i Askeladden |
| [laerling](laerling.md) | Referanse til Laerling (Utdanning) |
| [land](land.md) | Land der adressa befinn seg |
| [leder](leder.md) | Referanse til Personalressurs som er arbeidstakarens leiar |
| [maalform](maalform.md) | Målform personen føretrekkjer |
| [mappeId](mappeId.md) | Eintydig identifikasjon av mappa innanfor arkivet |
| [matrikkelnummer](matrikkelnummer.md) | Kulturminnets identifikator i Matrikkelen |
| [mellomnavn](mellomnavn.md) | Mellomnamn |
| [merknad](merknad.md) | Merknader knytt til mappe |
| [merknadRegistrertAv](merknadRegistrertAv.md) | Person som registrerte merknaden |
| [merknadsdato](merknadsdato.md) | Dato og klokkeslett merknaden vart registrert |
| [merknadstekst](merknadstekst.md) | Merknad frå saksbehandlar, leiar eller arkivpersonale |
| [merknadstypar](merknadstypar.md) |  |
| [merknadstype](merknadstype.md) | Type merknad |
| [mobiltelefonnummer](mobiltelefonnummer.md) | Mobiltelefonnummer |
| [morsmaal](morsmaal.md) | Morsmål til personen |
| [mottattDato](mottattDato.md) | Dato eit eksternt dokument vart motteke |
| [navn](navn.md) | Namn på administrativ eining |
| [nettsted](nettsted.md) | Adresse til eit nettstad |
| [noekkelord](noekkelord.md) | Nøkkelord som skildrar innhaldet |
| [nokkelord](nokkelord.md) | Nøkkelord som skildrar innhaldet |
| [nummerkode](nummerkode.md) | Nummerkode for aktuell valuta |
| [offentlighetsvurdertDato](offentlighetsvurdertDato.md) | Datoen offentlegheitsvurdering vart gjennomført |
| [offentligTittel](offentligTittel.md) | Offentleg tittel der skjerma ord er fjerna |
| [opprettetAv](opprettetAv.md) | Person som oppretta/registrerte arkivenheten |
| [opprettetDato](opprettetDato.md) | Dato og klokkeslett arkivenheten vart oppretta/registrert |
| [organisasjonselement](organisasjonselement.md) | Referanse til Organisasjonselement i Administrasjon-domenet |
| [organisasjonsnavn](organisasjonsnavn.md) | Organisasjonsnamn til føretaket som søkte om drosjeløyve |
| [organisasjonsnummer](organisasjonsnummer.md) | Organisasjonsnummer til føretaket som søkte om drosjeløyve |
| [otungdom](otungdom.md) | Referanse til OtUngdom (Utdanning) |
| [parorende](parorende.md) | Pårørande kontaktperson til personen |
| [part](part.md) | Partar til mappe |
| [partNavn](partNavn.md) | Namn på verksemd eller person som er part |
| [partRollar](partRollar.md) |  |
| [partRolle](partRolle.md) | Rolla til parten |
| [passiv](passiv.md) |  |
| [person](person.md) | Referanse til Person i Administrasjon-domenet |
| [personalmappe](personalmappe.md) |  |
| [personalressurs](personalressurs.md) | Referanse til Personalressurs i Administrasjon-domenet |
| [postadresse](postadresse.md) | Informasjon om postadresse til ein aktør |
| [postnummer](postnummer.md) | Postnummer |
| [poststed](poststed.md) | Poststad |
| [referanseArkivDel](referanseArkivDel.md) | Referanse til arkivdelen denne arkivenheten er tilknytt |
| [referanseArkivdel](referanseArkivdel.md) | Referanse til arkivdelen denne arkivenheten er tilknytt |
| [referanseDokumentfil](referanseDokumentfil.md) | Referanse til fila som inneheld det elektroniske dokumentet |
| [registreringsId](registreringsId.md) | Inngår i M004 journalpostID |
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
| [sendtDato](sendtDato.md) | Dato eit internt produsert dokument vart sendt/ekspedert |
| [sip](sip.md) | SIP-protokoll for VoIP (IP-telefoni) |
| [sjekksum](sjekksum.md) | Verdi som gir integritetssikring til dokumentets innhald |
| [sjekksumAlgoritme](sjekksumAlgoritme.md) | Algoritme nytta for å berekne sjekksummen |
| [skjerming](skjerming.md) | Skjerming av mappe |
| [skjermingsheimlar](skjermingsheimlar.md) |  |
| [skjermingshjemmel](skjermingshjemmel.md) | Skjermingsheimelen |
| [slutt](slutt.md) | Til tidspunkt |
| [soeknadDrosjeloeyve](soeknadDrosjeloeyve.md) |  |
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
| [tilknyttetAv](tilknyttetAv.md) | Person som knytte dokumentet til registreringa |
| [tilknyttetDato](tilknyttetDato.md) | Datoen eit dokument vart knytt til ei registrering |
| [tilknyttetRegistreringSom](tilknyttetRegistreringSom.md) | Rolle dokumentet har i høve registreringa |
| [tilknyttetRegistreringSomKodar](tilknyttetRegistreringSomKodar.md) |  |
| [tilskuddFartoy](tilskuddFartoy.md) |  |
| [tilskuddFredaBygningPrivatEie](tilskuddFredaBygningPrivatEie.md) |  |
| [tiltak](tiltak.md) | Skildrar kva tiltak som skal utførast på eigedommen |
| [tittel](tittel.md) | Tittel eller namn på arkivenheten |
| [type](type.md) | Beskriv kva slags type kontaktperson |
| [utlaantDato](utlaantDato.md) | Dato ein fysisk saksmappe eller journalpost vart utlånt |
| [variantFormat](variantFormat.md) | Kva variant dokumentet førekjem i |
| [variantformatar](variantformatar.md) |  |
| [versjonsnummer](versjonsnummer.md) | Identifikasjon av versjonar innanfor same dokument |
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
