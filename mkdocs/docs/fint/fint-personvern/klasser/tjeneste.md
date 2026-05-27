

# Slot: tjeneste 


_Tenesta som behandlinga tilhøyrer._





URI: [pvn:tjeneste](https://schema.fintlabs.no/personvern/tjeneste)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Behandling](behandling.md) | All bruk av personopplysningar (behandlingsaktivitet) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Tjeneste](tjeneste.md) |
| Domain Of | [Behandling](behandling.md) |
| Slot URI | [pvn:tjeneste](https://schema.fintlabs.no/personvern/tjeneste) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pvn:tjeneste |
| native | https://schema.fintlabs.no/personvern/:tjeneste |




## LinkML Source

<details>
```yaml
name: tjeneste
description: Tenesta som behandlinga tilhøyrer.
from_schema: https://data.norge.no/fint/fint-personvern
rank: 1000
slot_uri: pvn:tjeneste
domain_of:
- Behandling
range: Tjeneste

```
</details>