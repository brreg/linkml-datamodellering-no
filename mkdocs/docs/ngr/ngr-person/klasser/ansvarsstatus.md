

# Slot: ansvarsstatus 


_Status for foreldreansvaret (t.d. FELLES, ALENE)._





URI: [ngrp:ansvarsstatus](https://data.norge.no/vocabulary/ngr-person#ansvarsstatus)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ForeldreansvarForelder](foreldreansvarforelder.md) | Relasjonsklasse som registrerer kven som har det juridiske foreldreansvaret f... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [ForeldreansvarForelder](foreldreansvarforelder.md) |
| Slot URI | [ngrp:ansvarsstatus](https://data.norge.no/vocabulary/ngr-person#ansvarsstatus) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:ansvarsstatus |
| native | https://data.norge.no/ngr/ngr-person/ansvarsstatus |




## LinkML Source

<details>
```yaml
name: ansvarsstatus
description: Status for foreldreansvaret (t.d. FELLES, ALENE).
from_schema: https://data.norge.no/ngr/ngr-person
rank: 1000
slot_uri: ngrp:ansvarsstatus
domain_of:
- ForeldreansvarForelder
range: string

```
</details>