

# Slot: alternativ_term 


_Alternativ term for kodeelementet (skos:altLabel)._





URI: [skos:altLabel](http://www.w3.org/2004/02/skos/core#altLabel)
Alias: alternativ_term

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kodeelement](Kodeelement.md) | Eit element i ei kodeliste (modelldcatno:CodeElement) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](LangString.md) |
| Domain Of | [Kodeelement](Kodeelement.md) |
| Slot URI | [skos:altLabel](http://www.w3.org/2004/02/skos/core#altLabel) |

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
| self | skos:altLabel |
| native | https://data.norge.no/linkml/modelldcat-ap-no/alternativ_term |




## LinkML Source

<details>
```yaml
name: alternativ_term
description: Alternativ term for kodeelementet (skos:altLabel).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: skos:altLabel
alias: alternativ_term
domain_of:
- Kodeelement
range: LangString
multivalued: true

```
</details>