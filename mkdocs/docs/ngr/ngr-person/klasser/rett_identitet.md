

# Slot: rett_identitet 


_Den rette identiteten til ein person som har opptrådt med falsk identitet._





URI: [ngrp:rettIdentitet](https://data.norge.no/vocabulary/ngr-person#rettIdentitet)
Alias: rett_identitet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FalskIdentitet](FalskIdentitet.md) | Registrering av at ein person har opptrådt med falsk identitet |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Person](Person.md) |
| Domain Of | [FalskIdentitet](FalskIdentitet.md) |
| Slot URI | [ngrp:rettIdentitet](https://data.norge.no/vocabulary/ngr-person#rettIdentitet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:rettIdentitet |
| native | https://data.norge.no/linkml/ngr-person/rett_identitet |




## LinkML Source

<details>
```yaml
name: rett_identitet
description: Den rette identiteten til ein person som har opptrådt med falsk identitet.
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:rettIdentitet
alias: rett_identitet
domain_of:
- FalskIdentitet
range: Person

```
</details>