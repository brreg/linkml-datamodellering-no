

# Slot: ressurstilgjengelighet 


_Angir kva organisasjonseining og kor mange ressursar som skal tilordnast._





URI: [res:ressurstilgjengelighet](https://schema.fintlabs.no/ressurs/ressurstilgjengelighet)
Alias: ressurstilgjengelighet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Applikasjonsressurs](applikasjonsressurs.md) | Informasjon om kor ein applikasjon kan nyttast (lisensressurs) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Applikasjonsressurstilgjengelighet](applikasjonsressurstilgjengelighet.md) |
| Domain Of | [Applikasjonsressurs](applikasjonsressurs.md) |
| Slot URI | [res:ressurstilgjengelighet](https://schema.fintlabs.no/ressurs/ressurstilgjengelighet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Applikasjonsressurs](applikasjonsressurs.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:ressurstilgjengelighet |
| native | https://schema.fintlabs.no/ressurs/:ressurstilgjengelighet |




## LinkML Source

<details>
```yaml
name: ressurstilgjengelighet
description: Angir kva organisasjonseining og kor mange ressursar som skal tilordnast.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:ressurstilgjengelighet
alias: ressurstilgjengelighet
owner: Applikasjonsressurs
domain_of:
- Applikasjonsressurs
range: Applikasjonsressurstilgjengelighet
multivalued: true

```
</details>