

# Slot: journalDato 


_Datoen journalposten er oppretta/arkivert._





URI: [ark:journalDato](https://schema.fintlabs.no/arkiv/journalDato)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Journalpost](journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) |
| Domain Of | [Journalpost](journalpost.md) |
| Slot URI | [ark:journalDato](https://schema.fintlabs.no/arkiv/journalDato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:journalDato |
| native | https://schema.fintlabs.no/arkiv/:journalDato |




## LinkML Source

<details>
```yaml
name: journalDato
description: Datoen journalposten er oppretta/arkivert.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:journalDato
domain_of:
- Journalpost
range: datetime

```
</details>