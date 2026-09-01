

# Slot: stedsnavn 


_Namnet på staden (for adresser utan vegadresse)._





URI: [brreg_felles_geografisk_adresse:stedsnavn](https://data.norge.no/felles/brreg-felles-geografisk-adresse/stedsnavn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Stedsadresse](stedsadresse.md) | Ei stadfesta adresse utan vegadresse (t.d. i utmark). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Stedsadresse](stedsadresse.md) |
| Slot URI | [brreg_felles_geografisk_adresse:stedsnavn](https://data.norge.no/felles/brreg-felles-geografisk-adresse/stedsnavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brreg_felles_geografisk_adresse:stedsnavn |
| native | https://data.norge.no/felles/brreg-felles-geografisk-adresse/stedsnavn |




## LinkML Source

<details>
```yaml
name: stedsnavn
description: Namnet på staden (for adresser utan vegadresse).
from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
slot_uri: brreg_felles_geografisk_adresse:stedsnavn
domain_of:
- Stedsadresse
range: string

```
</details>