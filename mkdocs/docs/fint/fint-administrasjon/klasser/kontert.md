

# Slot: kontert 


_Tidspunkt då lønn vart kontert._





URI: [adm:kontert](https://schema.fintlabs.no/administrasjon/kontert)
Alias: kontert

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
| Slot URI | [adm:kontert](https://schema.fintlabs.no/administrasjon/kontert) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:kontert |
| native | https://schema.fintlabs.no/administrasjon/:kontert |




## LinkML Source

<details>
```yaml
name: kontert
description: Tidspunkt då lønn vart kontert.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:kontert
alias: kontert
domain_of:
- Lonn
range: datetime

```
</details>