

# Slot: attestert 


_Tidspunkt då lønn vart attestert._





URI: [adm:attestert](https://schema.fintlabs.no/administrasjon/attestert)
Alias: attestert

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Lonn](Lonn.md) | Informasjon om lønn for eit arbeidsforhold (abstrakt base) |  no  |
| [Fasttillegg](Fasttillegg.md) | Faste tillegg til utbetaling |  no  |
| [Variabellonn](Variabellonn.md) | Informasjon om variabel lønn |  no  |
| [Fastlonn](Fastlonn.md) | Informasjon om fast lønnsbeordring |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [Lonn](Lonn.md) |
| Slot URI | [adm:attestert](https://schema.fintlabs.no/administrasjon/attestert) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Lonn](Lonn.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:attestert |
| native | https://schema.fintlabs.no/administrasjon/:attestert |




## LinkML Source

<details>
```yaml
name: attestert
description: Tidspunkt då lønn vart attestert.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:attestert
alias: attestert
owner: Lonn
domain_of:
- Lonn
range: datetime

```
</details>