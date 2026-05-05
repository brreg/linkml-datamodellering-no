

# Slot: start 


_Frå tidspunkt._





URI: [fint:start](https://schema.fintlabs.no/start)
Alias: start

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Periode](periode.md) | Tidsperiode med obligatorisk start og valfri slutt |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](datetime.md) |
| Domain Of | [Periode](periode.md) |
| Slot URI | [fint:start](https://schema.fintlabs.no/start) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Periode](periode.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:start |
| native | https://schema.fintlabs.no/ressurs/:start |




## LinkML Source

<details>
```yaml
name: start
description: Frå tidspunkt.
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: fint:start
alias: start
owner: Periode
domain_of:
- Periode
range: datetime
required: true

```
</details>