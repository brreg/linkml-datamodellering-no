

# Slot: fagmerknader 



URI: [https://schema.fintlabs.no/utdanning/:fagmerknader](https://schema.fintlabs.no/utdanning/:fagmerknader)
Alias: fagmerknader

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](UtdanningContainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fagmerknad](Fagmerknad.md) |
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
| self | https://schema.fintlabs.no/utdanning/:fagmerknader |
| native | https://schema.fintlabs.no/utdanning/:fagmerknader |




## LinkML Source

<details>
```yaml
name: fagmerknader
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
alias: fagmerknader
owner: UtdanningContainer
domain_of:
- UtdanningContainer
range: Fagmerknad
multivalued: true
inlined: true
inlined_as_list: true

```
</details>