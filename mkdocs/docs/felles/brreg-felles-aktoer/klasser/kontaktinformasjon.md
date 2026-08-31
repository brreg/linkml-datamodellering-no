

# Slot: kontaktinformasjon 


_Kontaktinformasjon for aktøren/rolla._





URI: [brreg_felles_aktoer:kontaktinformasjon](https://data.norge.no/felles/brreg-felles-aktoer/kontaktinformasjon)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Aktoer](aktoer.md) | Ein aktør — person eller verksemd. Abstrakt basisklasse for Virksomhet og Person. |  no  |
| [Rolle](rolle.md) | Ei rolle ein aktør har overfor ein annan aktør (t.d. styreleiar, revisor). |  no  |
| [Virksomhet](virksomhet.md) | Ei verksemd registrert i Einingsregisteret. |  no  |
| [Person](person.md) | Ein fysisk person. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kontaktinformasjon](kontaktinformasjon.md) |
| Domain Of | [Aktoer](aktoer.md), [Rolle](rolle.md) |
| Slot URI | [brreg_felles_aktoer:kontaktinformasjon](https://data.norge.no/felles/brreg-felles-aktoer/kontaktinformasjon) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/felles/brreg-felles-aktoer




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brreg_felles_aktoer:kontaktinformasjon |
| native | https://data.norge.no/felles/brreg-felles-aktoer/kontaktinformasjon |




## LinkML Source

<details>
```yaml
name: kontaktinformasjon
description: Kontaktinformasjon for aktøren/rolla.
from_schema: https://data.norge.no/felles/brreg-felles-aktoer
slot_uri: brreg_felles_aktoer:kontaktinformasjon
domain_of:
- Aktoer
- Rolle
range: Kontaktinformasjon

```
</details>