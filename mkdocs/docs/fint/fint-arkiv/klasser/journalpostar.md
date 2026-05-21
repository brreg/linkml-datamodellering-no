

# Slot: journalpostar 



URI: [ark:journalpostar](https://schema.fintlabs.no/arkiv/journalpostar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ArkivContainer](arkivcontainer.md) | Rotcontainer for FINT Arkiv-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Journalpost](journalpost.md) |
| Domain Of | [ArkivContainer](arkivcontainer.md) |
| Slot URI | [ark:journalpostar](https://schema.fintlabs.no/arkiv/journalpostar) |

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
| self | ark:journalpostar |
| native | https://schema.fintlabs.no/arkiv/:journalpostar |




## LinkML Source

<details>
```yaml
name: journalpostar
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:journalpostar
domain_of:
- ArkivContainer
range: Journalpost
multivalued: true
inlined: true
inlined_as_list: true

```
</details>