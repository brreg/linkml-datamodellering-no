

# Slot: saksmappetypar 



URI: [https://schema.fintlabs.no/arkiv/:saksmappetypar](https://schema.fintlabs.no/arkiv/:saksmappetypar)
Alias: saksmappetypar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ArkivContainer](ArkivContainer.md) | Rotcontainer for FINT Arkiv-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Saksmappetype](Saksmappetype.md) |
| Domain Of | [ArkivContainer](ArkivContainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ArkivContainer](ArkivContainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/arkiv/:saksmappetypar |
| native | https://schema.fintlabs.no/arkiv/:saksmappetypar |




## LinkML Source

<details>
```yaml
name: saksmappetypar
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
alias: saksmappetypar
owner: ArkivContainer
domain_of:
- ArkivContainer
range: Saksmappetype
multivalued: true
inlined: true
inlined_as_list: true

```
</details>