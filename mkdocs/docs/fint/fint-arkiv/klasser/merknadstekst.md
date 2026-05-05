

# Slot: merknadstekst 


_Merknad frå saksbehandlar, leiar eller arkivpersonale._





URI: [ark:merknadstekst](https://schema.fintlabs.no/arkiv/merknadstekst)
Alias: merknadstekst

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Merknad](merknad.md) | Merknad knytt til mappe, registrering eller dokumentbeskrivelse |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Merknad](merknad.md) |
| Slot URI | [ark:merknadstekst](https://schema.fintlabs.no/arkiv/merknadstekst) |

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
| self | ark:merknadstekst |
| native | https://schema.fintlabs.no/arkiv/:merknadstekst |




## LinkML Source

<details>
```yaml
name: merknadstekst
description: Merknad frå saksbehandlar, leiar eller arkivpersonale.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:merknadstekst
alias: merknadstekst
owner: Merknad
domain_of:
- Merknad
range: string
required: true

```
</details>