

# Slot: opptjent 


_Periode der lønn vart opptent._





URI: [adm:opptjent](https://schema.fintlabs.no/administrasjon/opptjent)
Alias: opptjent

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
| Range | [Periode](Periode.md) |
| Domain Of | [Lonn](Lonn.md) |
| Slot URI | [adm:opptjent](https://schema.fintlabs.no/administrasjon/opptjent) |

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
| self | adm:opptjent |
| native | https://schema.fintlabs.no/administrasjon/:opptjent |




## LinkML Source

<details>
```yaml
name: opptjent
description: Periode der lønn vart opptent.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:opptjent
alias: opptjent
owner: Lonn
domain_of:
- Lonn
range: Periode
inlined: true

```
</details>