

# Slot: tidsopplosning 


_Minste tidsoppløysing i datasettet._





URI: [dcat:temporalResolution](http://www.w3.org/ns/dcat#temporalResolution)
Alias: tidsopplosning

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Duration](duration.md) |
| Domain Of | [Distribusjon](distribusjon.md) |
| Slot URI | [dcat:temporalResolution](http://www.w3.org/ns/dcat#temporalResolution) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:temporalResolution |
| native | samtbuskole:tidsopplosning |




## LinkML Source

<details>
```yaml
name: tidsopplosning
description: Minste tidsoppløysing i datasettet.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dcat:temporalResolution
alias: tidsopplosning
domain_of:
- Distribusjon
range: Duration

```
</details>