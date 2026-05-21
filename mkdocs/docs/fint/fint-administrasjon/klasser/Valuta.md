

# Slot: valuta 


_Alle valutaverdiar i containeren._





URI: [adm:valuta](https://schema.fintlabs.no/administrasjon/valuta)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Valuta](valuta.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md) |
| Slot URI | [adm:valuta](https://schema.fintlabs.no/administrasjon/valuta) |

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
| self | adm:valuta |
| native | https://schema.fintlabs.no/administrasjon/:valuta |




## LinkML Source

<details>
```yaml
name: valuta
description: Alle valutaverdiar i containeren.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:valuta
domain_of:
- AdministrasjonContainer
range: Valuta
multivalued: true
inlined: true
inlined_as_list: true

```
</details>