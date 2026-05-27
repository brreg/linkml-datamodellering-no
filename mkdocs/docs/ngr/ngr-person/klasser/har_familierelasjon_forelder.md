

# Slot: har_familierelasjon_forelder 


_Familierelasjonar der den relaterte personen er forelder (maks 2)._





URI: [ngrp:harFamilierelasjonForelder](https://data.norge.no/vocabulary/ngr-person#harFamilierelasjonForelder)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Ein fysisk person registrert i Folkeregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [FamilierelasjonForelder](familierelasjonforelder.md) |
| Domain Of | [Person](person.md) |
| Slot URI | [ngrp:harFamilierelasjonForelder](https://data.norge.no/vocabulary/ngr-person#harFamilierelasjonForelder) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:harFamilierelasjonForelder |
| native | https://data.norge.no/ngr/ngr-person/har_familierelasjon_forelder |




## LinkML Source

<details>
```yaml
name: har_familierelasjon_forelder
description: Familierelasjonar der den relaterte personen er forelder (maks 2).
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
slot_uri: ngrp:harFamilierelasjonForelder
domain_of:
- Person
range: FamilierelasjonForelder
multivalued: true

```
</details>