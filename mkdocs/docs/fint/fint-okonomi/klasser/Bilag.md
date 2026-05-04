

# Slot: bilag 


_Bilag til transaksjonen._





URI: [okn:bilag](https://schema.fintlabs.no/okonomi/bilag)
Alias: bilag

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Transaksjon](Transaksjon.md) | Overføring av pengar til eller frå eksterne partar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Bilag](Bilag.md) |
| Domain Of | [Transaksjon](Transaksjon.md) |
| Slot URI | [okn:bilag](https://schema.fintlabs.no/okonomi/bilag) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Transaksjon](Transaksjon.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:bilag |
| native | https://schema.fintlabs.no/okonomi/:bilag |




## LinkML Source

<details>
```yaml
name: bilag
description: Bilag til transaksjonen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:bilag
alias: bilag
owner: Transaksjon
domain_of:
- Transaksjon
range: Bilag
multivalued: true
inlined: true
inlined_as_list: true

```
</details>