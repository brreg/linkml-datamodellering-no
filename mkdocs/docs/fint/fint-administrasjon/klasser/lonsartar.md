

# Slot: lonsartar 


_Alle lønnsartar i containeren._





URI: [adm:lonsartar](https://schema.fintlabs.no/administrasjon/lonsartar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Lonsart](lonsart.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md) |
| Slot URI | [adm:lonsartar](https://schema.fintlabs.no/administrasjon/lonsartar) |

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
| self | adm:lonsartar |
| native | https://schema.fintlabs.no/administrasjon/:lonsartar |




## LinkML Source

<details>
```yaml
name: lonsartar
description: Alle lønnsartar i containeren.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:lonsartar
domain_of:
- AdministrasjonContainer
range: Lonsart
multivalued: true
inlined: true
inlined_as_list: true

```
</details>