

# Slot: mottattDato 


_Dato eit eksternt dokument vart motteke._





URI: [ark:mottattDato](https://schema.fintlabs.no/arkiv/mottattDato)
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
| Slot URI | [ark:mottattDato](https://schema.fintlabs.no/arkiv/mottattDato) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:mottattDato |
| native | https://schema.fintlabs.no/arkiv/:mottattDato |




## LinkML Source

<details>
```yaml
name: mottattDato
description: Dato eit eksternt dokument vart motteke.
from_schema: https://data.norge.no/fint/fint-arkiv
rank: 1000
slot_uri: ark:mottattDato
domain_of:
- Journalpost
range: datetime

```
</details>