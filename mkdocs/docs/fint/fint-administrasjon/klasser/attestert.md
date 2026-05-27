

# Slot: attestert 


_Tidspunkt då lønn vart attestert._





URI: [adm:attestert](https://schema.fintlabs.no/administrasjon/attestert)
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
| Range | [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) |
| Domain Of | [Lonn](lonn.md) |
| Slot URI | [adm:attestert](https://schema.fintlabs.no/administrasjon/attestert) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:attestert |
| native | https://schema.fintlabs.no/administrasjon/:attestert |




## LinkML Source

<details>
```yaml
name: attestert
description: Tidspunkt då lønn vart attestert.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:attestert
domain_of:
- Lonn
range: datetime

```
</details>