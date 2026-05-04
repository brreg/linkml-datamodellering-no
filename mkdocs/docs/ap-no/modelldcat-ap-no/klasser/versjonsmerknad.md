

# Slot: versjonsmerknad 


_Merknad om endringar i denne versjonen (adms:versionNotes)._





URI: [adms:versionNotes](http://www.w3.org/ns/adms#versionNotes)
Alias: versjonsmerknad

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
| Slot URI | [adms:versionNotes](http://www.w3.org/ns/adms#versionNotes) |

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
| self | adms:versionNotes |
| native | https://data.norge.no/linkml/modelldcat-ap-no/versjonsmerknad |




## LinkML Source

<details>
```yaml
name: versjonsmerknad
description: Merknad om endringar i denne versjonen (adms:versionNotes).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: adms:versionNotes
alias: versjonsmerknad
domain_of:
- Informasjonsmodell
range: LangString
multivalued: true

```
</details>