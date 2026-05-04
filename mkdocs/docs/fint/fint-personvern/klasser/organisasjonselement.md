

# Slot: organisasjonselement 


_Referanse til Organisasjonselement (Administrasjon) tilknytt samtykket._





URI: [pvn:organisasjonselement](https://schema.fintlabs.no/personvern/organisasjonselement)
Alias: organisasjonselement

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Samtykke](Samtykke.md) | Tillating til behandling av personopplysning |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Samtykke](Samtykke.md) |
| Slot URI | [pvn:organisasjonselement](https://schema.fintlabs.no/personvern/organisasjonselement) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Samtykke](Samtykke.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pvn:organisasjonselement |
| native | https://schema.fintlabs.no/personvern/:organisasjonselement |




## LinkML Source

<details>
```yaml
name: organisasjonselement
description: Referanse til Organisasjonselement (Administrasjon) tilknytt samtykket.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: pvn:organisasjonselement
alias: organisasjonselement
owner: Samtykke
domain_of:
- Samtykke
range: uriorcurie

```
</details>