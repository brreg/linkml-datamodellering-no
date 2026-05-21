

# Slot: produsentar 



URI: [res:produsentar](https://schema.fintlabs.no/ressurs/produsentar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RessursContainer](ressurscontainer.md) | Rotcontainer for FINT Ressurs-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Produsent](produsent.md) |
| Domain Of | [RessursContainer](ressurscontainer.md) |
| Slot URI | [res:produsentar](https://schema.fintlabs.no/ressurs/produsentar) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:produsentar |
| native | https://schema.fintlabs.no/ressurs/:produsentar |




## LinkML Source

<details>
```yaml
name: produsentar
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:produsentar
domain_of:
- RessursContainer
range: Produsent
multivalued: true
inlined: true
inlined_as_list: true

```
</details>