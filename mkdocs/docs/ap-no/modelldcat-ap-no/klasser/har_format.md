

# Slot: har_format 


_Dokument som representerer ein annan form av modellen (dct:hasFormat)._





URI: [dct:hasFormat](http://purl.org/dc/terms/hasFormat)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Informasjonsmodell](informasjonsmodell.md) | Ein informasjonsmodell som er katalogisert i ein modellkatalog (modelldcatno:... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Dokument](dokument.md) |
| Domain Of | [Informasjonsmodell](informasjonsmodell.md) |
| Slot URI | [dct:hasFormat](http://purl.org/dc/terms/hasFormat) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:hasFormat |
| native | https://data.norge.no/ap-no/modelldcat-ap-no/har_format |




## LinkML Source

<details>
```yaml
name: har_format
description: Dokument som representerer ein annan form av modellen (dct:hasFormat).
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
rank: 1000
slot_uri: dct:hasFormat
domain_of:
- Informasjonsmodell
range: Dokument
multivalued: true

```
</details>