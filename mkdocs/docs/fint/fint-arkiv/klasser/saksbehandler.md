

# Slot: saksbehandler 


_Person som er saksbehandlar._





URI: [ark:saksbehandler](https://schema.fintlabs.no/arkiv/saksbehandler)
Alias: saksbehandler

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
| Slot URI | [ark:saksbehandler](https://schema.fintlabs.no/arkiv/saksbehandler) |

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
| self | ark:saksbehandler |
| native | https://schema.fintlabs.no/arkiv/:saksbehandler |




## LinkML Source

<details>
```yaml
name: saksbehandler
description: Person som er saksbehandlar.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:saksbehandler
alias: saksbehandler
owner: Registrering
domain_of:
- Registrering
range: Arkivressurs

```
</details>