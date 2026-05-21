

# Slot: kontrakter 


_Alle kontrakter i containeren._





URI: [adm:kontrakter](https://schema.fintlabs.no/administrasjon/kontrakter)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kontrakt](kontrakt.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md) |
| Slot URI | [adm:kontrakter](https://schema.fintlabs.no/administrasjon/kontrakter) |

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
| self | adm:kontrakter |
| native | https://schema.fintlabs.no/administrasjon/:kontrakter |




## LinkML Source

<details>
```yaml
name: kontrakter
description: Alle kontrakter i containeren.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:kontrakter
domain_of:
- AdministrasjonContainer
range: Kontrakt
multivalued: true
inlined: true
inlined_as_list: true

```
</details>