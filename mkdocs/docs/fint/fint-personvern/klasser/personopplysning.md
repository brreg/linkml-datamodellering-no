

# Slot: personopplysning 


_Opplysning eller vurdering som kan knytast til ein enkeltperson._





URI: [pvn:personopplysning](https://schema.fintlabs.no/personvern/personopplysning)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Behandling](behandling.md) | All bruk av personopplysningar (behandlingsaktivitet) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personopplysning](personopplysning.md) |
| Domain Of | [Behandling](behandling.md) |
| Slot URI | [pvn:personopplysning](https://schema.fintlabs.no/personvern/personopplysning) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-personvern




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
from_schema: https://data.norge.no/fint/fint-personvern
rank: 1000
slot_uri: pvn:personopplysning
domain_of:
- Behandling
range: Personopplysning

```
</details>