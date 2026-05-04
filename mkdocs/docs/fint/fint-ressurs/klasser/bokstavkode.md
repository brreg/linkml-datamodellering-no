

# Slot: bokstavkode 


_Bokstavkode for aktuell valuta._





URI: [fint:bokstavkode](https://schema.fintlabs.no/bokstavkode)
Alias: bokstavkode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Valuta](Valuta.md) | Valutakodar for offisielle valutaer |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](Identifikator.md) |
| Domain Of | [Valuta](Valuta.md) |
| Slot URI | [fint:bokstavkode](https://schema.fintlabs.no/bokstavkode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Valuta](Valuta.md) |








## In Subsets


* [Obligatorisk](Obligatorisk.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:bokstavkode |
| native | https://schema.fintlabs.no/ressurs/:bokstavkode |




## LinkML Source

<details>
```yaml
name: bokstavkode
description: Bokstavkode for aktuell valuta.
in_subset:
- Obligatorisk
from_schema: https://data.norge.no/linkml/fint-ressurs
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