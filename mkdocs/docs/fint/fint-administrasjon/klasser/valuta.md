

# Slot: valuta 



URI: [https://schema.fintlabs.no/administrasjon/:valuta](https://schema.fintlabs.no/administrasjon/:valuta)
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
| self | https://schema.fintlabs.no/administrasjon/:valuta |
| native | https://schema.fintlabs.no/administrasjon/:valuta |




## LinkML Source

<details>
```yaml
name: valuta
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
owner: AdministrasjonContainer
domain_of:
- AdministrasjonContainer
range: Valuta
multivalued: true
inlined: true
inlined_as_list: true

```
</details>