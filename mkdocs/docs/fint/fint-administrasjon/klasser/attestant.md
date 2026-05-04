

# Slot: attestant 


_Personalressurs som har attestert lønsmeldinga etter fullmakt._





URI: [adm:attestant](https://schema.fintlabs.no/administrasjon/attestant)
Alias: attestant

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
| Slot URI | [adm:attestant](https://schema.fintlabs.no/administrasjon/attestant) |

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
| self | adm:attestant |
| native | https://schema.fintlabs.no/administrasjon/:attestant |




## LinkML Source

<details>
```yaml
name: attestant
description: Personalressurs som har attestert lønsmeldinga etter fullmakt.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:attestant
alias: attestant
owner: Lonn
domain_of:
- Lonn
range: Personalressurs

```
</details>