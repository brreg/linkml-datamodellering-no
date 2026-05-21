

# Slot: spraak 


_Alle språkverdiar i containeren._





URI: [adm:spraak](https://schema.fintlabs.no/administrasjon/spraak)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Spraak](spraak.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md) |
| Slot URI | [adm:spraak](https://schema.fintlabs.no/administrasjon/spraak) |

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
| self | adm:spraak |
| native | https://schema.fintlabs.no/administrasjon/:spraak |




## LinkML Source

<details>
```yaml
name: spraak
description: Alle språkverdiar i containeren.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:spraak
domain_of:
- AdministrasjonContainer
range: Spraak
multivalued: true
inlined: true
inlined_as_list: true

```
</details>