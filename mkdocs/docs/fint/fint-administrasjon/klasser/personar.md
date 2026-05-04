

# Slot: personar 



URI: [https://schema.fintlabs.no/administrasjon/:personar](https://schema.fintlabs.no/administrasjon/:personar)
Alias: personar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](AdministrasjonContainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Person](Person.md) |
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
| self | https://schema.fintlabs.no/administrasjon/:personar |
| native | https://schema.fintlabs.no/administrasjon/:personar |




## LinkML Source

<details>
```yaml
name: personar
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
alias: personar
owner: AdministrasjonContainer
domain_of:
- AdministrasjonContainer
range: Person
multivalued: true
inlined: true
inlined_as_list: true

```
</details>