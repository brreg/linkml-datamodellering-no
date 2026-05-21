

# Slot: organisasjonstypar 


_Alle organisasjonstypar i containeren._





URI: [adm:organisasjonstypar](https://schema.fintlabs.no/administrasjon/organisasjonstypar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Organisasjonstype](organisasjonstype.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md) |
| Slot URI | [adm:organisasjonstypar](https://schema.fintlabs.no/administrasjon/organisasjonstypar) |

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
| self | adm:organisasjonstypar |
| native | https://schema.fintlabs.no/administrasjon/:organisasjonstypar |




## LinkML Source

<details>
```yaml
name: organisasjonstypar
description: Alle organisasjonstypar i containeren.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:organisasjonstypar
domain_of:
- AdministrasjonContainer
range: Organisasjonstype
multivalued: true
inlined: true
inlined_as_list: true

```
</details>