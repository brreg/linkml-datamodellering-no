

# Slot: dokumentbeskrivelse 


_Dokumentbeskrivelsar til ei registrering._





URI: [ark:dokumentbeskrivelse](https://schema.fintlabs.no/arkiv/dokumentbeskrivelse)
Alias: dokumentbeskrivelse

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
| Range | [Dokumentbeskrivelse](Dokumentbeskrivelse.md) |
| Domain Of | [Registrering](Registrering.md) |
| Slot URI | [ark:dokumentbeskrivelse](https://schema.fintlabs.no/arkiv/dokumentbeskrivelse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
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
| self | ark:dokumentbeskrivelse |
| native | https://schema.fintlabs.no/arkiv/:dokumentbeskrivelse |




## LinkML Source

<details>
```yaml
name: dokumentbeskrivelse
description: Dokumentbeskrivelsar til ei registrering.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:dokumentbeskrivelse
alias: dokumentbeskrivelse
owner: Registrering
domain_of:
- Registrering
range: Dokumentbeskrivelse
multivalued: true

```
</details>