

# Slot: behandlingar 



URI: [https://schema.fintlabs.no/personvern/:behandlingar](https://schema.fintlabs.no/personvern/:behandlingar)
Alias: behandlingar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonvernContainer](PersonvernContainer.md) | Rotcontainer for FINT Personvern-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Behandling](Behandling.md) |
| Domain Of | [PersonvernContainer](PersonvernContainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PersonvernContainer](PersonvernContainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/personvern/:behandlingar |
| native | https://schema.fintlabs.no/personvern/:behandlingar |




## LinkML Source

<details>
```yaml
name: behandlingar
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
alias: behandlingar
owner: PersonvernContainer
domain_of:
- PersonvernContainer
range: Behandling
multivalued: true
inlined: true
inlined_as_list: true

```
</details>