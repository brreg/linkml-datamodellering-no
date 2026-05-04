

# Slot: status 


_OT-status for ungdommen._





URI: [utd:status](https://schema.fintlabs.no/utdanning/status)
Alias: status

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtUngdom](OtUngdom.md) | Eit ungdomsobjekt i oppfølgingstenesta (OT) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OtStatus](OtStatus.md) |
| Domain Of | [OtUngdom](OtUngdom.md) |
| Slot URI | [utd:status](https://schema.fintlabs.no/utdanning/status) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [OtUngdom](OtUngdom.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:status |
| native | https://schema.fintlabs.no/utdanning/:status |




## LinkML Source

<details>
```yaml
name: status
description: OT-status for ungdommen.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:status
alias: status
owner: OtUngdom
domain_of:
- OtUngdom
range: OtStatus

```
</details>