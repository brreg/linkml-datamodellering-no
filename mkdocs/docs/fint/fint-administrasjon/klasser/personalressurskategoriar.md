

# Slot: personalressurskategoriar 


_Alle personalressurskategoriar i containeren._





URI: [adm:personalressurskategoriar](https://schema.fintlabs.no/administrasjon/personalressurskategoriar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personalressurskategori](personalressurskategori.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md) |
| Slot URI | [adm:personalressurskategoriar](https://schema.fintlabs.no/administrasjon/personalressurskategoriar) |

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
| self | adm:personalressurskategoriar |
| native | https://schema.fintlabs.no/administrasjon/:personalressurskategoriar |




## LinkML Source

<details>
```yaml
name: personalressurskategoriar
description: Alle personalressurskategoriar i containeren.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:personalressurskategoriar
domain_of:
- AdministrasjonContainer
range: Personalressurskategori
multivalued: true
inlined: true
inlined_as_list: true

```
</details>