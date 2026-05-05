

# Slot: merknadsdato 


_Dato og klokkeslett merknaden vart registrert._





URI: [ark:merknadsdato](https://schema.fintlabs.no/arkiv/merknadsdato)
Alias: merknadsdato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Merknad](merknad.md) | Merknad knytt til mappe, registrering eller dokumentbeskrivelse |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](datetime.md) |
| Domain Of | [Merknad](merknad.md) |
| Slot URI | [ark:merknadsdato](https://schema.fintlabs.no/arkiv/merknadsdato) |

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
| self | ark:merknadsdato |
| native | https://schema.fintlabs.no/arkiv/:merknadsdato |




## LinkML Source

<details>
```yaml
name: merknadsdato
description: Dato og klokkeslett merknaden vart registrert.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:merknadsdato
alias: merknadsdato
owner: Merknad
domain_of:
- Merknad
range: datetime
required: true

```
</details>