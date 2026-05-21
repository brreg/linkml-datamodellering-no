

# Slot: identitetar 



URI: [res:identitetar](https://schema.fintlabs.no/ressurs/identitetar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RessursContainer](ressurscontainer.md) | Rotcontainer for FINT Ressurs-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identitet](identitet.md) |
| Domain Of | [RessursContainer](ressurscontainer.md) |
| Slot URI | [res:identitetar](https://schema.fintlabs.no/ressurs/identitetar) |

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
| self | res:identitetar |
| native | https://schema.fintlabs.no/ressurs/:identitetar |




## LinkML Source

<details>
```yaml
name: identitetar
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:identitetar
domain_of:
- RessursContainer
range: Identitet
multivalued: true
inlined: true
inlined_as_list: true

```
</details>