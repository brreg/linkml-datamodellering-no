

# Slot: slutt 


_Til tidspunkt._





URI: [fint:slutt](https://schema.fintlabs.no/slutt)
Alias: slutt

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
| Slot URI | [fint:slutt](https://schema.fintlabs.no/slutt) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Periode](periode.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:slutt |
| native | https://schema.fintlabs.no/okonomi/:slutt |




## LinkML Source

<details>
```yaml
name: slutt
description: Til tidspunkt.
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: fint:slutt
alias: slutt
owner: Periode
domain_of:
- Periode
range: datetime

```
</details>