

# Slot: delegert 


_Angir om deltakinga er delegert._





URI: [utd:delegert](https://schema.fintlabs.no/utdanning/delegert)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md) | Eit elevs deltaking i ei eksamensgruppe |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) |
| Domain Of | [Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md) |
| Slot URI | [utd:delegert](https://schema.fintlabs.no/utdanning/delegert) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:delegert |
| native | https://schema.fintlabs.no/utdanning/:delegert |




## LinkML Source

<details>
```yaml
name: delegert
description: Angir om deltakinga er delegert.
from_schema: https://data.norge.no/fint/fint-utdanning
rank: 1000
slot_uri: utd:delegert
domain_of:
- Eksamensgruppemedlemskap
range: boolean

```
</details>