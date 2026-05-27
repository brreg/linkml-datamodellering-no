

# Slot: aktiv 


_Status på behandling._





URI: [pvn:aktiv](https://schema.fintlabs.no/personvern/aktiv)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Behandling](behandling.md) | All bruk av personopplysningar (behandlingsaktivitet) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) |
| Domain Of | [Behandling](behandling.md) |
| Slot URI | [pvn:aktiv](https://schema.fintlabs.no/personvern/aktiv) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-personvern




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
from_schema: https://data.norge.no/fint/fint-personvern
rank: 1000
slot_uri: pvn:aktiv
domain_of:
- Behandling
range: boolean

```
</details>