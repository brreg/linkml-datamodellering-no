

# Slot: virksomhet 


_Referanse til Virksomhet som er leverandør._





URI: [okn:virksomhet](https://schema.fintlabs.no/okonomi/virksomhet)
Alias: virksomhet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Leverandor](leverandor.md) | Person eller verksemd som leverer produkt eller tenester (Leverandør) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Leverandor](leverandor.md) |
| Slot URI | [okn:virksomhet](https://schema.fintlabs.no/okonomi/virksomhet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Leverandor](leverandor.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:virksomhet |
| native | https://schema.fintlabs.no/okonomi/:virksomhet |




## LinkML Source

<details>
```yaml
name: virksomhet
description: Referanse til Virksomhet som er leverandør.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:virksomhet
alias: virksomhet
owner: Leverandor
domain_of:
- Leverandor
range: uriorcurie

```
</details>