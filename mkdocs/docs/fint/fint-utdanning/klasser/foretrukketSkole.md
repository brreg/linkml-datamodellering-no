

# Slot: foretrukketSkole 


_Angir om skulen er føretrekt for eksamenen._





URI: [utd:foretrukketSkole](https://schema.fintlabs.no/utdanning/foretrukketSkole)
Alias: foretrukketSkole

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eksamensgruppemedlemskap](Eksamensgruppemedlemskap.md) | Eit elevs deltaking i ei eksamensgruppe |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [Eksamensgruppemedlemskap](Eksamensgruppemedlemskap.md) |
| Slot URI | [utd:foretrukketSkole](https://schema.fintlabs.no/utdanning/foretrukketSkole) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Eksamensgruppemedlemskap](Eksamensgruppemedlemskap.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:foretrukketSkole |
| native | https://schema.fintlabs.no/utdanning/:foretrukketSkole |




## LinkML Source

<details>
```yaml
name: foretrukketSkole
description: Angir om skulen er føretrekt for eksamenen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:foretrukketSkole
alias: foretrukketSkole
owner: Eksamensgruppemedlemskap
domain_of:
- Eksamensgruppemedlemskap
range: boolean

```
</details>