# FINT Administrasjon

FINT-domenemodell for administrasjon og HR. Dekkjer personalressursar, arbeidsforhold, fullmakter og organisasjonsstruktur.


URI: https://data.norge.no/fint/fint-administrasjon

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
| [ansattnummer](ansattnummer.md) | Unik identifikator for den tilsette i HR-systemet |
| [ansettelsesperiode](ansettelsesperiode.md) | Perioden personalressursen er i eit tilhøve til organisasjonen |
| [ansettelsesprosent](ansettelsesprosent.md) | Prosenten personalressursen eig i høve til arbeidsavtalen |
| [ansiennitet](ansiennitet.md) | Ansiennitet for personalressurs hos arbeidsgjevar |
| [antall](antall.md) | Mengde som vert beskriven av tillegget, i hundredeler |
| [anviser](anviser.md) | Personalressurs som har anvist lønsmeldinga etter fullmakt |
| [anvist](anvist.md) | Tidspunkt då lønn vart anvist |
| [arbeidsforholdsperiode](arbeidsforholdsperiode.md) | Periode for ei gjeven stilling |
| [arbeidsforholdstype](arbeidsforholdstype.md) | Beskriven kode som kategoriserer kva funksjon stillinga er gruppert til |
| [arbeidslokasjon](arbeidslokasjon.md) | Fysisk lokasjon der den tilsette har sitt arbeidsstad |
| [arbeidssted](arbeidssted.md) | Tilhøyrsle til organisasjonsstrukturen |
| [art](art.md) | Type inntekt eller utgift |
| [attestant](attestant.md) | Personalressurs som har attestert lønsmeldinga etter fullmakt |
| [attestert](attestert.md) | Tidspunkt då lønn vart attestert |
| [belop](belop.md) | Beløp i øre |
| [brukernavn](brukernavn.md) | Brukarnamn til den tilsette |
| [forelder](forelder.md) | Foreldreelement i hierarki |
| [fortsettelse](fortsettelse.md) | Fortsetjande fråvær |
| [fortsetter](fortsetter.md) | Fråværet dette fråværet er fortsetjing av |
| [fravaersgrunn](fravaersgrunn.md) | Grunn til fråværet |
| [fravaerstype](fravaerstype.md) | Type fråvær |
| [fullmakt](fullmakt.md) | Fullmakt ressursen er knytt til |
| [fullmektig](fullmektig.md) | Personalressurs som har fått fullmakt til ei gjeven rolle |
| [funksjon](funksjon.md) | Det som vert produsert eller tenesta som vert levert |
| [godkjenner](godkjenner.md) | Personalressurs som har godkjent fråværsmeldinga |
| [godkjent](godkjent.md) | Tidspunkt då fråværet vart godkjent |
| [hovedstilling](hovedstilling.md) | Angir kva arbeidsforhold som er hovudarbeidsforhold |
| [jobbtittel](jobbtittel.md) | Namn som beskriv jobben eller stillinga |
| [kategori](kategori.md) | Kategori lønnsart |
| [kildesystemId](kildesystemid.md) | Kjeldesystemets unike identifikator |
| [konterer](konterer.md) | Personalressurs som har kontert lønsmeldinga etter fullmakt |
| [kontert](kontert.md) | Tidspunkt då lønn vart kontert |
| [kontostreng](kontostreng.md) | Kontering av lønn |
| [kontrakt](kontrakt.md) | Kontrakt ressursen er knytt til |
| [kortnavn](kortnavn.md) | Forkorta namn som beskriv organisasjonselementet |
| [leder](leder.md) | Ansvarleg leiar for organisasjonselementet |
| [lederFor](lederfor.md) | Organisasjonselement personalressursen er leiar for |
| [lokasjonskode](lokasjonskode.md) | Kode som identifiserer ein arbeidslokasjon |
| [lokasjonsnavn](lokasjonsnavn.md) | Namn som beskriv ein arbeidslokasjon |
| [lonnsprosent](lonnsprosent.md) | Prosent av årslønn den tilsette skal ha utbetalt |
| [lonsart](lonsart.md) | Lønnsart |
| [opptjent](opptjent.md) | Periode der lønn vart opptent |
| [organisasjonsId](organisasjonsid.md) | Unikt internnummer for organisasjonselementet |
| [organisasjonsKode](organisasjonskode.md) | Beskriven kode for organisasjonselementet |
| [organisasjonstype](organisasjonstype.md) | Kva type organisasjonselement dette er |
| [overfores](overfores.md) | Angir om fråvær av denne typen skal overførast til HR |
| [overordnet](overordnet.md) | Overordna element i hierarkiet |
| [periode](periode.md) | Periode for ressursen |
| [personalansvar](personalansvar.md) | Arbeidsforhold der personalressursen har personalansvar |
| [personalleder](personalleder.md) | Personalleiar til arbeidsforholdet |
| [personalressurs](personalressurs.md) | Personalressurs til arbeidsforholdet |
| [personalressurskategori](personalressurskategori.md) | Kategori for personalressursen |
| [prosent](prosent.md) | Prosent |
| [prosjektart](prosjektart.md) | Deloppgåve eller delprosjekt |
| [ramme](ramme.md) | Budsjettramme som skal bere kostnadane |
| [rolle](rolle.md) | Kva type fullmakt |
| [rolleNavn](rollenavn.md) | Namn på rolla; unik identifikator |
| [skole](skole.md) | Referanse til Skole (Utdanning) |
| [skoleressurs](skoleressurs.md) | Referanse til Skoleressurs (Utdanning) |
| [stedfortreder](stedfortreder.md) | Stedfortredar i fullmaktssamanheng |
| [stillingskode](stillingskode.md) | Firesifra stillingskode frå KS, eventuelt utvida med to siffer |
| [stillingsnummer](stillingsnummer.md) | Løpenummer for stillinga |
| [stillingstittel](stillingstittel.md) | Arbeidstakarens stillingstittel i gjeldande stilling |
| [tilstedeprosent](tilstedeprosent.md) | Det personalressursen faktisk jobbar |
| [timerPerUke](timerperuke.md) | Timer per veke i 100 % stilling |
| [underordnet](underordnet.md) | Underordna element i hierarkiet |
| [undervisningsforhold](undervisningsforhold.md) | Referanse til Undervisningsforhold (Utdanning) |


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
