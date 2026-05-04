

# Slot: delegertTil 


_Referanse til den deltakinga er delegert til._





URI: [utd:delegertTil](https://schema.fintlabs.no/utdanning/delegertTil)
Alias: delegertTil

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eksamensgruppemedlemskap](Eksamensgruppemedlemskap.md) | Eit elevs deltaking i ei eksamensgruppe |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Eksamensgruppemedlemskap](Eksamensgruppemedlemskap.md) |
| Slot URI | [utd:delegertTil](https://schema.fintlabs.no/utdanning/delegertTil) |

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
| self | utd:delegertTil |
| native | https://schema.fintlabs.no/utdanning/:delegertTil |




## LinkML Source

<details>
```yaml
name: delegertTil
description: Referanse til den deltakinga er delegert til.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:delegertTil
alias: delegertTil
owner: Eksamensgruppemedlemskap
domain_of:
- Eksamensgruppemedlemskap
range: uriorcurie

```
</details>