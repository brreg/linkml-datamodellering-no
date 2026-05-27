

# Slot: undervisningsgruppe 


_Undervisningsgruppe._





URI: [utd:undervisningsgruppe](https://schema.fintlabs.no/utdanning/undervisningsgruppe)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fag](fag.md) | Eit skulefag |  yes  |
| [Time](time.md) | Ein time i timeplanen |  yes  |
| [Undervisningsgruppemedlemskap](undervisningsgruppemedlemskap.md) | Eit elevs medlemskap i ei undervisningsgruppe |  yes  |
| [Fraversregistrering](fraversregistrering.md) | Ei enkelt fråversregistrering for ein elev |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Undervisningsgruppe](undervisningsgruppe.md) |
| Domain Of | [Fag](fag.md), [Time](time.md), [Undervisningsgruppemedlemskap](undervisningsgruppemedlemskap.md), [Fraversregistrering](fraversregistrering.md) |
| Slot URI | [utd:undervisningsgruppe](https://schema.fintlabs.no/utdanning/undervisningsgruppe) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:undervisningsgruppe |
| native | https://schema.fintlabs.no/utdanning/:undervisningsgruppe |




## LinkML Source

<details>
```yaml
name: undervisningsgruppe
description: Undervisningsgruppe.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:undervisningsgruppe
domain_of:
- Fag
- Time
- Undervisningsgruppemedlemskap
- Fraversregistrering
range: Undervisningsgruppe

```
</details>