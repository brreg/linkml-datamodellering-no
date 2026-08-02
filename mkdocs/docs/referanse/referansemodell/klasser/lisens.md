

# Slot: lisens 


_Lisens for bruk av ressursen. Verdien SKAL veljast frå EUs kontrollerte vokabular Licence (http://publications.europa.eu/resource/authority/licence/). For norske offentlege data er CC BY 4.0 eller NLOD 2.0 anbefalt per retningslinjene. Enumerasjonen EULicence i common-ap-no dekkjer dei mest brukte open source/open data-lisensane._





URI: [dct:license](http://purl.org/dc/terms/license)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett. |  yes  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt. |  yes  |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre katalogar. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Lisensdokument](lisensdokument.md) |
| Domain Of | [Distribusjon](distribusjon.md), [Datatjeneste](datatjeneste.md), [Katalog](katalog.md) |
| Slot URI | [dct:license](http://purl.org/dc/terms/license) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| gyldige_verdier | http://publications.europa.eu/resource/authority/licence/ |
| vokabular_krav | skal |
| enum_referanse | EULicence |
| enum_dekning | delvis |




### Schema Source


* from schema: https://data.norge.no/ap-no/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:license |
| native | https://data.norge.no/ap-no/common-ap-no/lisens |




## LinkML Source

<details>
```yaml
name: lisens
annotations:
  gyldige_verdier:
    tag: gyldige_verdier
    value: http://publications.europa.eu/resource/authority/licence/
  vokabular_krav:
    tag: vokabular_krav
    value: skal
  enum_referanse:
    tag: enum_referanse
    value: EULicence
  enum_dekning:
    tag: enum_dekning
    value: delvis
description: Lisens for bruk av ressursen. Verdien SKAL veljast frå EUs kontrollerte
  vokabular Licence (http://publications.europa.eu/resource/authority/licence/). For
  norske offentlege data er CC BY 4.0 eller NLOD 2.0 anbefalt per retningslinjene.
  Enumerasjonen EULicence i common-ap-no dekkjer dei mest brukte open source/open
  data-lisensane.
from_schema: https://data.norge.no/ap-no/common-ap-no
slot_uri: dct:license
domain_of:
- Distribusjon
- Datatjeneste
- Katalog
range: Lisensdokument

```
</details>