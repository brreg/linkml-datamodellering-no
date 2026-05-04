

# Slot: inneheld_teneste 


_Offentlege tenester i katalogen._





URI: [dcatno:containsService](https://data.norge.no/vocabulary/dcatno#containsService)
Alias: inneheld_teneste

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Katalog](Katalog.md) | Ein katalog over offentlege tenester og hendingar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OffentligTjeneste](OffentligTjeneste.md) |
| Domain Of | [Katalog](Katalog.md) |
| Slot URI | [dcatno:containsService](https://data.norge.no/vocabulary/dcatno#containsService) |

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
| self | dcatno:containsService |
| native | https://data.norge.no/linkml/cpsv-ap-no/inneheld_teneste |




## LinkML Source

<details>
```yaml
name: inneheld_teneste
description: Offentlege tenester i katalogen.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: dcatno:containsService
alias: inneheld_teneste
domain_of:
- Katalog
range: OffentligTjeneste
multivalued: true

```
</details>