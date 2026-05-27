

# Slot: opptjent 


_Periode der lønn vart opptent._





URI: [adm:opptjent](https://schema.fintlabs.no/administrasjon/opptjent)
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
| Range | [Periode](periode.md) |
| Domain Of | [Lonn](lonn.md) |
| Slot URI | [adm:opptjent](https://schema.fintlabs.no/administrasjon/opptjent) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:opptjent |
| native | https://schema.fintlabs.no/administrasjon/:opptjent |




## LinkML Source

<details>
```yaml
name: opptjent
description: Periode der lønn vart opptent.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:opptjent
domain_of:
- Lonn
range: Periode
inlined: true

```
</details>