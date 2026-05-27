

# Slot: samtykke 


_Samtykker tilknytt ei behandling._





URI: [pvn:samtykke](https://schema.fintlabs.no/personvern/samtykke)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Behandling](behandling.md) | All bruk av personopplysningar (behandlingsaktivitet) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Samtykke](samtykke.md) |
| Domain Of | [Behandling](behandling.md) |
| Slot URI | [pvn:samtykke](https://schema.fintlabs.no/personvern/samtykke) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pvn:samtykke |
| native | https://schema.fintlabs.no/personvern/:samtykke |




## LinkML Source

<details>
```yaml
name: samtykke
description: Samtykker tilknytt ei behandling.
from_schema: https://data.norge.no/fint/fint-personvern
rank: 1000
slot_uri: pvn:samtykke
domain_of:
- Behandling
range: Samtykke
multivalued: true

```
</details>