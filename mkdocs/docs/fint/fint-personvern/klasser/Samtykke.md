

# Slot: samtykke 


_Samtykker tilknytt ei behandling._





URI: [pvn:samtykke](https://schema.fintlabs.no/personvern/samtykke)
Alias: samtykke

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Behandling](behandling.md) | All bruk av personopplysningar (behandlingsaktivitet) |  no  |






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
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Behandling](behandling.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-personvern




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
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: pvn:samtykke
alias: samtykke
owner: Behandling
domain_of:
- Behandling
range: Samtykke
multivalued: true

```
</details>