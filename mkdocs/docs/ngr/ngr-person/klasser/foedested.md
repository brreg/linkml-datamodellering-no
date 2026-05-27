

# Slot: foedested 


_Fødested (kommune eller land)._





URI: [ngrp:foedested](https://data.norge.no/vocabulary/ngr-person#foedested)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Foedsel](foedsel.md) | Fødselsinformasjon om ein person registrert i Folkeregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Foedsel](foedsel.md) |
| Slot URI | [ngrp:foedested](https://data.norge.no/vocabulary/ngr-person#foedested) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:foedested |
| native | https://data.norge.no/ngr/ngr-person/foedested |




## LinkML Source

<details>
```yaml
name: foedested
description: Fødested (kommune eller land).
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
slot_uri: ngrp:foedested
domain_of:
- Foedsel
range: string

```
</details>