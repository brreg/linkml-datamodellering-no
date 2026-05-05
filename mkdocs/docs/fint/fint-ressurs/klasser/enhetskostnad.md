

# Slot: enhetskostnad 


_Kostnad per ressurs._





URI: [res:enhetskostnad](https://schema.fintlabs.no/ressurs/enhetskostnad)
Alias: enhetskostnad

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Applikasjonsressurs](applikasjonsressurs.md) | Informasjon om kor ein applikasjon kan nyttast (lisensressurs) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](integer.md) |
| Domain Of | [Applikasjonsressurs](applikasjonsressurs.md) |
| Slot URI | [res:enhetskostnad](https://schema.fintlabs.no/ressurs/enhetskostnad) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | res:enhetskostnad |
| native | https://schema.fintlabs.no/ressurs/:enhetskostnad |




## LinkML Source

<details>
```yaml
name: enhetskostnad
description: Kostnad per ressurs.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:enhetskostnad
alias: enhetskostnad
owner: Applikasjonsressurs
domain_of:
- Applikasjonsressurs
range: integer

```
</details>