

# Slot: relasjon 


_Relasjonar aktøren har til andre aktørar._





URI: [brreg_felles_aktoer:relasjon](https://data.norge.no/felles/brreg-felles-aktoer/relasjon)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Aktoer](aktoer.md) | Ein aktør — person eller verksemd. Abstrakt basisklasse for Virksomhet og Person. |  no  |
| [Virksomhet](virksomhet.md) | Ei verksemd registrert i Einingsregisteret. |  no  |
| [Person](person.md) | Ein fysisk person. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Relasjon](relasjon.md) |
| Domain Of | [Aktoer](aktoer.md) |
| Slot URI | [brreg_felles_aktoer:relasjon](https://data.norge.no/felles/brreg-felles-aktoer/relasjon) |

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
| self | brreg_felles_aktoer:relasjon |
| native | https://data.norge.no/felles/brreg-felles-aktoer/relasjon |




## LinkML Source

<details>
```yaml
name: relasjon
description: Relasjonar aktøren har til andre aktørar.
from_schema: https://data.norge.no/felles/brreg-felles-aktoer
slot_uri: brreg_felles_aktoer:relasjon
domain_of:
- Aktoer
range: Relasjon
multivalued: true

```
</details>