

# Slot: foreldrerelasjon_type 


_Type foreldrerelasjon (MOR, FAR, MEDMOR o.l.)._





URI: [ngrp:foreldrerelasjonType](https://data.norge.no/vocabulary/ngr-person#foreldrerelasjonType)
Alias: foreldrerelasjon_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FamilierelasjonForelder](FamilierelasjonForelder.md) | Familierelasjon der den relaterte personen er forelder |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [FamilierelasjonForelder](FamilierelasjonForelder.md) |
| Slot URI | [ngrp:foreldrerelasjonType](https://data.norge.no/vocabulary/ngr-person#foreldrerelasjonType) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:foreldrerelasjonType |
| native | https://data.norge.no/linkml/ngr-person/foreldrerelasjon_type |




## LinkML Source

<details>
```yaml
name: foreldrerelasjon_type
description: Type foreldrerelasjon (MOR, FAR, MEDMOR o.l.).
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:foreldrerelasjonType
alias: foreldrerelasjon_type
domain_of:
- FamilierelasjonForelder
range: string

```
</details>