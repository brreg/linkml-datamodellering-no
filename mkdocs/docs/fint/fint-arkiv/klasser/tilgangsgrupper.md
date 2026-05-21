

# Slot: tilgangsgrupper 



URI: [ark:tilgangsgrupper](https://schema.fintlabs.no/arkiv/tilgangsgrupper)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ArkivContainer](arkivcontainer.md) | Rotcontainer for FINT Arkiv-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Tilgangsgruppe](tilgangsgruppe.md) |
| Domain Of | [ArkivContainer](arkivcontainer.md) |
| Slot URI | [ark:tilgangsgrupper](https://schema.fintlabs.no/arkiv/tilgangsgrupper) |

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
| self | ark:tilgangsgrupper |
| native | https://schema.fintlabs.no/arkiv/:tilgangsgrupper |




## LinkML Source

<details>
```yaml
name: tilgangsgrupper
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:tilgangsgrupper
domain_of:
- ArkivContainer
range: Tilgangsgruppe
multivalued: true
inlined: true
inlined_as_list: true

```
</details>