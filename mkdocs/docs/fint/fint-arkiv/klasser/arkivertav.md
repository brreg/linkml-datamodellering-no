

# Slot: arkivertAv 


_Person som arkiverte arkivenheten._





URI: [ark:arkivertAv](https://schema.fintlabs.no/arkiv/arkivertAv)
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
| Slot URI | [ark:arkivertAv](https://schema.fintlabs.no/arkiv/arkivertAv) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




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
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:arkivertAv
domain_of:
- Registrering
range: Arkivressurs

```
</details>