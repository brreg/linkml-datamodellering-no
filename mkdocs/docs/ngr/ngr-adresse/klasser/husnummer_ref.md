

# Slot: husnummer_ref 


_Husnummer (nummer + bokstav) for adressa._





URI: [ngr:harHusnummer](https://data.norge.no/vocabulary/ngr-adresse#harHusnummer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OffisiellAdresse](offisielladresse.md) | Ei offisiell adresse tildelt av kommunen, beståande av vegadresse (adressenav... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Husnummer](husnummer.md) |
| Domain Of | [OffisiellAdresse](offisielladresse.md) |
| Slot URI | [ngr:harHusnummer](https://data.norge.no/vocabulary/ngr-adresse#harHusnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:harHusnummer |
| native | https://data.norge.no/ngr/ngr-adresse/husnummer_ref |




## LinkML Source

<details>
```yaml
name: husnummer_ref
description: Husnummer (nummer + bokstav) for adressa.
from_schema: https://data.norge.no/ngr/ngr-adresse
rank: 1000
slot_uri: ngr:harHusnummer
domain_of:
- OffisiellAdresse
range: Husnummer

```
</details>