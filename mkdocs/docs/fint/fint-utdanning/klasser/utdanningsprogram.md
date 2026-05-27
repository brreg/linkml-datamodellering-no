

# Slot: utdanningsprogram 


_Utdanningsprogram._





URI: [utd:utdanningsprogram](https://schema.fintlabs.no/utdanning/utdanningsprogram)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  yes  |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Utdanningsprogram](utdanningsprogram.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Skole](skole.md) |
| Slot URI | [utd:utdanningsprogram](https://schema.fintlabs.no/utdanning/utdanningsprogram) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:utdanningsprogram |
| native | https://schema.fintlabs.no/utdanning/:utdanningsprogram |




## LinkML Source

<details>
```yaml
name: utdanningsprogram
description: Utdanningsprogram.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:utdanningsprogram
domain_of:
- UtdanningContainer
- Skole
range: Utdanningsprogram
multivalued: true

```
</details>