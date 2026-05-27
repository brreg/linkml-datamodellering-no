

# Slot: sendt 


_Dato varselet vart sendt._





URI: [utd:sendt](https://schema.fintlabs.no/utdanning/sendt)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Varsel](varsel.md) | Eit varsel knytt til ein elev i ei faggruppe |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:date](http://www.w3.org/2001/XMLSchema#date) |
| Domain Of | [Varsel](varsel.md) |
| Slot URI | [utd:sendt](https://schema.fintlabs.no/utdanning/sendt) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:sendt |
| native | https://schema.fintlabs.no/utdanning/:sendt |




## LinkML Source

<details>
```yaml
name: sendt
description: Dato varselet vart sendt.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:sendt
domain_of:
- Varsel
range: date

```
</details>