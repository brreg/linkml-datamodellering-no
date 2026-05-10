

# Slot: vare 


_Vare i vareregisteret._





URI: [okn:vare](https://schema.fintlabs.no/okonomi/vare)
Alias: vare

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturautsteder](fakturautsteder.md) | Eining som utformar og oversender faktura og mottar betaling |  yes  |
| [Fakturalinje](fakturalinje.md) | Del av Fakturagrunnlag som skildrar ei enkelt vare (kompleks datatype) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Vare](vare.md) |
| Domain Of | [Fakturautsteder](fakturautsteder.md), [Fakturalinje](fakturalinje.md) |
| Slot URI | [okn:vare](https://schema.fintlabs.no/okonomi/vare) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:vare |
| native | https://schema.fintlabs.no/okonomi/:vare |




## LinkML Source

<details>
```yaml
name: vare
description: Vare i vareregisteret.
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:vare
alias: vare
domain_of:
- Fakturautsteder
- Fakturalinje
range: Vare

```
</details>