

# Slot: gyldig_til_og_med 


_Dato opplysinga er gyldig til og med._





URI: [ngrp:gyldigTilOgMed](https://data.norge.no/vocabulary/ngr-person#gyldigTilOgMed)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Statsborgerskap](statsborgerskap.md) | Statsborgerskap registrert på ein person i Folkeregisteret |  yes  |
| [Opphold](opphold.md) | Lovleg opphaldsgrunnlag for utanlandske statsborgarar registrert i Folkeregis... |  yes  |
| [Bostedsadresse](bostedsadresse.md) | Adressa personen er registrert busett på i Folkeregisteret |  yes  |
| [Postadresse](postadresse.md) | Adressa der personen mottar post |  yes  |
| [Oppholdsadresse](oppholdsadresse.md) | Adressa der personen faktisk oppheld seg (ikkje nødvendigvis bustadsadressa) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:date](http://www.w3.org/2001/XMLSchema#date) |
| Domain Of | [Statsborgerskap](statsborgerskap.md), [Opphold](opphold.md), [Bostedsadresse](bostedsadresse.md), [Postadresse](postadresse.md), [Oppholdsadresse](oppholdsadresse.md) |
| Slot URI | [ngrp:gyldigTilOgMed](https://data.norge.no/vocabulary/ngr-person#gyldigTilOgMed) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:gyldigTilOgMed |
| native | https://data.norge.no/ngr/ngr-person/gyldig_til_og_med |




## LinkML Source

<details>
```yaml
name: gyldig_til_og_med
description: Dato opplysinga er gyldig til og med.
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
slot_uri: ngrp:gyldigTilOgMed
domain_of:
- Statsborgerskap
- Opphold
- Bostedsadresse
- Postadresse
- Oppholdsadresse
range: date

```
</details>