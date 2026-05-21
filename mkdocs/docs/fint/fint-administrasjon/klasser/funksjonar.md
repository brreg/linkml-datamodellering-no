

# Slot: funksjonar 


_Alle funksjonar i containeren._





URI: [adm:funksjonar](https://schema.fintlabs.no/administrasjon/funksjonar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Funksjon](funksjon.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md) |
| Slot URI | [adm:funksjonar](https://schema.fintlabs.no/administrasjon/funksjonar) |

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
| self | adm:funksjonar |
| native | https://schema.fintlabs.no/administrasjon/:funksjonar |




## LinkML Source

<details>
```yaml
name: funksjonar
description: Alle funksjonar i containeren.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:funksjonar
domain_of:
- AdministrasjonContainer
range: Funksjon
multivalued: true
inlined: true
inlined_as_list: true

```
</details>