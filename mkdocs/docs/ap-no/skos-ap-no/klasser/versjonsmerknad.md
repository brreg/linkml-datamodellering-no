

# Slot: versjonsmerknad 


_Merknad om endringar i denne versjonen (adms:versionNotes)._





URI: [adms:versionNotes](http://www.w3.org/ns/adms#versionNotes)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Begrep](begrep.md) | Eit omgrep med definisjon og tilhøyrande metadata (skos:Concept) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](langstring.md) |
| Domain Of | [Begrep](begrep.md) |
| Slot URI | [adms:versionNotes](http://www.w3.org/ns/adms#versionNotes) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adms:versionNotes |
| native | https://data.norge.no/linkml/common-ap-no/versjonsmerknad |




## LinkML Source

<details>
```yaml
name: versjonsmerknad
description: Merknad om endringar i denne versjonen (adms:versionNotes).
from_schema: https://data.norge.no/linkml/common-ap-no
slot_uri: adms:versionNotes
domain_of:
- Begrep
range: LangString
multivalued: true

```
</details>