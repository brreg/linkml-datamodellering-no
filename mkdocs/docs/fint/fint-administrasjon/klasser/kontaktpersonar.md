

# Slot: kontaktpersonar 



URI: [https://schema.fintlabs.no/administrasjon/:kontaktpersonar](https://schema.fintlabs.no/administrasjon/:kontaktpersonar)
Alias: kontaktpersonar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](AdministrasjonContainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kontaktperson](Kontaktperson.md) |
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
| self | https://schema.fintlabs.no/administrasjon/:kontaktpersonar |
| native | https://schema.fintlabs.no/administrasjon/:kontaktpersonar |




## LinkML Source

<details>
```yaml
name: kontaktpersonar
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
alias: kontaktpersonar
owner: AdministrasjonContainer
domain_of:
- AdministrasjonContainer
range: Kontaktperson
multivalued: true
inlined: true
inlined_as_list: true

```
</details>