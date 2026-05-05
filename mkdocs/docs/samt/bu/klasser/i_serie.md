

# Slot: i_serie 


_Datasettserie dette datasettet er ein del av._





URI: [dcat:inSeries](http://www.w3.org/ns/dcat#inSeries)
Alias: i_serie

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datasettserie](datasettserie.md) |
| Domain Of | [Datasett](datasett.md) |
| Slot URI | [dcat:inSeries](http://www.w3.org/ns/dcat#inSeries) |

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
| self | dcat:inSeries |
| native | samtbuskole:i_serie |




## LinkML Source

<details>
```yaml
name: i_serie
description: Datasettserie dette datasettet er ein del av.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dcat:inSeries
alias: i_serie
domain_of:
- Datasett
range: Datasettserie
multivalued: true

```
</details>