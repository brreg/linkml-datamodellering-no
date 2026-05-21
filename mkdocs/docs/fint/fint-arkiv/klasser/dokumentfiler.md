

# Slot: dokumentfiler 



URI: [ark:dokumentfiler](https://schema.fintlabs.no/arkiv/dokumentfiler)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ArkivContainer](arkivcontainer.md) | Rotcontainer for FINT Arkiv-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Dokumentfil](dokumentfil.md) |
| Domain Of | [ArkivContainer](arkivcontainer.md) |
| Slot URI | [ark:dokumentfiler](https://schema.fintlabs.no/arkiv/dokumentfiler) |

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
| self | ark:dokumentfiler |
| native | https://schema.fintlabs.no/arkiv/:dokumentfiler |




## LinkML Source

<details>
```yaml
name: dokumentfiler
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:dokumentfiler
domain_of:
- ArkivContainer
range: Dokumentfil
multivalued: true
inlined: true
inlined_as_list: true

```
</details>