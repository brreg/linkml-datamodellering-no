

# Slot: slettet 


_Tidspunkt ressursen er sletta._





URI: [pvn:slettet](https://schema.fintlabs.no/personvern/slettet)
Alias: slettet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Behandling](behandling.md) | All bruk av personopplysningar (behandlingsaktivitet) |  yes  |
| [Tjeneste](tjeneste.md) | Teneste eller system som behandlar personopplysningar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) |
| Domain Of | [Behandling](behandling.md), [Tjeneste](tjeneste.md) |
| Slot URI | [pvn:slettet](https://schema.fintlabs.no/personvern/slettet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pvn:slettet |
| native | https://schema.fintlabs.no/personvern/:slettet |




## LinkML Source

<details>
```yaml
name: slettet
description: Tidspunkt ressursen er sletta.
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: pvn:slettet
alias: slettet
domain_of:
- Behandling
- Tjeneste
range: datetime

```
</details>