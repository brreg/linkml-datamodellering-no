

# Slot: digital_adresse_id 


_URI-identifikator for ressursen._





URI: [brreg_felles_digital_adresse:id](https://data.norge.no/felles/brreg-felles-digital-adresse/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DigitalAdresse](digitaladresse.md) | Ei digital adresse. Abstrakt basisklasse for dei konkrete digitale adressetypane under. |  no  |
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
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [DigitalAdresse](digitaladresse.md) |
| Slot URI | [brreg_felles_digital_adresse:id](https://data.norge.no/felles/brreg-felles-digital-adresse/id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/felles/brreg-felles-digital-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brreg_felles_digital_adresse:id |
| native | https://data.norge.no/felles/brreg-felles-digital-adresse/digital_adresse_id |




## LinkML Source

<details>
```yaml
name: digital_adresse_id
description: URI-identifikator for ressursen.
from_schema: https://data.norge.no/felles/brreg-felles-digital-adresse
slot_uri: brreg_felles_digital_adresse:id
identifier: true
alias: id
domain_of:
- DigitalAdresse
range: uriorcurie
required: true

```
</details>