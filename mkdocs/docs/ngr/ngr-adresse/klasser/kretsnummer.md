

# Slot: kretsnummer 


_Kommunalt kretsnummer._





URI: [ngr:kretsnummer](https://data.norge.no/vocabulary/ngr-adresse#kretsnummer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [KommunalKrets](kommunalkrets.md) | Ein kommunal krets (administrativ inndeling definert av kommunen) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [KommunalKrets](kommunalkrets.md) |
| Slot URI | [ngr:kretsnummer](https://data.norge.no/vocabulary/ngr-adresse#kretsnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:kretsnummer |
| native | https://data.norge.no/ngr/ngr-adresse/kretsnummer |




## LinkML Source

<details>
```yaml
name: kretsnummer
description: Kommunalt kretsnummer.
from_schema: https://data.norge.no/ngr/ngr-adresse
rank: 1000
slot_uri: ngr:kretsnummer
domain_of:
- KommunalKrets
range: string

```
</details>