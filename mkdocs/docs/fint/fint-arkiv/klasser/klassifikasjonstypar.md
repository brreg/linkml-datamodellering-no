

# Slot: klassifikasjonstypar 



URI: [https://schema.fintlabs.no/arkiv/:klassifikasjonstypar](https://schema.fintlabs.no/arkiv/:klassifikasjonstypar)
Alias: klassifikasjonstypar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ArkivContainer](ArkivContainer.md) | Rotcontainer for FINT Arkiv-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Klassifikasjonstype](Klassifikasjonstype.md) |
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
| self | https://schema.fintlabs.no/arkiv/:klassifikasjonstypar |
| native | https://schema.fintlabs.no/arkiv/:klassifikasjonstypar |




## LinkML Source

<details>
```yaml
name: klassifikasjonstypar
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
alias: klassifikasjonstypar
owner: ArkivContainer
domain_of:
- ArkivContainer
range: Klassifikasjonstype
multivalued: true
inlined: true
inlined_as_list: true

```
</details>