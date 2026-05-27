

# Slot: har_personidentifikasjon 


_Utanlandsk eller alternativ identifikasjon av personen._





URI: [ngrp:harPersonidentifikasjon](https://data.norge.no/vocabulary/ngr-person#harPersonidentifikasjon)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Ein fysisk person registrert i Folkeregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personidentifikasjon](personidentifikasjon.md) |
| Domain Of | [Person](person.md) |
| Slot URI | [ngrp:harPersonidentifikasjon](https://data.norge.no/vocabulary/ngr-person#harPersonidentifikasjon) |

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
| self | ngrp:harPersonidentifikasjon |
| native | https://data.norge.no/ngr/ngr-person/har_personidentifikasjon |




## LinkML Source

<details>
```yaml
name: har_personidentifikasjon
description: Utanlandsk eller alternativ identifikasjon av personen.
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
slot_uri: ngrp:harPersonidentifikasjon
domain_of:
- Person
range: Personidentifikasjon
multivalued: true

```
</details>