

# Slot: matrikkelnummer 


_Matrikkelnummer for adresser utan vegadresse (t.d. 28/2-2)._





URI: [ngr:matrikkelnummer](https://data.norge.no/vocabulary/ngr-adresse#matrikkelnummer)
Alias: matrikkelnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OffisiellAdresse](OffisiellAdresse.md) | Ei offisiell adresse tildelt av kommunen, beståande av vegadresse (adressenav... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OffisiellAdresse](OffisiellAdresse.md) |
| Slot URI | [ngr:matrikkelnummer](https://data.norge.no/vocabulary/ngr-adresse#matrikkelnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:matrikkelnummer |
| native | https://data.norge.no/linkml/ngr-adresse/matrikkelnummer |




## LinkML Source

<details>
```yaml
name: matrikkelnummer
description: Matrikkelnummer for adresser utan vegadresse (t.d. 28/2-2).
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
slot_uri: ngr:matrikkelnummer
alias: matrikkelnummer
domain_of:
- OffisiellAdresse
range: string

```
</details>