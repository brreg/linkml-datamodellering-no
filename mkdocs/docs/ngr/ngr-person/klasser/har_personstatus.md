

# Slot: har_personstatus 


_Status for personen i Folkeregisteret._





URI: [ngrp:harPersonstatus](https://data.norge.no/vocabulary/ngr-person#harPersonstatus)
Alias: har_personstatus

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Ein fysisk person registrert i Folkeregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personstatus](Personstatus.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [ngrp:harPersonstatus](https://data.norge.no/vocabulary/ngr-person#harPersonstatus) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-person




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngrp:harPersonstatus |
| native | https://data.norge.no/linkml/ngr-person/har_personstatus |




## LinkML Source

<details>
```yaml
name: har_personstatus
description: Status for personen i Folkeregisteret.
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:harPersonstatus
alias: har_personstatus
domain_of:
- Person
range: Personstatus

```
</details>