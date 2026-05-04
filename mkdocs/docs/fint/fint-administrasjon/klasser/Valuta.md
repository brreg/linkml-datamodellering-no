

# Slot: valuta 



URI: [https://schema.fintlabs.no/administrasjon/:valuta](https://schema.fintlabs.no/administrasjon/:valuta)
Alias: valuta

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](AdministrasjonContainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Valuta](Valuta.md) |
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
| self | https://schema.fintlabs.no/administrasjon/:valuta |
| native | https://schema.fintlabs.no/administrasjon/:valuta |




## LinkML Source

<details>
```yaml
name: valuta
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
alias: valuta
owner: AdministrasjonContainer
domain_of:
- AdministrasjonContainer
range: Valuta
multivalued: true
inlined: true
inlined_as_list: true

```
</details>