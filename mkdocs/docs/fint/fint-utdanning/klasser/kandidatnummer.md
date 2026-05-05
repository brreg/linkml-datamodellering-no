

# Slot: kandidatnummer 


_Kandidatnummer for eksamenen._





URI: [utd:kandidatnummer](https://schema.fintlabs.no/utdanning/kandidatnummer)
Alias: kandidatnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md) | Eit elevs deltaking i ei eksamensgruppe |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md) |
| Slot URI | [utd:kandidatnummer](https://schema.fintlabs.no/utdanning/kandidatnummer) |

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
| self | utd:kandidatnummer |
| native | https://schema.fintlabs.no/utdanning/:kandidatnummer |




## LinkML Source

<details>
```yaml
name: kandidatnummer
description: Kandidatnummer for eksamenen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:kandidatnummer
alias: kandidatnummer
owner: Eksamensgruppemedlemskap
domain_of:
- Eksamensgruppemedlemskap
range: string

```
</details>