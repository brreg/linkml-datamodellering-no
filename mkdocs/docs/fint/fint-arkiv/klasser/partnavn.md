

# Slot: partNavn 


_Namn på verksemd eller person som er part._





URI: [ark:partNavn](https://schema.fintlabs.no/arkiv/partNavn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Part](part.md) | Part til Mappe, Registrering eller Dokumentbeskrivelse |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Part](part.md) |
| Slot URI | [ark:partNavn](https://schema.fintlabs.no/arkiv/partNavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:partNavn |
| native | https://schema.fintlabs.no/arkiv/:partNavn |




## LinkML Source

<details>
```yaml
name: partNavn
description: Namn på verksemd eller person som er part.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:partNavn
domain_of:
- Part
range: string

```
</details>