

# Slot: medlem 


_Omgrep som er medlem av samlinga (skos:member)._





URI: [skos:member](http://www.w3.org/2004/02/skos/core#member)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Samling](samling.md) | Ei namngitt samling av omgrep (skos:Collection) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Begrep](begrep.md) |
| Domain Of | [Samling](samling.md) |
| Slot URI | [skos:member](http://www.w3.org/2004/02/skos/core#member) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/skos-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | skos:member |
| native | https://data.norge.no/ap-no/skos-ap-no/medlem |




## LinkML Source

<details>
```yaml
name: medlem
description: Omgrep som er medlem av samlinga (skos:member).
from_schema: https://data.norge.no/ap-no/skos-ap-no
rank: 1000
slot_uri: skos:member
domain_of:
- Samling
range: Begrep
multivalued: true

```
</details>