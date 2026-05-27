

# Slot: sendtDato 


_Dato eit internt produsert dokument vart sendt/ekspedert._





URI: [ark:sendtDato](https://schema.fintlabs.no/arkiv/sendtDato)
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
| Slot URI | [ark:sendtDato](https://schema.fintlabs.no/arkiv/sendtDato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:sendtDato |
| native | https://schema.fintlabs.no/arkiv/:sendtDato |




## LinkML Source

<details>
```yaml
name: sendtDato
description: Dato eit internt produsert dokument vart sendt/ekspedert.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:sendtDato
domain_of:
- Journalpost
range: datetime

```
</details>