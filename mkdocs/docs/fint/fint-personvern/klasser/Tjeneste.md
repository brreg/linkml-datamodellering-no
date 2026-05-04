

# Slot: tjeneste 


_Tenesta som behandlinga tilhøyrer._





URI: [pvn:tjeneste](https://schema.fintlabs.no/personvern/tjeneste)
Alias: tjeneste

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Behandling](Behandling.md) | All bruk av personopplysningar (behandlingsaktivitet) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Tjeneste](Tjeneste.md) |
| Domain Of | [Behandling](Behandling.md) |
| Slot URI | [pvn:tjeneste](https://schema.fintlabs.no/personvern/tjeneste) |

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
| self | pvn:tjeneste |
| native | https://schema.fintlabs.no/personvern/:tjeneste |




## LinkML Source

<details>
```yaml
name: tjeneste
description: Tenesta som behandlinga tilhøyrer.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: pvn:tjeneste
alias: tjeneste
owner: Behandling
domain_of:
- Behandling
range: Tjeneste
required: true

```
</details>