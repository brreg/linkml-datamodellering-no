

# Slot: kommunar 


_Alle kommuneverdiar i containeren._





URI: [adm:kommunar](https://schema.fintlabs.no/administrasjon/kommunar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kommune](kommune.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md) |
| Slot URI | [adm:kommunar](https://schema.fintlabs.no/administrasjon/kommunar) |

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
| self | adm:kommunar |
| native | https://schema.fintlabs.no/administrasjon/:kommunar |




## LinkML Source

<details>
```yaml
name: kommunar
description: Alle kommuneverdiar i containeren.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:kommunar
domain_of:
- AdministrasjonContainer
range: Kommune
multivalued: true
inlined: true
inlined_as_list: true

```
</details>