

# Slot: privateid 


_Angir om eininga er eigd av organisasjonen eller privatperson._





URI: [res:privateid](https://schema.fintlabs.no/ressurs/privateid)
Alias: privateid

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
| Slot URI | [res:privateid](https://schema.fintlabs.no/ressurs/privateid) |

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
| self | res:privateid |
| native | https://schema.fintlabs.no/ressurs/:privateid |




## LinkML Source

<details>
```yaml
name: privateid
description: Angir om eininga er eigd av organisasjonen eller privatperson.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:privateid
alias: privateid
owner: DigitalEnhet
domain_of:
- DigitalEnhet
range: boolean

```
</details>