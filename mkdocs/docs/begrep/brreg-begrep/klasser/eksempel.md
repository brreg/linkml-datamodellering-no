

# Slot: eksempel 


_Eksempel på bruk av omgrepet (skos:example)._





URI: [skos:example](http://www.w3.org/2004/02/skos/core#example)
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
| Slot URI | [skos:example](http://www.w3.org/2004/02/skos/core#example) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/skos-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | skos:example |
| native | https://data.norge.no/linkml/skos-ap-no/eksempel |




## LinkML Source

<details>
```yaml
name: eksempel
description: Eksempel på bruk av omgrepet (skos:example).
from_schema: https://data.norge.no/linkml/skos-ap-no
slot_uri: skos:example
domain_of:
- Begrep
range: LangString
multivalued: true

```
</details>