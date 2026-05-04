

# Slot: registreringsId 


_Inngår i M004 journalpostID._





URI: [ark:registreringsId](https://schema.fintlabs.no/arkiv/registreringsId)
Alias: registreringsId

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
| Range | [String](String.md) |
| Domain Of | [Registrering](Registrering.md) |
| Slot URI | [ark:registreringsId](https://schema.fintlabs.no/arkiv/registreringsId) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Registrering](Registrering.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:registreringsId |
| native | https://schema.fintlabs.no/arkiv/:registreringsId |




## LinkML Source

<details>
```yaml
name: registreringsId
description: Inngår i M004 journalpostID.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:registreringsId
alias: registreringsId
owner: Registrering
domain_of:
- Registrering
range: string

```
</details>