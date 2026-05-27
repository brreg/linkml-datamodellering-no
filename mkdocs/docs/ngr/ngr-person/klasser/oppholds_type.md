

# Slot: oppholds_type 


_Type opphald (MIDLERTIDIG, PERMANENT, OPPLYSNING_MANGLER)._





URI: [ngrp:oppholdType](https://data.norge.no/vocabulary/ngr-person#oppholdType)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Opphold](opphold.md) | Lovleg opphaldsgrunnlag for utanlandske statsborgarar registrert i Folkeregis... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OppholdstypeKode](oppholdstypekode.md) |
| Domain Of | [Opphold](opphold.md) |
| Slot URI | [ngrp:oppholdType](https://data.norge.no/vocabulary/ngr-person#oppholdType) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:oppholdType |
| native | https://data.norge.no/ngr/ngr-person/oppholds_type |




## LinkML Source

<details>
```yaml
name: oppholds_type
description: Type opphald (MIDLERTIDIG, PERMANENT, OPPLYSNING_MANGLER).
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
slot_uri: ngrp:oppholdType
domain_of:
- Opphold
range: OppholdstypeKode

```
</details>