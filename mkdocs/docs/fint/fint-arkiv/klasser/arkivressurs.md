

# Slot: arkivressurs 


_Arkivressursar._





URI: [ark:arkivressurs](https://schema.fintlabs.no/arkiv/arkivressurs)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Autorisasjon](autorisasjon.md) | Siling av kva ein innlogga brukar får lov til å gjere i løysinga |  yes  |
| [Tilgang](tilgang.md) | Styring av kven som har tilgang til kva opplysningar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Arkivressurs](arkivressurs.md) |
| Domain Of | [Autorisasjon](autorisasjon.md), [Tilgang](tilgang.md) |
| Slot URI | [ark:arkivressurs](https://schema.fintlabs.no/arkiv/arkivressurs) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:arkivressurs |
| native | https://schema.fintlabs.no/arkiv/:arkivressurs |




## LinkML Source

<details>
```yaml
name: arkivressurs
description: Arkivressursar.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:arkivressurs
domain_of:
- Autorisasjon
- Tilgang
range: Arkivressurs
multivalued: true

```
</details>