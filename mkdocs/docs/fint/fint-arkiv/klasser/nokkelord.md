

# Slot: nokkelord 


_Nøkkelord som skildrar innhaldet._





URI: [ark:nokkelord](https://schema.fintlabs.no/arkiv/nokkelord)
Alias: nokkelord

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
| Slot URI | [ark:nokkelord](https://schema.fintlabs.no/arkiv/nokkelord) |

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
| self | ark:nokkelord |
| native | https://schema.fintlabs.no/arkiv/:nokkelord |




## LinkML Source

<details>
```yaml
name: nokkelord
description: Nøkkelord som skildrar innhaldet.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:nokkelord
alias: nokkelord
owner: Registrering
domain_of:
- Registrering
range: string
multivalued: true

```
</details>