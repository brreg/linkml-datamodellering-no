

# Slot: fakturautstederear 



URI: [https://schema.fintlabs.no/okonomi/:fakturautstederear](https://schema.fintlabs.no/okonomi/:fakturautstederear)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OkonomiContainer](okonomicontainer.md) | Rotcontainer for FINT Økonomi-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fakturautsteder](fakturautsteder.md) |
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
| self | https://schema.fintlabs.no/okonomi/:fakturautstederear |
| native | https://schema.fintlabs.no/okonomi/:fakturautstederear |




## LinkML Source

<details>
```yaml
name: fakturautstederear
from_schema: https://data.norge.no/fint/fint-okonomi
rank: 1000
owner: OkonomiContainer
domain_of:
- OkonomiContainer
range: Fakturautsteder
multivalued: true
inlined: true
inlined_as_list: true

```
</details>