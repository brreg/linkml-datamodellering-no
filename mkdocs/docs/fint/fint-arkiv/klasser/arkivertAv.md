

# Slot: arkivertAv 


_Person som arkiverte arkivenheten._





URI: [ark:arkivertAv](https://schema.fintlabs.no/arkiv/arkivertAv)
Alias: arkivertAv

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Journalpost](Journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |  no  |
| [Registrering](Registrering.md) | Abstrakt basisklasse — arkivets primære byggeklossar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Arkivressurs](Arkivressurs.md) |
| Domain Of | [Registrering](Registrering.md) |
| Slot URI | [ark:arkivertAv](https://schema.fintlabs.no/arkiv/arkivertAv) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Registrering](Registrering.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:arkivertAv |
| native | https://schema.fintlabs.no/arkiv/:arkivertAv |




## LinkML Source

<details>
```yaml
name: arkivertAv
description: Person som arkiverte arkivenheten.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:arkivertAv
alias: arkivertAv
owner: Registrering
domain_of:
- Registrering
range: Arkivressurs
required: true

```
</details>