

# Slot: brukertypar 



URI: [https://schema.fintlabs.no/ressurs/:brukertypar](https://schema.fintlabs.no/ressurs/:brukertypar)
Alias: brukertypar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RessursContainer](RessursContainer.md) | Rotcontainer for FINT Ressurs-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Brukertype](Brukertype.md) |
| Domain Of | [RessursContainer](RessursContainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [RessursContainer](RessursContainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/ressurs/:brukertypar |
| native | https://schema.fintlabs.no/ressurs/:brukertypar |




## LinkML Source

<details>
```yaml
name: brukertypar
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
alias: brukertypar
owner: RessursContainer
domain_of:
- RessursContainer
range: Brukertype
multivalued: true
inlined: true
inlined_as_list: true

```
</details>