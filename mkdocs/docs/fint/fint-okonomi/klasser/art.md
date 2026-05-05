

# Slot: art 


_Artskonto (type utgift/inntekt)._





URI: [okn:art](https://schema.fintlabs.no/okonomi/art)
Alias: art

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontostreng](kontostreng.md) | Kontodimensjonar for ei postering (kompleks datatype) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Kontostreng](kontostreng.md) |
| Slot URI | [okn:art](https://schema.fintlabs.no/okonomi/art) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Kontostreng](kontostreng.md) |








## In Subsets


* [Anbefalt](anbefalt.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:art |
| native | https://schema.fintlabs.no/okonomi/:art |




## LinkML Source

<details>
```yaml
name: art
description: Artskonto (type utgift/inntekt).
in_subset:
- Anbefalt
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:art
alias: art
owner: Kontostreng
domain_of:
- Kontostreng
range: string

```
</details>