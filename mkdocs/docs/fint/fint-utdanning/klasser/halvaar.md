

# Slot: halvaar 


_Fråværsprosent for halvåret._





URI: [utd:halvaar](https://schema.fintlabs.no/utdanning/halvaar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fravarsoversikt](fravarsoversikt.md) | Oversikt over fråvær for ein elev i eit fag |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fravarsprosent](fravarsprosent.md) |
| Domain Of | [Fravarsoversikt](fravarsoversikt.md) |
| Slot URI | [utd:halvaar](https://schema.fintlabs.no/utdanning/halvaar) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:halvaar |
| native | https://schema.fintlabs.no/utdanning/:halvaar |




## LinkML Source

<details>
```yaml
name: halvaar
description: Fråværsprosent for halvåret.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:halvaar
domain_of:
- Fravarsoversikt
range: Fravarsprosent
inlined: true

```
</details>