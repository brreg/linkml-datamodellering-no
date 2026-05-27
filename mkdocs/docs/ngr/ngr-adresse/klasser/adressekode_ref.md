

# Slot: adressekode_ref 


_Kommunal adressekode for adressa._





URI: [ngr:harAdressekode](https://data.norge.no/vocabulary/ngr-adresse#harAdressekode)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OffisiellAdresse](offisielladresse.md) | Ei offisiell adresse tildelt av kommunen, beståande av vegadresse (adressenav... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Adressekode](adressekode.md) |
| Domain Of | [OffisiellAdresse](offisielladresse.md) |
| Slot URI | [ngr:harAdressekode](https://data.norge.no/vocabulary/ngr-adresse#harAdressekode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:harAdressekode |
| native | https://data.norge.no/ngr/ngr-adresse/adressekode_ref |




## LinkML Source

<details>
```yaml
name: adressekode_ref
description: Kommunal adressekode for adressa.
from_schema: https://data.norge.no/ngr/ngr-adresse
rank: 1000
slot_uri: ngr:harAdressekode
domain_of:
- OffisiellAdresse
range: Adressekode

```
</details>