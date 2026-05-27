

# Slot: rett_identitet_er_ukjent 


_Om den rette identiteten er ukjent (når falsk identitet er registrert)._





URI: [ngrp:rettIdentitetErUkjent](https://data.norge.no/vocabulary/ngr-person#rettIdentitetErUkjent)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FalskIdentitet](falskidentitet.md) | Registrering av at ein person har opptrådt med falsk identitet |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) |
| Domain Of | [FalskIdentitet](falskidentitet.md) |
| Slot URI | [ngrp:rettIdentitetErUkjent](https://data.norge.no/vocabulary/ngr-person#rettIdentitetErUkjent) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:rettIdentitetErUkjent |
| native | https://data.norge.no/ngr/ngr-person/rett_identitet_er_ukjent |




## LinkML Source

<details>
```yaml
name: rett_identitet_er_ukjent
description: Om den rette identiteten er ukjent (når falsk identitet er registrert).
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
slot_uri: ngrp:rettIdentitetErUkjent
domain_of:
- FalskIdentitet
range: boolean

```
</details>