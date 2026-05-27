

# Slot: har_personnavn 


_Offisielt registrert namn på personen._





URI: [ngrp:harPersonnavn](https://data.norge.no/vocabulary/ngr-person#harPersonnavn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Ein fysisk person registrert i Folkeregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personnavn](personnavn.md) |
| Domain Of | [Person](person.md) |
| Slot URI | [ngrp:harPersonnavn](https://data.norge.no/vocabulary/ngr-person#harPersonnavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:harPersonnavn |
| native | https://data.norge.no/ngr/ngr-person/har_personnavn |




## LinkML Source

<details>
```yaml
name: har_personnavn
description: Offisielt registrert namn på personen.
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
slot_uri: ngrp:harPersonnavn
domain_of:
- Person
range: Personnavn

```
</details>