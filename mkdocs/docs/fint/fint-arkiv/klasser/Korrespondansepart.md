

# Slot: korrespondansepart 


_Mottakar eller sendar av arkivdokument._





URI: [ark:korrespondansepart](https://schema.fintlabs.no/arkiv/korrespondansepart)
Alias: korrespondansepart

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
| Range | [Korrespondansepart](korrespondansepart.md) |
| Domain Of | [Registrering](registrering.md) |
| Slot URI | [ark:korrespondansepart](https://schema.fintlabs.no/arkiv/korrespondansepart) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










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
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:korrespondansepart
alias: korrespondansepart
domain_of:
- Registrering
range: Korrespondansepart
multivalued: true
inlined: true
inlined_as_list: true

```
</details>