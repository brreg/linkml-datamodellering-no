

# Slot: arkivertDato 


_Dato og klokkeslett alle dokument knytt til registreringa vart arkivert._





URI: [ark:arkivertDato](https://schema.fintlabs.no/arkiv/arkivertDato)
Alias: arkivertDato

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
| Range | [Datetime](Datetime.md) |
| Domain Of | [Registrering](Registrering.md) |
| Slot URI | [ark:arkivertDato](https://schema.fintlabs.no/arkiv/arkivertDato) |

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
| self | ark:arkivertDato |
| native | https://schema.fintlabs.no/arkiv/:arkivertDato |




## LinkML Source

<details>
```yaml
name: arkivertDato
description: Dato og klokkeslett alle dokument knytt til registreringa vart arkivert.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:arkivertDato
alias: arkivertDato
owner: Registrering
domain_of:
- Registrering
range: datetime

```
</details>