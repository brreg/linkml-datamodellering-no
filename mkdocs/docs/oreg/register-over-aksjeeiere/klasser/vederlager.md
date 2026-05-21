

# Slot: vederlager 


_Samling av vederlag._





URI: [aksje:vederlager](https://example.no/ontology/aksje#vederlager)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Containerklasse](containerklasse.md) | Containerklasse for alle forretningsobjekt i modellen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Vederlag](vederlag.md) |
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
| self | aksje:vederlager |
| native | aksje:vederlager |




## LinkML Source

<details>
```yaml
name: vederlager
description: Samling av vederlag.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
domain: Containerklasse
domain_of:
- Containerklasse
range: Vederlag
multivalued: true
inlined: true
inlined_as_list: true

```
</details>