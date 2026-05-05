

# Slot: kommunenummer_verdi 


_Firesifra kommunenummer (t.d. 0301 for Oslo)._





URI: [ngre:kommunenummer](https://data.norge.no/vocabulary/ngr-eiendom#kommunenummer)
Alias: kommunenummer_verdi

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kommune](kommune.md) | Norsk kommune |  yes  |
| [Kommunenummer](kommunenummer.md) | Firesifra kommunenummer (t |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Kommunenummer](kommunenummer.md), [Kommune](kommune.md) |
| Slot URI | [ngre:kommunenummer](https://data.norge.no/vocabulary/ngr-eiendom#kommunenummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:kommunenummer |
| native | https://data.norge.no/linkml/ngr-eiendom/kommunenummer_verdi |




## LinkML Source

<details>
```yaml
name: kommunenummer_verdi
description: Firesifra kommunenummer (t.d. 0301 for Oslo).
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
slot_uri: ngre:kommunenummer
alias: kommunenummer_verdi
domain_of:
- Kommunenummer
- Kommune
range: string

```
</details>