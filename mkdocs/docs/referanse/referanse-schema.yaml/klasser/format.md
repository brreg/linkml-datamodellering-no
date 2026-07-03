

# Slot: format 


_Filformat eller medietype (dct:format)._





URI: [dct:format](http://purl.org/dc/terms/format)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tekstdel](tekstdel.md) | Ein tekstleg del av ein kvalitetsmerknad (Web Annotation) |  yes  |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  yes  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Tekstdel](tekstdel.md), [Distribusjon](distribusjon.md), [Datatjeneste](datatjeneste.md) |
| Slot URI | [dct:format](http://purl.org/dc/terms/format) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:format |
| native | https://data.norge.no/ap-no/common-ap-no/format |




## LinkML Source

<details>
```yaml
name: format
description: Filformat eller medietype (dct:format).
from_schema: https://data.norge.no/ap-no/common-ap-no
slot_uri: dct:format
domain_of:
- Tekstdel
- Distribusjon
- Datatjeneste
range: string

```
</details>