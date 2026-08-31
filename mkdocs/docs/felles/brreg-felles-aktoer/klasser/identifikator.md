

# Slot: identifikator 


_Generisk identifikator (form varierer per samanheng — brukt både for digitale adresser og, via brreg-felles-aktoer, for aktørar generelt)._





URI: [brreg_felles_adresse:identifikator](https://data.norge.no/felles/brreg-felles-adresse/identifikator)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DigitalAdresse](digitaladresse.md) | Ei digital adresse. Abstrakt basisklasse for dei konkrete digitale adressetypane under. |  yes  |
| [Aktoer](aktoer.md) | Ein aktør — person eller verksemd. Abstrakt basisklasse for Virksomhet og Person. |  no  |
| [IPAdresse](ipadresse.md) | Ei IP-adresse. |  no  |
| [EPostadresse](epostadresse.md) | Ei e-postadresse, delt opp i brukarnamn og domenenavn. |  no  |
| [Nettadresse](nettadresse.md) | Ei nettadresse (protokoll, domenenavn og filsti). |  no  |
| [Meldingsboks](meldingsboks.md) | Ei digital meldingsboks (t.d. Altinn). |  no  |
| [Mobiltelefonnummer](mobiltelefonnummer.md) | Eit mobiltelefonnummer. |  no  |
| [Telefonnummer](telefonnummer.md) | Eit fasttelefonnummer. |  no  |
| [Virksomhet](virksomhet.md) | Ei verksemd registrert i Einingsregisteret. |  no  |
| [Person](person.md) | Ein fysisk person. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [DigitalAdresse](digitaladresse.md), [Aktoer](aktoer.md) |
| Slot URI | [brreg_felles_adresse:identifikator](https://data.norge.no/felles/brreg-felles-adresse/identifikator) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/felles/brreg-felles-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brreg_felles_adresse:identifikator |
| native | https://data.norge.no/felles/brreg-felles-adresse/identifikator |




## LinkML Source

<details>
```yaml
name: identifikator
description: Generisk identifikator (form varierer per samanheng — brukt både for
  digitale adresser og, via brreg-felles-aktoer, for aktørar generelt).
from_schema: https://data.norge.no/felles/brreg-felles-adresse
slot_uri: brreg_felles_adresse:identifikator
domain_of:
- DigitalAdresse
- Aktoer
range: string

```
</details>