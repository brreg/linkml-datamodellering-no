

# Slot: kontaktlaerergrupper 



URI: [https://schema.fintlabs.no/utdanning/:kontaktlaerergrupper](https://schema.fintlabs.no/utdanning/:kontaktlaerergrupper)
Alias: kontaktlaerergrupper

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kontaktlaerergruppe](kontaktlaerergruppe.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [UtdanningContainer](utdanningcontainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:kontaktlaerergrupper |
| native | https://schema.fintlabs.no/utdanning/:kontaktlaerergrupper |




## LinkML Source

<details>
```yaml
name: kontaktlaerergrupper
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
alias: kontaktlaerergrupper
owner: UtdanningContainer
domain_of:
- UtdanningContainer
range: Kontaktlaerergruppe
multivalued: true
inlined: true
inlined_as_list: true

```
</details>