

# Slot: konterer 


_Personalressurs som har kontert lønsmeldinga etter fullmakt._





URI: [adm:konterer](https://schema.fintlabs.no/administrasjon/konterer)
Alias: konterer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Lonn](lonn.md) | Informasjon om lønn for eit arbeidsforhold (abstrakt base) |  no  |
| [Variabellonn](variabellonn.md) | Informasjon om variabel lønn |  no  |
| [Fastlonn](fastlonn.md) | Informasjon om fast lønnsbeordring |  no  |
| [Fasttillegg](fasttillegg.md) | Faste tillegg til utbetaling |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personalressurs](personalressurs.md) |
| Domain Of | [Lonn](lonn.md) |
| Slot URI | [adm:konterer](https://schema.fintlabs.no/administrasjon/konterer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Lonn](lonn.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:konterer |
| native | https://schema.fintlabs.no/administrasjon/:konterer |




## LinkML Source

<details>
```yaml
name: konterer
description: Personalressurs som har kontert lønsmeldinga etter fullmakt.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:konterer
alias: konterer
owner: Lonn
domain_of:
- Lonn
range: Personalressurs

```
</details>