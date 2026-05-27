

# Slot: endretDato 


_Dato og tidspunkt for endringa._





URI: [utd:endretDato](https://schema.fintlabs.no/utdanning/endretDato)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Karakterhistorie](karakterhistorie.md) | Historikk over endringar i ein karakter |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) |
| Domain Of | [Karakterhistorie](karakterhistorie.md) |
| Slot URI | [utd:endretDato](https://schema.fintlabs.no/utdanning/endretDato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:endretDato |
| native | https://schema.fintlabs.no/utdanning/:endretDato |




## LinkML Source

<details>
```yaml
name: endretDato
description: Dato og tidspunkt for endringa.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:endretDato
domain_of:
- Karakterhistorie
range: datetime

```
</details>