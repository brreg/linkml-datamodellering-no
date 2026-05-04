

# Slot: artar 



URI: [https://schema.fintlabs.no/administrasjon/:artar](https://schema.fintlabs.no/administrasjon/:artar)
Alias: artar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](AdministrasjonContainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Art](Art.md) |
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
| self | https://schema.fintlabs.no/administrasjon/:artar |
| native | https://schema.fintlabs.no/administrasjon/:artar |




## LinkML Source

<details>
```yaml
name: artar
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
alias: artar
owner: AdministrasjonContainer
domain_of:
- AdministrasjonContainer
range: Art
multivalued: true
inlined: true
inlined_as_list: true

```
</details>