

# Slot: utdelinger 


_Samling av utdelingar._





URI: [aksje:utdelinger](https://example.no/ontology/aksje#utdelinger)
Alias: utdelinger

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Containerklasse](Containerklasse.md) | Containerklasse for alle forretningsobjekt i modellen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Utdeling](Utdeling.md) |
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
| self | aksje:utdelinger |
| native | aksje:utdelinger |




## LinkML Source

<details>
```yaml
name: utdelinger
description: Samling av utdelingar.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
domain: Containerklasse
alias: utdelinger
domain_of:
- Containerklasse
range: Utdeling
multivalued: true
inlined: true
inlined_as_list: true

```
</details>