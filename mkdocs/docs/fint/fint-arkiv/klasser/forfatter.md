

# Slot: forfatter 


_Namn på person eller organisasjon som skapte dokumentet._





URI: [ark:forfatter](https://schema.fintlabs.no/arkiv/forfatter)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Registrering](registrering.md) | Abstrakt basisklasse — arkivets primære byggeklossar |  yes  |
| [Dokumentbeskrivelse](dokumentbeskrivelse.md) | Skildring av eit dokument tilknytt ein journalpost |  yes  |
| [Journalpost](journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Registrering](registrering.md), [Dokumentbeskrivelse](dokumentbeskrivelse.md) |
| Slot URI | [ark:forfatter](https://schema.fintlabs.no/arkiv/forfatter) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:forfatter |
| native | https://schema.fintlabs.no/arkiv/:forfatter |




## LinkML Source

<details>
```yaml
name: forfatter
description: Namn på person eller organisasjon som skapte dokumentet.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:forfatter
domain_of:
- Registrering
- Dokumentbeskrivelse
range: string
multivalued: true

```
</details>