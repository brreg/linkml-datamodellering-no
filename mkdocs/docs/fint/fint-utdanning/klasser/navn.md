

# Slot: navn 


_Hovudnamn for ressursen._





URI: [fint:navn](https://schema.fintlabs.no/navn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  yes  |
| [Gruppe](gruppe.md) | Abstrakt basisklasse for alle gruppetypar i utdanning |  yes  |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  yes  |
| [Eksamen](eksamen.md) | Ein eksamen knytt til ei eksamensgruppe |  yes  |
| [Rom](rom.md) | Eit rom eller lokale ved ein skule |  yes  |
| [Time](time.md) | Ein time i timeplanen |  yes  |
| [Avbruddsaarsak](avbruddsaarsak.md) | Årsak til avbrot frå opplæring |  yes  |
| [Betalingsstatus](betalingsstatus.md) | Betalingsstatus for eksamensavgift |  yes  |
| [Bevistype](bevistype.md) | Type kompetansebevis for lærling |  yes  |
| [Brevtype](brevtype.md) | Type brev knytt til lærlingprøve |  yes  |
| [Eksamensform](eksamensform.md) | Form for gjennomføring av eksamen |  yes  |
| [Elevkategori](elevkategori.md) | Kategori for eit elevforhold (t |  yes  |
| [Fagmerknad](fagmerknad.md) | Merknad knytt til eit fag i ei faggruppe |  yes  |
| [Fagstatus](fagstatus.md) | Status for eit fag i eit faggruppemedlemskap |  yes  |
| [Fravartype](fravartype.md) | Type fråvær (t |  yes  |
| [Fullfortkode](fullfortkode.md) | Kode for fullførtresultat av lærling |  yes  |
| [Karakterskala](karakterskala.md) | Skala for karaktersetjing (t |  yes  |
| [Karakterstatus](karakterstatus.md) | Status for ein karakter (t |  yes  |
| [Karakterverdi](karakterverdi.md) | Ein konkret karakterverdi i ei karakterskala |  yes  |
| [OtEnhet](otenhet.md) | Eining i oppfølgingstenesta (OT) |  yes  |
| [OtStatus](otstatus.md) | Status for ein ungdom i oppfølgingstenesta |  yes  |
| [Provestatus](provestatus.md) | Status for ei lærlingprøve |  yes  |
| [Skoleaar](skoleaar.md) | Eit skoleår (t |  yes  |
| [Skoleeiertype](skoleeiertype.md) | Type skuleeigartilknyting |  yes  |
| [Termin](termin.md) | Ein skuleterm (t |  yes  |
| [Tilrettelegging](tilrettelegging.md) | Type tilrettelegging for elevar (t |  yes  |
| [Varseltype](varseltype.md) | Type varsel knytt til ein elev |  yes  |
| [Vitnemalsmerknad](vitnemalsmerknad.md) | Merknad på vitnemål |  yes  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Klasse](klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |  no  |
| [Kontaktlaerergruppe](kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |  no  |
| [Persongruppe](persongruppe.md) | Ei gruppe elevar definert for personlege føremål |  no  |
| [Arstrinn](arstrinn.md) | Eit årstrinn i skulen (t |  no  |
| [Programomrade](programomrade.md) | Eit programområde innanfor eit utdanningsprogram (t |  no  |
| [Utdanningsprogram](utdanningsprogram.md) | Eit utdanningsprogram (t |  no  |
| [Fag](fag.md) | Eit skulefag |  no  |
| [Faggruppe](faggruppe.md) | Ei gruppe elevar knytt til eit fag på ein skule |  no  |
| [Undervisningsgruppe](undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |  no  |
| [Eksamensgruppe](eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Begrep](begrep.md), [Gruppe](gruppe.md), [Skole](skole.md), [Eksamen](eksamen.md), [Rom](rom.md), [Time](time.md), [Avbruddsaarsak](avbruddsaarsak.md), [Betalingsstatus](betalingsstatus.md), [Bevistype](bevistype.md), [Brevtype](brevtype.md), [Eksamensform](eksamensform.md), [Elevkategori](elevkategori.md), [Fagmerknad](fagmerknad.md), [Fagstatus](fagstatus.md), [Fravartype](fravartype.md), [Fullfortkode](fullfortkode.md), [Karakterskala](karakterskala.md), [Karakterstatus](karakterstatus.md), [Karakterverdi](karakterverdi.md), [OtEnhet](otenhet.md), [OtStatus](otstatus.md), [Provestatus](provestatus.md), [Skoleaar](skoleaar.md), [Skoleeiertype](skoleeiertype.md), [Termin](termin.md), [Tilrettelegging](tilrettelegging.md), [Varseltype](varseltype.md), [Vitnemalsmerknad](vitnemalsmerknad.md) |
| Slot URI | [fint:navn](https://schema.fintlabs.no/navn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:navn |
| native | https://schema.fintlabs.no/:navn |




## LinkML Source

<details>
```yaml
name: navn
description: Hovudnamn for ressursen.
from_schema: https://data.norge.no/fint/fint-common
slot_uri: fint:navn
domain_of:
- Begrep
- Gruppe
- Skole
- Eksamen
- Rom
- Time
- Avbruddsaarsak
- Betalingsstatus
- Bevistype
- Brevtype
- Eksamensform
- Elevkategori
- Fagmerknad
- Fagstatus
- Fravartype
- Fullfortkode
- Karakterskala
- Karakterstatus
- Karakterverdi
- OtEnhet
- OtStatus
- Provestatus
- Skoleaar
- Skoleeiertype
- Termin
- Tilrettelegging
- Varseltype
- Vitnemalsmerknad
range: string

```
</details>