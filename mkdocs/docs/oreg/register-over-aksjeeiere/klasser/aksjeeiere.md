

# Slot: aksjeeiere 


_Samling av aksjeeigarar._





URI: [aksje:aksjeeiere](https://example.no/ontology/aksje#aksjeeiere)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Containerklasse](containerklasse.md) | Containerklasse for alle forretningsobjekt i modellen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Aksjeeier](aksjeeier.md) |
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
| self | aksje:aksjeeiere |
| native | aksje:aksjeeiere |




## LinkML Source

<details>
```yaml
name: aksjeeiere
description: Samling av aksjeeigarar.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
domain: Containerklasse
domain_of:
- Containerklasse
range: Aksjeeier
multivalued: true
inlined: true
inlined_as_list: true

```
</details>