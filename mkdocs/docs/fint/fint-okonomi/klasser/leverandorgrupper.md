

# Slot: leverandorgrupper 



URI: [https://schema.fintlabs.no/okonomi/:leverandorgrupper](https://schema.fintlabs.no/okonomi/:leverandorgrupper)
Alias: leverandorgrupper

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OkonomiContainer](OkonomiContainer.md) | Rotcontainer for FINT Økonomi-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Leverandorgruppe](Leverandorgruppe.md) |
| Domain Of | [OkonomiContainer](OkonomiContainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [OkonomiContainer](OkonomiContainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/okonomi/:leverandorgrupper |
| native | https://schema.fintlabs.no/okonomi/:leverandorgrupper |




## LinkML Source

<details>
```yaml
name: leverandorgrupper
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
alias: leverandorgrupper
owner: OkonomiContainer
domain_of:
- OkonomiContainer
range: Leverandorgruppe
multivalued: true
inlined: true
inlined_as_list: true

```
</details>