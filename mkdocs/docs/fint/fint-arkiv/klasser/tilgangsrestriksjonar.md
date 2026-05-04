

# Slot: tilgangsrestriksjonar 



URI: [https://schema.fintlabs.no/arkiv/:tilgangsrestriksjonar](https://schema.fintlabs.no/arkiv/:tilgangsrestriksjonar)
Alias: tilgangsrestriksjonar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ArkivContainer](ArkivContainer.md) | Rotcontainer for FINT Arkiv-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Tilgangsrestriksjon](Tilgangsrestriksjon.md) |
| Domain Of | [ArkivContainer](ArkivContainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ArkivContainer](ArkivContainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/arkiv/:tilgangsrestriksjonar |
| native | https://schema.fintlabs.no/arkiv/:tilgangsrestriksjonar |




## LinkML Source

<details>
```yaml
name: tilgangsrestriksjonar
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
alias: tilgangsrestriksjonar
owner: ArkivContainer
domain_of:
- ArkivContainer
range: Tilgangsrestriksjon
multivalued: true
inlined: true
inlined_as_list: true

```
</details>