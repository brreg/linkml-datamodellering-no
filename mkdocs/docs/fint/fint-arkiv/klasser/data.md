

# Slot: data 


_Dokumentfilens data, koda som Base64._





URI: [ark:data](https://schema.fintlabs.no/arkiv/data)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dokumentfil](dokumentfil.md) | Sjølve dokumentfila med data og metadata |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Dokumentfil](dokumentfil.md) |
| Slot URI | [ark:data](https://schema.fintlabs.no/arkiv/data) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:data |
| native | https://schema.fintlabs.no/arkiv/:data |




## LinkML Source

<details>
```yaml
name: data
description: Dokumentfilens data, koda som Base64.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:data
domain_of:
- Dokumentfil
range: string

```
</details>