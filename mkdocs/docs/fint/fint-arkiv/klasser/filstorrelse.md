

# Slot: filstorrelse 


_Storleiken på fila i antal bytes._





URI: [ark:filstorrelse](https://schema.fintlabs.no/arkiv/filstorrelse)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dokumentobjekt](dokumentobjekt.md) | Referanse til éin og berre éin dokumentfil |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Dokumentobjekt](dokumentobjekt.md) |
| Slot URI | [ark:filstorrelse](https://schema.fintlabs.no/arkiv/filstorrelse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:filstorrelse |
| native | https://schema.fintlabs.no/arkiv/:filstorrelse |




## LinkML Source

<details>
```yaml
name: filstorrelse
description: Storleiken på fila i antal bytes.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:filstorrelse
domain_of:
- Dokumentobjekt
range: string

```
</details>