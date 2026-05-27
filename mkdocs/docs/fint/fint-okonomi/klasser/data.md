

# Slot: data 


_Bilagets fil, koda som Base64._





URI: [okn:data](https://schema.fintlabs.no/okonomi/data)
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
| Slot URI | [okn:data](https://schema.fintlabs.no/okonomi/data) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:data |
| native | https://schema.fintlabs.no/okonomi/:data |




## LinkML Source

<details>
```yaml
name: data
description: Bilagets fil, koda som Base64.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:data
domain_of:
- Bilag
range: string

```
</details>