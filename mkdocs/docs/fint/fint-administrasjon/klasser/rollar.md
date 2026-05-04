

# Slot: rollar 



URI: [https://schema.fintlabs.no/administrasjon/:rollar](https://schema.fintlabs.no/administrasjon/:rollar)
Alias: rollar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](AdministrasjonContainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Rolle](Rolle.md) |
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
| self | https://schema.fintlabs.no/administrasjon/:rollar |
| native | https://schema.fintlabs.no/administrasjon/:rollar |




## LinkML Source

<details>
```yaml
name: rollar
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
alias: rollar
owner: AdministrasjonContainer
domain_of:
- AdministrasjonContainer
range: Rolle
multivalued: true
inlined: true
inlined_as_list: true

```
</details>