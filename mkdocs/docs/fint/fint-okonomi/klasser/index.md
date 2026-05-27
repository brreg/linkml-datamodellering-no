# FINT Økonomi

FINT-domenemodell for økonomi. Dekkjer tre sub-pakkar: okonomi.faktura (faktura, fakturagrunnlag, fakturautsteder), okonomi.regnskap (transaksjonar, posteringar, bilag, leverandørar) og okonomi.kodeverk (vare, merverdiavgift, valuta).


URI: https://data.norge.no/fint/fint-okonomi

Name: fint-okonomi



## Classes







### Obligatorisk

| Class | Description |
| --- | --- |
| [Bilag](bilag.md) | Dokumentasjon til ein transaksjon (kompleks datatype) |
| [Faktura](faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |
| [Fakturagrunnlag](fakturagrunnlag.md) | Grunnlag for fakturering |
| [Fakturalinje](fakturalinje.md) | Del av Fakturagrunnlag som skildrar ei enkelt vare (kompleks datatype) |
| [Fakturamottaker](fakturamottaker.md) | Aktør som skal betale faktura (kompleks datatype) |
| [Fakturautsteder](fakturautsteder.md) | Eining som utformar og oversender faktura og mottar betaling |
| [Leverandorgruppe](leverandorgruppe.md) | Gruppering av leverandørar |
| [Merverdiavgift](merverdiavgift.md) | Kodeverk for merverdiavgifter |
| [OkonomiValuta](okonomivaluta.md) | Valuta for transaksjonsbeløp |
| [Postering](postering.md) | Føring på ein konto i rekneskapet |
| [Transaksjon](transaksjon.md) | Overføring av pengar til eller frå eksterne partar |
| [Vare](vare.md) | Vare eller teneste som kan leverast og fakturerast |




### Anbefalt

| Class | Description |
| --- | --- |
| [Kontostreng](kontostreng.md) | Kontodimensjonar for ei postering (kompleks datatype) |




### Valgfri

| Class | Description |
| --- | --- |
| [Leverandor](leverandor.md) | Person eller verksemd som leverer produkt eller tenester |







## Slots

| Slot | Description |
| --- | --- |
| [ansvar](ansvar.md) | Ansvarsomrade |
| [ansvarlig](ansvarlig.md) | Referanse til Personalressurs (Administrasjon) som er ansvarleg |
| [antall](antall.md) | Mengd av varen levert |
| [art](art.md) | Artskonto (type utgift/inntekt) |
| [avgiftsbelop](avgiftsbelop.md) | Del av totalbeløp som er avgifter, i øre |
| [belop](belop.md) | Beløp, i øre |
| [betalt](betalt.md) | Status på betaling |
| [bilag](bilag.md) | Bilag til transaksjonen |
| [bilagsdato](bilagsdato.md) | Dato bilaget er registrert |
| [bilagsnummer](bilagsnummer.md) | Nummer på bilaget |
| [data](data.md) | Bilagets fil, koda som Base64 |
| [dato](dato.md) | Dato for utferding av faktura |
| [debet](debet.md) | Angir om posteringa er debet eller kredit |
| [enhet](enhet.md) | Namn på mengdeeininga varen leverast i |
| [faktura](faktura.md) | Utferdigde fakturaer for fakturagrunnlaget |
| [fakturalinjer](fakturalinjer.md) | Linjer av varer eller tenester som skal fakturerast |
| [fakturamottaker](fakturamottaker.md) | Mottakar som skal betale faktura |
| [fakturanummer](fakturanummer.md) | Identifikator oppretta i fakturaprogrammet |
| [fakturautsteder](fakturautsteder.md) | Utstedar av faktura og mottakar av betaling |
| [fakturert](fakturert.md) | Status på utsending |
| [filnavn](filnavn.md) | Namn på bilagets fil |
| [forfallsdato](forfallsdato.md) | Frist for betaling eller forfallsdato for transaksjon |
| [fritekst](fritekst.md) | Fritekst som skildrar varen slik han er levert |
| [funksjon](funksjon.md) | Funksjonskode (KOSTRA) |
| [kontering](kontering.md) | Kontodimensjonar |
| [kontonummer](kontonummer.md) | Kontonummer til leverandøren |
| [kreditert](kreditert.md) | Status på kreditering |
| [leverandor](leverandor.md) | Leverandør |
| [leverandorgruppe](leverandorgruppe.md) | Gruppe av leverandørar leverandøren tilhøyrer |
| [leverandornummer](leverandornummer.md) | Nummer som identifiserer ein leverandør |
| [leveringsdato](leveringsdato.md) | Dato varer eller tenester vart leverte |
| [merverdiavgift](merverdiavgift.md) | Varens avgiftsklasse og -sats |
| [mottaker](mottaker.md) | Namn på mottakar |
| [nettobelop](nettobelop.md) | Del av totalbeløp som utgjer summen av fakturalinjene, i øre |
| [oppdateringstidspunkt](oppdateringstidspunkt.md) | Tidspunkt for siste endring i transaksjonen |
| [ordrenummer](ordrenummer.md) | Unik identifikator for ordren det skal utferdigast faktura på |
| [organisasjonselement](organisasjonselement.md) | Referanse til Organisasjonselement (Administrasjon) |
| [personalressurs](personalressurs.md) | Referanse til Personalressurs (Administrasjon) |
| [postering](postering.md) | Posteringar tilhøyrande transaksjonen |
| [posteringsId](posteringsid.md) | Intern unik identifikator i økonomisystemet |
| [pris](pris.md) | Pris per eining, i øre |
| [prosjekt](prosjekt.md) | Prosjektkode |
| [referanse](referanse.md) | Ekstern referanse, t |
| [restbelop](restbelop.md) | Gjenståande beløp å betale, i øre |
| [sats](sats.md) | Sats for merverdiavgift |
| [totalbelop](totalbelop.md) | Totalt beløp på faktura inkl |
| [transaksjon](transaksjon.md) | Transaksjonen posteringa tilhøyrer |
| [transaksjonsId](transaksjonsid.md) | Intern unik identifikator i økonomisystemet |
| [transaksjonstidspunkt](transaksjonstidspunkt.md) | Tidspunkt for registrering av transaksjonen |
| [url](url.md) | URL til eksternt dokument |
| [valuta](valuta.md) | Valuta for oppgjeve beløp |
| [vare](vare.md) | Vare i vareregisteret |
| [virksomhet](virksomhet.md) | Referanse til Virksomhet som er leverandør |


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
