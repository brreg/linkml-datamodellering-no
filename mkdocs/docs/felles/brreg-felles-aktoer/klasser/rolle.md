

# Slot: rolle 


_Roller aktøren har._





URI: [brreg_felles_aktoer:rolle](https://data.norge.no/felles/brreg-felles-aktoer/rolle)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Aktoer](aktoer.md) | Ein aktør — person eller verksemd. Abstrakt basisklasse for Virksomhet og Person. |  no  |
| [Rolletypegruppe](rolletypegruppe.md) | Ei gruppering av rolletypar (t.d. "styre"). |  no  |
| [Virksomhet](virksomhet.md) | Ei verksemd registrert i Einingsregisteret. |  no  |
| [Person](person.md) | Ein fysisk person. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Rolle](rolle.md) |
| Domain Of | [Aktoer](aktoer.md), [Rolletypegruppe](rolletypegruppe.md) |
| Slot URI | [brreg_felles_aktoer:rolle](https://data.norge.no/felles/brreg-felles-aktoer/rolle) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/felles/brreg-felles-aktoer




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brreg_felles_aktoer:rolle |
| native | https://data.norge.no/felles/brreg-felles-aktoer/rolle |




## LinkML Source

<details>
```yaml
name: rolle
description: Roller aktøren har.
from_schema: https://data.norge.no/felles/brreg-felles-aktoer
slot_uri: brreg_felles_aktoer:rolle
domain_of:
- Aktoer
- Rolletypegruppe
range: Rolle
multivalued: true

```
</details>