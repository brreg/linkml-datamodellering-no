

# Slot: foedselsdato 


_Fødselsdato (kan vere ukjent for eldre registreringar)._





URI: [ngrp:foedselsdato](https://data.norge.no/vocabulary/ngr-person#foedselsdato)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Foedsel](foedsel.md) | Fødselsinformasjon om ein person registrert i Folkeregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:date](http://www.w3.org/2001/XMLSchema#date) |
| Domain Of | [Foedsel](foedsel.md) |
| Slot URI | [ngrp:foedselsdato](https://data.norge.no/vocabulary/ngr-person#foedselsdato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:foedselsdato |
| native | https://data.norge.no/ngr/ngr-person/foedselsdato |




## LinkML Source

<details>
```yaml
name: foedselsdato
description: Fødselsdato (kan vere ukjent for eldre registreringar).
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
slot_uri: ngrp:foedselsdato
domain_of:
- Foedsel
range: date

```
</details>