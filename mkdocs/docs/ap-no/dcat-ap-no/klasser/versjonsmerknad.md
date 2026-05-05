

# Slot: versjonsmerknad 


_Merknad om endringar i denne versjonen (adms:versionNotes)._





URI: [adms:versionNotes](http://www.w3.org/ns/adms#versionNotes)
Alias: versjonsmerknad

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](langstring.md) |
| Domain Of | [Datasett](datasett.md), [Datatjeneste](datatjeneste.md) |
| Slot URI | [adms:versionNotes](http://www.w3.org/ns/adms#versionNotes) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adms:versionNotes |
| native | https://data.norge.no/linkml/dcat-ap-no/versjonsmerknad |




## LinkML Source

<details>
```yaml
name: versjonsmerknad
description: Merknad om endringar i denne versjonen (adms:versionNotes).
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: adms:versionNotes
alias: versjonsmerknad
domain_of:
- Datasett
- Datatjeneste
range: LangString
multivalued: true

```
</details>