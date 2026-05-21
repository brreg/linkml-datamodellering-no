

# Slot: applikasjonar 



URI: [res:applikasjonar](https://schema.fintlabs.no/ressurs/applikasjonar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RessursContainer](ressurscontainer.md) | Rotcontainer for FINT Ressurs-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Applikasjon](applikasjon.md) |
| Domain Of | [RessursContainer](ressurscontainer.md) |
| Slot URI | [res:applikasjonar](https://schema.fintlabs.no/ressurs/applikasjonar) |

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
| self | res:applikasjonar |
| native | https://schema.fintlabs.no/ressurs/:applikasjonar |




## LinkML Source

<details>
```yaml
name: applikasjonar
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:applikasjonar
domain_of:
- RessursContainer
range: Applikasjon
multivalued: true
inlined: true
inlined_as_list: true

```
</details>