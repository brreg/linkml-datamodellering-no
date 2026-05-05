# FINT Utdanning

FINT-domenemodell for utdanning. Dekkjer elevar, skular, skoleressursar, elevforhold, undervisningsforhold, klasser, undervisningsgrupper, faggrupper, kontaktlærergrupper, utdanningsprogram, programområde, vurdering, lærling og OT.


URI: https://data.norge.no/linkml/fint-utdanning

Name: fint-utdanning



## Classes

| Class | Description |
| --- | --- |
| [Adresse](adresse.md) | Fysisk adresse eller postadresse |
| [Aktoer](aktoer.md) | Abstrakt base for person eller eining vi samhandlar med |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Person](person.md) | Fysiske private personar |
| [Anmerkninger](anmerkninger.md) | Åtferds- og ordensanmerkningar for ein elev i eit skoleår |
| [Avbruddsaarsak](avbruddsaarsak.md) | Årsak til avbrot frå opplæring |
| [AvlagtProve](avlagtprove.md) | Ei avlagt prøve for ein lærling |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fylke](fylke.md) | Liste over Norges fylker |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kommune](kommune.md) | Liste over Norges kommunar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |
| [Betalingsstatus](betalingsstatus.md) | Betalingsstatus for eksamensavgift |
| [Bevistype](bevistype.md) | Type kompetansebevis for lærling |
| [Brevtype](brevtype.md) | Type brev knytt til lærlingprøve |
| [Eksamen](eksamen.md) | Ein eksamen knytt til ei eksamensgruppe |
| [Eksamensform](eksamensform.md) | Form for gjennomføring av eksamen |
| [Elev](elev.md) | Ein elev registrert i skulesystemet |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |
| [Elevfravar](elevfravar.md) | Fråværsregistreringar for ein elev knytt til eit elevforhold |
| [Elevkategori](elevkategori.md) | Kategori for eit elevforhold (t |
| [Elevtilrettelegging](elevtilrettelegging.md) | Tilrettelegging for ein elev i eit elevforhold |
| [Elevvurdering](elevvurdering.md) | Samling av alle vurderingar for ein elev i eit elevforhold |
| [Fagmerknad](fagmerknad.md) | Merknad knytt til eit fag i ei faggruppe |
| [Fagstatus](fagstatus.md) | Status for eit fag i eit faggruppemedlemskap |
| [FagvurderingAbstrakt](fagvurderingabstrakt.md) | Abstrakt basisklasse for fagvurderingar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Eksamensvurdering](eksamensvurdering.md) | Vurdering gjeven i samband med ein eksamen |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Halvaarsfagvurdering](halvaarsfagvurdering.md) | Halvårsvurdering i eit fag |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Sluttfagvurdering](sluttfagvurdering.md) | Sluttkarakter i eit fag |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Underveisfagvurdering](underveisfagvurdering.md) | Underveisfagvurdering for ein elev |
| [Fravarsoversikt](fravarsoversikt.md) | Oversikt over fråvær for ein elev i eit fag |
| [Fravarsprosent](fravarsprosent.md) | Kompleks type som representerer fråværsprosent for ein periode |
| [Fravartype](fravartype.md) | Type fråvær (t |
| [Fraversregistrering](fraversregistrering.md) | Ei enkelt fråversregistrering for ein elev |
| [Fullfortkode](fullfortkode.md) | Kode for fullførtresultat av lærling |
| [Gruppe](gruppe.md) | Abstrakt basisklasse for alle gruppetypar i utdanning |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Arstrinn](arstrinn.md) | Eit årstrinn i skulen (t |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Eksamensgruppe](eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fag](fag.md) | Eit skulefag |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Faggruppe](faggruppe.md) | Ei gruppe elevar knytt til eit fag på ein skule |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Klasse](klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kontaktlaerergruppe](kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Persongruppe](persongruppe.md) | Ei gruppe elevar definert for personlege føremål |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Programomrade](programomrade.md) | Eit programområde innanfor eit utdanningsprogram (t |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Undervisningsgruppe](undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Utdanningsprogram](utdanningsprogram.md) | Eit utdanningsprogram (t |
| [Gruppemedlemskap](gruppemedlemskap.md) | Abstrakt basisklasse for gruppemedlemskapar i utdanning |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md) | Eit elevs deltaking i ei eksamensgruppe |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Faggruppemedlemskap](faggruppemedlemskap.md) | Eit elevs medlemskap i ei faggruppe |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Klassemedlemskap](klassemedlemskap.md) | Eit elevs medlemskap i ei klasse |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kontaktlaerergruppemedlemskap](kontaktlaerergruppemedlemskap.md) | Eit elevs medlemskap i ei kontaktlærargruppe |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Persongruppemedlemskap](persongruppemedlemskap.md) | Eit elevs medlemskap i ei persongruppe |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Programomrademedlemskap](programomrademedlemskap.md) | Eit elevs tilknyting til eit programområde |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Undervisningsgruppemedlemskap](undervisningsgruppemedlemskap.md) | Eit elevs medlemskap i ei undervisningsgruppe |
| [Identifikator](identifikator.md) | Unik identifikasjon til eit objekt |
| [Karakterhistorie](karakterhistorie.md) | Historikk over endringar i ein karakter |
| [Karakterskala](karakterskala.md) | Skala for karaktersetjing (t |
| [Karakterstatus](karakterstatus.md) | Status for ein karakter (t |
| [Karakterverdi](karakterverdi.md) | Ein konkret karakterverdi i ei karakterskala |
| [Kontaktinformasjon](kontaktinformasjon.md) | Informasjon som kan brukast for å oppnå kontakt |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |
| [Laerling](laerling.md) | Ein lærling i yrkesopplæring |
| [Matrikkelnummer](matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |
| [OrdensvurderingAbstrakt](ordensvurderingabstrakt.md) | Abstrakt basisklasse for ordensvurderingar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Halvaarsordensvurdering](halvaarsordensvurdering.md) | Halvårsordensvurdering for ein elev |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Sluttordensvurdering](sluttordensvurdering.md) | Sluttordensvurdering for ein elev |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Underveisordensvurdering](underveisordensvurdering.md) | Underveisordensvurdering for ein elev |
| [OtEnhet](otenhet.md) | Eining i oppfølgingstenesta (OT) |
| [OtStatus](otstatus.md) | Status for ein ungdom i oppfølgingstenesta |
| [OtUngdom](otungdom.md) | Eit ungdomsobjekt i oppfølgingstenesta (OT) |
| [Periode](periode.md) | Tidsperiode med obligatorisk start og valfri slutt |
| [Personnavn](personnavn.md) | Namn på ein person |
| [Provestatus](provestatus.md) | Status for ei lærlingprøve |
| [Rom](rom.md) | Eit rom eller lokale ved ein skule |
| [Sensor](sensor.md) | Ein sensor for ein eksamen |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |
| [Skoleaar](skoleaar.md) | Eit skoleår (t |
| [Skoleeiertype](skoleeiertype.md) | Type skuleeigartilknyting |
| [Skoleressurs](skoleressurs.md) | Ein lærar eller anna tilsett ved ein skule |
| [Termin](termin.md) | Ein skuleterm (t |
| [Tilrettelegging](tilrettelegging.md) | Type tilrettelegging for elevar (t |
| [Time](time.md) | Ein time i timeplanen |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |
| [Utdanningsforhold](utdanningsforhold.md) | Abstrakt basisklasse for undervisningsforhold i utdanning |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Undervisningsforhold](undervisningsforhold.md) | Eit tilhøve mellom ein skoleressurs og undervisningsaktivitetar |
| [Valuta](valuta.md) | Valutakodar for offisielle valutaer |
| [Varsel](varsel.md) | Eit varsel knytt til ein elev i ei faggruppe |
| [Varseltype](varseltype.md) | Type varsel knytt til ein elev |
| [Vitnemalsmerknad](vitnemalsmerknad.md) | Merknad på vitnemål |



## Slots

| Slot | Description |
| --- | --- |
| [adresse](adresse.md) | Adresse til matrikkeleining |
| [adresselinje](adresselinje.md) | Adresseinformasjon |
| [aktiv](aktiv.md) | Angir om sensoren er aktiv |
| [anmerkningar](anmerkningar.md) |  |
| [arbeidsforhold](arbeidsforhold.md) | Referanse til Arbeidsforhold i Administrasjon-domenet |
| [arstrinn](arstrinn.md) |  |
| [atferd](atferd.md) | Karakterverdi for åtferd |
| [avbruddsaarsaker](avbruddsaarsaker.md) |  |
| [avbruddsarsak](avbruddsarsak.md) | Årsak til avbrot frå opplæring |
| [avbruddsdato](avbruddsdato.md) | Dato for avbrot frå opplæring |
| [avlagteprover](avlagteprover.md) |  |
| [avlagtprove](avlagtprove.md) | Avlagde prøver for lærlingen |
| [bedrift](bedrift.md) | Referanse til bedrifta lærlingen er i |
| [beskrivelse](beskrivelse.md) | Skildring av gruppa |
| [betalingsstatus](betalingsstatus.md) |  |
| [bevistypar](bevistypar.md) |  |
| [bevistype](bevistype.md) | Type kompetansebevis |
| [bilde](bilde.md) | HTTP(S)-lenkje til eit bilete av personen |
| [bokstavkode](bokstavkode.md) | Bokstavkode for aktuell valuta |
| [bostedsadresse](bostedsadresse.md) | Folkeregistrert adresse til personen |
| [brevtypar](brevtypar.md) |  |
| [brevtype](brevtype.md) | Type brev knytt til prøva |
| [bruksnummer](bruksnummer.md) | Fortløpande nummerering av bruk under gårdsnummer |
| [delegert](delegert.md) | Angir om deltakinga er delegert |
| [delegertTil](delegerttil.md) | Referanse til den deltakinga er delegert til |
| [domenenavn](domenenavn.md) | Domenenamn for skulen |
| [eksamen](eksamen.md) |  |
| [eksamensdato](eksamensdato.md) | Dato for eksamenen |
| [eksamensform](eksamensform.md) | Eksamensform knytt til tilrettelegginga |
| [eksamensformer](eksamensformer.md) |  |
| [eksamensgruppe](eksamensgruppe.md) | Eksamensgrupper ved skulen |
| [eksamensgruppemedlemskap](eksamensgruppemedlemskap.md) |  |
| [eksamensgrupper](eksamensgrupper.md) |  |
| [eksamensvurdering](eksamensvurdering.md) |  |
| [elev](elev.md) | Eleven dette forholdet gjeld |
| [elevar](elevar.md) |  |
| [elevforhold](elevforhold.md) |  |
| [elevfravar](elevfravar.md) |  |
| [elevkategoriar](elevkategoriar.md) |  |
| [elevnummer](elevnummer.md) | Skulens interne elevnummer |
| [elevtilrettelegging](elevtilrettelegging.md) |  |
| [elevvurdering](elevvurdering.md) |  |
| [endretDato](endretdato.md) | Dato og tidspunkt for endringa |
| [enhet](enhet.md) | OT-eining knytt til ungdommen |
| [epostadresse](epostadresse.md) | Namngitt elektronisk adresse for mottak av e-post |
| [etternavn](etternavn.md) | Etternamn til personen |
| [fag](fag.md) |  |
| [faggruppe](faggruppe.md) | Faggrupper ved skulen |
| [faggruppemedlemskap](faggruppemedlemskap.md) |  |
| [faggrupper](faggrupper.md) |  |
| [fagmerknad](fagmerknad.md) | Merknad til faget for dette medlemskapet |
| [fagmerknader](fagmerknader.md) |  |
| [fagstatus](fagstatus.md) |  |
| [feidenavn](feidenavn.md) | Feide-identifikator for skoleressursen |
| [festenummer](festenummer.md) | Fortløpande nummerering av festar under gårdsnummer/bruksnummer |
| [fodselsdato](fodselsdato.md) | Dato for fødsel |
| [fodselsnummer](fodselsnummer.md) | Fødselsnummer eller ein av dei fiktive variantane |
| [foreldre](foreldre.md) | Den/dei som har foreldreansvar til personen |
| [foreldreansvar](foreldreansvar.md) | Personar denne personen har foreldreansvar for |
| [forersPaaVitnemaal](forerspaavitnemaal.md) | Angir om fråværet vert ført på vitnemålet |
| [foretrukketSensor](foretrukketsensor.md) | Angir om sensor er føretrekt |
| [foretrukketSkole](foretrukketskole.md) | Angir om skulen er føretrekt for eksamenen |
| [fornavn](fornavn.md) | Fornamn til personen |
| [forretningsadresse](forretningsadresse.md) | Forretningsadresse til skulen |
| [fravaerstimer](fravaerstimer.md) | Antal fråværstimar |
| [fravarsoversikt](fravarsoversikt.md) |  |
| [fravarsprosent](fravarsprosent.md) | Fråværsprosent ved utsending av varselet |
| [fravartypar](fravartypar.md) |  |
| [fravartype](fravartype.md) | Type fråvær |
| [fraversregistrering](fraversregistrering.md) |  |
| [fraversregistreringer](fraversregistreringer.md) | Fråværsregistreringar knytt til elevforholdet |
| [fullfortkode](fullfortkode.md) | Kode for fullførtresultatet |
| [fullfortkoder](fullfortkoder.md) |  |
| [fylke](fylke.md) | Fylket kommunen høyrer til |
| [gaardsnummer](gaardsnummer.md) | Nummerering av gårdseiging i matrikkelen, unik innanfor kommune |
| [grepreferanse](grepreferanse.md) | Referanse til GREP-registeret |
| [gruppemedlemskap](gruppemedlemskap.md) | Medlemskapar i denne kontaktlærergruppa |
| [gyldighetsperiode](gyldighetsperiode.md) | Perioden medlemskapet er gyldig |
| [halvaar](halvaar.md) | Fråværsprosent for halvåret |
| [halvaarsfagvurdering](halvaarsfagvurdering.md) |  |
| [halvaarsordensvurdering](halvaarsordensvurdering.md) |  |
| [id](id.md) | URI-identifikator for ressursen |
| [identifikatorverdi](identifikatorverdi.md) | Ein konkret kombinasjon av teikn og/eller bokstavar som utgjer ein bestemt id... |
| [juridiskNavn](juridisknavn.md) | Juridisk namn på skulen |
| [kandidatnummer](kandidatnummer.md) | Kandidatnummer for eksamenen |
| [karakter](karakter.md) | Karakterverdien gjeve i vurderinga |
| [karakteransvarlig](karakteransvarlig.md) | Skoleressurs som er ansvarleg for karakteren |
| [karakterhistorie](karakterhistorie.md) |  |
| [karakterskalaer](karakterskalaer.md) |  |
| [karakterstatus](karakterstatus.md) |  |
| [karakterverdi](karakterverdi.md) | Ny karakterverdi etter endringa |
| [karakterverdiar](karakterverdiar.md) |  |
| [kategori](kategori.md) | Kategori for elevforholdet |
| [kjonn](kjonn.md) | Kjønn for personen |
| [klasse](klasse.md) | Klassen dette medlemskapet er i |
| [klassemedlemskap](klassemedlemskap.md) |  |
| [klasser](klasser.md) |  |
| [kode](kode.md) |  |
| [kommentar](kommentar.md) | Kommentar til vurderinga |
| [kommune](kommune.md) | Referanse til kommunen OT-eininga dekker |
| [kommunenummer](kommunenummer.md) | Nummerering av kommunen i høve til SSB si offisielle liste |
| [kontaktinformasjon](kontaktinformasjon.md) | Den føretrekte måten å kome i kontakt med ein aktør |
| [kontaktlaerergruppe](kontaktlaerergruppe.md) | Kontaktlærergrupper knytt til klassen |
| [kontaktlaerergruppemedlemskap](kontaktlaerergruppemedlemskap.md) |  |
| [kontaktlaerergrupper](kontaktlaerergrupper.md) |  |
| [kontaktperson](kontaktperson.md) | Personar kontaktpersonen er pårørande for |
| [kontraktstype](kontraktstype.md) | Type kontrakt for lærlingen |
| [laerling](laerling.md) | Lærlingen som avla prøva |
| [laerlingar](laerlingar.md) |  |
| [land](land.md) | Land der adressa befinn seg |
| [laretid](laretid.md) | Læringstidsperiode for lærlingen |
| [maalform](maalform.md) | Målform personen føretrekkjer |
| [mellomnavn](mellomnavn.md) | Mellomnamn |
| [mobiltelefonnummer](mobiltelefonnummer.md) | Mobiltelefonnummer |
| [morsmaal](morsmaal.md) | Morsmål til personen |
| [navn](navn.md) | Namn på gruppa |
| [nettsted](nettsted.md) | Adresse til eit nettstad |
| [nummerkode](nummerkode.md) | Nummerkode for aktuell valuta |
| [nus](nus.md) | NUS-kode knytt til eksamensgruppemedlemskapet |
| [oppdatertAv](oppdatertav.md) | Skoleressurs som oppdaterte karakteren |
| [oppmoetetidspunkt](oppmoetetidspunkt.md) | Tidspunkt for oppmøte til eksamenen |
| [opprinneligKarakterstatus](opprinneligkarakterstatus.md) | Opphavleg karakterstatus før endringa |
| [opprinneligKarakterverdi](opprinneligkarakterverdi.md) | Opphavleg karakterverdi før endringa |
| [orden](orden.md) | Karakterverdi for orden |
| [organisasjon](organisasjon.md) | Referanse til Organisasjonselement i Administrasjon-domenet |
| [organisasjonsnavn](organisasjonsnavn.md) | Organisasjonsnamn for skulen |
| [organisasjonsnummer](organisasjonsnummer.md) | Organisasjonsnummer-identifikator |
| [otEnheter](otenheter.md) |  |
| [otStatus](otstatus.md) |  |
| [otUngdom](otungdom.md) |  |
| [otungdom](otungdom.md) | Referanse til OtUngdom (Utdanning) |
| [parorende](parorende.md) | Pårørande kontaktperson til personen |
| [passiv](passiv.md) |  |
| [periode](periode.md) | Perioden fråværet varte |
| [person](person.md) | Referanse til Person i Administrasjon-domenet |
| [personalressurs](personalressurs.md) | Referanse til Personalressurs i Administrasjon-domenet |
| [persongruppe](persongruppe.md) | Persongruppa dette medlemskapet er i |
| [persongruppemedlemskap](persongruppemedlemskap.md) |  |
| [persongrupper](persongrupper.md) |  |
| [postadresse](postadresse.md) | Postadresse til skulen |
| [postnummer](postnummer.md) | Postnummer |
| [poststed](poststed.md) | Poststad |
| [programomrade](programomrade.md) | Programområde knytt til årstrinnet |
| [programomrademedlemskap](programomrademedlemskap.md) |  |
| [programomrader](programomrader.md) |  |
| [prosent](prosent.md) | Fråværsprosent (heiltal) |
| [provedato](provedato.md) | Dato prøva vart avlagt |
| [provestatus](provestatus.md) | Status for prøva |
| [provestatuser](provestatuser.md) |  |
| [registrertAv](registrertav.md) | Skoleressurs som registrerte fråværet |
| [rom](rom.md) |  |
| [seksjonsnummer](seksjonsnummer.md) | Fortløpande nummerering av seksjonar under gårdsnummer/bruksnummer |
| [sendt](sendt.md) | Dato varselet vart sendt |
| [sensor](sensor.md) |  |
| [sensornummer](sensornummer.md) | Sensornummer |
| [sip](sip.md) | SIP-protokoll for VoIP (IP-telefoni) |
| [skala](skala.md) | Karakterskalaen denne verdien tilhøyrer |
| [skolar](skolar.md) |  |
| [skole](skole.md) | Skulen eleven er tilknytt |
| [skoleaar](skoleaar.md) |  |
| [skoleaarFravar](skoleaarfravar.md) | Fråværsprosent for heile skoleåret |
| [skoleeierType](skoleeiertype.md) | Kategori for skuleeigartilknyting |
| [skoleeijartypar](skoleeijartypar.md) |  |
| [skolenummer](skolenummer.md) | Nasjonal skulenummer-identifikator |
| [skoleressurs](skoleressurs.md) | Skoleressursar knytt til gruppa |
| [skoleressursar](skoleressursar.md) |  |
| [slutt](slutt.md) | Til tidspunkt |
| [sluttfagvurdering](sluttfagvurdering.md) |  |
| [sluttordensvurdering](sluttordensvurdering.md) |  |
| [start](start.md) | Frå tidspunkt |
| [statsborgerskap](statsborgerskap.md) | Alle statsborgarskap personen har |
| [status](status.md) | OT-status for ungdommen |
| [tekst](tekst.md) | Innhald i varselet |
| [telefonnummer](telefonnummer.md) | Telefonnummer |
| [termin](termin.md) | Terminar klassen er aktiv i |
| [terminar](terminar.md) |  |
| [tidsrom](tidsrom.md) | Tidsrom for eksamenen |
| [tilrettelegging](tilrettelegging.md) |  |
| [timar](timar.md) |  |
| [time](time.md) | Timar haldne i dette rommet |
| [tosprakligFagopplaering](tosprakligfagopplaering.md) | Indikerer om eleven har tospråkleg fagopplæring |
| [trinn](trinn.md) | Årstrinnet klassen tilhøyrer |
| [type](type.md) | Type varsel |
| [underveisfagvurdering](underveisfagvurdering.md) |  |
| [underveisordensvurdering](underveisordensvurdering.md) |  |
| [undervisningsforhold](undervisningsforhold.md) |  |
| [undervisningsgruppe](undervisningsgruppe.md) | Undervisningsgrupper som underviser i faget |
| [undervisningsgruppemedlemskap](undervisningsgruppemedlemskap.md) |  |
| [undervisningsgrupper](undervisningsgrupper.md) |  |
| [undervisningstimer](undervisningstimer.md) | Totalt antal undervisningstimar |
| [utdanningsprogram](utdanningsprogram.md) |  |
| [utsteder](utsteder.md) | Skoleressurs som sende varselet |
| [varsel](varsel.md) |  |
| [varseltypar](varseltypar.md) |  |
| [verdi](verdi.md) | Karakterverdiar i denne skalaen |
| [vigoreferanse](vigoreferanse.md) | Referanse til Vigo-systemet |
| [virksomhetsId](virksomhetsid.md) | Intern unik identifikator i økonomisystemet |
| [vitnemalsmerknad](vitnemalsmerknad.md) |  |
| [vurderingsdato](vurderingsdato.md) | Dato og tidspunkt for vurderinga |


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
