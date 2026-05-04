

# Slot: skala 


_Karakterskalaen denne verdien tilhøyrer._





URI: [utd:skala](https://schema.fintlabs.no/utdanning/skala)
Alias: skala

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Karakterverdi](Karakterverdi.md) | Ein konkret karakterverdi i ei karakterskala |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Karakterskala](Karakterskala.md) |
| Domain Of | [Karakterverdi](Karakterverdi.md) |
| Slot URI | [utd:skala](https://schema.fintlabs.no/utdanning/skala) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Karakterverdi](Karakterverdi.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:skala |
| native | https://schema.fintlabs.no/utdanning/:skala |




## LinkML Source

<details>
```yaml
name: skala
description: Karakterskalaen denne verdien tilhøyrer.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:skala
alias: skala
owner: Karakterverdi
domain_of:
- Karakterverdi
range: Karakterskala
required: true

```
</details>