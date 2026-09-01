

# Slot: adressenavn 


_Namnet på vegen/gata/staden._





URI: [brreg_felles_geografisk_adresse:adressenavn](https://data.norge.no/felles/brreg-felles-geografisk-adresse/adressenavn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Vegadresse](vegadresse.md) | Ei vegadresse (adressenavn + adressenummer). |  no  |
| [InternasjonalAdresse](internasjonaladresse.md) | Ei adresse i eit anna land enn Noreg, i fri form. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Vegadresse](vegadresse.md), [InternasjonalAdresse](internasjonaladresse.md) |
| Slot URI | [brreg_felles_geografisk_adresse:adressenavn](https://data.norge.no/felles/brreg-felles-geografisk-adresse/adressenavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brreg_felles_geografisk_adresse:adressenavn |
| native | https://data.norge.no/felles/brreg-felles-geografisk-adresse/adressenavn |




## LinkML Source

<details>
```yaml
name: adressenavn
description: Namnet på vegen/gata/staden.
from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
slot_uri: brreg_felles_geografisk_adresse:adressenavn
domain_of:
- Vegadresse
- InternasjonalAdresse
range: string

```
</details>