

# Slot: periode 


_Periode for ressursen._





URI: [adm:periode](https://schema.fintlabs.no/administrasjon/periode)
Alias: periode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Lonn](lonn.md) | Informasjon om lønn for eit arbeidsforhold (abstrakt base) |  yes  |
| [Fasttillegg](fasttillegg.md) | Faste tillegg til utbetaling |  no  |
| [Variabellonn](variabellonn.md) | Informasjon om variabel lønn |  no  |
| [Fravaer](fravaer.md) | Fråvær frå eit arbeidsforhold |  yes  |
| [Fastlonn](fastlonn.md) | Informasjon om fast lønnsbeordring |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Periode](periode.md) |
| Domain Of | [Lonn](lonn.md), [Fravaer](fravaer.md) |
| Slot URI | [adm:periode](https://schema.fintlabs.no/administrasjon/periode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:periode |
| native | https://schema.fintlabs.no/administrasjon/:periode |




## LinkML Source

<details>
```yaml
name: periode
description: Periode for ressursen.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:periode
alias: periode
domain_of:
- Lonn
- Fravaer
range: Periode
inlined: true

```
</details>