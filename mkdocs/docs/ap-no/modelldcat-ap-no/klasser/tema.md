

# Slot: tema 


_Tema frå eit kontrollert vokabular (dcat:theme)._





URI: [dcat:theme](http://www.w3.org/ns/dcat#theme)
Alias: tema

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
| Range | [Konsept](Konsept.md) |
| Domain Of | [Modelkatalog](Modelkatalog.md), [Informasjonsmodell](Informasjonsmodell.md) |
| Slot URI | [dcat:theme](http://www.w3.org/ns/dcat#theme) |

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
| self | dcat:theme |
| native | https://data.norge.no/linkml/modelldcat-ap-no/tema |




## LinkML Source

<details>
```yaml
name: tema
description: Tema frå eit kontrollert vokabular (dcat:theme).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: dcat:theme
alias: tema
domain_of:
- Modelkatalog
- Informasjonsmodell
range: Konsept
multivalued: true

```
</details>