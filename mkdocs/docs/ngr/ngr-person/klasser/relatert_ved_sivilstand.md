

# Slot: relatert_ved_sivilstand 


_Person ein er gift/partnar med (utfyller sivilstand GIFT, REGISTRERT_PARTNER o.l.)._





URI: [ngrp:relatertVedSivilstand](https://data.norge.no/vocabulary/ngr-person#relatertVedSivilstand)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sivilstand](sivilstand.md) | Sivilstand registrert på ein person i Folkeregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Person](person.md) |
| Domain Of | [Sivilstand](sivilstand.md) |
| Slot URI | [ngrp:relatertVedSivilstand](https://data.norge.no/vocabulary/ngr-person#relatertVedSivilstand) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:relatertVedSivilstand |
| native | https://data.norge.no/ngr/ngr-person/relatert_ved_sivilstand |




## LinkML Source

<details>
```yaml
name: relatert_ved_sivilstand
description: Person ein er gift/partnar med (utfyller sivilstand GIFT, REGISTRERT_PARTNER
  o.l.).
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
slot_uri: ngrp:relatertVedSivilstand
domain_of:
- Sivilstand
range: Person

```
</details>