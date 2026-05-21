

# Slot: personar 


_Alle personar i containeren._





URI: [adm:personar](https://schema.fintlabs.no/administrasjon/personar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Person](person.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md) |
| Slot URI | [adm:personar](https://schema.fintlabs.no/administrasjon/personar) |

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
| self | adm:personar |
| native | https://schema.fintlabs.no/administrasjon/:personar |




## LinkML Source

<details>
```yaml
name: personar
description: Alle personar i containeren.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:personar
domain_of:
- AdministrasjonContainer
range: Person
multivalued: true
inlined: true
inlined_as_list: true

```
</details>