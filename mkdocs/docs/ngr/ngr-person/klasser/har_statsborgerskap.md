

# Slot: har_statsborgerskap 


_Statsborgerskap registrert på personen (minimum 1)._





URI: [ngrp:harStatsborgerskap](https://data.norge.no/vocabulary/ngr-person#harStatsborgerskap)
Alias: har_statsborgerskap

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Ein fysisk person registrert i Folkeregisteret |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Statsborgerskap](Statsborgerskap.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [ngrp:harStatsborgerskap](https://data.norge.no/vocabulary/ngr-person#harStatsborgerskap) |

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
| self | ngrp:harStatsborgerskap |
| native | https://data.norge.no/linkml/ngr-person/har_statsborgerskap |




## LinkML Source

<details>
```yaml
name: har_statsborgerskap
description: Statsborgerskap registrert på personen (minimum 1).
from_schema: https://data.norge.no/linkml/ngr-person
rank: 1000
slot_uri: ngrp:harStatsborgerskap
alias: har_statsborgerskap
domain_of:
- Person
range: Statsborgerskap
multivalued: true

```
</details>