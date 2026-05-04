

# Slot: karakterverdi 


_Ny karakterverdi etter endringa._





URI: [utd:karakterverdi](https://schema.fintlabs.no/utdanning/karakterverdi)
Alias: karakterverdi

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
| Slot URI | [utd:karakterverdi](https://schema.fintlabs.no/utdanning/karakterverdi) |

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
| self | utd:karakterverdi |
| native | https://schema.fintlabs.no/utdanning/:karakterverdi |




## LinkML Source

<details>
```yaml
name: karakterverdi
description: Ny karakterverdi etter endringa.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:karakterverdi
alias: karakterverdi
owner: Karakterhistorie
domain_of:
- Karakterhistorie
range: Karakterverdi

```
</details>