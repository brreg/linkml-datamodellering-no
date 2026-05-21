

# Slot: varer 



URI: [okn:varer](https://schema.fintlabs.no/okonomi/varer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OkonomiContainer](okonomicontainer.md) | Rotcontainer for FINT Økonomi-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Vare](vare.md) |
| Domain Of | [OkonomiContainer](okonomicontainer.md) |
| Slot URI | [okn:varer](https://schema.fintlabs.no/okonomi/varer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:varer |
| native | https://schema.fintlabs.no/okonomi/:varer |




## LinkML Source

<details>
```yaml
name: varer
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:varer
domain_of:
- OkonomiContainer
range: Vare
multivalued: true
inlined: true
inlined_as_list: true

```
</details>