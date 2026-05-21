

# Slot: fakturaer 



URI: [okn:fakturaer](https://schema.fintlabs.no/okonomi/fakturaer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OkonomiContainer](okonomicontainer.md) | Rotcontainer for FINT Økonomi-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Faktura](faktura.md) |
| Domain Of | [OkonomiContainer](okonomicontainer.md) |
| Slot URI | [okn:fakturaer](https://schema.fintlabs.no/okonomi/fakturaer) |

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
| self | okn:fakturaer |
| native | https://schema.fintlabs.no/okonomi/:fakturaer |




## LinkML Source

<details>
```yaml
name: fakturaer
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:fakturaer
domain_of:
- OkonomiContainer
range: Faktura
multivalued: true
inlined: true
inlined_as_list: true

```
</details>