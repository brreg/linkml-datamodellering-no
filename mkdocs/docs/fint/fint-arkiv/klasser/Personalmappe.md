

# Slot: personalmappe 



URI: [https://schema.fintlabs.no/arkiv/:personalmappe](https://schema.fintlabs.no/arkiv/:personalmappe)
Alias: personalmappe

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ArkivContainer](arkivcontainer.md) | Rotcontainer for FINT Arkiv-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personalmappe](personalmappe.md) |
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
| self | https://schema.fintlabs.no/arkiv/:personalmappe |
| native | https://schema.fintlabs.no/arkiv/:personalmappe |




## LinkML Source

<details>
```yaml
name: personalmappe
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
alias: personalmappe
owner: ArkivContainer
domain_of:
- ArkivContainer
range: Personalmappe
multivalued: true
inlined: true
inlined_as_list: true

```
</details>