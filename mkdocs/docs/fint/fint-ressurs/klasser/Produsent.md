

# Slot: produsent 


_Namn på produsenten av eininga._





URI: [res:produsent](https://schema.fintlabs.no/ressurs/produsent)
Alias: produsent

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DigitalEnhet](DigitalEnhet.md) | Ei digital eining som t |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Produsent](Produsent.md) |
| Domain Of | [DigitalEnhet](DigitalEnhet.md) |
| Slot URI | [res:produsent](https://schema.fintlabs.no/ressurs/produsent) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [DigitalEnhet](DigitalEnhet.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:produsent |
| native | https://schema.fintlabs.no/ressurs/:produsent |




## LinkML Source

<details>
```yaml
name: produsent
description: Namn på produsenten av eininga.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:produsent
alias: produsent
owner: DigitalEnhet
domain_of:
- DigitalEnhet
range: Produsent

```
</details>