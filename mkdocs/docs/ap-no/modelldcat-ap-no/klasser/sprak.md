

# Slot: sprak 


_Språk brukt i ressursen (dct:language)._





URI: [dct:language](http://purl.org/dc/terms/language)
Alias: sprak

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Modelkatalog](Modelkatalog.md) | Ei kuratert samling av metadata om informasjonsmodellar (dcat:Catalog) |  yes  |
| [Dokument](Dokument.md) | Eit dokument (foaf:Document) |  no  |
| [Informasjonsmodell](Informasjonsmodell.md) | Ein informasjonsmodell som er katalogisert i ein modelkatalog (modelldcatno:I... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Spraak](Spraak.md) |
| Domain Of | [Dokument](Dokument.md), [Modelkatalog](Modelkatalog.md), [Informasjonsmodell](Informasjonsmodell.md) |
| Slot URI | [dct:language](http://purl.org/dc/terms/language) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:language |
| native | https://data.norge.no/linkml/modelldcat-ap-no/sprak |




## LinkML Source

<details>
```yaml
name: sprak
description: Språk brukt i ressursen (dct:language).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: dct:language
alias: sprak
domain_of:
- Dokument
- Modelkatalog
- Informasjonsmodell
range: Spraak
multivalued: true

```
</details>