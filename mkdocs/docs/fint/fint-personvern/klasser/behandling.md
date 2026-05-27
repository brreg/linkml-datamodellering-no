

# Slot: behandling 


_Behandlingsaktivitet._





URI: [pvn:behandling](https://schema.fintlabs.no/personvern/behandling)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Samtykke](samtykke.md) | Tillating til behandling av personopplysning |  yes  |
| [Tjeneste](tjeneste.md) | Teneste eller system som behandlar personopplysningar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Behandling](behandling.md) |
| Domain Of | [Samtykke](samtykke.md), [Tjeneste](tjeneste.md) |
| Slot URI | [pvn:behandling](https://schema.fintlabs.no/personvern/behandling) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pvn:behandling |
| native | https://schema.fintlabs.no/personvern/:behandling |




## LinkML Source

<details>
```yaml
name: behandling
description: Behandlingsaktivitet.
from_schema: https://data.norge.no/fint/fint-personvern
rank: 1000
slot_uri: pvn:behandling
domain_of:
- Samtykke
- Tjeneste
range: Behandling

```
</details>