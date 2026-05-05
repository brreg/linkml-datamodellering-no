

# Slot: delegert 


_Angir om deltakinga er delegert._





URI: [utd:delegert](https://schema.fintlabs.no/utdanning/delegert)
Alias: delegert

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md) | Eit elevs deltaking i ei eksamensgruppe |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](boolean.md) |
| Domain Of | [Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md) |
| Slot URI | [utd:delegert](https://schema.fintlabs.no/utdanning/delegert) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:delegert |
| native | https://schema.fintlabs.no/utdanning/:delegert |




## LinkML Source

<details>
```yaml
name: delegert
description: Angir om deltakinga er delegert.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:delegert
alias: delegert
owner: Eksamensgruppemedlemskap
domain_of:
- Eksamensgruppemedlemskap
range: boolean

```
</details>