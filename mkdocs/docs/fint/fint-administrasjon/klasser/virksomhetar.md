

# Slot: virksomhetar 


_Alle verksemder i containeren._





URI: [adm:virksomhetar](https://schema.fintlabs.no/administrasjon/virksomhetar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Virksomhet](virksomhet.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md) |
| Slot URI | [adm:virksomhetar](https://schema.fintlabs.no/administrasjon/virksomhetar) |

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
| self | adm:virksomhetar |
| native | https://schema.fintlabs.no/administrasjon/:virksomhetar |




## LinkML Source

<details>
```yaml
name: virksomhetar
description: Alle verksemder i containeren.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:virksomhetar
domain_of:
- AdministrasjonContainer
range: Virksomhet
multivalued: true
inlined: true
inlined_as_list: true

```
</details>