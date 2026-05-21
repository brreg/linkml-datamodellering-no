

# Slot: karakterstatus 


_Karakterstatus._





URI: [utd:karakterstatus](https://schema.fintlabs.no/utdanning/karakterstatus)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |  yes  |
| [Karakterhistorie](karakterhistorie.md) | Historikk over endringar i ein karakter |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Karakterstatus](karakterstatus.md) |
| Domain Of | [UtdanningContainer](utdanningcontainer.md), [Karakterhistorie](karakterhistorie.md) |
| Slot URI | [utd:karakterstatus](https://schema.fintlabs.no/utdanning/karakterstatus) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:karakterstatus |
| native | https://schema.fintlabs.no/utdanning/:karakterstatus |




## LinkML Source

<details>
```yaml
name: karakterstatus
description: Karakterstatus.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:karakterstatus
domain_of:
- UtdanningContainer
- Karakterhistorie
range: Karakterstatus

```
</details>