

# Slot: domenenavn 


_Domenenamnet i adressa._





URI: [brreg_felles_digital_adresse:domenenavn](https://data.norge.no/felles/brreg-felles-digital-adresse/domenenavn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EPostadresse](epostadresse.md) | Ei e-postadresse, delt opp i brukarnamn og domenenavn. |  no  |
| [Nettadresse](nettadresse.md) | Ei nettadresse (protokoll, domenenavn og filsti). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [EPostadresse](epostadresse.md), [Nettadresse](nettadresse.md) |
| Slot URI | [brreg_felles_digital_adresse:domenenavn](https://data.norge.no/felles/brreg-felles-digital-adresse/domenenavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/felles/brreg-felles-digital-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brreg_felles_digital_adresse:domenenavn |
| native | https://data.norge.no/felles/brreg-felles-digital-adresse/domenenavn |




## LinkML Source

<details>
```yaml
name: domenenavn
description: Domenenamnet i adressa.
from_schema: https://data.norge.no/felles/brreg-felles-digital-adresse
slot_uri: brreg_felles_digital_adresse:domenenavn
domain_of:
- EPostadresse
- Nettadresse
range: string

```
</details>