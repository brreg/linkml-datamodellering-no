

# Slot: sats 


_Sats for merverdiavgift._





URI: [okn:sats](https://schema.fintlabs.no/okonomi/sats)
Alias: sats

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Merverdiavgift](merverdiavgift.md) | Kodeverk for merverdiavgifter |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](integer.md) |
| Domain Of | [Merverdiavgift](merverdiavgift.md) |
| Slot URI | [okn:sats](https://schema.fintlabs.no/okonomi/sats) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Merverdiavgift](merverdiavgift.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:sats |
| native | https://schema.fintlabs.no/okonomi/:sats |




## LinkML Source

<details>
```yaml
name: sats
description: Sats for merverdiavgift.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:sats
alias: sats
owner: Merverdiavgift
domain_of:
- Merverdiavgift
range: integer
required: true

```
</details>