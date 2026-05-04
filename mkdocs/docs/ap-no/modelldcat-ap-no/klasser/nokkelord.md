

# Slot: nokkelord 


_Nøkkelord som beskriv ressursen (dcat:keyword)._





URI: [dcat:keyword](http://www.w3.org/ns/dcat#keyword)
Alias: nokkelord

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Informasjonsmodell](Informasjonsmodell.md) | Ein informasjonsmodell som er katalogisert i ein modelkatalog (modelldcatno:I... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](LangString.md) |
| Domain Of | [Informasjonsmodell](Informasjonsmodell.md) |
| Slot URI | [dcat:keyword](http://www.w3.org/ns/dcat#keyword) |

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
| self | dcat:keyword |
| native | https://data.norge.no/linkml/modelldcat-ap-no/nokkelord |




## LinkML Source

<details>
```yaml
name: nokkelord
description: Nøkkelord som beskriv ressursen (dcat:keyword).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: dcat:keyword
alias: nokkelord
domain_of:
- Informasjonsmodell
range: LangString
multivalued: true

```
</details>