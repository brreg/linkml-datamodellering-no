

# Slot: ansiennitet 


_Ansiennitet for personalressurs hos arbeidsgjevar._





URI: [adm:ansiennitet](https://schema.fintlabs.no/administrasjon/ansiennitet)
Alias: ansiennitet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personalressurs](Personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [Personalressurs](Personalressurs.md) |
| Slot URI | [adm:ansiennitet](https://schema.fintlabs.no/administrasjon/ansiennitet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Personalressurs](Personalressurs.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:ansiennitet |
| native | https://schema.fintlabs.no/administrasjon/:ansiennitet |




## LinkML Source

<details>
```yaml
name: ansiennitet
description: Ansiennitet for personalressurs hos arbeidsgjevar.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:ansiennitet
alias: ansiennitet
owner: Personalressurs
domain_of:
- Personalressurs
range: date

```
</details>