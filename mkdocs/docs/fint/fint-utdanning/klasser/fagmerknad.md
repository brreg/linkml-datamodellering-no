

# Slot: fagmerknad 


_Merknad til faget._





URI: [utd:fagmerknad](https://schema.fintlabs.no/utdanning/fagmerknad)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Faggruppemedlemskap](faggruppemedlemskap.md) | Eit elevs medlemskap i ei faggruppe |  yes  |






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










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:fagmerknad |
| native | https://schema.fintlabs.no/utdanning/:fagmerknad |




## LinkML Source

<details>
```yaml
name: fagmerknad
description: Merknad til faget.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:fagmerknad
domain_of:
- Faggruppemedlemskap
range: Fagmerknad

```
</details>