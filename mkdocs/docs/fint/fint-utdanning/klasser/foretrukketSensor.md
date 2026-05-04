

# Slot: foretrukketSensor 


_Angir om sensor er føretrekt._





URI: [utd:foretrukketSensor](https://schema.fintlabs.no/utdanning/foretrukketSensor)
Alias: foretrukketSensor

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
| Slot URI | [utd:foretrukketSensor](https://schema.fintlabs.no/utdanning/foretrukketSensor) |

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
| self | utd:foretrukketSensor |
| native | https://schema.fintlabs.no/utdanning/:foretrukketSensor |




## LinkML Source

<details>
```yaml
name: foretrukketSensor
description: Angir om sensor er føretrekt.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:foretrukketSensor
alias: foretrukketSensor
owner: Eksamensgruppemedlemskap
domain_of:
- Eksamensgruppemedlemskap
range: boolean

```
</details>