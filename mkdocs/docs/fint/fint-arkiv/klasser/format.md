

# Slot: format 


_Format på dokumentfil, som IANA Media Type._





URI: [ark:format](https://schema.fintlabs.no/arkiv/format)
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
| Slot URI | [ark:format](https://schema.fintlabs.no/arkiv/format) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:format |
| native | https://schema.fintlabs.no/arkiv/:format |




## LinkML Source

<details>
```yaml
name: format
description: Format på dokumentfil, som IANA Media Type.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:format
domain_of:
- Dokumentfil
range: string

```
</details>