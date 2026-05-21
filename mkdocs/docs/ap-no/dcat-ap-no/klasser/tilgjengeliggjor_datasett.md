

# Slot: tilgjengeliggjor_datasett 


_Datasett som datatjenesten tilgjengeleggjer._





URI: [dcat:servesDataset](http://www.w3.org/ns/dcat#servesDataset)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datasett](datasett.md) |
| Domain Of | [Datatjeneste](datatjeneste.md) |
| Slot URI | [dcat:servesDataset](http://www.w3.org/ns/dcat#servesDataset) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:servesDataset |
| native | https://data.norge.no/linkml/dcat-ap-no/tilgjengeliggjor_datasett |




## LinkML Source

<details>
```yaml
name: tilgjengeliggjor_datasett
description: Datasett som datatjenesten tilgjengeleggjer.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dcat:servesDataset
domain_of:
- Datatjeneste
range: Datasett
multivalued: true

```
</details>