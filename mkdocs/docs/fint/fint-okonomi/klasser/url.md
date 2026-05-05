

# Slot: url 


_URL til eksternt dokument._





URI: [okn:url](https://schema.fintlabs.no/okonomi/url)
Alias: url

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
| Slot URI | [okn:url](https://schema.fintlabs.no/okonomi/url) |

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
| self | okn:url |
| native | https://schema.fintlabs.no/okonomi/:url |




## LinkML Source

<details>
```yaml
name: url
description: URL til eksternt dokument.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:url
alias: url
owner: Bilag
domain_of:
- Bilag
range: string

```
</details>