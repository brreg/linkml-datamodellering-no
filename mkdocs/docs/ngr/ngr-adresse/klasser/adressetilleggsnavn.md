

# Slot: adressetilleggsnavn 


_Offisielt tilleggsnamn til vegadressa (t.d. gardsnamn, bruksnamn)._





URI: [ngr:adressetilleggsnavn](https://data.norge.no/vocabulary/ngr-adresse#adressetilleggsnavn)
Alias: adressetilleggsnavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OffisiellAdresse](offisielladresse.md) | Ei offisiell adresse tildelt av kommunen, beståande av vegadresse (adressenav... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [OffisiellAdresse](offisielladresse.md) |
| Slot URI | [ngr:adressetilleggsnavn](https://data.norge.no/vocabulary/ngr-adresse#adressetilleggsnavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:adressetilleggsnavn |
| native | https://data.norge.no/linkml/ngr-adresse/adressetilleggsnavn |




## LinkML Source

<details>
```yaml
name: adressetilleggsnavn
description: Offisielt tilleggsnamn til vegadressa (t.d. gardsnamn, bruksnamn).
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
slot_uri: ngr:adressetilleggsnavn
alias: adressetilleggsnavn
domain_of:
- OffisiellAdresse
range: string

```
</details>