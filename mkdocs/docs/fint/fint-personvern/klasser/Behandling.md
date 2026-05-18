

# Slot: behandling 


_Behandlingsaktivitet._





URI: [pvn:behandling](https://schema.fintlabs.no/personvern/behandling)
Alias: behandling

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tjeneste](tjeneste.md) | Teneste eller system som behandlar personopplysningar |  yes  |
| [Samtykke](samtykke.md) | Tillating til behandling av personopplysning |  yes  |






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


* from schema: https://data.norge.no/linkml/fint-personvern




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
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: pvn:behandling
alias: behandling
domain_of:
- Samtykke
- Tjeneste
range: Behandling

```
</details>