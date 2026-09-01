

# Slot: adressetilleggsnavn 


_Tilleggsnamn til adressa (t.d. stadnamn i tillegg til vegadresse)._





URI: [brreg_felles_geografisk_adresse:adressetilleggsnavn](https://data.norge.no/felles/brreg-felles-geografisk-adresse/adressetilleggsnavn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Vegadresse](vegadresse.md) | Ei vegadresse (adressenavn + adressenummer). |  no  |
| [Matrikkeladresse](matrikkeladresse.md) | Ei matrikkeladresse (knytt til eit matrikkelnummer). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Vegadresse](vegadresse.md), [Matrikkeladresse](matrikkeladresse.md) |
| Slot URI | [brreg_felles_geografisk_adresse:adressetilleggsnavn](https://data.norge.no/felles/brreg-felles-geografisk-adresse/adressetilleggsnavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | brreg_felles_geografisk_adresse:adressetilleggsnavn |
| native | https://data.norge.no/felles/brreg-felles-geografisk-adresse/adressetilleggsnavn |




## LinkML Source

<details>
```yaml
name: adressetilleggsnavn
description: Tilleggsnamn til adressa (t.d. stadnamn i tillegg til vegadresse).
from_schema: https://data.norge.no/felles/brreg-felles-geografisk-adresse
slot_uri: brreg_felles_geografisk_adresse:adressetilleggsnavn
domain_of:
- Vegadresse
- Matrikkeladresse
range: string

```
</details>