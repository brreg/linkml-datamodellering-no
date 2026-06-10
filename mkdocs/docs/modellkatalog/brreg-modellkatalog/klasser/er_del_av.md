

# Slot: er_del_av 


_Overordna ressurs denne er ein del av (dct:isPartOf)._





URI: [dct:isPartOf](http://purl.org/dc/terms/isPartOf)
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
| Slot URI | [dct:isPartOf](http://purl.org/dc/terms/isPartOf) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:isPartOf |
| native | https://data.norge.no/ap-no/modelldcat-ap-no/er_del_av |




## LinkML Source

<details>
```yaml
name: er_del_av
description: Overordna ressurs denne er ein del av (dct:isPartOf).
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
slot_uri: dct:isPartOf
domain_of:
- Modellkatalog
- Informasjonsmodell
range: KatalogisertRessurs

```
</details>