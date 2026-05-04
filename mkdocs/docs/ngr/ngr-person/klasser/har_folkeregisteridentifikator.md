

# Slot: har_folkeregisteridentifikator 


_Unik identifikator i Folkeregisteret (fødselsnummer eller D-nummer)._





URI: [ngrp:harFolkeregisteridentifikator](https://data.norge.no/vocabulary/ngr-person#harFolkeregisteridentifikator)
Alias: har_folkeregisteridentifikator

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Ein fysisk person registrert i Folkeregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Folkeregisteridentifikator](Folkeregisteridentifikator.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [ngrp:harFolkeregisteridentifikator](https://data.norge.no/vocabulary/ngr-person#harFolkeregisteridentifikator) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:harFolkeregisteridentifikator |
| native | https://data.norge.no/linkml/ngr-person/har_folkeregisteridentifikator |




## LinkML Source

<details>
```yaml
name: har_folkeregisteridentifikator
description: Unik identifikator i Folkeregisteret (fødselsnummer eller D-nummer).
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:harFolkeregisteridentifikator
alias: har_folkeregisteridentifikator
domain_of:
- Person
range: Folkeregisteridentifikator

```
</details>