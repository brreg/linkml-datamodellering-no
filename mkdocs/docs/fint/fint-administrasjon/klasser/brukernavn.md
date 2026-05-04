

# Slot: brukernavn 


_Brukarnamn til den tilsette._





URI: [adm:brukernavn](https://schema.fintlabs.no/administrasjon/brukernavn)
Alias: brukernavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personalressurs](Personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](Identifikator.md) |
| Domain Of | [Personalressurs](Personalressurs.md) |
| Slot URI | [adm:brukernavn](https://schema.fintlabs.no/administrasjon/brukernavn) |

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