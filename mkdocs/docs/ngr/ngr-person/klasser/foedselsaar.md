

# Slot: foedselsaar 


_Fødselsår (alltid tilgjengeleg, sjølv om fullstendig dato manglar)._





URI: [ngrp:foedselsaar](https://data.norge.no/vocabulary/ngr-person#foedselsaar)
Alias: foedselsaar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Foedsel](foedsel.md) | Fødselsinformasjon om ein person registrert i Folkeregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](integer.md) |
| Domain Of | [Foedsel](foedsel.md) |
| Slot URI | [ngrp:foedselsaar](https://data.norge.no/vocabulary/ngr-person#foedselsaar) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:foedselsaar |
| native | https://data.norge.no/linkml/ngr-person/foedselsaar |




## LinkML Source

<details>
```yaml
name: foedselsaar
description: Fødselsår (alltid tilgjengeleg, sjølv om fullstendig dato manglar).
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:foedselsaar
alias: foedselsaar
domain_of:
- Foedsel
range: integer

```
</details>