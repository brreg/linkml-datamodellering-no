

# Slot: debet 


_Angir om posteringa er debet eller kredit._





URI: [okn:debet](https://schema.fintlabs.no/okonomi/debet)
Alias: debet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Postering](Postering.md) | Føring på ein konto i rekneskapet |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [Postering](Postering.md) |
| Slot URI | [okn:debet](https://schema.fintlabs.no/okonomi/debet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Postering](Postering.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:debet |
| native | https://schema.fintlabs.no/okonomi/:debet |




## LinkML Source

<details>
```yaml
name: debet
description: Angir om posteringa er debet eller kredit.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:debet
alias: debet
owner: Postering
domain_of:
- Postering
range: boolean
required: true

```
</details>