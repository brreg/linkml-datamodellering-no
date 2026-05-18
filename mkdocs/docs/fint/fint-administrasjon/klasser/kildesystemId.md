

# Slot: kildesystemId 


_Kjeldesystemets unike identifikator._





URI: [adm:kildesystemId](https://schema.fintlabs.no/administrasjon/kildesystemId)
Alias: kildesystemId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Variabellonn](variabellonn.md) | Informasjon om variabel lønn |  no  |
| [Fasttillegg](fasttillegg.md) | Faste tillegg til utbetaling |  no  |
| [Fastlonn](fastlonn.md) | Informasjon om fast lønnsbeordring |  no  |
| [Fravaer](fravaer.md) | Fråvær frå eit arbeidsforhold |  yes  |
| [Lonn](lonn.md) | Informasjon om lønn for eit arbeidsforhold (abstrakt base) |  yes  |






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


* from schema: https://data.norge.no/linkml/fint-administrasjon




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
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:kildesystemId
alias: kildesystemId
domain_of:
- Lonn
- Fravaer
range: Identifikator
inlined: true

```
</details>