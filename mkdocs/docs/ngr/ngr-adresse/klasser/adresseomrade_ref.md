

# Slot: adresseomrade_ref 


_Adresseområdet dette adressenamnet eller adressekoden høyrer til._





URI: [ngr:harAdresseomrade](https://data.norge.no/vocabulary/ngr-adresse#harAdresseomrade)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Adressenavn](adressenavn.md) | Offisielt namn på ei veglenke eller eit adresseobjekt i ein kommune, tildelt ... |  yes  |
| [Adressekode](adressekode.md) | Firesifra kommunal kode som identifiserer eit adressenavn |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Adresseomrade](adresseomrade.md) |
| Domain Of | [Adressenavn](adressenavn.md), [Adressekode](adressekode.md) |
| Slot URI | [ngr:harAdresseomrade](https://data.norge.no/vocabulary/ngr-adresse#harAdresseomrade) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:harAdresseomrade |
| native | https://data.norge.no/ngr/ngr-adresse/adresseomrade_ref |




## LinkML Source

<details>
```yaml
name: adresseomrade_ref
description: Adresseområdet dette adressenamnet eller adressekoden høyrer til.
from_schema: https://data.norge.no/ngr/ngr-adresse
rank: 1000
slot_uri: ngr:harAdresseomrade
domain_of:
- Adressenavn
- Adressekode
range: Adresseomrade

```
</details>