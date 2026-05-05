

# Slot: algoritme 


_Hash-algoritme brukt for sjekksummen._





URI: [spdx:algorithm](http://spdx.org/rdf/terms#algorithm)
Alias: algoritme

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sjekksum](sjekksum.md) | Ein sjekksum for ein distribusjon |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Sjekksum](sjekksum.md) |
| Slot URI | [spdx:algorithm](http://spdx.org/rdf/terms#algorithm) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | spdx:algorithm |
| native | samtbuskole:algoritme |




## LinkML Source

<details>
```yaml
name: algoritme
description: Hash-algoritme brukt for sjekksummen.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: spdx:algorithm
alias: algoritme
domain_of:
- Sjekksum
range: string

```
</details>