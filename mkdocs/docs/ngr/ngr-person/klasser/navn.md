

# Slot: navn 


_Namn på person eller institusjon._





URI: [ngrp:namn](https://data.norge.no/vocabulary/ngr-person#namn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [KontaktinformasjonDoedsbo](kontaktinformasjondoedsbo.md) | Kontaktinformasjon for eit dødsbu |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [KontaktinformasjonDoedsbo](kontaktinformasjondoedsbo.md) |
| Slot URI | [ngrp:namn](https://data.norge.no/vocabulary/ngr-person#namn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:namn |
| native | https://data.norge.no/ngr/ngr-person/navn |




## LinkML Source

<details>
```yaml
name: navn
description: Namn på person eller institusjon.
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
slot_uri: ngrp:namn
domain_of:
- KontaktinformasjonDoedsbo
range: string

```
</details>