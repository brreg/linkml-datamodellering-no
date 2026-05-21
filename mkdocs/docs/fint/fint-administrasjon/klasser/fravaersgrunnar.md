

# Slot: fravaersgrunnar 


_Alle fråværsgrunnar i containeren._





URI: [adm:fravaersgrunnar](https://schema.fintlabs.no/administrasjon/fravaersgrunnar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fravaersgrunn](fravaersgrunn.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md) |
| Slot URI | [adm:fravaersgrunnar](https://schema.fintlabs.no/administrasjon/fravaersgrunnar) |

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
| self | adm:fravaersgrunnar |
| native | https://schema.fintlabs.no/administrasjon/:fravaersgrunnar |




## LinkML Source

<details>
```yaml
name: fravaersgrunnar
description: Alle fråværsgrunnar i containeren.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:fravaersgrunnar
domain_of:
- AdministrasjonContainer
range: Fravaersgrunn
multivalued: true
inlined: true
inlined_as_list: true

```
</details>