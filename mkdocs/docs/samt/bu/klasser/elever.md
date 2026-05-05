

# Slot: elever 


_Container slot for å legge tilrette for å kunne ha fleire instanser av elev i ei datafil._





URI: [samtbuskole:elever](https://example.no/ontology/skole#elever)
Alias: elever

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Containerklasse](containerklasse.md) | Containerklasse for alle klasser som kan inngå i datasettet |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Elev](elev.md) |
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
| self | samtbuskole:elever |
| native | samtbuskole:elever |




## LinkML Source

<details>
```yaml
name: elever
description: Container slot for å legge tilrette for å kunne ha fleire instanser av
  elev i ei datafil.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
alias: elever
domain_of:
- Containerklasse
range: Elev
multivalued: true
inlined: true
inlined_as_list: true

```
</details>