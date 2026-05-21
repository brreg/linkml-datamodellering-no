

# Slot: partRollar 



URI: [ark:partRollar](https://schema.fintlabs.no/arkiv/partRollar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ArkivContainer](arkivcontainer.md) | Rotcontainer for FINT Arkiv-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PartRolle](partrolle.md) |
| Domain Of | [ArkivContainer](arkivcontainer.md) |
| Slot URI | [ark:partRollar](https://schema.fintlabs.no/arkiv/partRollar) |

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
| self | ark:partRollar |
| native | https://schema.fintlabs.no/arkiv/:partRollar |




## LinkML Source

<details>
```yaml
name: partRollar
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:partRollar
domain_of:
- ArkivContainer
range: PartRolle
multivalued: true
inlined: true
inlined_as_list: true

```
</details>