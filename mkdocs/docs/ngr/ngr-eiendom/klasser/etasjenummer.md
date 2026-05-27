

# Slot: etasjenummer 


_Etasjenummer (t.d. 2 for 2. etasje)._





URI: [ngre:etasjenummer](https://data.norge.no/vocabulary/ngr-eiendom#etasjenummer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bruksenhetsnummer](bruksenhetsnummer.md) | Identifikator for ei brukseining innanfor ein bygning, t |  yes  |
| [Etasje](etasje.md) | Ei etasje i ein bygning |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:integer](http://www.w3.org/2001/XMLSchema#integer) |
| Domain Of | [Bruksenhetsnummer](bruksenhetsnummer.md), [Etasje](etasje.md) |
| Slot URI | [ngre:etasjenummer](https://data.norge.no/vocabulary/ngr-eiendom#etasjenummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:etasjenummer |
| native | https://data.norge.no/ngr/ngr-eiendom/etasjenummer |




## LinkML Source

<details>
```yaml
name: etasjenummer
description: Etasjenummer (t.d. 2 for 2. etasje).
from_schema: https://data.norge.no/ngr/ngr-eiendom
rank: 1000
slot_uri: ngre:etasjenummer
domain_of:
- Bruksenhetsnummer
- Etasje
range: integer

```
</details>