

# Slot: er_av_type_hovedenhet 


_Hovudeininga (juridisk person) som er rettigheitshavar._





URI: [ngre:erAvTypeHovedenhet](https://data.norge.no/vocabulary/ngr-eiendom#erAvTypeHovedenhet)
Alias: er_av_type_hovedenhet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Borettslag](borettslag.md) | Eit burettslag er ein type hovudeining (juridisk person) som eig burettslagsb... |  yes  |
| [Rettighetshaver](rettighetshaver.md) | Den som har ein rett knytt til ein eigedom |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Hovedenhet](hovedenhet.md) |
| Domain Of | [Rettighetshaver](rettighetshaver.md), [Borettslag](borettslag.md) |
| Slot URI | [ngre:erAvTypeHovedenhet](https://data.norge.no/vocabulary/ngr-eiendom#erAvTypeHovedenhet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/ngr-eiendom




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ngre:erAvTypeHovedenhet |
| native | https://data.norge.no/linkml/ngr-eiendom/er_av_type_hovedenhet |




## LinkML Source

<details>
```yaml
name: er_av_type_hovedenhet
description: Hovudeininga (juridisk person) som er rettigheitshavar.
from_schema: https://data.norge.no/linkml/ngr-eiendom
rank: 1000
slot_uri: ngre:erAvTypeHovedenhet
alias: er_av_type_hovedenhet
domain_of:
- Rettighetshaver
- Borettslag
range: Hovedenhet

```
</details>