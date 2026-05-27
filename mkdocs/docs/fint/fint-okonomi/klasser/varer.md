

# Slot: varer 



URI: [https://schema.fintlabs.no/okonomi/:varer](https://schema.fintlabs.no/okonomi/:varer)
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

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [OkonomiContainer](okonomicontainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/okonomi/:varer |
| native | https://schema.fintlabs.no/okonomi/:varer |




## LinkML Source

<details>
```yaml
name: varer
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
owner: OkonomiContainer
domain_of:
- OkonomiContainer
range: Vare
multivalued: true
inlined: true
inlined_as_list: true

```
</details>