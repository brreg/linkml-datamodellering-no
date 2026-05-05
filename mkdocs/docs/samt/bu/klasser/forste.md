

# Slot: forste 


_Første datasett i ei datasettserie._





URI: [dcat:first](http://www.w3.org/ns/dcat#first)
Alias: forste

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasettserie](datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datasett](datasett.md) |
| Domain Of | [Datasettserie](datasettserie.md) |
| Slot URI | [dcat:first](http://www.w3.org/ns/dcat#first) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:first |
| native | samtbuskole:forste |




## LinkML Source

<details>
```yaml
name: forste
description: Første datasett i ei datasettserie.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dcat:first
alias: forste
domain_of:
- Datasettserie
range: Datasett

```
</details>