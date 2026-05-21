

# Slot: arkivressursar 



URI: [ark:arkivressursar](https://schema.fintlabs.no/arkiv/arkivressursar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ArkivContainer](arkivcontainer.md) | Rotcontainer for FINT Arkiv-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Arkivressurs](arkivressurs.md) |
| Domain Of | [ArkivContainer](arkivcontainer.md) |
| Slot URI | [ark:arkivressursar](https://schema.fintlabs.no/arkiv/arkivressursar) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:arkivressursar |
| native | https://schema.fintlabs.no/arkiv/:arkivressursar |




## LinkML Source

<details>
```yaml
name: arkivressursar
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:arkivressursar
domain_of:
- ArkivContainer
range: Arkivressurs
multivalued: true
inlined: true
inlined_as_list: true

```
</details>