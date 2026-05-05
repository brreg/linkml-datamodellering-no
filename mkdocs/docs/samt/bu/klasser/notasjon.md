

# Slot: notasjon 


_Notasjon/kode for identifikatoren._





URI: [skos:notation](http://www.w3.org/2004/02/skos/core#notation)
Alias: notasjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Identifikator](identifikator.md) | Ein alternativ identifikator for ein ressurs |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Identifikator](identifikator.md) |
| Slot URI | [skos:notation](http://www.w3.org/2004/02/skos/core#notation) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | skos:notation |
| native | samtbuskole:notasjon |




## LinkML Source

<details>
```yaml
name: notasjon
description: Notasjon/kode for identifikatoren.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: skos:notation
alias: notasjon
domain_of:
- Identifikator
range: string

```
</details>