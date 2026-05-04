

# Slot: postering 


_Posteringar tilhøyrande transaksjonen._





URI: [okn:postering](https://schema.fintlabs.no/okonomi/postering)
Alias: postering

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Transaksjon](Transaksjon.md) | Overføring av pengar til eller frå eksterne partar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Postering](Postering.md) |
| Domain Of | [Transaksjon](Transaksjon.md) |
| Slot URI | [okn:postering](https://schema.fintlabs.no/okonomi/postering) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Transaksjon](Transaksjon.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:postering |
| native | https://schema.fintlabs.no/okonomi/:postering |




## LinkML Source

<details>
```yaml
name: postering
description: Posteringar tilhøyrande transaksjonen.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:postering
alias: postering
owner: Transaksjon
domain_of:
- Transaksjon
range: Postering
required: true
multivalued: true

```
</details>