

# Slot: provestatuser 



URI: [https://schema.fintlabs.no/utdanning/:provestatuser](https://schema.fintlabs.no/utdanning/:provestatuser)
Alias: provestatuser

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Provestatus](provestatus.md) |
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
| self | https://schema.fintlabs.no/utdanning/:provestatuser |
| native | https://schema.fintlabs.no/utdanning/:provestatuser |




## LinkML Source

<details>
```yaml
name: provestatuser
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
alias: provestatuser
owner: UtdanningContainer
domain_of:
- UtdanningContainer
range: Provestatus
multivalued: true
inlined: true
inlined_as_list: true

```
</details>