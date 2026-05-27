

# Slot: har_foreldreansvar_forelder 


_Personar med juridisk foreldreansvar for denne personen (maks 2)._





URI: [ngrp:harForeldreansvarForelder](https://data.norge.no/vocabulary/ngr-person#harForeldreansvarForelder)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Ein fysisk person registrert i Folkeregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ForeldreansvarForelder](foreldreansvarforelder.md) |
| Domain Of | [Person](person.md) |
| Slot URI | [ngrp:harForeldreansvarForelder](https://data.norge.no/vocabulary/ngr-person#harForeldreansvarForelder) |

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
| self | ngrp:harForeldreansvarForelder |
| native | https://data.norge.no/ngr/ngr-person/har_foreldreansvar_forelder |




## LinkML Source

<details>
```yaml
name: har_foreldreansvar_forelder
description: Personar med juridisk foreldreansvar for denne personen (maks 2).
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
slot_uri: ngrp:harForeldreansvarForelder
domain_of:
- Person
range: ForeldreansvarForelder
multivalued: true

```
</details>