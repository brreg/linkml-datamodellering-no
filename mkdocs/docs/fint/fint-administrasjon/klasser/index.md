# FINT Administrasjon

FINT-domenemodell for administrasjon og HR. Dekkjer personalressursar, arbeidsforhold, fullmakter og organisasjonsstruktur.


URI: https://data.norge.no/linkml/fint-administrasjon

Name: fint-administrasjon



## Classes





### Obligatorisk

| Class | Description |
| --- | --- |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |
| [Arbeidslokasjon](arbeidslokasjon.md) | Fysisk lokasjon der ein tilsett har sitt arbeidsstad |
| [Fastlonn](fastlonn.md) | Informasjon om fast lønnsbeordring |
| [Fasttillegg](fasttillegg.md) | Faste tillegg til utbetaling |
| [Fravaer](fravaer.md) | Fråvær frå eit arbeidsforhold |
| [Fullmakt](fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |
| [Kontostreng](kontostreng.md) | Sammensetning av kontodimensjonar for bokføring |
| [Lonn](lonn.md) | Informasjon om lønn for eit arbeidsforhold (abstrakt base) |
| [Organisasjonselement](organisasjonselement.md) | Eit element i organisasjonsstrukturen |
| [Personalressurs](personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |
| [Rolle](rolle.md) | Rettighet eller type fullmakt |
| [Variabellonn](variabellonn.md) | Informasjon om variabel lønn |






### Valgfri

| Class | Description |
| --- | --- |
| [Ansvar](ansvar.md) | Del av kontostrengen som beskriv kven som har ansvaret for ei utgift eller in... |
| [Arbeidsforholdstype](arbeidsforholdstype.md) | Viser kva behov hos arbeidsgjevar arbeidsforholdet dekkjer |
| [Fravaerstype](fravaerstype.md) | Type fråvær |
| [Funksjon](funksjon.md) | Del av kontostrengen som beskriv kva som vert produsert |
| [Lonsart](lonsart.md) | Type ytelse |
| [Prosjekt](prosjekt.md) | Del av kontostrengen som peikar på løpande prosjekt |
| [Prosjektart](prosjektart.md) | Element i ei prosjektnedbrytningsstruktur eller arbeidsnedbrytningsstruktur |
| [Stillingskode](stillingskode.md) | Felles kodeverk for stillingar |




### Andre

| Class | Description |
| --- | --- |
| [Aktivitet](aktivitet.md) | Del av kontostrengen og detaljering av funksjon |
| [Anlegg](anlegg.md) | Del av kontostrengen; objekt som skal aktiverast eller avskrivast |
| [Art](art.md) | Del av kontostrengen som beskriv kva slags inntekter og utgifter det gjeld |
| [Diverse](diverse.md) | Del av kontostrengen; supplement til øvrige dimensjonar |
| [Formaal](formaal.md) | Del av kontostrengen som detaljerer inntekter og utgifter ved drift |
| [Fravaersgrunn](fravaersgrunn.md) | Grunn til fråvær |
| [Kontrakt](kontrakt.md) | Kontrakt transaksjonen er knytt til |
| [Lopenummer](lopenummer.md) | Løpenummer i ei nummerserie |
| [Objekt](objekt.md) | Eit bygg, ein veg eller ein mottakar av ei teneste eller eit tilskott |
| [Organisasjonstype](organisasjonstype.md) | Typen til eit organisasjonselement |
| [Personalressurskategori](personalressurskategori.md) | Ansettelsesform til eit arbeidsforhold |
| [Ramme](ramme.md) | Del av kontostrengen som viser kva budsjettramme som skal bere kostnadane |
| [Uketimetall](uketimetall.md) | Timer per veke i 100 % stilling |





## Slots

| Slot | Description |
| --- | --- |
| [aarslonn](aarslonn.md) | Årslønn/grunnlønn i 100 % stilling |
| [aktivitet](aktivitet.md) | Detaljering av funksjon |
| [aktivitetar](aktivitetar.md) | Alle aktivitetar i containeren |
| [anlegg](anlegg.md) | Objekt som skal aktiverast eller avskrivast |
| [ansattnummer](ansattnummer.md) | Unik identifikator for den tilsette i HR-systemet |
| [ansettelsesperiode](ansettelsesperiode.md) | Perioden personalressursen er i eit tilhøve til organisasjonen |
| [ansettelsesprosent](ansettelsesprosent.md) | Prosenten personalressursen eig i høve til arbeidsavtalen |
| [ansiennitet](ansiennitet.md) | Ansiennitet for personalressurs hos arbeidsgjevar |
| [ansvar](ansvar.md) | Ansvarleg for ei utgift eller inntekt |
| [antall](antall.md) | Mengde som vert beskriven av tillegget, i hundredeler |
| [anviser](anviser.md) | Personalressurs som har anvist lønsmeldinga etter fullmakt |
| [anvist](anvist.md) | Tidspunkt då lønn vart anvist |
| [arbeidsforhold](arbeidsforhold.md) | Arbeidsforhold ressursen er knytt til |
| [arbeidsforholdsperiode](arbeidsforholdsperiode.md) | Periode for ei gjeven stilling |
| [arbeidsforholdstypar](arbeidsforholdstypar.md) | Alle arbeidsforholdstypar i containeren |
| [arbeidsforholdstype](arbeidsforholdstype.md) | Beskriven kode som kategoriserer kva funksjon stillinga er gruppert til |
| [arbeidslokasjon](arbeidslokasjon.md) | Fysisk lokasjon der den tilsette har sitt arbeidsstad |
| [arbeidslokasjoner](arbeidslokasjoner.md) | Alle arbeidslokasjoner i containeren |
| [arbeidssted](arbeidssted.md) | Tilhøyrsle til organisasjonsstrukturen |
| [art](art.md) | Type inntekt eller utgift |
| [artar](artar.md) | Alle artar i containeren |
| [attestant](attestant.md) | Personalressurs som har attestert lønsmeldinga etter fullmakt |
| [attestert](attestert.md) | Tidspunkt då lønn vart attestert |
| [belop](belop.md) | Beløp i øre |
| [brukernavn](brukernavn.md) | Brukarnamn til den tilsette |
| [diverse](diverse.md) | Spesifikasjon som ikkje kjem fram i øvrige dimensjonar |
| [fastlonn](fastlonn.md) | Fastlønn for arbeidsforholdet |
| [fasttillegg](fasttillegg.md) | Faste tillegg for arbeidsforholdet |
| [forelder](forelder.md) | Foreldreelement i hierarki |
| [formaal](formaal.md) | Formål viser aktivitet og tenesteproduksjon |
| [fortsettelse](fortsettelse.md) | Fortsetjande fråvær |
| [fortsetter](fortsetter.md) | Fråværet dette fråværet er fortsetjing av |
| [fravaer](fravaer.md) | Fråvær knytt til ressursen |
| [fravaersgrunn](fravaersgrunn.md) | Grunn til fråværet |
| [fravaersgrunnar](fravaersgrunnar.md) | Alle fråværsgrunnar i containeren |
| [fravaerstypar](fravaerstypar.md) | Alle fråværstypar i containeren |
| [fravaerstype](fravaerstype.md) | Type fråvær |
| [fullmakt](fullmakt.md) | Fullmakt ressursen er knytt til |
| [fullmakter](fullmakter.md) | Alle fullmakter i containeren |
| [fullmektig](fullmektig.md) | Personalressurs som har fått fullmakt til ei gjeven rolle |
| [funksjon](funksjon.md) | Det som vert produsert eller tenesta som vert levert |
| [funksjonar](funksjonar.md) | Alle funksjonar i containeren |
| [godkjenner](godkjenner.md) | Personalressurs som har godkjent fråværsmeldinga |
| [godkjent](godkjent.md) | Tidspunkt då fråværet vart godkjent |
| [hovedstilling](hovedstilling.md) | Angir kva arbeidsforhold som er hovudarbeidsforhold |
| [jobbtittel](jobbtittel.md) | Namn som beskriv jobben eller stillinga |
| [kategori](kategori.md) | Kategori lønnsart |
| [kildesystemId](kildesystemid.md) | Kjeldesystemets unike identifikator |
| [kommunar](kommunar.md) | Alle kommuneverdiar i containeren |
| [kontaktpersonar](kontaktpersonar.md) | Alle kontaktpersonar i containeren |
| [konterer](konterer.md) | Personalressurs som har kontert lønsmeldinga etter fullmakt |
| [kontert](kontert.md) | Tidspunkt då lønn vart kontert |
| [kontostreng](kontostreng.md) | Kontering av lønn |
| [kontrakt](kontrakt.md) | Kontrakt ressursen er knytt til |
| [kontrakter](kontrakter.md) | Alle kontrakter i containeren |
| [kortnavn](kortnavn.md) | Forkorta namn som beskriv organisasjonselementet |
| [landkodar](landkodar.md) | Alle landkodar i containeren |
| [leder](leder.md) | Ansvarleg leiar for organisasjonselementet |
| [lederFor](lederfor.md) | Organisasjonselement personalressursen er leiar for |
| [lokasjonskode](lokasjonskode.md) | Kode som identifiserer ein arbeidslokasjon |
| [lokasjonsnavn](lokasjonsnavn.md) | Namn som beskriv ein arbeidslokasjon |
| [lonnsprosent](lonnsprosent.md) | Prosent av årslønn den tilsette skal ha utbetalt |
| [lonsart](lonsart.md) | Lønnsart |
| [lonsartar](lonsartar.md) | Alle lønnsartar i containeren |
| [lopenummer](lopenummer.md) | Løpenummer i ei nummerserie |
| [objekt](objekt.md) | Objekt ressursen er knytt til |
| [opptjent](opptjent.md) | Periode der lønn vart opptent |
| [organisasjonselement](organisasjonselement.md) | Organisasjonselement ressursen er knytt til |
| [organisasjonsId](organisasjonsid.md) | Unikt internnummer for organisasjonselementet |
| [organisasjonsKode](organisasjonskode.md) | Beskriven kode for organisasjonselementet |
| [organisasjonstypar](organisasjonstypar.md) | Alle organisasjonstypar i containeren |
| [organisasjonstype](organisasjonstype.md) | Kva type organisasjonselement dette er |
| [overfores](overfores.md) | Angir om fråvær av denne typen skal overførast til HR |
| [overordnet](overordnet.md) | Overordna element i hierarkiet |
| [periode](periode.md) | Periode for ressursen |
| [personalansvar](personalansvar.md) | Arbeidsforhold der personalressursen har personalansvar |
| [personalleder](personalleder.md) | Personalleiar til arbeidsforholdet |
| [personalressurs](personalressurs.md) | Personalressurs til arbeidsforholdet |
| [personalressursar](personalressursar.md) | Alle personalressursar i containeren |
| [personalressurskategori](personalressurskategori.md) | Kategori for personalressursen |
| [personalressurskategoriar](personalressurskategoriar.md) | Alle personalressurskategoriar i containeren |
| [personar](personar.md) | Alle personar i containeren |
| [prosent](prosent.md) | Prosent |
| [prosjekt](prosjekt.md) | Prosjekt ressursen er knytt til |
| [prosjektart](prosjektart.md) | Deloppgåve eller delprosjekt |
| [prosjektartar](prosjektartar.md) | Alle prosjektartar i containeren |
| [ramme](ramme.md) | Budsjettramme som skal bere kostnadane |
| [rammer](rammer.md) | Alle rammer i containeren |
| [rollar](rollar.md) | Alle rollar i containeren |
| [rolle](rolle.md) | Kva type fullmakt |
| [rolleNavn](rollenavn.md) | Namn på rolla; unik identifikator |
| [skole](skole.md) | Referanse til Skole (Utdanning) |
| [skoleressurs](skoleressurs.md) | Referanse til Skoleressurs (Utdanning) |
| [spraak](spraak.md) | Alle språkverdiar i containeren |
| [stedfortreder](stedfortreder.md) | Stedfortredar i fullmaktssamanheng |
| [stillingskode](stillingskode.md) | Firesifra stillingskode frå KS, eventuelt utvida med to siffer |
| [stillingskoder](stillingskoder.md) | Alle stillingskoder i containeren |
| [stillingsnummer](stillingsnummer.md) | Løpenummer for stillinga |
| [stillingstittel](stillingstittel.md) | Arbeidstakarens stillingstittel i gjeldande stilling |
| [tilstedeprosent](tilstedeprosent.md) | Det personalressursen faktisk jobbar |
| [timerPerUke](timerperuke.md) | Timer per veke i 100 % stilling |
| [uketimetall](uketimetall.md) | Alle uketimetallverdiar i containeren |
| [underordnet](underordnet.md) | Underordna element i hierarkiet |
| [undervisningsforhold](undervisningsforhold.md) | Referanse til Undervisningsforhold (Utdanning) |
| [valuta](valuta.md) | Alle valutaverdiar i containeren |
| [variabellonn](variabellonn.md) | Variabel lønn for arbeidsforholdet |
| [virksomhetar](virksomhetar.md) | Alle verksemder i containeren |


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
