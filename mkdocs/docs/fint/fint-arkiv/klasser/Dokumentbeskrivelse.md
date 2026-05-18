

# Slot: dokumentbeskrivelse 


_Dokumentbeskrivelsar til ei registrering._





URI: [ark:dokumentbeskrivelse](https://schema.fintlabs.no/arkiv/dokumentbeskrivelse)
Alias: dokumentbeskrivelse

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
| Range | [Dokumentbeskrivelse](dokumentbeskrivelse.md) |
| Domain Of | [Registrering](registrering.md) |
| Slot URI | [ark:dokumentbeskrivelse](https://schema.fintlabs.no/arkiv/dokumentbeskrivelse) |

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
| self | ark:dokumentbeskrivelse |
| native | https://schema.fintlabs.no/arkiv/:dokumentbeskrivelse |




## LinkML Source

<details>
```yaml
name: dokumentbeskrivelse
description: Dokumentbeskrivelsar til ei registrering.
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:dokumentbeskrivelse
alias: dokumentbeskrivelse
domain_of:
- Registrering
range: Dokumentbeskrivelse
multivalued: true

```
</details>