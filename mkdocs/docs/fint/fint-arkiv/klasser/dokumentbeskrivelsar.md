

# Slot: dokumentbeskrivelsar 



URI: [https://schema.fintlabs.no/arkiv/:dokumentbeskrivelsar](https://schema.fintlabs.no/arkiv/:dokumentbeskrivelsar)
Alias: dokumentbeskrivelsar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ArkivContainer](ArkivContainer.md) | Rotcontainer for FINT Arkiv-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Dokumentbeskrivelse](Dokumentbeskrivelse.md) |
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
| self | https://schema.fintlabs.no/arkiv/:dokumentbeskrivelsar |
| native | https://schema.fintlabs.no/arkiv/:dokumentbeskrivelsar |




## LinkML Source

<details>
```yaml
name: dokumentbeskrivelsar
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
alias: dokumentbeskrivelsar
owner: ArkivContainer
domain_of:
- ArkivContainer
range: Dokumentbeskrivelse
multivalued: true
inlined: true
inlined_as_list: true

```
</details>