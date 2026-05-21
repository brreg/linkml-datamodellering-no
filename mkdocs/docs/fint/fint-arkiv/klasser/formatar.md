

# Slot: formatar 



URI: [ark:formatar](https://schema.fintlabs.no/arkiv/formatar)
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
| Slot URI | [ark:formatar](https://schema.fintlabs.no/arkiv/formatar) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:formatar |
| native | https://schema.fintlabs.no/arkiv/:formatar |




## LinkML Source

<details>
```yaml
name: formatar
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:formatar
domain_of:
- ArkivContainer
range: Format
multivalued: true
inlined: true
inlined_as_list: true

```
</details>