

# Slot: saksbehandler 


_Person som er saksbehandlar._





URI: [ark:saksbehandler](https://schema.fintlabs.no/arkiv/saksbehandler)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Registrering](registrering.md) | Abstrakt basisklasse — arkivets primære byggeklossar |  yes  |
| [Journalpost](journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Arkivressurs](arkivressurs.md) |
| Domain Of | [Registrering](registrering.md) |
| Slot URI | [ark:saksbehandler](https://schema.fintlabs.no/arkiv/saksbehandler) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




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
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:saksbehandler
domain_of:
- Registrering
range: Arkivressurs

```
</details>