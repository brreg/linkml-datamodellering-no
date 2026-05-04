

# Slot: stillingskoder 



URI: [https://schema.fintlabs.no/administrasjon/:stillingskoder](https://schema.fintlabs.no/administrasjon/:stillingskoder)
Alias: stillingskoder

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](AdministrasjonContainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Stillingskode](Stillingskode.md) |
| Domain Of | [AdministrasjonContainer](AdministrasjonContainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AdministrasjonContainer](AdministrasjonContainer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/administrasjon/:stillingskoder |
| native | https://schema.fintlabs.no/administrasjon/:stillingskoder |




## LinkML Source

<details>
```yaml
name: stillingskoder
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
alias: stillingskoder
owner: AdministrasjonContainer
domain_of:
- AdministrasjonContainer
range: Stillingskode
multivalued: true
inlined: true
inlined_as_list: true

```
</details>