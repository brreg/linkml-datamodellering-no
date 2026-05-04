

# Slot: konterer 


_Personalressurs som har kontert lønsmeldinga etter fullmakt._





URI: [adm:konterer](https://schema.fintlabs.no/administrasjon/konterer)
Alias: konterer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Lonn](Lonn.md) | Informasjon om lønn for eit arbeidsforhold (abstrakt base) |  no  |
| [Fasttillegg](Fasttillegg.md) | Faste tillegg til utbetaling |  no  |
| [Variabellonn](Variabellonn.md) | Informasjon om variabel lønn |  no  |
| [Fastlonn](Fastlonn.md) | Informasjon om fast lønnsbeordring |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personalressurs](Personalressurs.md) |
| Domain Of | [Lonn](Lonn.md) |
| Slot URI | [adm:konterer](https://schema.fintlabs.no/administrasjon/konterer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Lonn](Lonn.md) |








## In Subsets


* [Valgfri](Valgfri.md)






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