

# Slot: elevkategoriar 



URI: [https://schema.fintlabs.no/utdanning/:elevkategoriar](https://schema.fintlabs.no/utdanning/:elevkategoriar)
Alias: elevkategoriar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](UtdanningContainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Elevkategori](Elevkategori.md) |
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
| self | https://schema.fintlabs.no/utdanning/:elevkategoriar |
| native | https://schema.fintlabs.no/utdanning/:elevkategoriar |




## LinkML Source

<details>
```yaml
name: elevkategoriar
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
alias: elevkategoriar
owner: UtdanningContainer
domain_of:
- UtdanningContainer
range: Elevkategori
multivalued: true
inlined: true
inlined_as_list: true

```
</details>