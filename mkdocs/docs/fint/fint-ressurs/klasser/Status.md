

# Slot: status 


_Status på eininga i fagsystemet._





URI: [res:status](https://schema.fintlabs.no/ressurs/status)
Alias: status

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DigitalEnhet](DigitalEnhet.md) | Ei digital eining som t |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Status](Status.md) |
| Domain Of | [DigitalEnhet](DigitalEnhet.md) |
| Slot URI | [res:status](https://schema.fintlabs.no/ressurs/status) |

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
| self | res:status |
| native | https://schema.fintlabs.no/ressurs/:status |




## LinkML Source

<details>
```yaml
name: status
description: Status på eininga i fagsystemet.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:status
alias: status
owner: DigitalEnhet
domain_of:
- DigitalEnhet
range: Status

```
</details>