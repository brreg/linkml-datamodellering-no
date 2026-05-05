

# Slot: opprinneligKarakterstatus 


_Opphavleg karakterstatus før endringa._





URI: [utd:opprinneligKarakterstatus](https://schema.fintlabs.no/utdanning/opprinneligKarakterstatus)
Alias: opprinneligKarakterstatus

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Karakterhistorie](karakterhistorie.md) | Historikk over endringar i ein karakter |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Karakterstatus](karakterstatus.md) |
| Domain Of | [Karakterhistorie](karakterhistorie.md) |
| Slot URI | [utd:opprinneligKarakterstatus](https://schema.fintlabs.no/utdanning/opprinneligKarakterstatus) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Karakterhistorie](karakterhistorie.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:opprinneligKarakterstatus |
| native | https://schema.fintlabs.no/utdanning/:opprinneligKarakterstatus |




## LinkML Source

<details>
```yaml
name: opprinneligKarakterstatus
description: Opphavleg karakterstatus før endringa.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:opprinneligKarakterstatus
alias: opprinneligKarakterstatus
owner: Karakterhistorie
domain_of:
- Karakterhistorie
range: Karakterstatus

```
</details>