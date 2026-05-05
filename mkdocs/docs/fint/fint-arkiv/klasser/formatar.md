

# Slot: formatar 



URI: [https://schema.fintlabs.no/arkiv/:formatar](https://schema.fintlabs.no/arkiv/:formatar)
Alias: formatar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ArkivContainer](arkivcontainer.md) | Rotcontainer for FINT Arkiv-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Format](format.md) |
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
| self | https://schema.fintlabs.no/arkiv/:formatar |
| native | https://schema.fintlabs.no/arkiv/:formatar |




## LinkML Source

<details>
```yaml
name: formatar
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
alias: formatar
owner: ArkivContainer
domain_of:
- ArkivContainer
range: Format
multivalued: true
inlined: true
inlined_as_list: true

```
</details>