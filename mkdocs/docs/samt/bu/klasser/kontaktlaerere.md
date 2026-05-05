

# Slot: kontaktlaerere 


_Container slot for å legge tilrette for å kunne ha fleire instanser av kontaktlaerer i ei datafil._





URI: [samtbuskole:kontaktlaerere](https://example.no/ontology/skole#kontaktlaerere)
Alias: kontaktlaerere

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Containerklasse](containerklasse.md) | Containerklasse for alle klasser som kan inngå i datasettet |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kontaktlaerer](kontaktlaerer.md) |
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
| self | samtbuskole:kontaktlaerere |
| native | samtbuskole:kontaktlaerere |




## LinkML Source

<details>
```yaml
name: kontaktlaerere
description: Container slot for å legge tilrette for å kunne ha fleire instanser av
  kontaktlaerer i ei datafil.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
alias: kontaktlaerere
domain_of:
- Containerklasse
range: Kontaktlaerer
multivalued: true
inlined: true
inlined_as_list: true

```
</details>