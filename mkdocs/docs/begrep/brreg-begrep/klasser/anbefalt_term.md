

# Slot: anbefalt_term 


_Føretrukke term/namn for ressursen (skos:prefLabel)._





URI: [skos:prefLabel](http://www.w3.org/2004/02/skos/core#prefLabel)
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
| Slot URI | [skos:prefLabel](http://www.w3.org/2004/02/skos/core#prefLabel) |

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
| self | skos:prefLabel |
| native | https://data.norge.no/linkml/common-ap-no/anbefalt_term |




## LinkML Source

<details>
```yaml
name: anbefalt_term
description: Føretrukke term/namn for ressursen (skos:prefLabel).
from_schema: https://data.norge.no/linkml/common-ap-no
slot_uri: skos:prefLabel
domain_of:
- Begrep
range: LangString
multivalued: true

```
</details>