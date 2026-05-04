

# Slot: rolle 


_Rolle tilknytt tilgangen._





URI: [ark:rolle](https://schema.fintlabs.no/arkiv/rolle)
Alias: rolle

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tilgang](Tilgang.md) | Styring av kven som har tilgang til kva opplysningar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Rolle](Rolle.md) |
| Domain Of | [Tilgang](Tilgang.md) |
| Slot URI | [ark:rolle](https://schema.fintlabs.no/arkiv/rolle) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Tilgang](Tilgang.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:rolle |
| native | https://schema.fintlabs.no/arkiv/:rolle |




## LinkML Source

<details>
```yaml
name: rolle
description: Rolle tilknytt tilgangen.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:rolle
alias: rolle
owner: Tilgang
domain_of:
- Tilgang
range: Rolle
required: true

```
</details>