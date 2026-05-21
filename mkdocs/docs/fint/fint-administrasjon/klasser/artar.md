

# Slot: artar 


_Alle artar i containeren._





URI: [adm:artar](https://schema.fintlabs.no/administrasjon/artar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Art](art.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md) |
| Slot URI | [adm:artar](https://schema.fintlabs.no/administrasjon/artar) |

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
| self | adm:artar |
| native | https://schema.fintlabs.no/administrasjon/:artar |




## LinkML Source

<details>
```yaml
name: artar
description: Alle artar i containeren.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:artar
domain_of:
- AdministrasjonContainer
range: Art
multivalued: true
inlined: true
inlined_as_list: true

```
</details>