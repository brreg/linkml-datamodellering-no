

# Slot: aksjeklasser 


_Samling av aksjeklasser._





URI: [aksje:aksjeklasser](https://example.no/ontology/aksje#aksjeklasser)
Alias: aksjeklasser

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Containerklasse](Containerklasse.md) | Containerklasse for alle forretningsobjekt i modellen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Aksjeklasse](Aksjeklasse.md) |
| Domain | [Containerklasse](Containerklasse.md) |
| Domain Of | [Containerklasse](Containerklasse.md) |

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
| self | aksje:aksjeklasser |
| native | aksje:aksjeklasser |




## LinkML Source

<details>
```yaml
name: aksjeklasser
description: Samling av aksjeklasser.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
domain: Containerklasse
alias: aksjeklasser
domain_of:
- Containerklasse
range: Aksjeklasse
multivalued: true
inlined: true
inlined_as_list: true

```
</details>