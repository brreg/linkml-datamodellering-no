

# Slot: anvist 


_Tidspunkt då lønn vart anvist._





URI: [adm:anvist](https://schema.fintlabs.no/administrasjon/anvist)
Alias: anvist

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
| Range | [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) |
| Domain Of | [Lonn](lonn.md) |
| Slot URI | [adm:anvist](https://schema.fintlabs.no/administrasjon/anvist) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:anvist |
| native | https://schema.fintlabs.no/administrasjon/:anvist |




## LinkML Source

<details>
```yaml
name: anvist
description: Tidspunkt då lønn vart anvist.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:anvist
alias: anvist
domain_of:
- Lonn
range: datetime

```
</details>