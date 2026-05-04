

# Slot: flerbrukerenhet 


_Kvifor eininga er ein- eller flerbrukarenheit._





URI: [res:flerbrukerenhet](https://schema.fintlabs.no/ressurs/flerbrukerenhet)
Alias: flerbrukerenhet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DigitalEnhet](DigitalEnhet.md) | Ei digital eining som t |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [DigitalEnhet](DigitalEnhet.md) |
| Slot URI | [res:flerbrukerenhet](https://schema.fintlabs.no/ressurs/flerbrukerenhet) |

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
| self | res:flerbrukerenhet |
| native | https://schema.fintlabs.no/ressurs/:flerbrukerenhet |




## LinkML Source

<details>
```yaml
name: flerbrukerenhet
description: Kvifor eininga er ein- eller flerbrukarenheit.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:flerbrukerenhet
alias: flerbrukerenhet
owner: DigitalEnhet
domain_of:
- DigitalEnhet
range: boolean

```
</details>