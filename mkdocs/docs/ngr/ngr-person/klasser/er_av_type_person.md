

# Slot: er_av_type_person 


_Personen som denne relasjonen peikar til._





URI: [ngrp:erAvTypePerson](https://data.norge.no/vocabulary/ngr-person#erAvTypePerson)
Alias: er_av_type_person

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ForeldreansvarBarn](foreldreansvarbarn.md) | Relasjonsklasse som registrerer at eit barn er under foreldreansvaret til ein... |  yes  |
| [Verge](verge.md) | Ein verje (anten person eller institusjon) som er oppnemnd for å ivareta inte... |  yes  |
| [FamilierelasjonEktefelle](familierelasjonektefelle.md) | Familierelasjon der den relaterte personen er ektefelle eller registrert part... |  yes  |
| [FamilierelasjonBarn](familierelasjonbarn.md) | Familierelasjon der den relaterte personen er barn |  yes  |
| [ForeldreansvarForelder](foreldreansvarforelder.md) | Relasjonsklasse som registrerer kven som har det juridiske foreldreansvaret f... |  yes  |
| [FamilierelasjonForelder](familierelasjonforelder.md) | Familierelasjon der den relaterte personen er forelder |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Person](person.md) |
| Domain Of | [ForeldreansvarForelder](foreldreansvarforelder.md), [ForeldreansvarBarn](foreldreansvarbarn.md), [FamilierelasjonForelder](familierelasjonforelder.md), [FamilierelasjonBarn](familierelasjonbarn.md), [FamilierelasjonEktefelle](familierelasjonektefelle.md), [Verge](verge.md) |
| Slot URI | [ngrp:erAvTypePerson](https://data.norge.no/vocabulary/ngr-person#erAvTypePerson) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:erAvTypePerson |
| native | https://data.norge.no/linkml/ngr-person/er_av_type_person |




## LinkML Source

<details>
```yaml
name: er_av_type_person
description: Personen som denne relasjonen peikar til.
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:erAvTypePerson
alias: er_av_type_person
domain_of:
- ForeldreansvarForelder
- ForeldreansvarBarn
- FamilierelasjonForelder
- FamilierelasjonBarn
- FamilierelasjonEktefelle
- Verge
range: Person

```
</details>