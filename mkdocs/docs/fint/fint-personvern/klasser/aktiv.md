

# Slot: aktiv 


_Status på behandling._





URI: [pvn:aktiv](https://schema.fintlabs.no/personvern/aktiv)
Alias: aktiv

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Behandling](Behandling.md) | All bruk av personopplysningar (behandlingsaktivitet) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [Behandling](Behandling.md) |
| Slot URI | [pvn:aktiv](https://schema.fintlabs.no/personvern/aktiv) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Behandling](Behandling.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pvn:aktiv |
| native | https://schema.fintlabs.no/personvern/:aktiv |




## LinkML Source

<details>
```yaml
name: aktiv
description: Status på behandling.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: pvn:aktiv
alias: aktiv
owner: Behandling
domain_of:
- Behandling
range: boolean
required: true

```
</details>