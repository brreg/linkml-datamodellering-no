

# Slot: personalressursar 


_Alle personalressursar i containeren._





URI: [adm:personalressursar](https://schema.fintlabs.no/administrasjon/personalressursar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personalressurs](personalressurs.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md) |
| Slot URI | [adm:personalressursar](https://schema.fintlabs.no/administrasjon/personalressursar) |

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
| self | adm:personalressursar |
| native | https://schema.fintlabs.no/administrasjon/:personalressursar |




## LinkML Source

<details>
```yaml
name: personalressursar
description: Alle personalressursar i containeren.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:personalressursar
domain_of:
- AdministrasjonContainer
range: Personalressurs
multivalued: true
inlined: true
inlined_as_list: true

```
</details>