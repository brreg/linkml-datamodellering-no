

# Slot: arkivertDato 


_Dato og klokkeslett alle dokument knytt til registreringa vart arkivert._





URI: [ark:arkivertDato](https://schema.fintlabs.no/arkiv/arkivertDato)
Alias: arkivertDato

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
| Range | [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) |
| Domain Of | [Registrering](registrering.md) |
| Slot URI | [ark:arkivertDato](https://schema.fintlabs.no/arkiv/arkivertDato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










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
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:arkivertDato
alias: arkivertDato
domain_of:
- Registrering
range: datetime

```
</details>