

# Slot: poststed 


_Poststedet adressa høyrer til._





URI: [brreg_felles_geografisk_adresse:poststed](https://data.norge.no/felles/brreg-felles-geografisk-adresse/poststed)
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
| Range | [Poststed](poststed.md) |
| Domain Of | [Postboksadresse](postboksadresse.md), [Stedsadresse](stedsadresse.md), [Vegadresse](vegadresse.md) |
| Slot URI | [brreg_felles_geografisk_adresse:poststed](https://data.norge.no/felles/brreg-felles-geografisk-adresse/poststed) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brreg_felles_geografisk_adresse:poststed |
| native | https://data.norge.no/felles/brreg-felles-geografisk-adresse/poststed |




## LinkML Source

<details>
```yaml
name: poststed
description: Poststedet adressa høyrer til.
from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
slot_uri: brreg_felles_geografisk_adresse:poststed
domain_of:
- Postboksadresse
- Stedsadresse
- Vegadresse
range: Poststed

```
</details>