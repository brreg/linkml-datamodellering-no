

# Slot: elevar 



URI: [https://schema.fintlabs.no/utdanning/:elevar](https://schema.fintlabs.no/utdanning/:elevar)
Alias: elevar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](UtdanningContainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Elev](Elev.md) |
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
| self | https://schema.fintlabs.no/utdanning/:elevar |
| native | https://schema.fintlabs.no/utdanning/:elevar |




## LinkML Source

<details>
```yaml
name: elevar
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
alias: elevar
owner: UtdanningContainer
domain_of:
- UtdanningContainer
range: Elev
multivalued: true
inlined: true
inlined_as_list: true

```
</details>