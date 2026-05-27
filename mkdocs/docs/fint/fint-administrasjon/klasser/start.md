

# Slot: start 


_Frå tidspunkt._





URI: [fint:start](https://schema.fintlabs.no/start)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Periode](periode.md) | Tidsperiode med obligatorisk start og valfri slutt |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) |
| Domain Of | [Periode](periode.md) |
| Slot URI | [fint:start](https://schema.fintlabs.no/start) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:start |
| native | https://schema.fintlabs.no/:start |




## LinkML Source

<details>
```yaml
name: start
description: Frå tidspunkt.
from_schema: https://data.norge.no/fint/fint-common
slot_uri: fint:start
domain_of:
- Periode
range: datetime

```
</details>