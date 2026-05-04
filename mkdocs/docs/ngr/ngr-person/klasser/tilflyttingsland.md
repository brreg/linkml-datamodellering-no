

# Slot: tilflyttingsland 


_ISO 3166-1 landkode for landet personen flytta til._





URI: [ngrp:tilflyttingsland](https://data.norge.no/vocabulary/ngr-person#tilflyttingsland)
Alias: tilflyttingsland

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
| Slot URI | [ngrp:tilflyttingsland](https://data.norge.no/vocabulary/ngr-person#tilflyttingsland) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:tilflyttingsland |
| native | https://data.norge.no/linkml/ngr-person/tilflyttingsland |




## LinkML Source

<details>
```yaml
name: tilflyttingsland
description: ISO 3166-1 landkode for landet personen flytta til.
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:tilflyttingsland
alias: tilflyttingsland
domain_of:
- UtflyttingFraNorge
range: string

```
</details>