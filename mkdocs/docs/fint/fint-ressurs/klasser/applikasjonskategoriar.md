

# Slot: applikasjonskategoriar 



URI: [https://schema.fintlabs.no/ressurs/:applikasjonskategoriar](https://schema.fintlabs.no/ressurs/:applikasjonskategoriar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RessursContainer](ressurscontainer.md) | Rotcontainer for FINT Ressurs-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Applikasjonskategori](applikasjonskategori.md) |
| Domain Of | [RessursContainer](ressurscontainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [RessursContainer](ressurscontainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/ressurs/:applikasjonskategoriar |
| native | https://schema.fintlabs.no/ressurs/:applikasjonskategoriar |




## LinkML Source

<details>
```yaml
name: applikasjonskategoriar
from_schema: https://data.norge.no/fint/fint-ressurs
rank: 1000
owner: RessursContainer
domain_of:
- RessursContainer
range: Applikasjonskategori
multivalued: true
inlined: true
inlined_as_list: true

```
</details>