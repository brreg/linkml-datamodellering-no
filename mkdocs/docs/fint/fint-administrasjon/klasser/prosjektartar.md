

# Slot: prosjektartar 


_Alle prosjektartar i containeren._





URI: [adm:prosjektartar](https://schema.fintlabs.no/administrasjon/prosjektartar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Prosjektart](prosjektart.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md) |
| Slot URI | [adm:prosjektartar](https://schema.fintlabs.no/administrasjon/prosjektartar) |

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
| self | adm:prosjektartar |
| native | https://schema.fintlabs.no/administrasjon/:prosjektartar |




## LinkML Source

<details>
```yaml
name: prosjektartar
description: Alle prosjektartar i containeren.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:prosjektartar
domain_of:
- AdministrasjonContainer
range: Prosjektart
multivalued: true
inlined: true
inlined_as_list: true

```
</details>