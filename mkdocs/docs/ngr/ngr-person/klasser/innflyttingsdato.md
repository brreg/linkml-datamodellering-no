

# Slot: innflyttingsdato 


_Dato personen vart registrert innflytta til Noreg._





URI: [ngrp:innflyttingsdato](https://data.norge.no/vocabulary/ngr-person#innflyttingsdato)
Alias: innflyttingsdato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InnflyttingTilNorge](innflyttingtilnorge.md) | Registrering av innflytting til Noreg i Folkeregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:date](http://www.w3.org/2001/XMLSchema#date) |
| Domain Of | [InnflyttingTilNorge](innflyttingtilnorge.md) |
| Slot URI | [ngrp:innflyttingsdato](https://data.norge.no/vocabulary/ngr-person#innflyttingsdato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:innflyttingsdato |
| native | https://data.norge.no/linkml/ngr-person/innflyttingsdato |




## LinkML Source

<details>
```yaml
name: innflyttingsdato
description: Dato personen vart registrert innflytta til Noreg.
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:innflyttingsdato
alias: innflyttingsdato
domain_of:
- InnflyttingTilNorge
range: date

```
</details>