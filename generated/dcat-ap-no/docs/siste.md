

# Slot: siste 


_Siste datasett i ei datasettserie._





URI: [dcat:last](http://www.w3.org/ns/dcat#last)
Alias: siste

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasettserie](Datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datasett](Datasett.md) |
| Domain Of | [Datasettserie](Datasettserie.md) |
| Slot URI | [dcat:last](http://www.w3.org/ns/dcat#last) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:last |
| native | https://data.norge.no/linkml/dcat-ap-no/siste |




## LinkML Source

<details>
```yaml
name: siste
description: Siste datasett i ei datasettserie.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dcat:last
alias: siste
domain_of:
- Datasettserie
range: Datasett

```
</details>