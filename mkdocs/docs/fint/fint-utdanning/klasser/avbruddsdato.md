

# Slot: avbruddsdato 


_Dato for avbrot frå opplæring._





URI: [utd:avbruddsdato](https://schema.fintlabs.no/utdanning/avbruddsdato)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:date](http://www.w3.org/2001/XMLSchema#date) |
| Domain Of | [Elevforhold](elevforhold.md) |
| Slot URI | [utd:avbruddsdato](https://schema.fintlabs.no/utdanning/avbruddsdato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:avbruddsdato |
| native | https://schema.fintlabs.no/utdanning/:avbruddsdato |




## LinkML Source

<details>
```yaml
name: avbruddsdato
description: Dato for avbrot frå opplæring.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:avbruddsdato
domain_of:
- Elevforhold
range: date

```
</details>