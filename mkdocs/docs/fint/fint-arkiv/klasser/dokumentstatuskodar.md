

# Slot: dokumentstatuskodar 



URI: [ark:dokumentstatuskodar](https://schema.fintlabs.no/arkiv/dokumentstatuskodar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ArkivContainer](arkivcontainer.md) | Rotcontainer for FINT Arkiv-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DokumentStatus](dokumentstatus.md) |
| Domain Of | [ArkivContainer](arkivcontainer.md) |
| Slot URI | [ark:dokumentstatuskodar](https://schema.fintlabs.no/arkiv/dokumentstatuskodar) |

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
| self | ark:dokumentstatuskodar |
| native | https://schema.fintlabs.no/arkiv/:dokumentstatuskodar |




## LinkML Source

<details>
```yaml
name: dokumentstatuskodar
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:dokumentstatuskodar
domain_of:
- ArkivContainer
range: DokumentStatus
multivalued: true
inlined: true
inlined_as_list: true

```
</details>