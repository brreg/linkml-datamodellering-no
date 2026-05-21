

# Slot: selskapshendelser 


_Samling av selskapshendingar._





URI: [aksje:selskapshendelser](https://example.no/ontology/aksje#selskapshendelser)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Containerklasse](containerklasse.md) | Containerklasse for alle forretningsobjekt i modellen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Selskapshendelse](selskapshendelse.md) |
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
| self | aksje:selskapshendelser |
| native | aksje:selskapshendelser |




## LinkML Source

<details>
```yaml
name: selskapshendelser
description: Samling av selskapshendingar.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
domain: Containerklasse
domain_of:
- Containerklasse
range: Selskapshendelse
multivalued: true
inlined: true
inlined_as_list: true

```
</details>