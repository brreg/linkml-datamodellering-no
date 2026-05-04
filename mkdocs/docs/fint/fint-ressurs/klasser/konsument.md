

# Slot: konsument 


_Referanse til Organisasjonselement som har tilgang til denne ressursen._





URI: [res:konsument](https://schema.fintlabs.no/ressurs/konsument)
Alias: konsument

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Applikasjonsressurstilgjengelighet](Applikasjonsressurstilgjengelighet.md) | Kva organisasjonselements brukarar som har tilgang til ein ressurs |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Applikasjonsressurstilgjengelighet](Applikasjonsressurstilgjengelighet.md) |
| Slot URI | [res:konsument](https://schema.fintlabs.no/ressurs/konsument) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Applikasjonsressurstilgjengelighet](Applikasjonsressurstilgjengelighet.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:konsument |
| native | https://schema.fintlabs.no/ressurs/:konsument |




## LinkML Source

<details>
```yaml
name: konsument
description: Referanse til Organisasjonselement som har tilgang til denne ressursen.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:konsument
alias: konsument
owner: Applikasjonsressurstilgjengelighet
domain_of:
- Applikasjonsressurstilgjengelighet
range: uriorcurie
required: true

```
</details>