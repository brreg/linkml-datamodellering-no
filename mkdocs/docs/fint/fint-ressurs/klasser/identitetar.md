

# Slot: identitetar 



URI: [https://schema.fintlabs.no/ressurs/:identitetar](https://schema.fintlabs.no/ressurs/:identitetar)
Alias: identitetar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RessursContainer](RessursContainer.md) | Rotcontainer for FINT Ressurs-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identitet](Identitet.md) |
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
| self | https://schema.fintlabs.no/ressurs/:identitetar |
| native | https://schema.fintlabs.no/ressurs/:identitetar |




## LinkML Source

<details>
```yaml
name: identitetar
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
alias: identitetar
owner: RessursContainer
domain_of:
- RessursContainer
range: Identitet
multivalued: true
inlined: true
inlined_as_list: true

```
</details>