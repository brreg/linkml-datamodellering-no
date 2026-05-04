

# Slot: merknadstype 


_Type merknad._





URI: [ark:merknadstype](https://schema.fintlabs.no/arkiv/merknadstype)
Alias: merknadstype

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Merknad](Merknad.md) | Merknad knytt til mappe, registrering eller dokumentbeskrivelse |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Merknadstype](Merknadstype.md) |
| Domain Of | [Merknad](Merknad.md) |
| Slot URI | [ark:merknadstype](https://schema.fintlabs.no/arkiv/merknadstype) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Merknad](Merknad.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:merknadstype |
| native | https://schema.fintlabs.no/arkiv/:merknadstype |




## LinkML Source

<details>
```yaml
name: merknadstype
description: Type merknad.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:merknadstype
alias: merknadstype
owner: Merknad
domain_of:
- Merknad
range: Merknadstype
required: true

```
</details>