

# Slot: har_definisjon 


_Definisjon av dimensjonen eller målet._





URI: [skos:definition](http://www.w3.org/2004/02/skos/core#definition)
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
| Slot URI | [skos:definition](http://www.w3.org/2004/02/skos/core#definition) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | skos:definition |
| native | https://data.norge.no/ap-no/dqv-ap-no/har_definisjon |




## LinkML Source

<details>
```yaml
name: har_definisjon
description: Definisjon av dimensjonen eller målet.
from_schema: https://data.norge.no/ap-no/dqv-ap-no
rank: 1000
slot_uri: skos:definition
domain_of:
- Kvalitetsdimensjon
- Kvalitetsmaal
range: LangString
multivalued: true

```
</details>