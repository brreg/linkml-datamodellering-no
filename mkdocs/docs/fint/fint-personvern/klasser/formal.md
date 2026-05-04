

# Slot: formal 


_Grunngjeving for behandling av personopplysning._





URI: [pvn:formal](https://schema.fintlabs.no/personvern/formal)
Alias: formal

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Behandling](Behandling.md) | All bruk av personopplysningar (behandlingsaktivitet) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Behandling](Behandling.md) |
| Slot URI | [pvn:formal](https://schema.fintlabs.no/personvern/formal) |

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
| self | pvn:formal |
| native | https://schema.fintlabs.no/personvern/:formal |




## LinkML Source

<details>
```yaml
name: formal
description: Grunngjeving for behandling av personopplysning.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: pvn:formal
alias: formal
owner: Behandling
domain_of:
- Behandling
range: string
required: true

```
</details>