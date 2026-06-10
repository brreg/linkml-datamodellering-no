

# Slot: har_del 


_Del-ressurs inkludert i denne ressursen (dct:hasPart)._





URI: [dct:hasPart](http://purl.org/dc/terms/hasPart)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Modellkatalog](modellkatalog.md) | Ei kuratert samling av metadata om informasjonsmodellar (dcat:Catalog) |  yes  |
| [Informasjonsmodell](informasjonsmodell.md) | Ein informasjonsmodell som er katalogisert i ein modellkatalog (modelldcatno:... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [KatalogisertRessurs](katalogisertressurs.md) |
| Domain Of | [Modellkatalog](modellkatalog.md), [Informasjonsmodell](informasjonsmodell.md) |
| Slot URI | [dct:hasPart](http://purl.org/dc/terms/hasPart) |

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
| self | dct:hasPart |
| native | https://data.norge.no/ap-no/modelldcat-ap-no/har_del |




## LinkML Source

<details>
```yaml
name: har_del
description: Del-ressurs inkludert i denne ressursen (dct:hasPart).
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
slot_uri: dct:hasPart
domain_of:
- Modellkatalog
- Informasjonsmodell
range: KatalogisertRessurs
multivalued: true

```
</details>