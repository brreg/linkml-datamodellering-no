

# Slot: personalmappe_liste 



URI: [ark:personalmappe](https://schema.fintlabs.no/arkiv/personalmappe)
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
| Slot URI | [ark:personalmappe](https://schema.fintlabs.no/arkiv/personalmappe) |

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
| self | ark:personalmappe |
| native | https://schema.fintlabs.no/arkiv/:personalmappe_liste |




## LinkML Source

<details>
```yaml
name: personalmappe_liste
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:personalmappe
domain_of:
- ArkivContainer
range: Personalmappe
multivalued: true
inlined: true
inlined_as_list: true

```
</details>