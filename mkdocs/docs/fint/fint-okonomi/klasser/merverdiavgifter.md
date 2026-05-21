

# Slot: merverdiavgifter 



URI: [okn:merverdiavgifter](https://schema.fintlabs.no/okonomi/merverdiavgifter)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OkonomiContainer](okonomicontainer.md) | Rotcontainer for FINT Økonomi-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Merverdiavgift](merverdiavgift.md) |
| Domain Of | [OkonomiContainer](okonomicontainer.md) |
| Slot URI | [okn:merverdiavgifter](https://schema.fintlabs.no/okonomi/merverdiavgifter) |

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
| self | okn:merverdiavgifter |
| native | https://schema.fintlabs.no/okonomi/:merverdiavgifter |




## LinkML Source

<details>
```yaml
name: merverdiavgifter
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:merverdiavgifter
domain_of:
- OkonomiContainer
range: Merverdiavgift
multivalued: true
inlined: true
inlined_as_list: true

```
</details>