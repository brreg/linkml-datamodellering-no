

# Slot: epostadresse_verdi 


_E-postadresse._





URI: [ngrp:epostadresse](https://data.norge.no/vocabulary/ngr-person#epostadresse)
Alias: epostadresse_verdi

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktopplysninger](Kontaktopplysninger.md) | Kontaktopplysningar (e-post og mobilnummer) for digital kommunikasjon med det... |  yes  |
| [KontaktinformasjonDoedsbo](KontaktinformasjonDoedsbo.md) | Kontaktinformasjon for eit dødsbu |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [KontaktinformasjonDoedsbo](KontaktinformasjonDoedsbo.md), [Kontaktopplysninger](Kontaktopplysninger.md) |
| Slot URI | [ngrp:epostadresse](https://data.norge.no/vocabulary/ngr-person#epostadresse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:epostadresse |
| native | https://data.norge.no/linkml/ngr-person/epostadresse_verdi |




## LinkML Source

<details>
```yaml
name: epostadresse_verdi
description: E-postadresse.
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:epostadresse
alias: epostadresse_verdi
domain_of:
- KontaktinformasjonDoedsbo
- Kontaktopplysninger
range: string

```
</details>