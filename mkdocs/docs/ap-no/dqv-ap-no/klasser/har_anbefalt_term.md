

# Slot: har_anbefalt_term 


_Føretrekt term/namn for dimensjonen eller målet._





URI: [skos:prefLabel](http://www.w3.org/2004/02/skos/core#prefLabel)
Alias: har_anbefalt_term

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kvalitetsdimensjon](kvalitetsdimensjon.md) | Ein kvalitetsdimensjon som grupperer relaterte kvalitetsmål |  yes  |
| [Kvalitetsmaal](kvalitetsmaal.md) | Eit kvalitetsmål som operasjonaliserer ein kvalitetsdeldimensjon |  yes  |
| [Kvalitetsdeldimensjon](kvalitetsdeldimensjon.md) | Ein deldimensjon av ein kvalitetsdimensjon |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](langstring.md) |
| Domain Of | [Kvalitetsdimensjon](kvalitetsdimensjon.md), [Kvalitetsmaal](kvalitetsmaal.md) |
| Slot URI | [skos:prefLabel](http://www.w3.org/2004/02/skos/core#prefLabel) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | skos:prefLabel |
| native | https://data.norge.no/linkml/dqv-ap-no/har_anbefalt_term |




## LinkML Source

<details>
```yaml
name: har_anbefalt_term
description: Føretrekt term/namn for dimensjonen eller målet.
from_schema: https://data.norge.no/linkml/dqv-ap-no
rank: 1000
slot_uri: skos:prefLabel
alias: har_anbefalt_term
domain_of:
- Kvalitetsdimensjon
- Kvalitetsmaal
range: LangString
multivalued: true

```
</details>