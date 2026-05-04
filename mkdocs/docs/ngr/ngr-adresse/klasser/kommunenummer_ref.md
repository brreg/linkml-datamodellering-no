

# Slot: kommunenummer_ref 


_Kommunen denne adressa ligg i._





URI: [ngr:harKommunenummer](https://data.norge.no/vocabulary/ngr-adresse#harKommunenummer)
Alias: kommunenummer_ref

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OffisiellAdresse](OffisiellAdresse.md) | Ei offisiell adresse tildelt av kommunen, beståande av vegadresse (adressenav... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kommune](Kommune.md) |
| Domain Of | [OffisiellAdresse](OffisiellAdresse.md) |
| Slot URI | [ngr:harKommunenummer](https://data.norge.no/vocabulary/ngr-adresse#harKommunenummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:harKommunenummer |
| native | https://data.norge.no/linkml/ngr-adresse/kommunenummer_ref |




## LinkML Source

<details>
```yaml
name: kommunenummer_ref
description: Kommunen denne adressa ligg i.
from_schema: https://data.norge.no/linkml/ngr-adresse
rank: 1000
slot_uri: ngr:harKommunenummer
alias: kommunenummer_ref
domain_of:
- OffisiellAdresse
range: Kommune

```
</details>