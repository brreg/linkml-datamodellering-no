

# Slot: skoler 


_Container slot for å legge tilrette for å kunne ha fleire instanser av skole i ei datafil._





URI: [samtbuskole:skoler](https://example.no/ontology/skole#skoler)
Alias: skoler

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Containerklasse](containerklasse.md) | Containerklasse for alle klasser som kan inngå i datasettet |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Skole](skole.md) |
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
| self | samtbuskole:skoler |
| native | samtbuskole:skoler |




## LinkML Source

<details>
```yaml
name: skoler
description: Container slot for å legge tilrette for å kunne ha fleire instanser av
  skole i ei datafil.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
alias: skoler
domain_of:
- Containerklasse
range: Skole
multivalued: true
inlined: true
inlined_as_list: true

```
</details>