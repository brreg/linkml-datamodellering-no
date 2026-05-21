

# Slot: fullmakter 


_Alle fullmakter i containeren._





URI: [adm:fullmakter](https://schema.fintlabs.no/administrasjon/fullmakter)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fullmakt](fullmakt.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md) |
| Slot URI | [adm:fullmakter](https://schema.fintlabs.no/administrasjon/fullmakter) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:fullmakter |
| native | https://schema.fintlabs.no/administrasjon/:fullmakter |




## LinkML Source

<details>
```yaml
name: fullmakter
description: Alle fullmakter i containeren.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:fullmakter
domain_of:
- AdministrasjonContainer
range: Fullmakt
multivalued: true
inlined: true
inlined_as_list: true

```
</details>