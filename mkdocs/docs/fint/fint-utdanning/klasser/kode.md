

# Slot: kode 



URI: [https://schema.fintlabs.no/utdanning/:kode](https://schema.fintlabs.no/utdanning/:kode)
Alias: kode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Vitnemalsmerknad](vitnemalsmerknad.md) | Merknad på vitnemål |  no  |
| [Varseltype](varseltype.md) | Type varsel knytt til ein elev |  no  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Brevtype](brevtype.md) | Type brev knytt til lærlingprøve |  no  |
| [Karakterstatus](karakterstatus.md) | Status for ein karakter (t |  no  |
| [Fullfortkode](fullfortkode.md) | Kode for fullførtresultat av lærling |  no  |
| [OtStatus](otstatus.md) | Status for ein ungdom i oppfølgingstenesta |  no  |
| [Eksamensform](eksamensform.md) | Form for gjennomføring av eksamen |  no  |
| [Fravartype](fravartype.md) | Type fråvær (t |  no  |
| [Bevistype](bevistype.md) | Type kompetansebevis for lærling |  no  |
| [Provestatus](provestatus.md) | Status for ei lærlingprøve |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Fagstatus](fagstatus.md) | Status for eit fag i eit faggruppemedlemskap |  no  |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Karakterskala](karakterskala.md) | Skala for karaktersetjing (t |  no  |
| [Skoleeiertype](skoleeiertype.md) | Type skuleeigartilknyting |  no  |
| [Betalingsstatus](betalingsstatus.md) | Betalingsstatus for eksamensavgift |  no  |
| [Karakterverdi](karakterverdi.md) | Ein konkret karakterverdi i ei karakterskala |  no  |
| [Fagmerknad](fagmerknad.md) | Merknad knytt til eit fag i ei faggruppe |  no  |
| [OtEnhet](otenhet.md) | Eining i oppfølgingstenesta (OT) |  no  |
| [Elevkategori](elevkategori.md) | Kategori for eit elevforhold (t |  no  |
| [Tilrettelegging](tilrettelegging.md) | Type tilrettelegging for elevar (t |  no  |
| [Termin](termin.md) | Ein skuleterm (t |  no  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Skoleaar](skoleaar.md) | Eit skoleår (t |  no  |
| [Avbruddsaarsak](avbruddsaarsak.md) | Årsak til avbrot frå opplæring |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Avbruddsaarsak](avbruddsaarsak.md), [Betalingsstatus](betalingsstatus.md), [Bevistype](bevistype.md), [Brevtype](brevtype.md), [Eksamensform](eksamensform.md), [Elevkategori](elevkategori.md), [Fagmerknad](fagmerknad.md), [Fagstatus](fagstatus.md), [Fravartype](fravartype.md), [Fullfortkode](fullfortkode.md), [Karakterskala](karakterskala.md), [Karakterstatus](karakterstatus.md), [Karakterverdi](karakterverdi.md), [OtEnhet](otenhet.md), [OtStatus](otstatus.md), [Provestatus](provestatus.md), [Skoleaar](skoleaar.md), [Skoleeiertype](skoleeiertype.md), [Termin](termin.md), [Tilrettelegging](tilrettelegging.md), [Varseltype](varseltype.md), [Vitnemalsmerknad](vitnemalsmerknad.md), [Begrep](begrep.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:kode |
| native | https://schema.fintlabs.no/utdanning/:kode |




## LinkML Source

<details>
```yaml
name: kode
alias: kode
domain_of:
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
- Begrep
range: string

```
</details>