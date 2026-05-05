

# Slot: organisasjon 


_Referanse til Organisasjonselement i Administrasjon-domenet._





URI: [utd:organisasjon](https://schema.fintlabs.no/utdanning/organisasjon)
Alias: organisasjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Skole](skole.md) |
| Slot URI | [utd:organisasjon](https://schema.fintlabs.no/utdanning/organisasjon) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Skole](skole.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:organisasjon |
| native | https://schema.fintlabs.no/utdanning/:organisasjon |




## LinkML Source

<details>
```yaml
name: organisasjon
description: Referanse til Organisasjonselement i Administrasjon-domenet.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:organisasjon
alias: organisasjon
owner: Skole
domain_of:
- Skole
range: uriorcurie

```
</details>