

# Slot: enhetstype 


_Type digital eining._





URI: [res:enhetstype](https://schema.fintlabs.no/ressurs/enhetstype)
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
| Range | [Enhetstype](enhetstype.md) |
| Domain Of | [DigitalEnhet](digitalenhet.md), [Enhetsgruppe](enhetsgruppe.md) |
| Slot URI | [res:enhetstype](https://schema.fintlabs.no/ressurs/enhetstype) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:enhetstype |
| native | https://schema.fintlabs.no/ressurs/:enhetstype |




## LinkML Source

<details>
```yaml
name: enhetstype
description: Type digital eining.
from_schema: https://data.norge.no/fint/fint-ressurs
rank: 1000
slot_uri: res:enhetstype
domain_of:
- DigitalEnhet
- Enhetsgruppe
range: Enhetstype

```
</details>