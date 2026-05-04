

# Slot: autorisasjon 


_Autorisasjonar gjevne til arkivressursen._





URI: [ark:autorisasjon](https://schema.fintlabs.no/arkiv/autorisasjon)
Alias: autorisasjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arkivressurs](Arkivressurs.md) | Ansatt med rolle og rettar innanfor arkiv |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Autorisasjon](Autorisasjon.md) |
| Domain Of | [Arkivressurs](Arkivressurs.md) |
| Slot URI | [ark:autorisasjon](https://schema.fintlabs.no/arkiv/autorisasjon) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
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
| self | ark:autorisasjon |
| native | https://schema.fintlabs.no/arkiv/:autorisasjon |




## LinkML Source

<details>
```yaml
name: autorisasjon
description: Autorisasjonar gjevne til arkivressursen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:autorisasjon
alias: autorisasjon
owner: Arkivressurs
domain_of:
- Arkivressurs
range: Autorisasjon
multivalued: true

```
</details>