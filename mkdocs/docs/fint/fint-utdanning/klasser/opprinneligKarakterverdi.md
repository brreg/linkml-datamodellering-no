

# Slot: opprinneligKarakterverdi 


_Opphavleg karakterverdi før endringa._





URI: [utd:opprinneligKarakterverdi](https://schema.fintlabs.no/utdanning/opprinneligKarakterverdi)
Alias: opprinneligKarakterverdi

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Karakterhistorie](Karakterhistorie.md) | Historikk over endringar i ein karakter |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Karakterverdi](Karakterverdi.md) |
| Domain Of | [Karakterhistorie](Karakterhistorie.md) |
| Slot URI | [utd:opprinneligKarakterverdi](https://schema.fintlabs.no/utdanning/opprinneligKarakterverdi) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Karakterhistorie](Karakterhistorie.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:opprinneligKarakterverdi |
| native | https://schema.fintlabs.no/utdanning/:opprinneligKarakterverdi |




## LinkML Source

<details>
```yaml
name: opprinneligKarakterverdi
description: Opphavleg karakterverdi før endringa.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:opprinneligKarakterverdi
alias: opprinneligKarakterverdi
owner: Karakterhistorie
domain_of:
- Karakterhistorie
range: Karakterverdi

```
</details>