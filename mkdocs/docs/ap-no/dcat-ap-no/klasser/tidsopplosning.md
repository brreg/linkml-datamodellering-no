

# Slot: tidsopplosning 


_Minste tidsoppløysing i datasettet._





URI: [dcat:temporalResolution](http://www.w3.org/ns/dcat#temporalResolution)
Alias: tidsopplosning

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Distribusjon](Distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Duration](Duration.md) |
| Domain Of | [Distribusjon](Distribusjon.md) |
| Slot URI | [dcat:temporalResolution](http://www.w3.org/ns/dcat#temporalResolution) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:temporalResolution |
| native | https://data.norge.no/linkml/dcat-ap-no/tidsopplosning |




## LinkML Source

<details>
```yaml
name: tidsopplosning
description: Minste tidsoppløysing i datasettet.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dcat:temporalResolution
alias: tidsopplosning
domain_of:
- Distribusjon
range: Duration

```
</details>