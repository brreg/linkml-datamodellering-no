

# Slot: ansattnummer 


_Unik identifikator for den tilsette i HR-systemet._





URI: [adm:ansattnummer](https://schema.fintlabs.no/administrasjon/ansattnummer)
Alias: ansattnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personalressurs](personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Personalressurs](personalressurs.md) |
| Slot URI | [adm:ansattnummer](https://schema.fintlabs.no/administrasjon/ansattnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Personalressurs](personalressurs.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:ansattnummer |
| native | https://schema.fintlabs.no/administrasjon/:ansattnummer |




## LinkML Source

<details>
```yaml
name: ansattnummer
description: Unik identifikator for den tilsette i HR-systemet.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:ansattnummer
alias: ansattnummer
owner: Personalressurs
domain_of:
- Personalressurs
range: Identifikator
required: true
inlined: true

```
</details>