

# Slot: utgivelsesdato 


_Dato ressursen vart første gong publisert (dct:issued)._





URI: [dct:issued](http://purl.org/dc/terms/issued)
Alias: utgivelsesdato

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
| Slot URI | [dct:issued](http://purl.org/dc/terms/issued) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:issued |
| native | https://data.norge.no/linkml/modelldcat-ap-no/utgivelsesdato |




## LinkML Source

<details>
```yaml
name: utgivelsesdato
description: Dato ressursen vart første gong publisert (dct:issued).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: dct:issued
alias: utgivelsesdato
domain_of:
- Modelkatalog
- Informasjonsmodell
range: date

```
</details>