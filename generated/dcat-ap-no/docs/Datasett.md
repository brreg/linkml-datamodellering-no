

# Slot: datasett 


_Datasett som er del av katalogen._





URI: [dcat:dataset](http://www.w3.org/ns/dcat#dataset)
Alias: datasett

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) | Rotklasse for DCAT-AP-NO-datafiler |  no  |
| [Katalog](Katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datasett](Datasett.md) |
| Domain Of | [Container](Container.md), [Katalog](Katalog.md) |
| Slot URI | [dcat:dataset](http://www.w3.org/ns/dcat#dataset) |

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
| self | dcat:dataset |
| native | https://data.norge.no/linkml/dcat-ap-no/datasett |




## LinkML Source

<details>
```yaml
name: datasett
description: Datasett som er del av katalogen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dcat:dataset
alias: datasett
domain_of:
- Container
- Katalog
range: Datasett
multivalued: true

```
</details>