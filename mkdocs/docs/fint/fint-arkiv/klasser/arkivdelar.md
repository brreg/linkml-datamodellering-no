

# Slot: arkivdelar 



URI: [ark:arkivdelar](https://schema.fintlabs.no/arkiv/arkivdelar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ArkivContainer](arkivcontainer.md) | Rotcontainer for FINT Arkiv-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Arkivdel](arkivdel.md) |
| Domain Of | [ArkivContainer](arkivcontainer.md) |
| Slot URI | [ark:arkivdelar](https://schema.fintlabs.no/arkiv/arkivdelar) |

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
| self | ark:arkivdelar |
| native | https://schema.fintlabs.no/arkiv/:arkivdelar |




## LinkML Source

<details>
```yaml
name: arkivdelar
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:arkivdelar
domain_of:
- ArkivContainer
range: Arkivdel
multivalued: true
inlined: true
inlined_as_list: true

```
</details>