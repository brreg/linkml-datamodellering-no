

# Slot: filnavn 


_Namn på bilagets fil._





URI: [okn:filnavn](https://schema.fintlabs.no/okonomi/filnavn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bilag](bilag.md) | Dokumentasjon til ein transaksjon (kompleks datatype) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Bilag](bilag.md) |
| Slot URI | [okn:filnavn](https://schema.fintlabs.no/okonomi/filnavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:filnavn |
| native | https://schema.fintlabs.no/okonomi/:filnavn |




## LinkML Source

<details>
```yaml
name: filnavn
description: Namn på bilagets fil.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:filnavn
domain_of:
- Bilag
range: string

```
</details>