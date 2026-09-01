

# Slot: type 


_Diskriminator for kva slag adresse dette er._





URI: [brreg_felles_geografisk_adresse:type](https://data.norge.no/felles/brreg-felles-geografisk-adresse/type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeografiskAdresse](geografiskadresse.md) | Ei geografisk adresse. Abstrakt basisklasse for dei konkrete adressetypane under. |  yes  |
| [Postboksadresse](postboksadresse.md) | Ei postboksadresse. |  no  |
| [Stedsadresse](stedsadresse.md) | Ei stadfesta adresse utan vegadresse (t.d. i utmark). |  no  |
| [Vegadresse](vegadresse.md) | Ei vegadresse (adressenavn + adressenummer). |  no  |
| [Matrikkeladresse](matrikkeladresse.md) | Ei matrikkeladresse (knytt til eit matrikkelnummer). |  no  |
| [InternasjonalAdresse](internasjonaladresse.md) | Ei adresse i eit anna land enn Noreg, i fri form. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [GeografiskAdresse](geografiskadresse.md) |
| Slot URI | [brreg_felles_geografisk_adresse:type](https://data.norge.no/felles/brreg-felles-geografisk-adresse/type) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brreg_felles_geografisk_adresse:type |
| native | https://data.norge.no/felles/brreg-felles-geografisk-adresse/type |




## LinkML Source

<details>
```yaml
name: type
description: Diskriminator for kva slag adresse dette er.
from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
slot_uri: brreg_felles_geografisk_adresse:type
domain_of:
- GeografiskAdresse
range: string

```
</details>