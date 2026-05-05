

# Slot: bokstavkode 


_Bokstavkode for aktuell valuta._





URI: [fint:bokstavkode](https://schema.fintlabs.no/bokstavkode)
Alias: bokstavkode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Valuta](valuta.md) | Valutakodar for offisielle valutaer |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Valuta](valuta.md) |
| Slot URI | [fint:bokstavkode](https://schema.fintlabs.no/bokstavkode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Valuta](valuta.md) |








## In Subsets


* [Obligatorisk](obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:bokstavkode |
| native | https://schema.fintlabs.no/okonomi/:bokstavkode |




## LinkML Source

<details>
```yaml
name: bokstavkode
description: Bokstavkode for aktuell valuta.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: fint:bokstavkode
alias: bokstavkode
owner: Valuta
domain_of:
- Valuta
range: Identifikator
required: true
inlined: true

```
</details>