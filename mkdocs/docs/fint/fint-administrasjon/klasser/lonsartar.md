

# Slot: lonsartar 



URI: [https://schema.fintlabs.no/administrasjon/:lonsartar](https://schema.fintlabs.no/administrasjon/:lonsartar)
Alias: lonsartar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Lonsart](lonsart.md) |
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


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/administrasjon/:lonsartar |
| native | https://schema.fintlabs.no/administrasjon/:lonsartar |




## LinkML Source

<details>
```yaml
name: lonsartar
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
alias: lonsartar
owner: AdministrasjonContainer
domain_of:
- AdministrasjonContainer
range: Lonsart
multivalued: true
inlined: true
inlined_as_list: true

```
</details>