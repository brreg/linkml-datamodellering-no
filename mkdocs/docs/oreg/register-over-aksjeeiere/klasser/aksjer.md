

# Slot: aksjer 


_Samling av aksjar._





URI: [aksje:aksjer](https://example.no/ontology/aksje#aksjer)
Alias: aksjer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Containerklasse](containerklasse.md) | Containerklasse for alle forretningsobjekt i modellen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Aksje](aksje.md) |
| Domain | [Containerklasse](containerklasse.md) |
| Domain Of | [Containerklasse](containerklasse.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aksje:aksjer |
| native | aksje:aksjer |




## LinkML Source

<details>
```yaml
name: aksjer
description: Samling av aksjar.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
domain: Containerklasse
alias: aksjer
domain_of:
- Containerklasse
range: Aksje
multivalued: true
inlined: true
inlined_as_list: true

```
</details>