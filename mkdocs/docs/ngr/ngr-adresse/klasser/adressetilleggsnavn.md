

# Slot: adressetilleggsnavn 


_Offisielt tilleggsnamn til vegadressa (t.d. gardsnamn, bruksnamn)._





URI: [ngr:adressetilleggsnavn](https://data.norge.no/vocabulary/ngr-adresse#adressetilleggsnavn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OffisiellAdresse](offisielladresse.md) | Ei offisiell adresse tildelt av kommunen, beståande av vegadresse (adressenav... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [OffisiellAdresse](offisielladresse.md) |
| Slot URI | [ngr:adressetilleggsnavn](https://data.norge.no/vocabulary/ngr-adresse#adressetilleggsnavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:adressetilleggsnavn |
| native | https://data.norge.no/ngr/ngr-adresse/adressetilleggsnavn |




## LinkML Source

<details>
```yaml
name: adressetilleggsnavn
description: Offisielt tilleggsnamn til vegadressa (t.d. gardsnamn, bruksnamn).
from_schema: https://data.norge.no/ngr/ngr-adresse
rank: 1000
slot_uri: ngr:adressetilleggsnavn
domain_of:
- OffisiellAdresse
range: string

```
</details>