

# Slot: sakar 



URI: [ark:sakar](https://schema.fintlabs.no/arkiv/sakar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ArkivContainer](arkivcontainer.md) | Rotcontainer for FINT Arkiv-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Sak](sak.md) |
| Domain Of | [ArkivContainer](arkivcontainer.md) |
| Slot URI | [ark:sakar](https://schema.fintlabs.no/arkiv/sakar) |

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
| self | ark:sakar |
| native | https://schema.fintlabs.no/arkiv/:sakar |




## LinkML Source

<details>
```yaml
name: sakar
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:sakar
domain_of:
- ArkivContainer
range: Sak
multivalued: true
inlined: true
inlined_as_list: true

```
</details>