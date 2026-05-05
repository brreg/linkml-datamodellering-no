

# Slot: inneheld_hending 


_Hendingar i katalogen._





URI: [dcatno:containsEvent](https://data.norge.no/vocabulary/dcatno#containsEvent)
Alias: inneheld_hending

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Katalog](katalog.md) | Ein katalog over offentlege tenester og hendingar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Hendelse](hendelse.md) |
| Domain Of | [Katalog](katalog.md) |
| Slot URI | [dcatno:containsEvent](https://data.norge.no/vocabulary/dcatno#containsEvent) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcatno:containsEvent |
| native | https://data.norge.no/linkml/cpsv-ap-no/inneheld_hending |




## LinkML Source

<details>
```yaml
name: inneheld_hending
description: Hendingar i katalogen.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: dcatno:containsEvent
alias: inneheld_hending
domain_of:
- Katalog
range: Hendelse
multivalued: true

```
</details>