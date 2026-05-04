

# Slot: kontostreng 


_Kontering av lønn._





URI: [adm:kontostreng](https://schema.fintlabs.no/administrasjon/kontostreng)
Alias: kontostreng

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
| Range | [Kontostreng](Kontostreng.md) |
| Domain Of | [Lonn](Lonn.md) |
| Slot URI | [adm:kontostreng](https://schema.fintlabs.no/administrasjon/kontostreng) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Lonn](Lonn.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:kontostreng |
| native | https://schema.fintlabs.no/administrasjon/:kontostreng |




## LinkML Source

<details>
```yaml
name: kontostreng
description: Kontering av lønn.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:kontostreng
alias: kontostreng
owner: Lonn
domain_of:
- Lonn
range: Kontostreng
required: true
inlined: true

```
</details>