

# Slot: gyldig_fra_og_med 


_Dato opplysinga er gyldig frå og med._





URI: [ngrp:gyldigFraOgMed](https://data.norge.no/vocabulary/ngr-person#gyldigFraOgMed)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kjoenn](kjoenn.md) | Kjønn registrert på ein person i Folkeregisteret |  yes  |
| [Sivilstand](sivilstand.md) | Sivilstand registrert på ein person i Folkeregisteret |  yes  |
| [Personstatus](personstatus.md) | Status for ein person i Folkeregisteret (t |  yes  |
| [Statsborgerskap](statsborgerskap.md) | Statsborgerskap registrert på ein person i Folkeregisteret |  yes  |
| [Opphold](opphold.md) | Lovleg opphaldsgrunnlag for utanlandske statsborgarar registrert i Folkeregis... |  yes  |
| [Bostedsadresse](bostedsadresse.md) | Adressa personen er registrert busett på i Folkeregisteret |  yes  |
| [Postadresse](postadresse.md) | Adressa der personen mottar post |  yes  |
| [Oppholdsadresse](oppholdsadresse.md) | Adressa der personen faktisk oppheld seg (ikkje nødvendigvis bustadsadressa) |  yes  |
| [ReservasjonMotKommunikasjonPaaNett](reservasjonmotkommunikasjonpaanett.md) | Registrering av at ein person har reservert seg mot digital kommunikasjon frå... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:date](http://www.w3.org/2001/XMLSchema#date) |
| Domain Of | [Kjoenn](kjoenn.md), [Sivilstand](sivilstand.md), [Personstatus](personstatus.md), [Statsborgerskap](statsborgerskap.md), [Opphold](opphold.md), [Bostedsadresse](bostedsadresse.md), [Postadresse](postadresse.md), [Oppholdsadresse](oppholdsadresse.md), [ReservasjonMotKommunikasjonPaaNett](reservasjonmotkommunikasjonpaanett.md) |
| Slot URI | [ngrp:gyldigFraOgMed](https://data.norge.no/vocabulary/ngr-person#gyldigFraOgMed) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:gyldigFraOgMed |
| native | https://data.norge.no/ngr/ngr-person/gyldig_fra_og_med |




## LinkML Source

<details>
```yaml
name: gyldig_fra_og_med
description: Dato opplysinga er gyldig frå og med.
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
slot_uri: ngrp:gyldigFraOgMed
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