

# Slot: jobbtittel 


_Namn som beskriv jobben eller stillinga._





URI: [adm:jobbtittel](https://schema.fintlabs.no/administrasjon/jobbtittel)
Alias: jobbtittel

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personalressurs](personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Personalressurs](personalressurs.md) |
| Slot URI | [adm:jobbtittel](https://schema.fintlabs.no/administrasjon/jobbtittel) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Personalressurs](personalressurs.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:jobbtittel |
| native | https://schema.fintlabs.no/administrasjon/:jobbtittel |




## LinkML Source

<details>
```yaml
name: jobbtittel
description: Namn som beskriv jobben eller stillinga.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:jobbtittel
alias: jobbtittel
owner: Personalressurs
domain_of:
- Personalressurs
range: string

```
</details>