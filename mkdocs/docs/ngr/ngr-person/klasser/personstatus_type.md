

# Slot: personstatus_type 


_Personstatustype (BOSATT, UTFLYTTET, DOED o.l.)._





URI: [ngrp:personstatusType](https://data.norge.no/vocabulary/ngr-person#personstatusType)
Alias: personstatus_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personstatus](personstatus.md) | Status for ein person i Folkeregisteret (t |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PersonstatusType](personstatustype.md) |
| Domain Of | [Personstatus](personstatus.md) |
| Slot URI | [ngrp:personstatusType](https://data.norge.no/vocabulary/ngr-person#personstatusType) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:personstatusType |
| native | https://data.norge.no/linkml/ngr-person/personstatus_type |




## LinkML Source

<details>
```yaml
name: personstatus_type
description: Personstatustype (BOSATT, UTFLYTTET, DOED o.l.).
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:personstatusType
alias: personstatus_type
domain_of:
- Personstatus
range: PersonstatusType

```
</details>