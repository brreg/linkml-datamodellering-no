

# Slot: rettigheter 


_Rettar knytte til ressursen._





URI: [dct:rights](http://purl.org/dc/terms/rights)
Alias: rettigheter

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  no  |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Rettighetserklaring](rettighetserklaring.md) |
| Domain Of | [Distribusjon](distribusjon.md), [Datatjeneste](datatjeneste.md), [Katalog](katalog.md) |
| Slot URI | [dct:rights](http://purl.org/dc/terms/rights) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:rights |
| native | https://data.norge.no/linkml/dcat-ap-no/rettigheter |




## LinkML Source

<details>
```yaml
name: rettigheter
description: Rettar knytte til ressursen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
slot_uri: dct:rights
alias: rettigheter
domain_of:
- Distribusjon
- Datatjeneste
- Katalog
range: Rettighetserklaring

```
</details>