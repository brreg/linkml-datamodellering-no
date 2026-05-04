

# Slot: telefonnummer 


_Telefonnummer._





URI: [ngrp:telefonnummer](https://data.norge.no/vocabulary/ngr-person#telefonnummer)
Alias: telefonnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [KontaktinformasjonDoedsbo](KontaktinformasjonDoedsbo.md) | Kontaktinformasjon for eit dødsbu |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [KontaktinformasjonDoedsbo](KontaktinformasjonDoedsbo.md) |
| Slot URI | [ngrp:telefonnummer](https://data.norge.no/vocabulary/ngr-person#telefonnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:telefonnummer |
| native | https://data.norge.no/linkml/ngr-person/telefonnummer |




## LinkML Source

<details>
```yaml
name: telefonnummer
description: Telefonnummer.
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:telefonnummer
alias: telefonnummer
domain_of:
- KontaktinformasjonDoedsbo
range: string

```
</details>