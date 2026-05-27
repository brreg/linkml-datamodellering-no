

# Slot: status 


_OT-status for ungdommen._





URI: [utd:status](https://schema.fintlabs.no/utdanning/status)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtUngdom](otungdom.md) | Eit ungdomsobjekt i oppfølgingstenesta (OT) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OtStatus](otstatus.md) |
| Domain Of | [OtUngdom](otungdom.md) |
| Slot URI | [utd:status](https://schema.fintlabs.no/utdanning/status) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




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
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:status
domain_of:
- OtUngdom
range: OtStatus

```
</details>