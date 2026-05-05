

# Slot: anvist 


_Tidspunkt då lønn vart anvist._





URI: [adm:anvist](https://schema.fintlabs.no/administrasjon/anvist)
Alias: anvist

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Lonn](lonn.md) | Informasjon om lønn for eit arbeidsforhold (abstrakt base) |  no  |
| [Variabellonn](variabellonn.md) | Informasjon om variabel lønn |  no  |
| [Fastlonn](fastlonn.md) | Informasjon om fast lønnsbeordring |  no  |
| [Fasttillegg](fasttillegg.md) | Faste tillegg til utbetaling |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](datetime.md) |
| Domain Of | [Lonn](lonn.md) |
| Slot URI | [adm:anvist](https://schema.fintlabs.no/administrasjon/anvist) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Lonn](lonn.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:anvist |
| native | https://schema.fintlabs.no/administrasjon/:anvist |




## LinkML Source

<details>
```yaml
name: anvist
description: Tidspunkt då lønn vart anvist.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:anvist
alias: anvist
owner: Lonn
domain_of:
- Lonn
range: datetime

```
</details>