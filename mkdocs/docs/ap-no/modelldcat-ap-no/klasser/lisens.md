

# Slot: lisens 


_Lisens for bruk av ressursen (dct:license)._





URI: [dct:license](http://purl.org/dc/terms/license)
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
| Range | [Lisensdokument](lisensdokument.md) |
| Domain Of | [Modellkatalog](modellkatalog.md), [Informasjonsmodell](informasjonsmodell.md) |
| Slot URI | [dct:license](http://purl.org/dc/terms/license) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:license |
| native | https://data.norge.no/ap-no/modelldcat-ap-no/lisens |




## LinkML Source

<details>
```yaml
name: lisens
description: Lisens for bruk av ressursen (dct:license).
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
rank: 1000
slot_uri: dct:license
domain_of:
- Modellkatalog
- Informasjonsmodell
range: Lisensdokument

```
</details>