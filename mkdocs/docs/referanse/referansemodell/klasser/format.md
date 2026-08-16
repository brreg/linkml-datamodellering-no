

# Slot: format 


_Filformat eller medietype. Verdien SKAL veljast frå EUs kontrollerte vokabular File type (http://publications.europa.eu/resource/authority/file-type/). Enumerasjonen EUFileType i common-ap-no dekkjer dei mest brukte formata (RDF, JSON, CSV, PDF, osv.). For andre format, bruk URI frå EU File Type-vokabularet._





URI: [dct:format](http://purl.org/dc/terms/format)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tekstdel](tekstdel.md) | Ein tekstleg del av ein kvalitetsmerknad (Web Annotation). |  yes  |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett. |  yes  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](konsept.md) |
| Domain Of | [Tekstdel](tekstdel.md), [Distribusjon](distribusjon.md), [Datatjeneste](datatjeneste.md) |
| Slot URI | [dct:format](http://purl.org/dc/terms/format) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| gyldige_verdier | http://publications.europa.eu/resource/authority/file-type/ |
| vokabular_krav | skal |
| vokabular_pattern | `^http://publications\.europa\.eu/resource/authority/file-type/[A-Z_]+$` |
| enum_referanse | EUFileType |
| enum_dekning | delvis |




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
annotations:
  gyldige_verdier:
    tag: gyldige_verdier
    value: http://publications.europa.eu/resource/authority/file-type/
  vokabular_krav:
    tag: vokabular_krav
    value: skal
  vokabular_pattern:
    tag: vokabular_pattern
    value: ^http://publications\.europa\.eu/resource/authority/file-type/[A-Z_]+$
  enum_referanse:
    tag: enum_referanse
    value: EUFileType
  enum_dekning:
    tag: enum_dekning
    value: delvis
description: Filformat eller medietype. Verdien SKAL veljast frå EUs kontrollerte
  vokabular File type (http://publications.europa.eu/resource/authority/file-type/).
  Enumerasjonen EUFileType i common-ap-no dekkjer dei mest brukte formata (RDF, JSON,
  CSV, PDF, osv.). For andre format, bruk URI frå EU File Type-vokabularet.
from_schema: https://data.norge.no/ap-no/common-ap-no
slot_uri: dct:format
domain_of:
- Tekstdel
- Distribusjon
- Datatjeneste
range: Konsept

```
</details>