

# Slot: rektorer 


_Container slot for å legge tilrette for å kunne ha fleire instanser av rektor i ei datafil._





URI: [samtbuskole:rektorer](https://example.no/ontology/skole#rektorer)
Alias: rektorer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Containerklasse](containerklasse.md) | Containerklasse for alle klasser som kan inngå i datasettet |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Rektor](rektor.md) |
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
| self | samtbuskole:rektorer |
| native | samtbuskole:rektorer |




## LinkML Source

<details>
```yaml
name: rektorer
description: Container slot for å legge tilrette for å kunne ha fleire instanser av
  rektor i ei datafil.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
alias: rektorer
domain_of:
- Containerklasse
range: Rektor
multivalued: true
inlined: true
inlined_as_list: true

```
</details>