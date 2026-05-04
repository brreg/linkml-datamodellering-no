

# Slot: produsentar 



URI: [https://schema.fintlabs.no/ressurs/:produsentar](https://schema.fintlabs.no/ressurs/:produsentar)
Alias: produsentar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RessursContainer](RessursContainer.md) | Rotcontainer for FINT Ressurs-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Produsent](Produsent.md) |
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
| self | https://schema.fintlabs.no/ressurs/:produsentar |
| native | https://schema.fintlabs.no/ressurs/:produsentar |




## LinkML Source

<details>
```yaml
name: produsentar
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
alias: produsentar
owner: RessursContainer
domain_of:
- RessursContainer
range: Produsent
multivalued: true
inlined: true
inlined_as_list: true

```
</details>