

# Slot: stemmekretsnummer 


_Stemmekretsnummer._





URI: [ngr:stemmekretsnummer](https://data.norge.no/vocabulary/ngr-adresse#stemmekretsnummer)
Alias: stemmekretsnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Stemmekrets](stemmekrets.md) | Ei stemmekrets brukt ved val |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Stemmekrets](stemmekrets.md) |
| Slot URI | [ngr:stemmekretsnummer](https://data.norge.no/vocabulary/ngr-adresse#stemmekretsnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:stemmekretsnummer |
| native | https://data.norge.no/linkml/ngr-adresse/stemmekretsnummer |




## LinkML Source

<details>
```yaml
name: stemmekretsnummer
description: Stemmekretsnummer.
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
slot_uri: ngr:stemmekretsnummer
alias: stemmekretsnummer
domain_of:
- Stemmekrets
range: string

```
</details>