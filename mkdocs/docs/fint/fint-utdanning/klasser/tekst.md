

# Slot: tekst 


_Innhald i varselet._





URI: [utd:tekst](https://schema.fintlabs.no/utdanning/tekst)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Varsel](varsel.md) | Eit varsel knytt til ein elev i ei faggruppe |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Varsel](varsel.md) |
| Slot URI | [utd:tekst](https://schema.fintlabs.no/utdanning/tekst) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:tekst |
| native | https://schema.fintlabs.no/utdanning/:tekst |




## LinkML Source

<details>
```yaml
name: tekst
description: Innhald i varselet.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:tekst
domain_of:
- Varsel
range: string

```
</details>