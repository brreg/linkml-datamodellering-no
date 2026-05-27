

# Slot: persongruppe 


_Persongruppe._





URI: [utd:persongruppe](https://schema.fintlabs.no/utdanning/persongruppe)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Persongruppemedlemskap](persongruppemedlemskap.md) | Eit elevs medlemskap i ei persongruppe |  yes  |






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










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:persongruppe |
| native | https://schema.fintlabs.no/utdanning/:persongruppe |




## LinkML Source

<details>
```yaml
name: persongruppe
description: Persongruppe.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:persongruppe
domain_of:
- Persongruppemedlemskap
range: Persongruppe

```
</details>