

# Slot: fravaersgrunnar 



URI: [https://schema.fintlabs.no/administrasjon/:fravaersgrunnar](https://schema.fintlabs.no/administrasjon/:fravaersgrunnar)
Alias: fravaersgrunnar

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fravaersgrunn](fravaersgrunn.md) |
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
| self | https://schema.fintlabs.no/administrasjon/:fravaersgrunnar |
| native | https://schema.fintlabs.no/administrasjon/:fravaersgrunnar |




## LinkML Source

<details>
```yaml
name: fravaersgrunnar
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
alias: fravaersgrunnar
owner: AdministrasjonContainer
domain_of:
- AdministrasjonContainer
range: Fravaersgrunn
multivalued: true
inlined: true
inlined_as_list: true

```
</details>