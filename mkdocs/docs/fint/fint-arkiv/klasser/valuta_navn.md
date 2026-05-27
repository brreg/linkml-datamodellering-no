

# Slot: valuta_navn 


_Namn på valuta._





URI: [fint:valutaNavn](https://schema.fintlabs.no/valutaNavn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Valuta](valuta.md) | Valutakodar for offisielle valutaer |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Valuta](valuta.md) |
| Slot URI | [fint:valutaNavn](https://schema.fintlabs.no/valutaNavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:valutaNavn |
| native | https://schema.fintlabs.no/:valuta_navn |




## LinkML Source

<details>
```yaml
name: valuta_navn
description: Namn på valuta.
from_schema: https://data.norge.no/fint/fint-common
slot_uri: fint:valutaNavn
domain_of:
- Valuta
range: string

```
</details>