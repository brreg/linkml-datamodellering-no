

# Slot: kommuner 


_Container slot for å legge tilrette for å kunne ha fleire instanser av kommune i ei datafil._





URI: [samtbuskole:kommuner](https://example.no/ontology/skole#kommuner)
Alias: kommuner

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Containerklasse](containerklasse.md) | Containerklasse for alle klasser som kan inngå i datasettet |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kommune](kommune.md) |
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
| self | samtbuskole:kommuner |
| native | samtbuskole:kommuner |




## LinkML Source

<details>
```yaml
name: kommuner
description: Container slot for å legge tilrette for å kunne ha fleire instanser av
  kommune i ei datafil.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
alias: kommuner
domain_of:
- Containerklasse
range: Kommune
multivalued: true
inlined: true
inlined_as_list: true

```
</details>