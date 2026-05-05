

# Slot: datasettdistribusjon 


_Tilgjengelege distribusjonar av datasettet._





URI: [dcat:distribution](http://www.w3.org/ns/dcat#distribution)
Alias: datasettdistribusjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Distribusjon](distribusjon.md) |
| Domain Of | [Datasett](datasett.md) |
| Slot URI | [dcat:distribution](http://www.w3.org/ns/dcat#distribution) |

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
| self | dcat:distribution |
| native | samtbuskole:datasettdistribusjon |




## LinkML Source

<details>
```yaml
name: datasettdistribusjon
description: Tilgjengelege distribusjonar av datasettet.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dcat:distribution
alias: datasettdistribusjon
domain_of:
- Datasett
range: Distribusjon
multivalued: true

```
</details>