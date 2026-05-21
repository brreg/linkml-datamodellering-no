

# Slot: eierposisjoner 


_Samling av eigarposisjonar._





URI: [aksje:eierposisjoner](https://example.no/ontology/aksje#eierposisjoner)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Containerklasse](containerklasse.md) | Containerklasse for alle forretningsobjekt i modellen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Eierposisjon](eierposisjon.md) |
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
| self | aksje:eierposisjoner |
| native | aksje:eierposisjoner |




## LinkML Source

<details>
```yaml
name: eierposisjoner
description: Samling av eigarposisjonar.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
domain: Containerklasse
domain_of:
- Containerklasse
range: Eierposisjon
multivalued: true
inlined: true
inlined_as_list: true

```
</details>