

# Slot: antall 


_Mengde som vert beskriven av tillegget, i hundredeler._





URI: [adm:antall](https://schema.fintlabs.no/administrasjon/antall)
Alias: antall

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Variabellonn](Variabellonn.md) | Informasjon om variabel lønn |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Variabellonn](Variabellonn.md) |
| Slot URI | [adm:antall](https://schema.fintlabs.no/administrasjon/antall) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Variabellonn](Variabellonn.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:antall |
| native | https://schema.fintlabs.no/administrasjon/:antall |




## LinkML Source

<details>
```yaml
name: antall
description: Mengde som vert beskriven av tillegget, i hundredeler.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:antall
alias: antall
owner: Variabellonn
domain_of:
- Variabellonn
range: integer
required: true

```
</details>