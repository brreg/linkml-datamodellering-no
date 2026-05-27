

# Slot: plattformar 



URI: [https://schema.fintlabs.no/ressurs/:plattformar](https://schema.fintlabs.no/ressurs/:plattformar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RessursContainer](ressurscontainer.md) | Rotcontainer for FINT Ressurs-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Plattform](plattform.md) |
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
| self | https://schema.fintlabs.no/ressurs/:plattformar |
| native | https://schema.fintlabs.no/ressurs/:plattformar |




## LinkML Source

<details>
```yaml
name: plattformar
from_schema: https://data.norge.no/fint/fint-ressurs
rank: 1000
owner: RessursContainer
domain_of:
- RessursContainer
range: Plattform
multivalued: true
inlined: true
inlined_as_list: true

```
</details>