

# Slot: format 


_Filformat eller medietype (dct:format)._





URI: [dct:format](http://purl.org/dc/terms/format)
Alias: format

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](Datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  yes  |
| [Distribusjon](Distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Mediatype](Mediatype.md) |
| Domain Of | [Distribusjon](Distribusjon.md), [Datatjeneste](Datatjeneste.md) |
| Slot URI | [dct:format](http://purl.org/dc/terms/format) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:format |
| native | https://data.norge.no/linkml/dcat-ap-no/format |




## LinkML Source

<details>
```yaml
name: format
description: Filformat eller medietype (dct:format).
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dct:format
alias: format
domain_of:
- Distribusjon
- Datatjeneste
range: Mediatype

```
</details>