

# Slot: definisjon 


_Direkte definisjon som fritekst (skos:definition)._





URI: [skos:definition](http://www.w3.org/2004/02/skos/core#definition)
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
| Slot URI | [skos:definition](http://www.w3.org/2004/02/skos/core#definition) |

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
| self | skos:definition |
| native | https://data.norge.no/linkml/skos-ap-no/definisjon |




## LinkML Source

<details>
```yaml
name: definisjon
description: Direkte definisjon som fritekst (skos:definition).
from_schema: https://data.norge.no/linkml/skos-ap-no
slot_uri: skos:definition
domain_of:
- Begrep
range: LangString
multivalued: true

```
</details>