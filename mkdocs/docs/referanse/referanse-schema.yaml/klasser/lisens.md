

# Slot: lisens 


_Lisens for bruk av ressursen. For offentlege data skal CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/) eller NLOD 2.0 (https://data.norge.no/nlod/no/2.0) nyttast per retningslinjene._





URI: [dct:license](http://purl.org/dc/terms/license)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  yes  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  yes  |






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



### Annotations

| property | value |
| --- | --- |
| gyldige_verdier | https://creativecommons.org/licenses/by/4.0/ https://data.norge.no/nlod/no/2.0 |




### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:license |
| native | https://data.norge.no/ap-no/dcat-ap-no/lisens |




## LinkML Source

<details>
```yaml
name: lisens
annotations:
  gyldige_verdier:
    tag: gyldige_verdier
    value: https://creativecommons.org/licenses/by/4.0/ https://data.norge.no/nlod/no/2.0
description: Lisens for bruk av ressursen. For offentlege data skal CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)
  eller NLOD 2.0 (https://data.norge.no/nlod/no/2.0) nyttast per retningslinjene.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
slot_uri: dct:license
domain_of:
- Distribusjon
- Datatjeneste
- Katalog
range: string

```
</details>