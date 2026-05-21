

# Slot: leverandorar 



URI: [okn:leverandorar](https://schema.fintlabs.no/okonomi/leverandorar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OkonomiContainer](okonomicontainer.md) | Rotcontainer for FINT Økonomi-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Leverandor](leverandor.md) |
| Domain Of | [OkonomiContainer](okonomicontainer.md) |
| Slot URI | [okn:leverandorar](https://schema.fintlabs.no/okonomi/leverandorar) |

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
| self | okn:leverandorar |
| native | https://schema.fintlabs.no/okonomi/:leverandorar |




## LinkML Source

<details>
```yaml
name: leverandorar
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:leverandorar
domain_of:
- OkonomiContainer
range: Leverandor
multivalued: true
inlined: true
inlined_as_list: true

```
</details>