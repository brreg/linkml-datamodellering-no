

# Slot: adresserer_bruksenhet 


_Brukseining denne adressa er tildelt (forvaltar: Matrikkelen)._





URI: [ngr:adressererBruksenhet](https://data.norge.no/vocabulary/ngr-adresse#adressererBruksenhet)
Alias: adresserer_bruksenhet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OffisiellAdresse](OffisiellAdresse.md) | Ei offisiell adresse tildelt av kommunen, beståande av vegadresse (adressenav... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Bruksenhet](Bruksenhet.md) |
| Domain Of | [OffisiellAdresse](OffisiellAdresse.md) |
| Slot URI | [ngr:adressererBruksenhet](https://data.norge.no/vocabulary/ngr-adresse#adressererBruksenhet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:adressererBruksenhet |
| native | https://data.norge.no/linkml/ngr-adresse/adresserer_bruksenhet |




## LinkML Source

<details>
```yaml
name: adresserer_bruksenhet
description: 'Brukseining denne adressa er tildelt (forvaltar: Matrikkelen).'
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
slot_uri: ngr:adressererBruksenhet
alias: adresserer_bruksenhet
domain_of:
- OffisiellAdresse
range: Bruksenhet

```
</details>