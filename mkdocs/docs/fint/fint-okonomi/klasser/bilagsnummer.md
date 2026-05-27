

# Slot: bilagsnummer 


_Nummer på bilaget._





URI: [okn:bilagsnummer](https://schema.fintlabs.no/okonomi/bilagsnummer)
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
| Slot URI | [okn:bilagsnummer](https://schema.fintlabs.no/okonomi/bilagsnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:bilagsnummer |
| native | https://schema.fintlabs.no/okonomi/:bilagsnummer |




## LinkML Source

<details>
```yaml
name: bilagsnummer
description: Nummer på bilaget.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:bilagsnummer
domain_of:
- Bilag
range: string

```
</details>