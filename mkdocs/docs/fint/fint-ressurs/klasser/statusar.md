

# Slot: statusar 



URI: [https://schema.fintlabs.no/ressurs/:statusar](https://schema.fintlabs.no/ressurs/:statusar)
Alias: statusar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RessursContainer](RessursContainer.md) | Rotcontainer for FINT Ressurs-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Status](Status.md) |
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
| self | https://schema.fintlabs.no/ressurs/:statusar |
| native | https://schema.fintlabs.no/ressurs/:statusar |




## LinkML Source

<details>
```yaml
name: statusar
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
alias: statusar
owner: RessursContainer
domain_of:
- RessursContainer
range: Status
multivalued: true
inlined: true
inlined_as_list: true

```
</details>