

# Slot: datasett 


_Datasett som er del av katalogen._





URI: [dcat:dataset](http://www.w3.org/ns/dcat#dataset)
Alias: datasett

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datasett](datasett.md) |
| Domain Of | [Katalog](katalog.md) |
| Slot URI | [dcat:dataset](http://www.w3.org/ns/dcat#dataset) |

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
| self | dcat:dataset |
| native | samtbuskole:datasett |




## LinkML Source

<details>
```yaml
name: datasett
description: Datasett som er del av katalogen.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dcat:dataset
alias: datasett
domain_of:
- Katalog
range: Datasett
multivalued: true

```
</details>