

# Slot: landkodar 


_Alle landkodar i containeren._





URI: [adm:landkodar](https://schema.fintlabs.no/administrasjon/landkodar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Landkode](landkode.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md) |
| Slot URI | [adm:landkodar](https://schema.fintlabs.no/administrasjon/landkodar) |

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
| self | adm:landkodar |
| native | https://schema.fintlabs.no/administrasjon/:landkodar |




## LinkML Source

<details>
```yaml
name: landkodar
description: Alle landkodar i containeren.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:landkodar
domain_of:
- AdministrasjonContainer
range: Landkode
multivalued: true
inlined: true
inlined_as_list: true

```
</details>