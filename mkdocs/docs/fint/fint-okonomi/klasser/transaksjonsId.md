

# Slot: transaksjonsId 


_Intern unik identifikator i økonomisystemet._





URI: [okn:transaksjonsId](https://schema.fintlabs.no/okonomi/transaksjonsId)
Alias: transaksjonsId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Transaksjon](Transaksjon.md) | Overføring av pengar til eller frå eksterne partar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](Identifikator.md) |
| Domain Of | [Transaksjon](Transaksjon.md) |
| Slot URI | [okn:transaksjonsId](https://schema.fintlabs.no/okonomi/transaksjonsId) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
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
| self | okn:transaksjonsId |
| native | https://schema.fintlabs.no/okonomi/:transaksjonsId |




## LinkML Source

<details>
```yaml
name: transaksjonsId
description: Intern unik identifikator i økonomisystemet.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:transaksjonsId
alias: transaksjonsId
owner: Transaksjon
domain_of:
- Transaksjon
range: Identifikator
required: true
inlined: true

```
</details>