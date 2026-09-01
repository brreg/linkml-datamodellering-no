

# Slot: digital_adresse_type 


_Diskriminator for kva slag adresse dette er._





URI: [brreg_felles_digital_adresse:type](https://data.norge.no/felles/brreg-felles-digital-adresse/type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DigitalAdresse](digitaladresse.md) | Ei digital adresse. Abstrakt basisklasse for dei konkrete digitale adressetypane under. |  yes  |
| [IPAdresse](ipadresse.md) | Ei IP-adresse. |  no  |
| [EPostadresse](epostadresse.md) | Ei e-postadresse, delt opp i brukarnamn og domenenavn. |  no  |
| [Nettadresse](nettadresse.md) | Ei nettadresse (protokoll, domenenavn og filsti). |  no  |
| [Meldingsboks](meldingsboks.md) | Ei digital meldingsboks (t.d. Altinn). |  no  |
| [Mobiltelefonnummer](mobiltelefonnummer.md) | Eit mobiltelefonnummer. |  no  |
| [Telefonnummer](telefonnummer.md) | Eit fasttelefonnummer. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [DigitalAdresse](digitaladresse.md) |
| Slot URI | [brreg_felles_digital_adresse:type](https://data.norge.no/felles/brreg-felles-digital-adresse/type) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/felles/brreg-felles-digital-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brreg_felles_digital_adresse:type |
| native | https://data.norge.no/felles/brreg-felles-digital-adresse/digital_adresse_type |




## LinkML Source

<details>
```yaml
name: digital_adresse_type
description: Diskriminator for kva slag adresse dette er.
from_schema: https://data.norge.no/felles/brreg-felles-digital-adresse
slot_uri: brreg_felles_digital_adresse:type
alias: type
domain_of:
- DigitalAdresse
range: string

```
</details>