

# Slot: otEnheter 


_Alle OT-einingar i containeren._





URI: [utd:otEnheter](https://schema.fintlabs.no/utdanning/otEnheter)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OtEnhet](otenhet.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |
| Slot URI | [utd:otEnheter](https://schema.fintlabs.no/utdanning/otEnheter) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:otEnheter |
| native | https://schema.fintlabs.no/utdanning/:otEnheter |




## LinkML Source

<details>
```yaml
name: otEnheter
description: Alle OT-einingar i containeren.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:otEnheter
domain_of:
- UtdanningContainer
range: OtEnhet
multivalued: true
inlined: true
inlined_as_list: true

```
</details>