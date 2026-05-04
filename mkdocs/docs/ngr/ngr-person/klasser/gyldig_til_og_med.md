

# Slot: gyldig_til_og_med 


_Dato opplysinga er gyldig til og med._





URI: [ngrp:gyldigTilOgMed](https://data.norge.no/vocabulary/ngr-person#gyldigTilOgMed)
Alias: gyldig_til_og_med

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Statsborgerskap](Statsborgerskap.md) | Statsborgerskap registrert på ein person i Folkeregisteret |  yes  |
| [Opphold](Opphold.md) | Lovleg opphaldsgrunnlag for utanlandske statsborgarar registrert i Folkeregis... |  yes  |
| [Oppholdsadresse](Oppholdsadresse.md) | Adressa der personen faktisk oppheld seg (ikkje nødvendigvis bustadsadressa) |  yes  |
| [Bostedsadresse](Bostedsadresse.md) | Adressa personen er registrert busett på i Folkeregisteret |  yes  |
| [Postadresse](Postadresse.md) | Adressa der personen mottar post |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [Statsborgerskap](Statsborgerskap.md), [Opphold](Opphold.md), [Bostedsadresse](Bostedsadresse.md), [Postadresse](Postadresse.md), [Oppholdsadresse](Oppholdsadresse.md) |
| Slot URI | [ngrp:gyldigTilOgMed](https://data.norge.no/vocabulary/ngr-person#gyldigTilOgMed) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:gyldigTilOgMed |
| native | https://data.norge.no/linkml/ngr-person/gyldig_til_og_med |




## LinkML Source

<details>
```yaml
name: gyldig_til_og_med
description: Dato opplysinga er gyldig til og med.
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:gyldigTilOgMed
alias: gyldig_til_og_med
domain_of:
- Statsborgerskap
- Opphold
- Bostedsadresse
- Postadresse
- Oppholdsadresse
range: date

```
</details>