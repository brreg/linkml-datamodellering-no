

# Slot: enhetsgruppemedlemskap 


_Einingsgruppemelemskap._





URI: [res:enhetsgruppemedlemskap](https://schema.fintlabs.no/ressurs/enhetsgruppemedlemskap)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DigitalEnhet](digitalenhet.md) | Ei digital eining som t |  yes  |
| [Enhetsgruppe](enhetsgruppe.md) | Ei gruppering av einsarta digitale einingar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Enhetsgruppemedlemskap](enhetsgruppemedlemskap.md) |
| Domain Of | [DigitalEnhet](digitalenhet.md), [Enhetsgruppe](enhetsgruppe.md) |
| Slot URI | [res:enhetsgruppemedlemskap](https://schema.fintlabs.no/ressurs/enhetsgruppemedlemskap) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:enhetsgruppemedlemskap |
| native | https://schema.fintlabs.no/ressurs/:enhetsgruppemedlemskap |




## LinkML Source

<details>
```yaml
name: enhetsgruppemedlemskap
description: Einingsgruppemelemskap.
from_schema: https://data.norge.no/fint/fint-ressurs
rank: 1000
slot_uri: res:enhetsgruppemedlemskap
domain_of:
- DigitalEnhet
- Enhetsgruppe
range: Enhetsgruppemedlemskap
multivalued: true

```
</details>