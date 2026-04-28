

# Slot: lisens 


_Lisens for bruk av ressursen._





URI: [dct:license](http://purl.org/dc/terms/license)
Alias: lisens

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](Datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |
| [Distribusjon](Distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  yes  |
| [Katalog](Katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Begrep](Begrep.md) |
| Domain Of | [Distribusjon](Distribusjon.md), [Datatjeneste](Datatjeneste.md), [Katalog](Katalog.md) |
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
rank: 1000
slot_uri: dct:license
alias: lisens
domain_of:
- Distribusjon
- Datatjeneste
- Katalog
range: Begrep

```
</details>