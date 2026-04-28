

# Slot: rettigheter 


_Rettar knytte til ressursen._





URI: [dct:rights](http://purl.org/dc/terms/rights)
Alias: rettigheter

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](Datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |
| [Distribusjon](Distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |
| [Katalog](Katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Rettighetserklaring](Rettighetserklaring.md) |
| Domain Of | [Distribusjon](Distribusjon.md), [Datatjeneste](Datatjeneste.md), [Katalog](Katalog.md) |
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
rank: 1000
slot_uri: dct:rights
alias: rettigheter
domain_of:
- Distribusjon
- Datatjeneste
- Katalog
range: Rettighetserklaring

```
</details>