

# Slot: administrativeEiningar 



URI: [ark:administrativeEiningar](https://schema.fintlabs.no/arkiv/administrativeEiningar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ArkivContainer](arkivcontainer.md) | Rotcontainer for FINT Arkiv-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AdministrativEnhet](administrativenhet.md) |
| Domain Of | [ArkivContainer](arkivcontainer.md) |
| Slot URI | [ark:administrativeEiningar](https://schema.fintlabs.no/arkiv/administrativeEiningar) |

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
| self | ark:administrativeEiningar |
| native | https://schema.fintlabs.no/arkiv/:administrativeEiningar |




## LinkML Source

<details>
```yaml
name: administrativeEiningar
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:administrativeEiningar
domain_of:
- ArkivContainer
range: AdministrativEnhet
multivalued: true
inlined: true
inlined_as_list: true

```
</details>