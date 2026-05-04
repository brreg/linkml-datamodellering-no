

# Slot: etternavn 


_Etternamn til personen._





URI: [ngrp:etternavn](https://data.norge.no/vocabulary/ngr-person#etternavn)
Alias: etternavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personnavn](Personnavn.md) | Offisielt registrert namn på ein person i Folkeregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Personnavn](Personnavn.md) |
| Slot URI | [ngrp:etternavn](https://data.norge.no/vocabulary/ngr-person#etternavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:etternavn |
| native | https://data.norge.no/linkml/ngr-person/etternavn |




## LinkML Source

<details>
```yaml
name: etternavn
description: Etternamn til personen.
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:etternavn
alias: etternavn
domain_of:
- Personnavn
range: string

```
</details>