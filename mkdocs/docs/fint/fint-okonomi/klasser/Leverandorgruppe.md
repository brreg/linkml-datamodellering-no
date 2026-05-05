

# Slot: leverandorgruppe 


_Gruppe av leverandørar leverandøren tilhøyrer (leverandørgruppe)._





URI: [okn:leverandorgruppe](https://schema.fintlabs.no/okonomi/leverandorgruppe)
Alias: leverandorgruppe

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Leverandor](leverandor.md) | Person eller verksemd som leverer produkt eller tenester (Leverandør) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Leverandorgruppe](leverandorgruppe.md) |
| Domain Of | [Leverandor](leverandor.md) |
| Slot URI | [okn:leverandorgruppe](https://schema.fintlabs.no/okonomi/leverandorgruppe) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Leverandor](leverandor.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:leverandorgruppe |
| native | https://schema.fintlabs.no/okonomi/:leverandorgruppe |




## LinkML Source

<details>
```yaml
name: leverandorgruppe
description: Gruppe av leverandørar leverandøren tilhøyrer (leverandørgruppe).
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:leverandorgruppe
alias: leverandorgruppe
owner: Leverandor
domain_of:
- Leverandor
range: Leverandorgruppe

```
</details>