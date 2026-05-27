

# Slot: fullmakter 



URI: [https://schema.fintlabs.no/administrasjon/:fullmakter](https://schema.fintlabs.no/administrasjon/:fullmakter)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fullmakt](fullmakt.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AdministrasjonContainer](administrasjoncontainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/administrasjon/:fullmakter |
| native | https://schema.fintlabs.no/administrasjon/:fullmakter |




## LinkML Source

<details>
```yaml
name: fullmakter
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
owner: AdministrasjonContainer
domain_of:
- AdministrasjonContainer
range: Fullmakt
multivalued: true
inlined: true
inlined_as_list: true

```
</details>