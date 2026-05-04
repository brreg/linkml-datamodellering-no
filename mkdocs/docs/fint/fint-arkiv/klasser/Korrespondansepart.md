

# Slot: korrespondansepart 


_Mottakar eller sendar av arkivdokument._





URI: [ark:korrespondansepart](https://schema.fintlabs.no/arkiv/korrespondansepart)
Alias: korrespondansepart

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
| Range | [Korrespondansepart](Korrespondansepart.md) |
| Domain Of | [Registrering](Registrering.md) |
| Slot URI | [ark:korrespondansepart](https://schema.fintlabs.no/arkiv/korrespondansepart) |

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
| self | ark:korrespondansepart |
| native | https://schema.fintlabs.no/arkiv/:korrespondansepart |




## LinkML Source

<details>
```yaml
name: korrespondansepart
description: Mottakar eller sendar av arkivdokument.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:korrespondansepart
alias: korrespondansepart
owner: Registrering
domain_of:
- Registrering
range: Korrespondansepart
multivalued: true
inlined: true
inlined_as_list: true

```
</details>