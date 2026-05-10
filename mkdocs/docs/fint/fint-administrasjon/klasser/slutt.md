

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
| Range | [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) |
| Domain Of | [Periode](periode.md) |
| Slot URI | [fint:slutt](https://schema.fintlabs.no/slutt) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:slutt |
| native | https://schema.fintlabs.no/:slutt |




## LinkML Source

<details>
```yaml
name: slutt
description: Til tidspunkt.
from_schema: https://data.norge.no/linkml/fint-common
slot_uri: fint:slutt
alias: slutt
domain_of:
- Periode
range: datetime

```
</details>