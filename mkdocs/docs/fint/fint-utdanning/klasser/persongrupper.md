

# Slot: persongrupper 



URI: [https://schema.fintlabs.no/utdanning/:persongrupper](https://schema.fintlabs.no/utdanning/:persongrupper)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Persongruppe](persongruppe.md) |
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


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/utdanning/:persongrupper |
| native | https://schema.fintlabs.no/utdanning/:persongrupper |




## LinkML Source

<details>
```yaml
name: persongrupper
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
owner: UtdanningContainer
domain_of:
- UtdanningContainer
range: Persongruppe
multivalued: true
inlined: true
inlined_as_list: true

```
</details>