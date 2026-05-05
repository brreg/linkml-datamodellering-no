

# Slot: avskrivning 


_Avskriving av journalposten._





URI: [ark:avskrivning](https://schema.fintlabs.no/arkiv/avskrivning)
Alias: avskrivning

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Journalpost](journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Avskrivning](avskrivning.md) |
| Domain Of | [Journalpost](journalpost.md) |
| Slot URI | [ark:avskrivning](https://schema.fintlabs.no/arkiv/avskrivning) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Journalpost](journalpost.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:avskrivning |
| native | https://schema.fintlabs.no/arkiv/:avskrivning |




## LinkML Source

<details>
```yaml
name: avskrivning
description: Avskriving av journalposten.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:avskrivning
alias: avskrivning
owner: Journalpost
domain_of:
- Journalpost
range: Avskrivning
inlined: true

```
</details>