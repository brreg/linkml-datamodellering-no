

# Slot: tidsopplosning 


_Minste tidsoppløysing i datasettet._





URI: [dcat:temporalResolution](http://www.w3.org/ns/dcat#temporalResolution)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett. |  yes  |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Duration](duration.md) |
| Domain Of | [Distribusjon](distribusjon.md), [Datasett](datasett.md) |
| Slot URI | [dcat:temporalResolution](http://www.w3.org/ns/dcat#temporalResolution) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:temporalResolution |
| native | https://data.norge.no/ap-no/dcat-ap-no/tidsopplosning |




## LinkML Source

<details>
```yaml
name: tidsopplosning
description: Minste tidsoppløysing i datasettet.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
slot_uri: dcat:temporalResolution
domain_of:
- Distribusjon
- Datasett
range: Duration

```
</details>