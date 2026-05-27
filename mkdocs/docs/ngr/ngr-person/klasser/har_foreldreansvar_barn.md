

# Slot: har_foreldreansvar_barn 


_Barn som denne personen har juridisk foreldreansvar for._





URI: [ngrp:harForeldreansvarBarn](https://data.norge.no/vocabulary/ngr-person#harForeldreansvarBarn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Ein fysisk person registrert i Folkeregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ForeldreansvarBarn](foreldreansvarbarn.md) |
| Domain Of | [Person](person.md) |
| Slot URI | [ngrp:harForeldreansvarBarn](https://data.norge.no/vocabulary/ngr-person#harForeldreansvarBarn) |

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
| self | ngrp:harForeldreansvarBarn |
| native | https://data.norge.no/ngr/ngr-person/har_foreldreansvar_barn |




## LinkML Source

<details>
```yaml
name: har_foreldreansvar_barn
description: Barn som denne personen har juridisk foreldreansvar for.
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
slot_uri: ngrp:harForeldreansvarBarn
domain_of:
- Person
range: ForeldreansvarBarn
multivalued: true

```
</details>