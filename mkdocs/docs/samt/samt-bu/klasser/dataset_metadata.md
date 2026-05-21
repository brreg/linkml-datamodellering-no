

# Slot: dataset_metadata 


_Metadata om datasettet._





URI: [samtbuskole:dataset_metadata](https://example.no/ontology/skole#dataset_metadata)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Containerklasse](containerklasse.md) | Containerklasse for alle klasser som kan inngå i datasettet |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datasett](datasett.md) |
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
| self | samtbuskole:dataset_metadata |
| native | samtbuskole:dataset_metadata |




## LinkML Source

<details>
```yaml
name: dataset_metadata
description: Metadata om datasettet.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
domain_of:
- Containerklasse
range: Datasett
multivalued: true
inlined: true
inlined_as_list: true

```
</details>