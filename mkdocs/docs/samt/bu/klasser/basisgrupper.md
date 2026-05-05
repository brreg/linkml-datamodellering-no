

# Slot: basisgrupper 


_Container slot for å legge tilrette for å kunne ha fleire instanser av basisgruppe i ei datafil._





URI: [samtbuskole:basisgrupper](https://example.no/ontology/skole#basisgrupper)
Alias: basisgrupper

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Containerklasse](containerklasse.md) | Containerklasse for alle klasser som kan inngå i datasettet |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Basisgruppe](basisgruppe.md) |
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
| self | samtbuskole:basisgrupper |
| native | samtbuskole:basisgrupper |




## LinkML Source

<details>
```yaml
name: basisgrupper
description: Container slot for å legge tilrette for å kunne ha fleire instanser av
  basisgruppe i ei datafil.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
alias: basisgrupper
domain_of:
- Containerklasse
range: Basisgruppe
multivalued: true
inlined: true
inlined_as_list: true

```
</details>