

# Slot: dokumentbeskrivelsar 



URI: [ark:dokumentbeskrivelsar](https://schema.fintlabs.no/arkiv/dokumentbeskrivelsar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ArkivContainer](arkivcontainer.md) | Rotcontainer for FINT Arkiv-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Dokumentbeskrivelse](dokumentbeskrivelse.md) |
| Domain Of | [ArkivContainer](arkivcontainer.md) |
| Slot URI | [ark:dokumentbeskrivelsar](https://schema.fintlabs.no/arkiv/dokumentbeskrivelsar) |

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
| self | ark:dokumentbeskrivelsar |
| native | https://schema.fintlabs.no/arkiv/:dokumentbeskrivelsar |




## LinkML Source

<details>
```yaml
name: dokumentbeskrivelsar
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:dokumentbeskrivelsar
domain_of:
- ArkivContainer
range: Dokumentbeskrivelse
multivalued: true
inlined: true
inlined_as_list: true

```
</details>