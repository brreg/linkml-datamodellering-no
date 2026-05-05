

# Slot: dokumenttypar 



URI: [https://schema.fintlabs.no/arkiv/:dokumenttypar](https://schema.fintlabs.no/arkiv/:dokumenttypar)
Alias: dokumenttypar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ArkivContainer](arkivcontainer.md) | Rotcontainer for FINT Arkiv-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DokumentType](dokumenttype.md) |
| Domain Of | [ArkivContainer](arkivcontainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ArkivContainer](arkivcontainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/arkiv/:dokumenttypar |
| native | https://schema.fintlabs.no/arkiv/:dokumenttypar |




## LinkML Source

<details>
```yaml
name: dokumenttypar
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
alias: dokumenttypar
owner: ArkivContainer
domain_of:
- ArkivContainer
range: DokumentType
multivalued: true
inlined: true
inlined_as_list: true

```
</details>