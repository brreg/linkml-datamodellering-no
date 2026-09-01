

# Slot: adressenummer_tekst 


_Adressenummer som fritekst (for utanlandske adresser med anna format enn norsk husnummer/husbokstav)._





URI: [brreg_felles_geografisk_adresse:adressenummerTekst](https://data.norge.no/felles/brreg-felles-geografisk-adresse/adressenummerTekst)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InternasjonalAdresse](internasjonaladresse.md) | Ei adresse i eit anna land enn Noreg, i fri form. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [InternasjonalAdresse](internasjonaladresse.md) |
| Slot URI | [brreg_felles_geografisk_adresse:adressenummerTekst](https://data.norge.no/felles/brreg-felles-geografisk-adresse/adressenummerTekst) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brreg_felles_geografisk_adresse:adressenummerTekst |
| native | https://data.norge.no/felles/brreg-felles-geografisk-adresse/adressenummer_tekst |




## LinkML Source

<details>
```yaml
name: adressenummer_tekst
description: Adressenummer som fritekst (for utanlandske adresser med anna format
  enn norsk husnummer/husbokstav).
from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
slot_uri: brreg_felles_geografisk_adresse:adressenummerTekst
domain_of:
- InternasjonalAdresse
range: string

```
</details>