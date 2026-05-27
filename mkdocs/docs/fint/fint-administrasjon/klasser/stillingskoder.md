

# Slot: stillingskoder 



URI: [https://schema.fintlabs.no/administrasjon/:stillingskoder](https://schema.fintlabs.no/administrasjon/:stillingskoder)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Stillingskode](stillingskode.md) |
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
| self | https://schema.fintlabs.no/administrasjon/:stillingskoder |
| native | https://schema.fintlabs.no/administrasjon/:stillingskoder |




## LinkML Source

<details>
```yaml
name: stillingskoder
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
owner: AdministrasjonContainer
domain_of:
- AdministrasjonContainer
range: Stillingskode
multivalued: true
inlined: true
inlined_as_list: true

```
</details>