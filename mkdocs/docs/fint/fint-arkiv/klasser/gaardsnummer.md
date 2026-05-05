

# Slot: gaardsnummer 


_Nummerering av gårdseiging i matrikkelen, unik innanfor kommune._





URI: [fint:gaardsnummer](https://schema.fintlabs.no/gaardsnummer)
Alias: gaardsnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Matrikkelnummer](matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Matrikkelnummer](matrikkelnummer.md) |
| Slot URI | [fint:gaardsnummer](https://schema.fintlabs.no/gaardsnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Matrikkelnummer](matrikkelnummer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:gaardsnummer |
| native | https://schema.fintlabs.no/arkiv/:gaardsnummer |




## LinkML Source

<details>
```yaml
name: gaardsnummer
description: Nummerering av gårdseiging i matrikkelen, unik innanfor kommune.
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: fint:gaardsnummer
alias: gaardsnummer
owner: Matrikkelnummer
domain_of:
- Matrikkelnummer
range: string

```
</details>