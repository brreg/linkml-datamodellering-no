

# Slot: epostadresse_verdi 


_E-postadresse._





URI: [ngrp:epostadresse](https://data.norge.no/vocabulary/ngr-person#epostadresse)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [KontaktinformasjonDoedsbo](kontaktinformasjondoedsbo.md) | Kontaktinformasjon for eit dødsbu |  yes  |
| [Kontaktopplysninger](kontaktopplysninger.md) | Kontaktopplysningar (e-post og mobilnummer) for digital kommunikasjon med det... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [KontaktinformasjonDoedsbo](kontaktinformasjondoedsbo.md), [Kontaktopplysninger](kontaktopplysninger.md) |
| Slot URI | [ngrp:epostadresse](https://data.norge.no/vocabulary/ngr-person#epostadresse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:epostadresse |
| native | https://data.norge.no/ngr/ngr-person/epostadresse_verdi |




## LinkML Source

<details>
```yaml
name: epostadresse_verdi
description: E-postadresse.
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
slot_uri: ngrp:epostadresse
domain_of:
- KontaktinformasjonDoedsbo
- Kontaktopplysninger
range: string

```
</details>