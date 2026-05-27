

# Slot: forkortet_navn 


_Forkorta versjon av fullt namn._





URI: [ngrp:forkortetNavn](https://data.norge.no/vocabulary/ngr-person#forkortetNavn)
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
| Slot URI | [ngrp:forkortetNavn](https://data.norge.no/vocabulary/ngr-person#forkortetNavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:forkortetNavn |
| native | https://data.norge.no/ngr/ngr-person/forkortet_navn |




## LinkML Source

<details>
```yaml
name: forkortet_navn
description: Forkorta versjon av fullt namn.
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
slot_uri: ngrp:forkortetNavn
domain_of:
- Personnavn
range: string

```
</details>