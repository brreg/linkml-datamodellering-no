

# Slot: fornavn 


_Fornamn(et/a) til personen._





URI: [ngrp:fornavn](https://data.norge.no/vocabulary/ngr-person#fornavn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personnavn](personnavn.md) | Offisielt registrert namn på ein person i Folkeregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Personnavn](personnavn.md) |
| Slot URI | [ngrp:fornavn](https://data.norge.no/vocabulary/ngr-person#fornavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:fornavn |
| native | https://data.norge.no/ngr/ngr-person/fornavn |




## LinkML Source

<details>
```yaml
name: fornavn
description: Fornamn(et/a) til personen.
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
slot_uri: ngrp:fornavn
domain_of:
- Personnavn
range: string

```
</details>