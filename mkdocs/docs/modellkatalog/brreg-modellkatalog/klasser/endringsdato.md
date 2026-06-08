

# Slot: endringsdato 


_Dato for siste endring av ressursen (dct:modified)._





URI: [dct:modified](http://purl.org/dc/terms/modified)
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
| Range | [xsd:date](http://www.w3.org/2001/XMLSchema#date) |
| Domain Of | [Modellkatalog](modellkatalog.md), [Informasjonsmodell](informasjonsmodell.md) |
| Slot URI | [dct:modified](http://purl.org/dc/terms/modified) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:modified |
| native | https://data.norge.no/ap-no/common-ap-no/endringsdato |




## LinkML Source

<details>
```yaml
name: endringsdato
description: Dato for siste endring av ressursen (dct:modified).
from_schema: https://data.norge.no/ap-no/common-ap-no
slot_uri: dct:modified
domain_of:
- Modellkatalog
- Informasjonsmodell
range: date

```
</details>