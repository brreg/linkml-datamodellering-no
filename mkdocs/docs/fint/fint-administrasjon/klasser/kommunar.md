

# Slot: kommunar 



URI: [https://schema.fintlabs.no/administrasjon/:kommunar](https://schema.fintlabs.no/administrasjon/:kommunar)
Alias: kommunar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](AdministrasjonContainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kommune](Kommune.md) |
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
| self | https://schema.fintlabs.no/administrasjon/:kommunar |
| native | https://schema.fintlabs.no/administrasjon/:kommunar |




## LinkML Source

<details>
```yaml
name: kommunar
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
alias: kommunar
owner: AdministrasjonContainer
domain_of:
- AdministrasjonContainer
range: Kommune
multivalued: true
inlined: true
inlined_as_list: true

```
</details>