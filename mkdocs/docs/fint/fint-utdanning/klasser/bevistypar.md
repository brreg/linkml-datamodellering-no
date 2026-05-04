

# Slot: bevistypar 



URI: [https://schema.fintlabs.no/utdanning/:bevistypar](https://schema.fintlabs.no/utdanning/:bevistypar)
Alias: bevistypar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](UtdanningContainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Bevistype](Bevistype.md) |
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
| self | https://schema.fintlabs.no/utdanning/:bevistypar |
| native | https://schema.fintlabs.no/utdanning/:bevistypar |




## LinkML Source

<details>
```yaml
name: bevistypar
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
alias: bevistypar
owner: UtdanningContainer
domain_of:
- UtdanningContainer
range: Bevistype
multivalued: true
inlined: true
inlined_as_list: true

```
</details>