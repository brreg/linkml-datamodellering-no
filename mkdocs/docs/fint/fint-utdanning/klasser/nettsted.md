

# Slot: nettsted 


_Adresse til eit nettstad._





URI: [fint:nettsted](https://schema.fintlabs.no/nettsted)
Alias: nettsted

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktinformasjon](Kontaktinformasjon.md) | Informasjon som kan brukast for å oppnå kontakt |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Kontaktinformasjon](Kontaktinformasjon.md) |
| Slot URI | [fint:nettsted](https://schema.fintlabs.no/nettsted) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Kontaktinformasjon](Kontaktinformasjon.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:nettsted |
| native | https://schema.fintlabs.no/utdanning/:nettsted |




## LinkML Source

<details>
```yaml
name: nettsted
description: Adresse til eit nettstad.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: fint:nettsted
alias: nettsted
owner: Kontaktinformasjon
domain_of:
- Kontaktinformasjon
range: string

```
</details>