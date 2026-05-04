

# Slot: endringsdato 


_Dato for siste endring av ressursen (dct:modified)._





URI: [dct:modified](http://purl.org/dc/terms/modified)
Alias: endringsdato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Modelkatalog](Modelkatalog.md) | Ei kuratert samling av metadata om informasjonsmodellar (dcat:Catalog) |  yes  |
| [Informasjonsmodell](Informasjonsmodell.md) | Ein informasjonsmodell som er katalogisert i ein modelkatalog (modelldcatno:I... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [Modelkatalog](Modelkatalog.md), [Informasjonsmodell](Informasjonsmodell.md) |
| Slot URI | [dct:modified](http://purl.org/dc/terms/modified) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:modified |
| native | https://data.norge.no/linkml/modelldcat-ap-no/endringsdato |




## LinkML Source

<details>
```yaml
name: endringsdato
description: Dato for siste endring av ressursen (dct:modified).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: dct:modified
alias: endringsdato
domain_of:
- Modelkatalog
- Informasjonsmodell
range: date

```
</details>