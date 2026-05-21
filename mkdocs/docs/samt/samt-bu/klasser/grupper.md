

# Slot: grupper 


_Grupper knytt til datasettet._





URI: [samtbuskole:grupper](https://example.no/ontology/skole#grupper)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Containerklasse](containerklasse.md) | Containerklasse for alle klasser som kan inngå i datasettet |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Aktor](aktor.md) |
| Domain Of | [Containerklasse](containerklasse.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | samtbuskole:grupper |
| native | samtbuskole:grupper |




## LinkML Source

<details>
```yaml
name: grupper
description: Grupper knytt til datasettet.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
domain_of:
- Containerklasse
range: Aktor
multivalued: true
inlined: true
inlined_as_list: true

```
</details>