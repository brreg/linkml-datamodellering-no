

# Slot: arbeidslokasjoner 


_Alle arbeidslokasjoner i containeren._





URI: [adm:arbeidslokasjoner](https://schema.fintlabs.no/administrasjon/arbeidslokasjoner)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Arbeidslokasjon](arbeidslokasjon.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md) |
| Slot URI | [adm:arbeidslokasjoner](https://schema.fintlabs.no/administrasjon/arbeidslokasjoner) |

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
| self | adm:arbeidslokasjoner |
| native | https://schema.fintlabs.no/administrasjon/:arbeidslokasjoner |




## LinkML Source

<details>
```yaml
name: arbeidslokasjoner
description: Alle arbeidslokasjoner i containeren.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:arbeidslokasjoner
domain_of:
- AdministrasjonContainer
range: Arbeidslokasjon
multivalued: true
inlined: true
inlined_as_list: true

```
</details>