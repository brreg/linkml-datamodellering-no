

# Slot: tilflyttingssted_i_utlandet 


_Stad i utlandet personen flytta til._





URI: [ngrp:tilflyttingsstedIUtlandet](https://data.norge.no/vocabulary/ngr-person#tilflyttingsstedIUtlandet)
Alias: tilflyttingssted_i_utlandet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtflyttingFraNorge](UtflyttingFraNorge.md) | Registrering av utflytting frå Noreg i Folkeregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [UtflyttingFraNorge](UtflyttingFraNorge.md) |
| Slot URI | [ngrp:tilflyttingsstedIUtlandet](https://data.norge.no/vocabulary/ngr-person#tilflyttingsstedIUtlandet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:tilflyttingsstedIUtlandet |
| native | https://data.norge.no/linkml/ngr-person/tilflyttingssted_i_utlandet |




## LinkML Source

<details>
```yaml
name: tilflyttingssted_i_utlandet
description: Stad i utlandet personen flytta til.
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:tilflyttingsstedIUtlandet
alias: tilflyttingssted_i_utlandet
domain_of:
- UtflyttingFraNorge
range: string

```
</details>