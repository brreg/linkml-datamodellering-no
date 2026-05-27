

# Slot: kommunenummer_kode 


_Firesifra kommunenummer (t.d. 0301 for Oslo)._





URI: [ngr:kommunenummer](https://data.norge.no/vocabulary/ngr-adresse#kommunenummer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kommune](kommune.md) | Ein norsk kommune |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Kommune](kommune.md) |
| Slot URI | [ngr:kommunenummer](https://data.norge.no/vocabulary/ngr-adresse#kommunenummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ngr/ngr-adresse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngr:kommunenummer |
| native | https://data.norge.no/ngr/ngr-adresse/kommunenummer_kode |




## LinkML Source

<details>
```yaml
name: kommunenummer_kode
description: Firesifra kommunenummer (t.d. 0301 for Oslo).
from_schema: https://data.norge.no/ngr/ngr-adresse
rank: 1000
slot_uri: ngr:kommunenummer
domain_of:
- Kommune
range: string

```
</details>