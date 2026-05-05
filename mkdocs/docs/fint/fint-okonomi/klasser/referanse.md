

# Slot: referanse 


_Ekstern referanse, t.d. fakturanummer._





URI: [okn:referanse](https://schema.fintlabs.no/okonomi/referanse)
Alias: referanse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bilag](bilag.md) | Dokumentasjon til ein transaksjon (kompleks datatype) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Bilag](bilag.md) |
| Slot URI | [okn:referanse](https://schema.fintlabs.no/okonomi/referanse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Bilag](bilag.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:referanse |
| native | https://schema.fintlabs.no/okonomi/:referanse |




## LinkML Source

<details>
```yaml
name: referanse
description: Ekstern referanse, t.d. fakturanummer.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:referanse
alias: referanse
owner: Bilag
domain_of:
- Bilag
range: string

```
</details>