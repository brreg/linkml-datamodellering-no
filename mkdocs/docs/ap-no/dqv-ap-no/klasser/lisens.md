

# Slot: lisens 


_Lisens for bruk av ressursen._





URI: [dct:license](http://purl.org/dc/terms/license)
Alias: lisens

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  yes  |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  yes  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Distribusjon](distribusjon.md), [Datatjeneste](datatjeneste.md), [Katalog](katalog.md) |
| Slot URI | [dct:license](http://purl.org/dc/terms/license) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:license |
| native | https://data.norge.no/linkml/dcat-ap-no/lisens |




## LinkML Source

<details>
```yaml
name: lisens
description: Lisens for bruk av ressursen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
slot_uri: dct:license
alias: lisens
domain_of:
- Distribusjon
- Datatjeneste
- Katalog
range: string

```
</details>