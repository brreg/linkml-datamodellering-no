

# Slot: notat 


_Generelt notat om kodeelementet (skos:note)._





URI: [skos:note](http://www.w3.org/2004/02/skos/core#note)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kodeelement](kodeelement.md) | Eit element i ei kodeliste (modelldcatno:CodeElement) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](langstring.md) |
| Domain Of | [Kodeelement](kodeelement.md) |
| Slot URI | [skos:note](http://www.w3.org/2004/02/skos/core#note) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | skos:note |
| native | https://data.norge.no/ap-no/modelldcat-ap-no/notat |




## LinkML Source

<details>
```yaml
name: notat
description: Generelt notat om kodeelementet (skos:note).
from_schema: https://data.norge.no/ap-no/modelldcat-ap-no
rank: 1000
slot_uri: skos:note
domain_of:
- Kodeelement
range: LangString
multivalued: true

```
</details>