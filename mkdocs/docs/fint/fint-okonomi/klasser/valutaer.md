

# Slot: valutaer 



URI: [okn:valutaer](https://schema.fintlabs.no/okonomi/valutaer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OkonomiContainer](okonomicontainer.md) | Rotcontainer for FINT Økonomi-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OkonomiValuta](okonomivaluta.md) |
| Domain Of | [OkonomiContainer](okonomicontainer.md) |
| Slot URI | [okn:valutaer](https://schema.fintlabs.no/okonomi/valutaer) |

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
| self | okn:valutaer |
| native | https://schema.fintlabs.no/okonomi/:valutaer |




## LinkML Source

<details>
```yaml
name: valutaer
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:valutaer
domain_of:
- OkonomiContainer
range: OkonomiValuta
multivalued: true
inlined: true
inlined_as_list: true

```
</details>