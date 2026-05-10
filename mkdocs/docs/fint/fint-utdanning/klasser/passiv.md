

# Slot: passiv 


_Angir at koden er passiv og ikkje kan veljast._





URI: [fint:passiv](https://schema.fintlabs.no/passiv)
Alias: passiv

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  yes  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [OtEnhet](otenhet.md) | Eining i oppfølgingstenesta (OT) |  yes  |
| [Brevtype](brevtype.md) | Type brev knytt til lærlingprøve |  yes  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Fullfortkode](fullfortkode.md) | Kode for fullførtresultat av lærling |  yes  |
| [Fagstatus](fagstatus.md) | Status for eit fag i eit faggruppemedlemskap |  yes  |
| [Termin](termin.md) | Ein skuleterm (t |  yes  |
| [Varseltype](varseltype.md) | Type varsel knytt til ein elev |  yes  |
| [Karakterskala](karakterskala.md) | Skala for karaktersetjing (t |  yes  |
| [Karakterstatus](karakterstatus.md) | Status for ein karakter (t |  yes  |
| [Karakterverdi](karakterverdi.md) | Ein konkret karakterverdi i ei karakterskala |  yes  |
| [OtStatus](otstatus.md) | Status for ein ungdom i oppfølgingstenesta |  yes  |
| [Tilrettelegging](tilrettelegging.md) | Type tilrettelegging for elevar (t |  yes  |
| [Elevkategori](elevkategori.md) | Kategori for eit elevforhold (t |  yes  |
| [Skoleaar](skoleaar.md) | Eit skoleår (t |  yes  |
| [Fravartype](fravartype.md) | Type fråvær (t |  yes  |
| [Vitnemalsmerknad](vitnemalsmerknad.md) | Merknad på vitnemål |  yes  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Eksamensform](eksamensform.md) | Form for gjennomføring av eksamen |  yes  |
| [Bevistype](bevistype.md) | Type kompetansebevis for lærling |  yes  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Betalingsstatus](betalingsstatus.md) | Betalingsstatus for eksamensavgift |  yes  |
| [Skoleeiertype](skoleeiertype.md) | Type skuleeigartilknyting |  yes  |
| [Fagmerknad](fagmerknad.md) | Merknad knytt til eit fag i ei faggruppe |  yes  |
| [Provestatus](provestatus.md) | Status for ei lærlingprøve |  yes  |
| [Avbruddsaarsak](avbruddsaarsak.md) | Årsak til avbrot frå opplæring |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) |
| Domain Of | [Begrep](begrep.md), [Avbruddsaarsak](avbruddsaarsak.md), [Betalingsstatus](betalingsstatus.md), [Bevistype](bevistype.md), [Brevtype](brevtype.md), [Eksamensform](eksamensform.md), [Elevkategori](elevkategori.md), [Fagmerknad](fagmerknad.md), [Fagstatus](fagstatus.md), [Fravartype](fravartype.md), [Fullfortkode](fullfortkode.md), [Karakterskala](karakterskala.md), [Karakterstatus](karakterstatus.md), [Karakterverdi](karakterverdi.md), [OtEnhet](otenhet.md), [OtStatus](otstatus.md), [Provestatus](provestatus.md), [Skoleaar](skoleaar.md), [Skoleeiertype](skoleeiertype.md), [Termin](termin.md), [Tilrettelegging](tilrettelegging.md), [Varseltype](varseltype.md), [Vitnemalsmerknad](vitnemalsmerknad.md) |
| Slot URI | [fint:passiv](https://schema.fintlabs.no/passiv) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:passiv |
| native | https://schema.fintlabs.no/:passiv |




## LinkML Source

<details>
```yaml
name: passiv
description: Angir at koden er passiv og ikkje kan veljast.
from_schema: https://data.norge.no/linkml/fint-common
slot_uri: fint:passiv
alias: passiv
domain_of:
- Begrep
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
range: boolean

```
</details>