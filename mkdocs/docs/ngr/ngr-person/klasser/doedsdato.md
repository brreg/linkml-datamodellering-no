

# Slot: doedsdato 


_Dato for dødsfallet._





URI: [ngrp:doedsdato](https://data.norge.no/vocabulary/ngr-person#doedsdato)
Alias: doedsdato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dodsfall](dodsfall.md) | Dødsfallsinformasjon om ein person registrert i Folkeregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](date.md) |
| Domain Of | [Dodsfall](dodsfall.md) |
| Slot URI | [ngrp:doedsdato](https://data.norge.no/vocabulary/ngr-person#doedsdato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:doedsdato |
| native | https://data.norge.no/linkml/ngr-person/doedsdato |




## LinkML Source

<details>
```yaml
name: doedsdato
description: Dato for dødsfallet.
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:doedsdato
alias: doedsdato
domain_of:
- Dodsfall
range: date

```
</details>