

# Slot: tilgang 


_Tilgangar gjevne til arkivressursen._





URI: [ark:tilgang](https://schema.fintlabs.no/arkiv/tilgang)
Alias: tilgang

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arkivressurs](arkivressurs.md) | Ansatt med rolle og rettar innanfor arkiv |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Tilgang](tilgang.md) |
| Domain Of | [Arkivressurs](arkivressurs.md) |
| Slot URI | [ark:tilgang](https://schema.fintlabs.no/arkiv/tilgang) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Arkivressurs](arkivressurs.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:tilgang |
| native | https://schema.fintlabs.no/arkiv/:tilgang |




## LinkML Source

<details>
```yaml
name: tilgang
description: Tilgangar gjevne til arkivressursen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:tilgang
alias: tilgang
owner: Arkivressurs
domain_of:
- Arkivressurs
range: Tilgang
multivalued: true

```
</details>