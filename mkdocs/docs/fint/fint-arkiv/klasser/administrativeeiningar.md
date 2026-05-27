

# Slot: administrativeEiningar 



URI: [https://schema.fintlabs.no/arkiv/:administrativeEiningar](https://schema.fintlabs.no/arkiv/:administrativeEiningar)
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


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/arkiv/:administrativeEiningar |
| native | https://schema.fintlabs.no/arkiv/:administrativeEiningar |




## LinkML Source

<details>
```yaml
name: administrativeEiningar
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
owner: ArkivContainer
domain_of:
- ArkivContainer
range: AdministrativEnhet
multivalued: true
inlined: true
inlined_as_list: true

```
</details>