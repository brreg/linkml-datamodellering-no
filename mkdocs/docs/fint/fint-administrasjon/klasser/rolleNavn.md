

# Slot: rolleNavn 


_Namn på rolla; unik identifikator._





URI: [adm:rolleNavn](https://schema.fintlabs.no/administrasjon/rolleNavn)
Alias: rolleNavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Rolle](rolle.md) | Rettighet eller type fullmakt |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Rolle](rolle.md) |
| Slot URI | [adm:rolleNavn](https://schema.fintlabs.no/administrasjon/rolleNavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Rolle](rolle.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:rolleNavn |
| native | https://schema.fintlabs.no/administrasjon/:rolleNavn |




## LinkML Source

<details>
```yaml
name: rolleNavn
description: Namn på rolla; unik identifikator.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:rolleNavn
alias: rolleNavn
owner: Rolle
domain_of:
- Rolle
range: Identifikator
required: true
inlined: true

```
</details>