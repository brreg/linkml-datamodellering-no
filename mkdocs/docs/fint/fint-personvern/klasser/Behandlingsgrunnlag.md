

# Slot: behandlingsgrunnlag 


_Rettsleg grunnlag for behandling av personopplysning._





URI: [pvn:behandlingsgrunnlag](https://schema.fintlabs.no/personvern/behandlingsgrunnlag)
Alias: behandlingsgrunnlag

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Behandling](behandling.md) | All bruk av personopplysningar (behandlingsaktivitet) |  yes  |
| [PersonvernContainer](personverncontainer.md) | Rotcontainer for FINT Personvern-instansar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Behandlingsgrunnlag](behandlingsgrunnlag.md) |
| Domain Of | [PersonvernContainer](personverncontainer.md), [Behandling](behandling.md) |
| Slot URI | [pvn:behandlingsgrunnlag](https://schema.fintlabs.no/personvern/behandlingsgrunnlag) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pvn:behandlingsgrunnlag |
| native | https://schema.fintlabs.no/personvern/:behandlingsgrunnlag |




## LinkML Source

<details>
```yaml
name: behandlingsgrunnlag
description: Rettsleg grunnlag for behandling av personopplysning.
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: pvn:behandlingsgrunnlag
alias: behandlingsgrunnlag
domain_of:
- PersonvernContainer
- Behandling
range: Behandlingsgrunnlag

```
</details>