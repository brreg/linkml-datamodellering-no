

# Slot: utgivelsesdato 


_Dato ressursen vart første gong publisert (dct:issued)._





URI: [dct:issued](http://purl.org/dc/terms/issued)
Alias: utgivelsesdato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Informasjonsmodell](informasjonsmodell.md) | Ein informasjonsmodell som er katalogisert i ein modelkatalog (modelldcatno:I... |  yes  |
| [Modelkatalog](modelkatalog.md) | Ei kuratert samling av metadata om informasjonsmodellar (dcat:Catalog) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:date](http://www.w3.org/2001/XMLSchema#date) |
| Domain Of | [Modelkatalog](modelkatalog.md), [Informasjonsmodell](informasjonsmodell.md) |
| Slot URI | [dct:issued](http://purl.org/dc/terms/issued) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:issued |
| native | https://data.norge.no/linkml/common-ap-no/utgivelsesdato |




## LinkML Source

<details>
```yaml
name: utgivelsesdato
description: Dato ressursen vart første gong publisert (dct:issued).
from_schema: https://data.norge.no/linkml/common-ap-no
slot_uri: dct:issued
alias: utgivelsesdato
domain_of:
- Modelkatalog
- Informasjonsmodell
range: date

```
</details>