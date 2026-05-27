

# Slot: skoleaarFravar 


_Fråværsprosent for heile skoleåret._





URI: [utd:skoleaarFravar](https://schema.fintlabs.no/utdanning/skoleaarFravar)
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
| Slot URI | [utd:skoleaarFravar](https://schema.fintlabs.no/utdanning/skoleaarFravar) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:skoleaarFravar |
| native | https://schema.fintlabs.no/utdanning/:skoleaarFravar |




## LinkML Source

<details>
```yaml
name: skoleaarFravar
description: Fråværsprosent for heile skoleåret.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:skoleaarFravar
domain_of:
- Fravarsoversikt
range: Fravarsprosent
inlined: true

```
</details>