

# Slot: har_dodsfall 


_Dødsfallsinformasjon om personen._





URI: [ngrp:harDodsfall](https://data.norge.no/vocabulary/ngr-person#harDodsfall)
Alias: har_dodsfall

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Ein fysisk person registrert i Folkeregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Dodsfall](Dodsfall.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [ngrp:harDodsfall](https://data.norge.no/vocabulary/ngr-person#harDodsfall) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:harDodsfall |
| native | https://data.norge.no/linkml/ngr-person/har_dodsfall |




## LinkML Source

<details>
```yaml
name: har_dodsfall
description: Dødsfallsinformasjon om personen.
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:harDodsfall
alias: har_dodsfall
domain_of:
- Person
range: Dodsfall

```
</details>