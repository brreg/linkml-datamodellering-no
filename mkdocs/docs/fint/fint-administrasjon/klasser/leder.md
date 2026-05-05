

# Slot: leder 


_Ansvarleg leiar for organisasjonselementet._





URI: [adm:leder](https://schema.fintlabs.no/administrasjon/leder)
Alias: leder

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organisasjonselement](organisasjonselement.md) | Eit element i organisasjonsstrukturen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personalressurs](personalressurs.md) |
| Domain Of | [Organisasjonselement](organisasjonselement.md) |
| Slot URI | [adm:leder](https://schema.fintlabs.no/administrasjon/leder) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Organisasjonselement](organisasjonselement.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:leder |
| native | https://schema.fintlabs.no/administrasjon/:leder |




## LinkML Source

<details>
```yaml
name: leder
description: Ansvarleg leiar for organisasjonselementet.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:leder
alias: leder
owner: Organisasjonselement
domain_of:
- Organisasjonselement
range: Personalressurs

```
</details>