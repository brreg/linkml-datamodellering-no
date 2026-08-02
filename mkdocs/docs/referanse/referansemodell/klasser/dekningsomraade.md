

# Slot: dekningsomraade 


_Geografisk dekningsområde. Verdien BØR veljast frå Geonames (http://sws.geonames.org/) eller EUs kontrollerte vokabular Continent, Country, Place (http://publications.europa.eu/resource/authority/continent/, http://publications.europa.eu/resource/authority/country/, http://publications.europa.eu/resource/authority/place/)._





URI: [dct:spatial](http://purl.org/dc/terms/spatial)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør. |  yes  |
| [Datasettserie](datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata. |  yes  |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre katalogar. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](konsept.md) |
| Domain Of | [Datasett](datasett.md), [Datasettserie](datasettserie.md), [Katalog](katalog.md) |
| Slot URI | [dct:spatial](http://purl.org/dc/terms/spatial) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| gyldige_verdier | http://sws.geonames.org/ |
| vokabular_krav | bør |
| sekundare_vokabular | http://publications.europa.eu/resource/authority/country/ |
| sekundare_vokabular_krav | kan |




### Schema Source


* from schema: https://data.norge.no/ap-no/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:spatial |
| native | https://data.norge.no/ap-no/common-ap-no/dekningsomraade |




## LinkML Source

<details>
```yaml
name: dekningsomraade
annotations:
  gyldige_verdier:
    tag: gyldige_verdier
    value: http://sws.geonames.org/
  vokabular_krav:
    tag: vokabular_krav
    value: bør
  sekundare_vokabular:
    tag: sekundare_vokabular
    value: http://publications.europa.eu/resource/authority/country/
  sekundare_vokabular_krav:
    tag: sekundare_vokabular_krav
    value: kan
description: Geografisk dekningsområde. Verdien BØR veljast frå Geonames (http://sws.geonames.org/)
  eller EUs kontrollerte vokabular Continent, Country, Place (http://publications.europa.eu/resource/authority/continent/,
  http://publications.europa.eu/resource/authority/country/, http://publications.europa.eu/resource/authority/place/).
from_schema: https://data.norge.no/ap-no/common-ap-no
slot_uri: dct:spatial
domain_of:
- Datasett
- Datasettserie
- Katalog
range: Konsept
multivalued: true

```
</details>