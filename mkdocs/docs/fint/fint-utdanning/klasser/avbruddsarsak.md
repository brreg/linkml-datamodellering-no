

# Slot: avbruddsarsak 


_Årsak til avbrot frå opplæring._





URI: [utd:avbruddsarsak](https://schema.fintlabs.no/utdanning/avbruddsarsak)
Alias: avbruddsarsak

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Avbruddsaarsak](avbruddsaarsak.md) |
| Domain Of | [Elevforhold](elevforhold.md) |
| Slot URI | [utd:avbruddsarsak](https://schema.fintlabs.no/utdanning/avbruddsarsak) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Elevforhold](elevforhold.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:avbruddsarsak |
| native | https://schema.fintlabs.no/utdanning/:avbruddsarsak |




## LinkML Source

<details>
```yaml
name: avbruddsarsak
description: Årsak til avbrot frå opplæring.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:avbruddsarsak
alias: avbruddsarsak
owner: Elevforhold
domain_of:
- Elevforhold
range: Avbruddsaarsak

```
</details>