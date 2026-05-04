

# Slot: kildesystemId 


_Kildesystemets identifikator for arkivressursen._





URI: [ark:kildesystemId](https://schema.fintlabs.no/arkiv/kildesystemId)
Alias: kildesystemId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arkivressurs](Arkivressurs.md) | Ansatt med rolle og rettar innanfor arkiv |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](Identifikator.md) |
| Domain Of | [Arkivressurs](Arkivressurs.md) |
| Slot URI | [ark:kildesystemId](https://schema.fintlabs.no/arkiv/kildesystemId) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Arkivressurs](Arkivressurs.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:kildesystemId |
| native | https://schema.fintlabs.no/arkiv/:kildesystemId |




## LinkML Source

<details>
```yaml
name: kildesystemId
description: Kildesystemets identifikator for arkivressursen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:kildesystemId
alias: kildesystemId
owner: Arkivressurs
domain_of:
- Arkivressurs
range: Identifikator
inlined: true

```
</details>