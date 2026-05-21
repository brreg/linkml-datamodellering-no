

# Slot: rollar 


_Alle rollar i containeren._





URI: [adm:rollar](https://schema.fintlabs.no/administrasjon/rollar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Rolle](rolle.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md) |
| Slot URI | [adm:rollar](https://schema.fintlabs.no/administrasjon/rollar) |

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
| self | adm:rollar |
| native | https://schema.fintlabs.no/administrasjon/:rollar |




## LinkML Source

<details>
```yaml
name: rollar
description: Alle rollar i containeren.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:rollar
domain_of:
- AdministrasjonContainer
range: Rolle
multivalued: true
inlined: true
inlined_as_list: true

```
</details>