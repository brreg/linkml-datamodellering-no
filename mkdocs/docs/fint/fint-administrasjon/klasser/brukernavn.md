

# Slot: brukernavn 


_Brukarnamn til den tilsette._





URI: [adm:brukernavn](https://schema.fintlabs.no/administrasjon/brukernavn)
Alias: brukernavn

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
| Slot URI | [adm:brukernavn](https://schema.fintlabs.no/administrasjon/brukernavn) |

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
| self | adm:brukernavn |
| native | https://schema.fintlabs.no/administrasjon/:brukernavn |




## LinkML Source

<details>
```yaml
name: brukernavn
description: Brukarnamn til den tilsette.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:brukernavn
alias: brukernavn
owner: Personalressurs
domain_of:
- Personalressurs
range: Identifikator
inlined: true

```
</details>