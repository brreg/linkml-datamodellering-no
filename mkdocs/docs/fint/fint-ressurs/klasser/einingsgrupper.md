

# Slot: einingsgrupper 



URI: [res:einingsgrupper](https://schema.fintlabs.no/ressurs/einingsgrupper)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RessursContainer](ressurscontainer.md) | Rotcontainer for FINT Ressurs-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Enhetsgruppe](enhetsgruppe.md) |
| Domain Of | [RessursContainer](ressurscontainer.md) |
| Slot URI | [res:einingsgrupper](https://schema.fintlabs.no/ressurs/einingsgrupper) |

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
| self | res:einingsgrupper |
| native | https://schema.fintlabs.no/ressurs/:einingsgrupper |




## LinkML Source

<details>
```yaml
name: einingsgrupper
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:einingsgrupper
domain_of:
- RessursContainer
range: Enhetsgruppe
multivalued: true
inlined: true
inlined_as_list: true

```
</details>