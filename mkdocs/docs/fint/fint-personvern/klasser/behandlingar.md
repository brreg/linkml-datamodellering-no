

# Slot: behandlingar 



URI: [https://schema.fintlabs.no/personvern/:behandlingar](https://schema.fintlabs.no/personvern/:behandlingar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonvernContainer](personverncontainer.md) | Rotcontainer for FINT Personvern-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Behandling](behandling.md) |
| Domain Of | [PersonvernContainer](personverncontainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PersonvernContainer](personverncontainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/personvern/:behandlingar |
| native | https://schema.fintlabs.no/personvern/:behandlingar |




## LinkML Source

<details>
```yaml
name: behandlingar
from_schema: https://data.norge.no/fint/fint-personvern
rank: 1000
owner: PersonvernContainer
domain_of:
- PersonvernContainer
range: Behandling
multivalued: true
inlined: true
inlined_as_list: true

```
</details>