

# Slot: geografisk_adresse 


_Geografisk adresse knytt til aktøren/rolla._





URI: [brreg_felles_aktoer:geografiskAdresse](https://data.norge.no/felles/brreg-felles-aktoer/geografiskAdresse)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Aktoer](aktoer.md) | Ein aktør — person eller verksemd. Abstrakt basisklasse for Virksomhet og Person. |  no  |
| [Kontaktinformasjon](kontaktinformasjon.md) | Kontaktinformasjon (digital og/eller geografisk adresse) for ein aktør. |  no  |
| [Rolle](rolle.md) | Ei rolle ein aktør har overfor ein annan aktør (t.d. styreleiar, revisor). |  no  |
| [Virksomhet](virksomhet.md) | Ei verksemd registrert i Einingsregisteret. |  no  |
| [Person](person.md) | Ein fysisk person. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeografiskAdresse](geografiskadresse.md) |
| Domain Of | [Aktoer](aktoer.md), [Kontaktinformasjon](kontaktinformasjon.md), [Rolle](rolle.md) |
| Slot URI | [brreg_felles_aktoer:geografiskAdresse](https://data.norge.no/felles/brreg-felles-aktoer/geografiskAdresse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/felles/brreg-felles-aktoer




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brreg_felles_aktoer:geografiskAdresse |
| native | https://data.norge.no/felles/brreg-felles-aktoer/geografisk_adresse |




## LinkML Source

<details>
```yaml
name: geografisk_adresse
description: Geografisk adresse knytt til aktøren/rolla.
from_schema: https://data.norge.no/felles/brreg-felles-aktoer
slot_uri: brreg_felles_aktoer:geografiskAdresse
domain_of:
- Aktoer
- Kontaktinformasjon
- Rolle
range: GeografiskAdresse

```
</details>