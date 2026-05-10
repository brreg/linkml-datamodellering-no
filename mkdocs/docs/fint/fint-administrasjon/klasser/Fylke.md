

# Slot: fylke 


_Fylke._





URI: [fint:fylke](https://schema.fintlabs.no/fylke)
Alias: fylke

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  yes  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fylke](fylke.md) |
| Domain Of | [Kommune](kommune.md), [AdministrasjonContainer](administrasjoncontainer.md) |
| Slot URI | [fint:fylke](https://schema.fintlabs.no/fylke) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:fylke |
| native | https://schema.fintlabs.no/:fylke |




## LinkML Source

<details>
```yaml
name: fylke
description: Fylke.
from_schema: https://data.norge.no/linkml/fint-common
slot_uri: fint:fylke
alias: fylke
domain_of:
- Kommune
- AdministrasjonContainer
range: Fylke

```
</details>