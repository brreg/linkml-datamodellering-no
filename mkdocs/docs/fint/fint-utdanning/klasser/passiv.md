

# Slot: passiv 



URI: [https://schema.fintlabs.no/utdanning/:passiv](https://schema.fintlabs.no/utdanning/:passiv)
Alias: passiv

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Begrep](Begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Landkode](Landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Tilrettelegging](Tilrettelegging.md) | Type tilrettelegging for elevar (t |  no  |
| [Fagstatus](Fagstatus.md) | Status for eit fag i eit faggruppemedlemskap |  no  |
| [Provestatus](Provestatus.md) | Status for ei lærlingprøve |  no  |
| [OtStatus](OtStatus.md) | Status for ein ungdom i oppfølgingstenesta |  no  |
| [OtEnhet](OtEnhet.md) | Eining i oppfølgingstenesta (OT) |  no  |
| [Karakterskala](Karakterskala.md) | Skala for karaktersetjing (t |  no  |
| [Betalingsstatus](Betalingsstatus.md) | Betalingsstatus for eksamensavgift |  no  |
| [Karakterstatus](Karakterstatus.md) | Status for ein karakter (t |  no  |
| [Vitnemalsmerknad](Vitnemalsmerknad.md) | Merknad på vitnemål |  no  |
| [Termin](Termin.md) | Ein skuleterm (t |  no  |
| [Brevtype](Brevtype.md) | Type brev knytt til lærlingprøve |  no  |
| [Avbruddsaarsak](Avbruddsaarsak.md) | Årsak til avbrot frå opplæring |  no  |
| [Karakterverdi](Karakterverdi.md) | Ein konkret karakterverdi i ei karakterskala |  no  |
| [Elevkategori](Elevkategori.md) | Kategori for eit elevforhold (t |  no  |
| [Fravartype](Fravartype.md) | Type fråvær (t |  no  |
| [Bevistype](Bevistype.md) | Type kompetansebevis for lærling |  no  |
| [Fagmerknad](Fagmerknad.md) | Merknad knytt til eit fag i ei faggruppe |  no  |
| [Kjonn](Kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Skoleaar](Skoleaar.md) | Eit skoleår (t |  no  |
| [Spraak](Spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Fylke](Fylke.md) | Liste over Norges fylker |  no  |
| [Skoleeiertype](Skoleeiertype.md) | Type skuleeigartilknyting |  no  |
| [Fullfortkode](Fullfortkode.md) | Kode for fullførtresultat av lærling |  no  |
| [Eksamensform](Eksamensform.md) | Form for gjennomføring av eksamen |  no  |
| [Kommune](Kommune.md) | Liste over Norges kommunar |  no  |
| [Varseltype](Varseltype.md) | Type varsel knytt til ein elev |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Avbruddsaarsak](Avbruddsaarsak.md), [Betalingsstatus](Betalingsstatus.md), [Bevistype](Bevistype.md), [Brevtype](Brevtype.md), [Eksamensform](Eksamensform.md), [Elevkategori](Elevkategori.md), [Fagmerknad](Fagmerknad.md), [Fagstatus](Fagstatus.md), [Fravartype](Fravartype.md), [Fullfortkode](Fullfortkode.md), [Karakterskala](Karakterskala.md), [Karakterstatus](Karakterstatus.md), [Karakterverdi](Karakterverdi.md), [OtEnhet](OtEnhet.md), [OtStatus](OtStatus.md), [Provestatus](Provestatus.md), [Skoleaar](Skoleaar.md), [Skoleeiertype](Skoleeiertype.md), [Termin](Termin.md), [Tilrettelegging](Tilrettelegging.md), [Varseltype](Varseltype.md), [Vitnemalsmerknad](Vitnemalsmerknad.md), [Begrep](Begrep.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:passiv |
| native | https://schema.fintlabs.no/utdanning/:passiv |




## LinkML Source

<details>
```yaml
name: passiv
alias: passiv
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