

# Slot: fagmerknad 


_Merknad til faget for dette medlemskapet._





URI: [utd:fagmerknad](https://schema.fintlabs.no/utdanning/fagmerknad)
Alias: fagmerknad

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Faggruppemedlemskap](faggruppemedlemskap.md) | Eit elevs medlemskap i ei faggruppe |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fagmerknad](fagmerknad.md) |
| Domain Of | [Faggruppemedlemskap](faggruppemedlemskap.md) |
| Slot URI | [utd:fagmerknad](https://schema.fintlabs.no/utdanning/fagmerknad) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Faggruppemedlemskap](faggruppemedlemskap.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:fagmerknad |
| native | https://schema.fintlabs.no/utdanning/:fagmerknad |




## LinkML Source

<details>
```yaml
name: fagmerknad
description: Merknad til faget for dette medlemskapet.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:fagmerknad
alias: fagmerknad
owner: Faggruppemedlemskap
domain_of:
- Faggruppemedlemskap
range: Fagmerknad

```
</details>