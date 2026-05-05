

# Slot: persongruppe 


_Persongruppa dette medlemskapet er i._





URI: [utd:persongruppe](https://schema.fintlabs.no/utdanning/persongruppe)
Alias: persongruppe

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Persongruppemedlemskap](persongruppemedlemskap.md) | Eit elevs medlemskap i ei persongruppe |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Persongruppe](persongruppe.md) |
| Domain Of | [Persongruppemedlemskap](persongruppemedlemskap.md) |
| Slot URI | [utd:persongruppe](https://schema.fintlabs.no/utdanning/persongruppe) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Persongruppemedlemskap](persongruppemedlemskap.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:persongruppe |
| native | https://schema.fintlabs.no/utdanning/:persongruppe |




## LinkML Source

<details>
```yaml
name: persongruppe
description: Persongruppa dette medlemskapet er i.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:persongruppe
alias: persongruppe
owner: Persongruppemedlemskap
domain_of:
- Persongruppemedlemskap
range: Persongruppe

```
</details>