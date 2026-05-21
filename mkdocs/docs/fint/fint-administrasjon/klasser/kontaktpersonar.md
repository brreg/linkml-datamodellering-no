

# Slot: kontaktpersonar 


_Alle kontaktpersonar i containeren._





URI: [adm:kontaktpersonar](https://schema.fintlabs.no/administrasjon/kontaktpersonar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kontaktperson](kontaktperson.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md) |
| Slot URI | [adm:kontaktpersonar](https://schema.fintlabs.no/administrasjon/kontaktpersonar) |

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
| self | adm:kontaktpersonar |
| native | https://schema.fintlabs.no/administrasjon/:kontaktpersonar |




## LinkML Source

<details>
```yaml
name: kontaktpersonar
description: Alle kontaktpersonar i containeren.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:kontaktpersonar
domain_of:
- AdministrasjonContainer
range: Kontaktperson
multivalued: true
inlined: true
inlined_as_list: true

```
</details>