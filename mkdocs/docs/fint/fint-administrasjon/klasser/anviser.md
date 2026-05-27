

# Slot: anviser 


_Personalressurs som har anvist lønsmeldinga etter fullmakt._





URI: [adm:anviser](https://schema.fintlabs.no/administrasjon/anviser)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Lonn](lonn.md) | Informasjon om lønn for eit arbeidsforhold (abstrakt base) |  yes  |
| [Fastlonn](fastlonn.md) | Informasjon om fast lønnsbeordring |  no  |
| [Fasttillegg](fasttillegg.md) | Faste tillegg til utbetaling |  no  |
| [Variabellonn](variabellonn.md) | Informasjon om variabel lønn |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personalressurs](personalressurs.md) |
| Domain Of | [Lonn](lonn.md) |
| Slot URI | [adm:anviser](https://schema.fintlabs.no/administrasjon/anviser) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:anviser |
| native | https://schema.fintlabs.no/administrasjon/:anviser |




## LinkML Source

<details>
```yaml
name: anviser
description: Personalressurs som har anvist lønsmeldinga etter fullmakt.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:anviser
domain_of:
- Lonn
range: Personalressurs

```
</details>