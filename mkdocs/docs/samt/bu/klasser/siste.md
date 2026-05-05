

# Slot: siste 


_Siste datasett i ei datasettserie._





URI: [dcat:last](http://www.w3.org/ns/dcat#last)
Alias: siste

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasettserie](datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datasett](datasett.md) |
| Domain Of | [Datasettserie](datasettserie.md) |
| Slot URI | [dcat:last](http://www.w3.org/ns/dcat#last) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:last |
| native | samtbuskole:siste |




## LinkML Source

<details>
```yaml
name: siste
description: Siste datasett i ei datasettserie.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dcat:last
alias: siste
domain_of:
- Datasettserie
range: Datasett

```
</details>