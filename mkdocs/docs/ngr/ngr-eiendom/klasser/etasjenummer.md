

# Slot: etasjenummer 


_Etasjenummer (t.d. 2 for 2. etasje)._





URI: [ngre:etasjenummer](https://data.norge.no/vocabulary/ngr-eiendom#etasjenummer)
Alias: etasjenummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bruksenhetsnummer](Bruksenhetsnummer.md) | Identifikator for ei brukseining innanfor ein bygning, t |  yes  |
| [Etasje](Etasje.md) | Ei etasje i ein bygning |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Bruksenhetsnummer](Bruksenhetsnummer.md), [Etasje](Etasje.md) |
| Slot URI | [ngre:etasjenummer](https://data.norge.no/vocabulary/ngr-eiendom#etasjenummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:etasjenummer |
| native | https://data.norge.no/linkml/ngr-eiendom/etasjenummer |




## LinkML Source

<details>
```yaml
name: etasjenummer
description: Etasjenummer (t.d. 2 for 2. etasje).
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
slot_uri: ngre:etasjenummer
alias: etasjenummer
domain_of:
- Bruksenhetsnummer
- Etasje
range: integer

```
</details>