

# Slot: aksjekapitaler 


_Samling av aksjekapitalar._





URI: [aksje:aksjekapitaler](https://example.no/ontology/aksje#aksjekapitaler)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Containerklasse](containerklasse.md) | Containerklasse for alle forretningsobjekt i modellen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Aksjekapital](aksjekapital.md) |
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
| self | aksje:aksjekapitaler |
| native | aksje:aksjekapitaler |




## LinkML Source

<details>
```yaml
name: aksjekapitaler
description: Samling av aksjekapitalar.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
domain: Containerklasse
domain_of:
- Containerklasse
range: Aksjekapital
multivalued: true
inlined: true
inlined_as_list: true

```
</details>