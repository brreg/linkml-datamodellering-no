

# Slot: utbytter 


_Samling av utbytte._





URI: [aksje:utbytter](https://example.no/ontology/aksje#utbytter)
Alias: utbytter

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Containerklasse](containerklasse.md) | Containerklasse for alle forretningsobjekt i modellen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Utbytte](utbytte.md) |
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
| self | aksje:utbytter |
| native | aksje:utbytter |




## LinkML Source

<details>
```yaml
name: utbytter
description: Samling av utbytte.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
domain: Containerklasse
alias: utbytter
domain_of:
- Containerklasse
range: Utbytte
multivalued: true
inlined: true
inlined_as_list: true

```
</details>