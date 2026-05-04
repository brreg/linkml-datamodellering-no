

# Slot: er_av_type_person 


_Personen som denne relasjonen peikar til._





URI: [ngrp:erAvTypePerson](https://data.norge.no/vocabulary/ngr-person#erAvTypePerson)
Alias: er_av_type_person

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FamilierelasjonForelder](FamilierelasjonForelder.md) | Familierelasjon der den relaterte personen er forelder |  yes  |
| [FamilierelasjonEktefelle](FamilierelasjonEktefelle.md) | Familierelasjon der den relaterte personen er ektefelle eller registrert part... |  yes  |
| [ForeldreansvarForelder](ForeldreansvarForelder.md) | Relasjonsklasse som registrerer kven som har det juridiske foreldreansvaret f... |  yes  |
| [FamilierelasjonBarn](FamilierelasjonBarn.md) | Familierelasjon der den relaterte personen er barn |  yes  |
| [Verge](Verge.md) | Ein verje (anten person eller institusjon) som er oppnemnd for å ivareta inte... |  yes  |
| [ForeldreansvarBarn](ForeldreansvarBarn.md) | Relasjonsklasse som registrerer at eit barn er under foreldreansvaret til ein... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Person](Person.md) |
| Domain Of | [ForeldreansvarForelder](ForeldreansvarForelder.md), [ForeldreansvarBarn](ForeldreansvarBarn.md), [FamilierelasjonForelder](FamilierelasjonForelder.md), [FamilierelasjonBarn](FamilierelasjonBarn.md), [FamilierelasjonEktefelle](FamilierelasjonEktefelle.md), [Verge](Verge.md) |
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