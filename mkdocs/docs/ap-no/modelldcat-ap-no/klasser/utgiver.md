

# Slot: utgiver 


_Aktøren ansvarleg for å tilgjengeleggjere ressursen (dct:publisher)._





URI: [dct:publisher](http://purl.org/dc/terms/publisher)
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
| Range | [Aktor](aktor.md) |
| Domain Of | [Modellkatalog](modellkatalog.md), [Informasjonsmodell](informasjonsmodell.md) |
| Slot URI | [dct:publisher](http://purl.org/dc/terms/publisher) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:publisher |
| native | https://data.norge.no/ap-no/modelldcat-ap-no/utgiver |




## LinkML Source

<details>
```yaml
name: utgiver
description: Aktøren ansvarleg for å tilgjengeleggjere ressursen (dct:publisher).
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
rank: 1000
slot_uri: dct:publisher
domain_of:
- Modellkatalog
- Informasjonsmodell
range: Aktor

```
</details>