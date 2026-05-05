

# Slot: fylker 


_Container slot for å legge tilrette for å kunne ha fleire instanser av fylke i ei datafil._





URI: [samtbuskole:fylker](https://example.no/ontology/skole#fylker)
Alias: fylker

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Containerklasse](containerklasse.md) | Containerklasse for alle klasser som kan inngå i datasettet |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fylke](fylke.md) |
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
| self | samtbuskole:fylker |
| native | samtbuskole:fylker |




## LinkML Source

<details>
```yaml
name: fylker
description: Container slot for å legge tilrette for å kunne ha fleire instanser av
  fylke i ei datafil.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
alias: fylker
domain_of:
- Containerklasse
range: Fylke
multivalued: true
inlined: true
inlined_as_list: true

```
</details>