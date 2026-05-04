

# Slot: digitalEnhet 


_Den digitale eininga dette medlemskapet tilhøyrer._





URI: [res:digitalEnhet](https://schema.fintlabs.no/ressurs/digitalEnhet)
Alias: digitalEnhet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Enhetsgruppemedlemskap](Enhetsgruppemedlemskap.md) | Medlemskap mellom ei digital eining og ei einingsgruppe |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DigitalEnhet](DigitalEnhet.md) |
| Domain Of | [Enhetsgruppemedlemskap](Enhetsgruppemedlemskap.md) |
| Slot URI | [res:digitalEnhet](https://schema.fintlabs.no/ressurs/digitalEnhet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Enhetsgruppemedlemskap](Enhetsgruppemedlemskap.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:digitalEnhet |
| native | https://schema.fintlabs.no/ressurs/:digitalEnhet |




## LinkML Source

<details>
```yaml
name: digitalEnhet
description: Den digitale eininga dette medlemskapet tilhøyrer.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:digitalEnhet
alias: digitalEnhet
owner: Enhetsgruppemedlemskap
domain_of:
- Enhetsgruppemedlemskap
range: DigitalEnhet
required: true

```
</details>