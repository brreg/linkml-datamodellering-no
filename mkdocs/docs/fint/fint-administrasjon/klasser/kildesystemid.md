

# Slot: kildesystemId 


_Kjeldesystemets unike identifikator._





URI: [adm:kildesystemId](https://schema.fintlabs.no/administrasjon/kildesystemId)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Lonn](lonn.md) | Informasjon om lønn for eit arbeidsforhold (abstrakt base) |  yes  |
| [Fravaer](fravaer.md) | Fråvær frå eit arbeidsforhold |  yes  |
| [Fastlonn](fastlonn.md) | Informasjon om fast lønnsbeordring |  no  |
| [Fasttillegg](fasttillegg.md) | Faste tillegg til utbetaling |  no  |
| [Variabellonn](variabellonn.md) | Informasjon om variabel lønn |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Lonn](lonn.md), [Fravaer](fravaer.md) |
| Slot URI | [adm:kildesystemId](https://schema.fintlabs.no/administrasjon/kildesystemId) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:kildesystemId |
| native | https://schema.fintlabs.no/administrasjon/:kildesystemId |




## LinkML Source

<details>
```yaml
name: kildesystemId
description: Kjeldesystemets unike identifikator.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:kildesystemId
domain_of:
- Lonn
- Fravaer
range: Identifikator
inlined: true

```
</details>