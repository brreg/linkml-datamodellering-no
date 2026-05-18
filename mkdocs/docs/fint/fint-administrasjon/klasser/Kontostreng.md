

# Slot: kontostreng 


_Kontering av lønn._





URI: [adm:kontostreng](https://schema.fintlabs.no/administrasjon/kontostreng)
Alias: kontostreng

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fastlonn](fastlonn.md) | Informasjon om fast lønnsbeordring |  no  |
| [Variabellonn](variabellonn.md) | Informasjon om variabel lønn |  no  |
| [Fasttillegg](fasttillegg.md) | Faste tillegg til utbetaling |  no  |
| [Lonn](lonn.md) | Informasjon om lønn for eit arbeidsforhold (abstrakt base) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kontostreng](kontostreng.md) |
| Domain Of | [Lonn](lonn.md) |
| Slot URI | [adm:kontostreng](https://schema.fintlabs.no/administrasjon/kontostreng) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:kontostreng |
| native | https://schema.fintlabs.no/administrasjon/:kontostreng |




## LinkML Source

<details>
```yaml
name: kontostreng
description: Kontering av lønn.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:kontostreng
alias: kontostreng
domain_of:
- Lonn
range: Kontostreng
inlined: true

```
</details>