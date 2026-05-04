

# Slot: doedssted 


_Stad for dødsfallet._





URI: [ngrp:doedssted](https://data.norge.no/vocabulary/ngr-person#doedssted)
Alias: doedssted

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dodsfall](Dodsfall.md) | Dødsfallsinformasjon om ein person registrert i Folkeregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Dodsfall](Dodsfall.md) |
| Slot URI | [ngrp:doedssted](https://data.norge.no/vocabulary/ngr-person#doedssted) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:doedssted |
| native | https://data.norge.no/linkml/ngr-person/doedssted |




## LinkML Source

<details>
```yaml
name: doedssted
description: Stad for dødsfallet.
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:doedssted
alias: doedssted
domain_of:
- Dodsfall
range: string

```
</details>