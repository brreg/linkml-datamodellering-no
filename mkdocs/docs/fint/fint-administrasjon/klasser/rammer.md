

# Slot: rammer 


_Alle rammer i containeren._





URI: [adm:rammer](https://schema.fintlabs.no/administrasjon/rammer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Ramme](ramme.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md) |
| Slot URI | [adm:rammer](https://schema.fintlabs.no/administrasjon/rammer) |

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
| self | adm:rammer |
| native | https://schema.fintlabs.no/administrasjon/:rammer |




## LinkML Source

<details>
```yaml
name: rammer
description: Alle rammer i containeren.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:rammer
domain_of:
- AdministrasjonContainer
range: Ramme
multivalued: true
inlined: true
inlined_as_list: true

```
</details>