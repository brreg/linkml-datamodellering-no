

# Slot: dokumentstatus 


_Status til dokumentet._





URI: [ark:dokumentstatus](https://schema.fintlabs.no/arkiv/dokumentstatus)
Alias: dokumentstatus

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dokumentbeskrivelse](dokumentbeskrivelse.md) | Skildring av eit dokument tilknytt ein journalpost |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DokumentStatus](dokumentstatus.md) |
| Domain Of | [Dokumentbeskrivelse](dokumentbeskrivelse.md) |
| Slot URI | [ark:dokumentstatus](https://schema.fintlabs.no/arkiv/dokumentstatus) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Dokumentbeskrivelse](dokumentbeskrivelse.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:dokumentstatus |
| native | https://schema.fintlabs.no/arkiv/:dokumentstatus |




## LinkML Source

<details>
```yaml
name: dokumentstatus
description: Status til dokumentet.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:dokumentstatus
alias: dokumentstatus
owner: Dokumentbeskrivelse
domain_of:
- Dokumentbeskrivelse
range: DokumentStatus
required: true

```
</details>