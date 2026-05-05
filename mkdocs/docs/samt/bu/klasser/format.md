

# Slot: format 


_Filformat eller medietype (dct:format)._





URI: [dct:format](http://purl.org/dc/terms/format)
Alias: format

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  yes  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Mediatype](mediatype.md) |
| Domain Of | [Distribusjon](distribusjon.md), [Datatjeneste](datatjeneste.md) |
| Slot URI | [dct:format](http://purl.org/dc/terms/format) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:format |
| native | samtbuskole:format |




## LinkML Source

<details>
```yaml
name: format
description: Filformat eller medietype (dct:format).
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dct:format
alias: format
domain_of:
- Distribusjon
- Datatjeneste
range: Mediatype

```
</details>