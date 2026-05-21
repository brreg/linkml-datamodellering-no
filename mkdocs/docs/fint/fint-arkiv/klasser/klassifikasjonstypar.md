

# Slot: klassifikasjonstypar 



URI: [ark:klassifikasjonstypar](https://schema.fintlabs.no/arkiv/klassifikasjonstypar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ArkivContainer](arkivcontainer.md) | Rotcontainer for FINT Arkiv-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Klassifikasjonstype](klassifikasjonstype.md) |
| Domain Of | [ArkivContainer](arkivcontainer.md) |
| Slot URI | [ark:klassifikasjonstypar](https://schema.fintlabs.no/arkiv/klassifikasjonstypar) |

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
| self | ark:klassifikasjonstypar |
| native | https://schema.fintlabs.no/arkiv/:klassifikasjonstypar |




## LinkML Source

<details>
```yaml
name: klassifikasjonstypar
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:klassifikasjonstypar
domain_of:
- ArkivContainer
range: Klassifikasjonstype
multivalued: true
inlined: true
inlined_as_list: true

```
</details>