

# Slot: har_foreldreansvar_barn 


_Barn som denne personen har juridisk foreldreansvar for._





URI: [ngrp:harForeldreansvarBarn](https://data.norge.no/vocabulary/ngr-person#harForeldreansvarBarn)
Alias: har_foreldreansvar_barn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Ein fysisk person registrert i Folkeregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ForeldreansvarBarn](ForeldreansvarBarn.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [ngrp:harForeldreansvarBarn](https://data.norge.no/vocabulary/ngr-person#harForeldreansvarBarn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:harForeldreansvarBarn |
| native | https://data.norge.no/linkml/ngr-person/har_foreldreansvar_barn |




## LinkML Source

<details>
```yaml
name: har_foreldreansvar_barn
description: Barn som denne personen har juridisk foreldreansvar for.
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:harForeldreansvarBarn
alias: har_foreldreansvar_barn
domain_of:
- Person
range: ForeldreansvarBarn
multivalued: true

```
</details>