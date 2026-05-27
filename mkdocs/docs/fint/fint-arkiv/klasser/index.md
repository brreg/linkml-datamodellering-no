# FINT Arkiv

FINT-domenemodell for arkiv basert på Noark 5-standarden. Dekkjer sakshandtering, journalpostar, dokumenthandsaming, tilgangsstyring og spesialiserte saksmappe-typar.


URI: https://data.norge.no/fint/fint-arkiv

Name: fint-arkiv



## Classes







### Obligatorisk

| Class | Description |
| --- | --- |
| [AdministrativEnhet](administrativenhet.md) | Administrativ eining med ansvar for saksbehandling |
| [Arkivdel](arkivdel.md) | Ein vilkårleg definert del av eit arkiv |
| [Arkivressurs](arkivressurs.md) | Ansatt med rolle og rettar innanfor arkiv |
| [Autorisasjon](autorisasjon.md) | Siling av kva ein innlogga brukar får lov til å gjere i løysinga |
| [Avskrivning](avskrivning.md) | Avskriving av ein journalpost (markering som ferdigbehandla) |
| [DispensasjonAutomatiskFredaKulturminne](dispensasjonautomatiskfredakulturminne.md) | Sak om søknad om dispensasjon for tiltak på automatisk freda kulturminne |
| [Dokumentbeskrivelse](dokumentbeskrivelse.md) | Skildring av eit dokument tilknytt ein journalpost |
| [Dokumentfil](dokumentfil.md) | Sjølve dokumentfila med data og metadata |
| [Dokumentobjekt](dokumentobjekt.md) | Referanse til éin og berre éin dokumentfil |
| [DokumentStatus](dokumentstatus.md) | Status til eit dokument |
| [DokumentType](dokumenttype.md) | Type dokument |
| [Format](format.md) | Dokumentets filformat |
| [Journalpost](journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |
| [JournalpostType](journalposttype.md) | Namn på type journalpost |
| [JournalStatus](journalstatus.md) | Status til journalposten |
| [Klasse](klasse.md) | Ein klasse i eit klassifikasjonssystem |
| [Klassifikasjonssystem](klassifikasjonssystem.md) | Overordna struktur for mappene i ein eller fleire arkivdelar |
| [Klassifikasjonstype](klassifikasjonstype.md) | Type klassifikasjonssystem |
| [Korrespondansepart](korrespondansepart.md) | Verksemd eller person som arkivskapar mottek eller sender arkivdokument til |
| [KorrespondansepartType](korrespondanseparttype.md) | Type korrespondansepart |
| [Mappe](mappe.md) | Abstrakt basisklasse for alle mappetypar |
| [Merknad](merknad.md) | Merknad knytt til mappe, registrering eller dokumentbeskrivelse |
| [Merknadstype](merknadstype.md) | Namn på type merknad |
| [Part](part.md) | Part til Mappe, Registrering eller Dokumentbeskrivelse |
| [PartRolle](partrolle.md) | Rolla til ein part |
| [Personalmappe](personalmappe.md) | Saksmappe med opplysningar om ein arbeidstakars arbeidsforhold |
| [Registrering](registrering.md) | Abstrakt basisklasse — arkivets primære byggeklossar |
| [Rolle](rolle.md) | Rolla til ein arkivressurs |
| [Saksmappe](saksmappe.md) | Abstrakt spesialisering av Mappe som svarar til ei "sak" i Noark |
| [Saksmappetype](saksmappetype.md) | Type saksmappe — differensierer innhald og behandlingsrutine |
| [Saksstatus](saksstatus.md) | Status til saksmappa |
| [Skjerming](skjerming.md) | Skjerming av mappe, registrering eller dokument etter offentleglova |
| [Skjermingshjemmel](skjermingshjemmel.md) | Tilvising til heimel i offentleglova, tryggingslova eller tryggingsinstruksen |
| [SoeknadDrosjeloeyve](soeknaddrosjeloeyve.md) | Sak om søknad om løyve til å køyre drosje |
| [Tilgang](tilgang.md) | Styring av kven som har tilgang til kva opplysningar |
| [Tilgangsgruppe](tilgangsgruppe.md) | Tilgangsgruppe for intern skjerming av innhald |
| [Tilgangsrestriksjon](tilgangsrestriksjon.md) | Angiving av at dokumenta ikkje er offentleg tilgjengelege |
| [TilknyttetRegistreringSom](tilknyttetregistreringsom.md) | Kva rolle dokumentet har i høve registreringa (t |
| [TilskuddFartoy](tilskuddfartoy.md) | Sak om søknad om tilskudd til freda fartøy |
| [TilskuddFredaBygningPrivatEie](tilskuddfredabygningprivateie.md) | Sak om søknad om tilskudd til freda bygningar i privat eige (FRIP) |
| [Variantformat](variantformat.md) | Angiving av kva variant eit dokument førekjem i |








### Andre

| Class | Description |
| --- | --- |
| [Sak](sak.md) | Generisk saksmappe (konkret Sak i Noark) |





## Slots

| Slot | Description |
| --- | --- |
| [administrativEnhet](administrativenhet.md) | Administrativ eining som har ansvar for saksbehandlinga |
| [administrativenhet](administrativenhet.md) | Administrative einingar autorisasjonen er gyldig for |
| [antallVedlegg](antallvedlegg.md) | Antal fysiske vedlegg til eit fysisk hoveddokument |
| [arbeidssted](arbeidssted.md) | Referanse til Organisasjonselement som er arbeidstakarens arbeidsstad |
| [arkivdel](arkivdel.md) | Arkivdel arkivenheten tilhøyrer |
| [arkivertAv](arkivertav.md) | Person som arkiverte arkivenheten |
| [arkivertDato](arkivertdato.md) | Dato og klokkeslett alle dokument knytt til registreringa vart arkivert |
| [arkivressurs](arkivressurs.md) | Arkivressursar |
| [autorisasjon](autorisasjon.md) | Autorisasjonar gjevne til arkivressursen |
| [avskrevetAv](avskrevetav.md) | Person som avskriva journalposten |
| [avskrivning](avskrivning.md) | Avskriving av journalposten |
| [avskrivningsdato](avskrivningsdato.md) | Dato og klokkeslett for avskrivinga |
| [avskrivningsmate](avskrivningsmate.md) | Korleis journalposten er avskriven |
| [avsluttetAv](avsluttetav.md) | Person som avslutta/lukka arkivenheten |
| [avsluttetAvNavn](avsluttetavnavn.md) | Namn på person som avslutta/lukka arkivenheten |
| [avsluttetDato](avsluttetdato.md) | Dato og klokkeslett når arkivenheten vart avslutta/lukka |
| [bygningsnavn](bygningsnavn.md) | Bygningens namn |
| [data](data.md) | Dokumentfilens data, koda som Base64 |
| [dokumentbeskrivelse](dokumentbeskrivelse.md) | Dokumentbeskrivelsar til ei registrering |
| [dokumentetsDato](dokumentetsdato.md) | Dato påført sjølve dokumentet |
| [dokumentnummer](dokumentnummer.md) | Identifikasjon av dokumenta innanfor ei registrering |
| [dokumentobjekt](dokumentobjekt.md) | Dokumentobjekt tilhøyrande dokumentbeskrivelsa |
| [dokumentstatus](dokumentstatus.md) | Status til dokumentet |
| [dokumentType](dokumenttype.md) | Namn på type dokument |
| [fartoyNavn](fartoynavn.md) | Fartøyets namn |
| [filformat](filformat.md) | Dokumentets format |
| [filnavn](filnavn.md) | Dokumentfilens namn |
| [filstorrelse](filstorrelse.md) | Storleiken på fila i antal bytes |
| [foedselsnummer](foedselsnummer.md) | Fødselsnummer |
| [forfallsDato](forfallsdato.md) | Frist for å svare på eit inngåande dokument |
| [forfatter](forfatter.md) | Namn på person eller organisasjon som skapte dokumentet |
| [format](format.md) | Format på dokumentfil, som IANA Media Type |
| [formatDetaljer](formatdetaljer.md) | Nærare spesifikasjon av dokumentets format |
| [journalAr](journalar.md) | Året journalposten vart oppretta |
| [journalDato](journaldato.md) | Datoen journalposten er oppretta/arkivert |
| [journalenhet](journalenhet.md) | Eining med arkivmessig ansvar |
| [journalpost](journalpost.md) | Journalpostar knytt til saksmappa |
| [journalPostnummer](journalpostnummer.md) | Rekkjefølgja journalpostane vart oppretta innanfor saksmappa |
| [journalposttype](journalposttype.md) | Namn på type journalpost |
| [journalSekvensnummer](journalsekvensnummer.md) | Rekkjefølgja journalposten vart oppretta under året |
| [journalstatus](journalstatus.md) | Status til journalposten |
| [kallesignal](kallesignal.md) | Fartøyets kallesignal |
| [kildesystemId](kildesystemid.md) | Kildesystemets identifikator for arkivressursen |
| [klasse](klasse.md) | Klassifisering av arkivenhet |
| [klasseId](klasseid.md) | Eintydig identifikasjon av klassen innanfor klassifikasjonssystemet |
| [klassifikasjonstype](klassifikasjonstype.md) | Type klassifikasjonssystem |
| [kontaktperson_str](kontaktperson_str.md) | Kontaktperson hos ein organisasjon som er avsender, mottakar eller sakspart |
| [korrespondansepart](korrespondansepart.md) | Mottakar eller sendar av arkivdokument |
| [korrespondansepartNavn](korrespondansepartnavn.md) | Namn på person eller organisasjon som er avsender eller mottakar |
| [korrespondanseparttype](korrespondanseparttype.md) | Type korrespondansepart |
| [kulturminneId](kulturminneid.md) | Kulturminnets ID i Askeladden |
| [leder](leder.md) | Referanse til Personalressurs som er arbeidstakarens leiar |
| [mappeId](mappeid.md) | Eintydig identifikasjon av mappa innanfor arkivet |
| [matrikkelnummer](matrikkelnummer.md) | Kulturminnets/bygningens identifikator i Matrikkelen |
| [merknad](merknad.md) | Merknader knytt til arkivenhet |
| [merknadRegistrertAv](merknadregistrertav.md) | Person som registrerte merknaden |
| [merknadsdato](merknadsdato.md) | Dato og klokkeslett merknaden vart registrert |
| [merknadstekst](merknadstekst.md) | Merknad frå saksbehandlar, leiar eller arkivpersonale |
| [merknadstype](merknadstype.md) | Type merknad |
| [mottattDato](mottattdato.md) | Dato eit eksternt dokument vart motteke |
| [noekkelord](noekkelord.md) | Nøkkelord som skildrar innhaldet (Mappe) |
| [nokkelord](nokkelord.md) | Nøkkelord som skildrar innhaldet (Registrering) |
| [offentlighetsvurdertDato](offentlighetsvurdertdato.md) | Datoen offentlegheitsvurdering vart gjennomført |
| [offentligTittel](offentligtittel.md) | Offentleg tittel der skjerma ord er fjerna |
| [opprettetAv](opprettetav.md) | Person som oppretta/registrerte arkivenheten |
| [opprettetAvNavn](opprettetavnavn.md) | Namn på person som oppretta/registrerte arkivenheten |
| [opprettetDato](opprettetdato.md) | Dato og klokkeslett arkivenheten vart oppretta/registrert |
| [organisasjonselement](organisasjonselement.md) | Referanse til Organisasjonselement i Administrasjon-domenet |
| [orgnummer](orgnummer.md) | Organisasjonsnummer |
| [part](part.md) | Partar til arkivenhet |
| [partNavn](partnavn.md) | Namn på verksemd eller person som er part |
| [partRolle](partrolle.md) | Rolla til parten |
| [personalressurs](personalressurs.md) | Referanse til Personalressurs i Administrasjon-domenet |
| [personnavn](personnavn.md) | Namn på person (Personnavn-objekt) |
| [referanseArkivDel](referansearkivdel.md) | Referanse til arkivdelen denne arkivenheten er tilknytt |
| [referanseArkivdel](referansearkivdel.md) | Referanse til arkivdelen denne arkivenheten er tilknytt |
| [referanseDokumentfil](referansedokumentfil.md) | Referanse til fila som inneheld det elektroniske dokumentet |
| [registreringsId](registreringsid.md) | Inngår i M004 journalpostID |
| [rekkefoelge](rekkefoelge.md) | Rekkjefølgje for klassifiseringar |
| [rolle](rolle.md) | Rolle tilknytt tilgangen |
| [saksaar](saksaar.md) | Inngår i M003 mappeID — viser året saksmappa vart oppretta |
| [saksansvarlig](saksansvarlig.md) | Person som er saksansvarleg |
| [saksbehandler](saksbehandler.md) | Person som er saksbehandlar |
| [saksdato](saksdato.md) | Datoen saka er oppretta |
| [saksmappetype](saksmappetype.md) | Type saksmappe |
| [sakssekvensnummer](sakssekvensnummer.md) | Inngår i M003 mappeID — viser rekkjefølgja saksmappene vart oppretta |
| [saksstatus](saksstatus.md) | Status til saksmappa |
| [sendtDato](sendtdato.md) | Dato eit internt produsert dokument vart sendt/ekspedert |
| [sjekksum](sjekksum.md) | Verdi som gir integritetssikring til dokumentets innhald |
| [sjekksumAlgoritme](sjekksumalgoritme.md) | Algoritme nytta for å berekne sjekksummen |
| [skjerming](skjerming.md) | Skjerming av arkivenhet |
| [skjermingshjemmel](skjermingshjemmel.md) | Skjermingsheimelen |
| [soeknadsnummer](soeknadsnummer.md) | Søknadsnummer frå Digisak |
| [tilgang](tilgang.md) | Tilgangar gjevne til arkivressursen |
| [tilgangsgruppe](tilgangsgruppe.md) | Tilgangsgruppe som har tilgang til arkivenheten |
| [tilgangsrestriksjon](tilgangsrestriksjon.md) | Tilgangsrestriksjon |
| [tilknyttetAv](tilknyttetav.md) | Person som knytte dokumentet til registreringa |
| [tilknyttetDato](tilknyttetdato.md) | Datoen eit dokument vart knytt til ei registrering |
| [tilknyttetRegistreringSom](tilknyttetregistreringsom.md) | Rolle dokumentet har i høve registreringa |
| [tiltak](tiltak.md) | Skildrar kva tiltak som skal utførast på eigedommen |
| [tittel](tittel.md) | Tittel eller namn på arkivenheten |
| [utlaantDato](utlaantdato.md) | Dato ein fysisk saksmappe eller journalpost vart utlånt |
| [variantFormat](variantformat.md) | Kva variant dokumentet førekjem i |
| [versjonsnummer](versjonsnummer.md) | Identifikasjon av versjonar innanfor same dokument |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |


## Subsets

| Subset | Description |
| --- | --- |
| [Anbefalt](anbefalt.md) | Anbefalt eigensskap |
| [Obligatorisk](obligatorisk.md) | Obligatorisk eigensskap |
| [Valgfri](valgfri.md) | Valfri eigensskap |
