

# Slot: enhetsgruppe 


_Einingsgruppen dette medlemskapet tilhøyrer._





URI: [res:enhetsgruppe](https://schema.fintlabs.no/ressurs/enhetsgruppe)
Alias: enhetsgruppe

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Enhetsgruppemedlemskap](enhetsgruppemedlemskap.md) | Medlemskap mellom ei digital eining og ei einingsgruppe |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Enhetsgruppe](enhetsgruppe.md) |
| Domain Of | [Enhetsgruppemedlemskap](enhetsgruppemedlemskap.md) |
| Slot URI | [res:enhetsgruppe](https://schema.fintlabs.no/ressurs/enhetsgruppe) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Enhetsgruppemedlemskap](enhetsgruppemedlemskap.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:enhetsgruppe |
| native | https://schema.fintlabs.no/ressurs/:enhetsgruppe |




## LinkML Source

<details>
```yaml
name: enhetsgruppe
description: Einingsgruppen dette medlemskapet tilhøyrer.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:enhetsgruppe
alias: enhetsgruppe
owner: Enhetsgruppemedlemskap
domain_of:
- Enhetsgruppemedlemskap
range: Enhetsgruppe
required: true

```
</details>