

# Slot: aksjeposter 


_Samling av aksjepostar._





URI: [aksje:aksjeposter](https://example.no/ontology/aksje#aksjeposter)
Alias: aksjeposter

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Containerklasse](containerklasse.md) | Containerklasse for alle forretningsobjekt i modellen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Aksjepost](aksjepost.md) |
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
| self | aksje:aksjeposter |
| native | aksje:aksjeposter |




## LinkML Source

<details>
```yaml
name: aksjeposter
description: Samling av aksjepostar.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
domain: Containerklasse
alias: aksjeposter
domain_of:
- Containerklasse
range: Aksjepost
multivalued: true
inlined: true
inlined_as_list: true

```
</details>