

# Slot: gyldig_fra_og_med 


_Dato opplysinga er gyldig frå og med._





URI: [ngrp:gyldigFraOgMed](https://data.norge.no/vocabulary/ngr-person#gyldigFraOgMed)
Alias: gyldig_fra_og_med

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Statsborgerskap](Statsborgerskap.md) | Statsborgerskap registrert på ein person i Folkeregisteret |  yes  |
| [Personstatus](Personstatus.md) | Status for ein person i Folkeregisteret (t |  yes  |
| [Sivilstand](Sivilstand.md) | Sivilstand registrert på ein person i Folkeregisteret |  yes  |
| [Postadresse](Postadresse.md) | Adressa der personen mottar post |  yes  |
| [ReservasjonMotKommunikasjonPaaNett](ReservasjonMotKommunikasjonPaaNett.md) | Registrering av at ein person har reservert seg mot digital kommunikasjon frå... |  yes  |
| [Opphold](Opphold.md) | Lovleg opphaldsgrunnlag for utanlandske statsborgarar registrert i Folkeregis... |  yes  |
| [Oppholdsadresse](Oppholdsadresse.md) | Adressa der personen faktisk oppheld seg (ikkje nødvendigvis bustadsadressa) |  yes  |
| [Bostedsadresse](Bostedsadresse.md) | Adressa personen er registrert busett på i Folkeregisteret |  yes  |
| [Kjoenn](Kjoenn.md) | Kjønn registrert på ein person i Folkeregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [Kjoenn](Kjoenn.md), [Sivilstand](Sivilstand.md), [Personstatus](Personstatus.md), [Statsborgerskap](Statsborgerskap.md), [Opphold](Opphold.md), [Bostedsadresse](Bostedsadresse.md), [Postadresse](Postadresse.md), [Oppholdsadresse](Oppholdsadresse.md), [ReservasjonMotKommunikasjonPaaNett](ReservasjonMotKommunikasjonPaaNett.md) |
| Slot URI | [ngrp:gyldigFraOgMed](https://data.norge.no/vocabulary/ngr-person#gyldigFraOgMed) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:gyldigFraOgMed |
| native | https://data.norge.no/linkml/ngr-person/gyldig_fra_og_med |




## LinkML Source

<details>
```yaml
name: gyldig_fra_og_med
description: Dato opplysinga er gyldig frå og med.
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:gyldigFraOgMed
alias: gyldig_fra_og_med
domain_of:
- Kjoenn
- Sivilstand
- Personstatus
- Statsborgerskap
- Opphold
- Bostedsadresse
- Postadresse
- Oppholdsadresse
- ReservasjonMotKommunikasjonPaaNett
range: date

```
</details>