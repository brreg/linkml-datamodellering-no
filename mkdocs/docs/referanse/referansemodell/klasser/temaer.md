

# Slot: temaer 


_Temavokabular som vert brukt i katalogen. Verdien SKAL inkludere Los-referansen (https://psi.norge.no/los/) for å signalisere til Felles datakatalog at Los vert brukt. Andre temavokabular (t.d. EuroVoc) kan òg inkluderast._





URI: [dcat:themeTaxonomy](http://www.w3.org/ns/dcat#themeTaxonomy)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre katalogar. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Begrepssamling](begrepssamling.md) |
| Domain Of | [Katalog](katalog.md) |
| Slot URI | [dcat:themeTaxonomy](http://www.w3.org/ns/dcat#themeTaxonomy) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| gyldige_verdier | https://psi.norge.no/los/ |
| vokabular_krav | skal |
| sekundare_vokabular | http://publications.europa.eu/resource/authority/eurovoc/ |
| sekundare_vokabular_krav | kan |




### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:themeTaxonomy |
| native | https://data.norge.no/ap-no/dcat-ap-no/temaer |




## LinkML Source

<details>
```yaml
name: temaer
annotations:
  gyldige_verdier:
    tag: gyldige_verdier
    value: https://psi.norge.no/los/
  vokabular_krav:
    tag: vokabular_krav
    value: skal
  sekundare_vokabular:
    tag: sekundare_vokabular
    value: http://publications.europa.eu/resource/authority/eurovoc/
  sekundare_vokabular_krav:
    tag: sekundare_vokabular_krav
    value: kan
description: Temavokabular som vert brukt i katalogen. Verdien SKAL inkludere Los-referansen
  (https://psi.norge.no/los/) for å signalisere til Felles datakatalog at Los vert
  brukt. Andre temavokabular (t.d. EuroVoc) kan òg inkluderast.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
slot_uri: dcat:themeTaxonomy
domain_of:
- Katalog
range: Begrepssamling
multivalued: true

```
</details>