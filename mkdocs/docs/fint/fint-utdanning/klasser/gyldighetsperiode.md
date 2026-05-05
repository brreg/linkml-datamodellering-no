

# Slot: gyldighetsperiode 



URI: [https://schema.fintlabs.no/utdanning/:gyldighetsperiode](https://schema.fintlabs.no/utdanning/:gyldighetsperiode)
Alias: gyldighetsperiode

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
| [Programomrademedlemskap](programomrademedlemskap.md) | Eit elevs tilknyting til eit programområde |  no  |
| [Bevistype](bevistype.md) | Type kompetansebevis for lærling |  no  |
| [Provestatus](provestatus.md) | Status for ei lærlingprøve |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Fagstatus](fagstatus.md) | Status for eit fag i eit faggruppemedlemskap |  no  |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Klassemedlemskap](klassemedlemskap.md) | Eit elevs medlemskap i ei klasse |  no  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Karakterskala](karakterskala.md) | Skala for karaktersetjing (t |  no  |
| [Skoleeiertype](skoleeiertype.md) | Type skuleeigartilknyting |  no  |
| [Betalingsstatus](betalingsstatus.md) | Betalingsstatus for eksamensavgift |  no  |
| [Identifikator](identifikator.md) | Unik identifikasjon til eit objekt |  no  |
| [Karakterverdi](karakterverdi.md) | Ein konkret karakterverdi i ei karakterskala |  no  |
| [Fagmerknad](fagmerknad.md) | Merknad knytt til eit fag i ei faggruppe |  no  |
| [Persongruppemedlemskap](persongruppemedlemskap.md) | Eit elevs medlemskap i ei persongruppe |  no  |
| [OtEnhet](otenhet.md) | Eining i oppfølgingstenesta (OT) |  no  |
| [Elevkategori](elevkategori.md) | Kategori for eit elevforhold (t |  no  |
| [Tilrettelegging](tilrettelegging.md) | Type tilrettelegging for elevar (t |  no  |
| [Faggruppemedlemskap](faggruppemedlemskap.md) | Eit elevs medlemskap i ei faggruppe |  no  |
| [Skoleaar](skoleaar.md) | Eit skoleår (t |  no  |
| [Termin](termin.md) | Ein skuleterm (t |  no  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md) | Eit elevs deltaking i ei eksamensgruppe |  no  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Undervisningsgruppemedlemskap](undervisningsgruppemedlemskap.md) | Eit elevs medlemskap i ei undervisningsgruppe |  no  |
| [Kontaktlaerergruppemedlemskap](kontaktlaerergruppemedlemskap.md) | Eit elevs medlemskap i ei kontaktlærargruppe |  no  |
| [Gruppemedlemskap](gruppemedlemskap.md) | Abstrakt basisklasse for gruppemedlemskapar i utdanning |  no  |
| [Avbruddsaarsak](avbruddsaarsak.md) | Årsak til avbrot frå opplæring |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Gruppemedlemskap](gruppemedlemskap.md), [Avbruddsaarsak](avbruddsaarsak.md), [Betalingsstatus](betalingsstatus.md), [Bevistype](bevistype.md), [Brevtype](brevtype.md), [Eksamensform](eksamensform.md), [Elevkategori](elevkategori.md), [Fagmerknad](fagmerknad.md), [Fagstatus](fagstatus.md), [Fravartype](fravartype.md), [Fullfortkode](fullfortkode.md), [Karakterskala](karakterskala.md), [Karakterstatus](karakterstatus.md), [Karakterverdi](karakterverdi.md), [OtEnhet](otenhet.md), [OtStatus](otstatus.md), [Provestatus](provestatus.md), [Skoleaar](skoleaar.md), [Skoleeiertype](skoleeiertype.md), [Termin](termin.md), [Tilrettelegging](tilrettelegging.md), [Varseltype](varseltype.md), [Vitnemalsmerknad](vitnemalsmerknad.md), [Begrep](begrep.md), [Identifikator](identifikator.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:gyldighetsperiode |
| native | https://schema.fintlabs.no/utdanning/:gyldighetsperiode |




## LinkML Source

<details>
```yaml
name: gyldighetsperiode
alias: gyldighetsperiode
domain_of:
- Gruppemedlemskap
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
- Identifikator
range: string

```
</details>