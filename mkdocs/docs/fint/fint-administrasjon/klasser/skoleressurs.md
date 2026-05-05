

# Slot: skoleressurs 


_Referanse til Skoleressurs (Utdanning)._





URI: [adm:skoleressurs](https://schema.fintlabs.no/administrasjon/skoleressurs)
Alias: skoleressurs

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personalressurs](personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Personalressurs](personalressurs.md) |
| Slot URI | [adm:skoleressurs](https://schema.fintlabs.no/administrasjon/skoleressurs) |

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
| self | adm:skoleressurs |
| native | https://schema.fintlabs.no/administrasjon/:skoleressurs |




## LinkML Source

<details>
```yaml
name: skoleressurs
description: Referanse til Skoleressurs (Utdanning).
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:skoleressurs
alias: skoleressurs
owner: Personalressurs
domain_of:
- Personalressurs
range: uriorcurie

```
</details>