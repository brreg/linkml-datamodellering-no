

# Slot: arbeidsforholdstypar 



URI: [https://schema.fintlabs.no/administrasjon/:arbeidsforholdstypar](https://schema.fintlabs.no/administrasjon/:arbeidsforholdstypar)
Alias: arbeidsforholdstypar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](AdministrasjonContainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Arbeidsforholdstype](Arbeidsforholdstype.md) |
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
| self | https://schema.fintlabs.no/administrasjon/:arbeidsforholdstypar |
| native | https://schema.fintlabs.no/administrasjon/:arbeidsforholdstypar |




## LinkML Source

<details>
```yaml
name: arbeidsforholdstypar
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
alias: arbeidsforholdstypar
owner: AdministrasjonContainer
domain_of:
- AdministrasjonContainer
range: Arbeidsforholdstype
multivalued: true
inlined: true
inlined_as_list: true

```
</details>