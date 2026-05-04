

# Slot: har_personidentifikasjon 


_Utanlandsk eller alternativ identifikasjon av personen._





URI: [ngrp:harPersonidentifikasjon](https://data.norge.no/vocabulary/ngr-person#harPersonidentifikasjon)
Alias: har_personidentifikasjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Ein fysisk person registrert i Folkeregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personidentifikasjon](Personidentifikasjon.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [ngrp:harPersonidentifikasjon](https://data.norge.no/vocabulary/ngr-person#harPersonidentifikasjon) |

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
| self | ngrp:harPersonidentifikasjon |
| native | https://data.norge.no/linkml/ngr-person/har_personidentifikasjon |




## LinkML Source

<details>
```yaml
name: har_personidentifikasjon
description: Utanlandsk eller alternativ identifikasjon av personen.
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:harPersonidentifikasjon
alias: har_personidentifikasjon
domain_of:
- Person
range: Personidentifikasjon
multivalued: true

```
</details>