

# Slot: statusar 



URI: [res:statusar](https://schema.fintlabs.no/ressurs/statusar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RessursContainer](ressurscontainer.md) | Rotcontainer for FINT Ressurs-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Status](status.md) |
| Domain Of | [RessursContainer](ressurscontainer.md) |
| Slot URI | [res:statusar](https://schema.fintlabs.no/ressurs/statusar) |

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
| self | res:statusar |
| native | https://schema.fintlabs.no/ressurs/:statusar |




## LinkML Source

<details>
```yaml
name: statusar
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:statusar
domain_of:
- RessursContainer
range: Status
multivalued: true
inlined: true
inlined_as_list: true

```
</details>