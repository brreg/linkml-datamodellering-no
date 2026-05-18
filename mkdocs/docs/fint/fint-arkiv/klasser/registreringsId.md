

# Slot: registreringsId 


_Inngår i M004 journalpostID._





URI: [ark:registreringsId](https://schema.fintlabs.no/arkiv/registreringsId)
Alias: registreringsId

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
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Registrering](registrering.md) |
| Slot URI | [ark:registreringsId](https://schema.fintlabs.no/arkiv/registreringsId) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










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
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:registreringsId
alias: registreringsId
domain_of:
- Registrering
range: string

```
</details>