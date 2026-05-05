

# Slot: merknadRegistrertAv 


_Person som registrerte merknaden._





URI: [ark:merknadRegistrertAv](https://schema.fintlabs.no/arkiv/merknadRegistrertAv)
Alias: merknadRegistrertAv

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Merknad](merknad.md) | Merknad knytt til mappe, registrering eller dokumentbeskrivelse |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Arkivressurs](arkivressurs.md) |
| Domain Of | [Merknad](merknad.md) |
| Slot URI | [ark:merknadRegistrertAv](https://schema.fintlabs.no/arkiv/merknadRegistrertAv) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Merknad](merknad.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:merknadRegistrertAv |
| native | https://schema.fintlabs.no/arkiv/:merknadRegistrertAv |




## LinkML Source

<details>
```yaml
name: merknadRegistrertAv
description: Person som registrerte merknaden.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:merknadRegistrertAv
alias: merknadRegistrertAv
owner: Merknad
domain_of:
- Merknad
range: Arkivressurs
required: true

```
</details>