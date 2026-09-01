

# Slot: kommune 


_Kommunen adressa ligg i._





URI: [brreg_felles_geografisk_adresse:kommune](https://data.norge.no/felles/brreg-felles-geografisk-adresse/kommune)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Postboksadresse](postboksadresse.md) | Ei postboksadresse. |  no  |
| [Stedsadresse](stedsadresse.md) | Ei stadfesta adresse utan vegadresse (t.d. i utmark). |  no  |
| [Vegadresse](vegadresse.md) | Ei vegadresse (adressenavn + adressenummer). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kommune](kommune.md) |
| Domain Of | [Postboksadresse](postboksadresse.md), [Stedsadresse](stedsadresse.md), [Vegadresse](vegadresse.md) |
| Slot URI | [brreg_felles_geografisk_adresse:kommune](https://data.norge.no/felles/brreg-felles-geografisk-adresse/kommune) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brreg_felles_geografisk_adresse:kommune |
| native | https://data.norge.no/felles/brreg-felles-geografisk-adresse/kommune |




## LinkML Source

<details>
```yaml
name: kommune
description: Kommunen adressa ligg i.
from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
slot_uri: brreg_felles_geografisk_adresse:kommune
domain_of:
- Postboksadresse
- Stedsadresse
- Vegadresse
range: Kommune

```
</details>