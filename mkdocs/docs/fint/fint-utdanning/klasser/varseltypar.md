

# Slot: varseltypar 



URI: [https://schema.fintlabs.no/utdanning/:varseltypar](https://schema.fintlabs.no/utdanning/:varseltypar)
Alias: varseltypar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](UtdanningContainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Varseltype](Varseltype.md) |
| Domain Of | [UtdanningContainer](UtdanningContainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [UtdanningContainer](UtdanningContainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:varseltypar |
| native | https://schema.fintlabs.no/utdanning/:varseltypar |




## LinkML Source

<details>
```yaml
name: varseltypar
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
alias: varseltypar
owner: UtdanningContainer
domain_of:
- UtdanningContainer
range: Varseltype
multivalued: true
inlined: true
inlined_as_list: true

```
</details>