

# Slot: utflyttingsdato 


_Dato personen vart registrert utflytta frå Noreg._





URI: [ngrp:utflyttingsdato](https://data.norge.no/vocabulary/ngr-person#utflyttingsdato)
Alias: utflyttingsdato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtflyttingFraNorge](utflyttingfranorge.md) | Registrering av utflytting frå Noreg i Folkeregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](date.md) |
| Domain Of | [UtflyttingFraNorge](utflyttingfranorge.md) |
| Slot URI | [ngrp:utflyttingsdato](https://data.norge.no/vocabulary/ngr-person#utflyttingsdato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:utflyttingsdato |
| native | https://data.norge.no/linkml/ngr-person/utflyttingsdato |




## LinkML Source

<details>
```yaml
name: utflyttingsdato
description: Dato personen vart registrert utflytta frå Noreg.
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:utflyttingsdato
alias: utflyttingsdato
domain_of:
- UtflyttingFraNorge
range: date

```
</details>