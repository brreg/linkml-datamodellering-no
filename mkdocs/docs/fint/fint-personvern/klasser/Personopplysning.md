

# Slot: personopplysning 


_Opplysning eller vurdering som kan knytast til ein enkeltperson._





URI: [pvn:personopplysning](https://schema.fintlabs.no/personvern/personopplysning)
Alias: personopplysning

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Behandling](Behandling.md) | All bruk av personopplysningar (behandlingsaktivitet) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personopplysning](Personopplysning.md) |
| Domain Of | [Behandling](Behandling.md) |
| Slot URI | [pvn:personopplysning](https://schema.fintlabs.no/personvern/personopplysning) |

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
| self | pvn:personopplysning |
| native | https://schema.fintlabs.no/personvern/:personopplysning |




## LinkML Source

<details>
```yaml
name: personopplysning
description: Opplysning eller vurdering som kan knytast til ein enkeltperson.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: pvn:personopplysning
alias: personopplysning
owner: Behandling
domain_of:
- Behandling
range: Personopplysning
required: true

```
</details>