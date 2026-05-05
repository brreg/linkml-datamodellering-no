

# Slot: organisasjonsId 


_Unikt internnummer for organisasjonselementet._





URI: [adm:organisasjonsId](https://schema.fintlabs.no/administrasjon/organisasjonsId)
Alias: organisasjonsId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organisasjonselement](organisasjonselement.md) | Eit element i organisasjonsstrukturen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Organisasjonselement](organisasjonselement.md) |
| Slot URI | [adm:organisasjonsId](https://schema.fintlabs.no/administrasjon/organisasjonsId) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Organisasjonselement](organisasjonselement.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:organisasjonsId |
| native | https://schema.fintlabs.no/administrasjon/:organisasjonsId |




## LinkML Source

<details>
```yaml
name: organisasjonsId
description: Unikt internnummer for organisasjonselementet.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:organisasjonsId
alias: organisasjonsId
owner: Organisasjonselement
domain_of:
- Organisasjonselement
range: Identifikator
required: true
inlined: true

```
</details>