

# Slot: kontrakter 



URI: [https://schema.fintlabs.no/administrasjon/:kontrakter](https://schema.fintlabs.no/administrasjon/:kontrakter)
Alias: kontrakter

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](AdministrasjonContainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kontrakt](Kontrakt.md) |
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
| self | https://schema.fintlabs.no/administrasjon/:kontrakter |
| native | https://schema.fintlabs.no/administrasjon/:kontrakter |




## LinkML Source

<details>
```yaml
name: kontrakter
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
alias: kontrakter
owner: AdministrasjonContainer
domain_of:
- AdministrasjonContainer
range: Kontrakt
multivalued: true
inlined: true
inlined_as_list: true

```
</details>