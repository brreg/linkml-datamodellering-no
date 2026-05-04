

# Slot: rett_identitet_er_ukjent 


_Om den rette identiteten er ukjent (når falsk identitet er registrert)._





URI: [ngrp:rettIdentitetErUkjent](https://data.norge.no/vocabulary/ngr-person#rettIdentitetErUkjent)
Alias: rett_identitet_er_ukjent

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FalskIdentitet](FalskIdentitet.md) | Registrering av at ein person har opptrådt med falsk identitet |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [FalskIdentitet](FalskIdentitet.md) |
| Slot URI | [ngrp:rettIdentitetErUkjent](https://data.norge.no/vocabulary/ngr-person#rettIdentitetErUkjent) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:rettIdentitetErUkjent |
| native | https://data.norge.no/linkml/ngr-person/rett_identitet_er_ukjent |




## LinkML Source

<details>
```yaml
name: rett_identitet_er_ukjent
description: Om den rette identiteten er ukjent (når falsk identitet er registrert).
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:rettIdentitetErUkjent
alias: rett_identitet_er_ukjent
domain_of:
- FalskIdentitet
range: boolean

```
</details>