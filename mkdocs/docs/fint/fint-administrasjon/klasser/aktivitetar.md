

# Slot: aktivitetar 


_Alle aktivitetar i containeren._





URI: [adm:aktivitetar](https://schema.fintlabs.no/administrasjon/aktivitetar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Aktivitet](aktivitet.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md) |
| Slot URI | [adm:aktivitetar](https://schema.fintlabs.no/administrasjon/aktivitetar) |

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
| self | adm:aktivitetar |
| native | https://schema.fintlabs.no/administrasjon/:aktivitetar |




## LinkML Source

<details>
```yaml
name: aktivitetar
description: Alle aktivitetar i containeren.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:aktivitetar
domain_of:
- AdministrasjonContainer
range: Aktivitet
multivalued: true
inlined: true
inlined_as_list: true

```
</details>