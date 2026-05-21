

# Slot: leverandorgrupper 



URI: [okn:leverandorgrupper](https://schema.fintlabs.no/okonomi/leverandorgrupper)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OkonomiContainer](okonomicontainer.md) | Rotcontainer for FINT Økonomi-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Leverandorgruppe](leverandorgruppe.md) |
| Domain Of | [OkonomiContainer](okonomicontainer.md) |
| Slot URI | [okn:leverandorgrupper](https://schema.fintlabs.no/okonomi/leverandorgrupper) |

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
| self | okn:leverandorgrupper |
| native | https://schema.fintlabs.no/okonomi/:leverandorgrupper |




## LinkML Source

<details>
```yaml
name: leverandorgrupper
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:leverandorgrupper
domain_of:
- OkonomiContainer
range: Leverandorgruppe
multivalued: true
inlined: true
inlined_as_list: true

```
</details>