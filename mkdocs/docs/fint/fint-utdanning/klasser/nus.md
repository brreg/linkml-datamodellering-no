

# Slot: nus 


_NUS-kode knytt til eksamensgruppemedlemskapet._





URI: [utd:nus](https://schema.fintlabs.no/utdanning/nus)
Alias: nus

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md) | Eit elevs deltaking i ei eksamensgruppe |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Karakterstatus](karakterstatus.md) |
| Domain Of | [Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md) |
| Slot URI | [utd:nus](https://schema.fintlabs.no/utdanning/nus) |

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
| self | utd:nus |
| native | https://schema.fintlabs.no/utdanning/:nus |




## LinkML Source

<details>
```yaml
name: nus
description: NUS-kode knytt til eksamensgruppemedlemskapet.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:nus
alias: nus
owner: Eksamensgruppemedlemskap
domain_of:
- Eksamensgruppemedlemskap
range: Karakterstatus

```
</details>