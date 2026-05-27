

# Slot: attestant 


_Personalressurs som har attestert lønsmeldinga etter fullmakt._





URI: [adm:attestant](https://schema.fintlabs.no/administrasjon/attestant)
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
| Slot URI | [adm:attestant](https://schema.fintlabs.no/administrasjon/attestant) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




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
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:attestant
domain_of:
- Lonn
range: Personalressurs

```
</details>