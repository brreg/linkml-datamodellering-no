

# Slot: bilagsdato 


_Dato bilaget er registrert._





URI: [okn:bilagsdato](https://schema.fintlabs.no/okonomi/bilagsdato)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bilag](bilag.md) | Dokumentasjon til ein transaksjon (kompleks datatype) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:date](http://www.w3.org/2001/XMLSchema#date) |
| Domain Of | [Bilag](bilag.md) |
| Slot URI | [okn:bilagsdato](https://schema.fintlabs.no/okonomi/bilagsdato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:bilagsdato |
| native | https://schema.fintlabs.no/okonomi/:bilagsdato |




## LinkML Source

<details>
```yaml
name: bilagsdato
description: Dato bilaget er registrert.
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
slot_uri: okn:bilagsdato
domain_of:
- Bilag
range: date

```
</details>