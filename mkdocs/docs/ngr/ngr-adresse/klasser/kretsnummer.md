

# Slot: kretsnummer 


_Kommunalt kretsnummer._





URI: [ngr:kretsnummer](https://data.norge.no/vocabulary/ngr-adresse#kretsnummer)
Alias: kretsnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [KommunalKrets](KommunalKrets.md) | Ein kommunal krets (administrativ inndeling definert av kommunen) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [KommunalKrets](KommunalKrets.md) |
| Slot URI | [ngr:kretsnummer](https://data.norge.no/vocabulary/ngr-adresse#kretsnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:kretsnummer |
| native | https://data.norge.no/linkml/ngr-adresse/kretsnummer |




## LinkML Source

<details>
```yaml
name: kretsnummer
description: Kommunalt kretsnummer.
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
slot_uri: ngr:kretsnummer
alias: kretsnummer
domain_of:
- KommunalKrets
range: string

```
</details>