

# Slot: rollar 



URI: [ark:rollar](https://schema.fintlabs.no/arkiv/rollar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ArkivContainer](arkivcontainer.md) | Rotcontainer for FINT Arkiv-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Rolle](rolle.md) |
| Domain Of | [ArkivContainer](arkivcontainer.md) |
| Slot URI | [ark:rollar](https://schema.fintlabs.no/arkiv/rollar) |

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
| self | ark:rollar |
| native | https://schema.fintlabs.no/arkiv/:rollar |




## LinkML Source

<details>
```yaml
name: rollar
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:rollar
domain_of:
- ArkivContainer
range: Rolle
multivalued: true
inlined: true
inlined_as_list: true

```
</details>