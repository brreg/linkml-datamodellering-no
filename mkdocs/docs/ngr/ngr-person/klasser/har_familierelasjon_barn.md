

# Slot: har_familierelasjon_barn 


_Familierelasjonar der den relaterte personen er barn._





URI: [ngrp:harFamilierelasjonBarn](https://data.norge.no/vocabulary/ngr-person#harFamilierelasjonBarn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Ein fysisk person registrert i Folkeregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [FamilierelasjonBarn](familierelasjonbarn.md) |
| Domain Of | [Person](person.md) |
| Slot URI | [ngrp:harFamilierelasjonBarn](https://data.norge.no/vocabulary/ngr-person#harFamilierelasjonBarn) |

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
| self | ngrp:harFamilierelasjonBarn |
| native | https://data.norge.no/ngr/ngr-person/har_familierelasjon_barn |




## LinkML Source

<details>
```yaml
name: har_familierelasjon_barn
description: Familierelasjonar der den relaterte personen er barn.
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
slot_uri: ngrp:harFamilierelasjonBarn
domain_of:
- Person
range: FamilierelasjonBarn
multivalued: true

```
</details>