

# Slot: lonsart 


_Lønnsart._





URI: [adm:lonsart](https://schema.fintlabs.no/administrasjon/lonsart)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fravaerstype](fravaerstype.md) | Type fråvær |  yes  |
| [Fastlonn](fastlonn.md) | Informasjon om fast lønnsbeordring |  yes  |
| [Fasttillegg](fasttillegg.md) | Faste tillegg til utbetaling |  yes  |
| [Variabellonn](variabellonn.md) | Informasjon om variabel lønn |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Lonsart](lonsart.md) |
| Domain Of | [Fravaerstype](fravaerstype.md), [Fastlonn](fastlonn.md), [Fasttillegg](fasttillegg.md), [Variabellonn](variabellonn.md) |
| Slot URI | [adm:lonsart](https://schema.fintlabs.no/administrasjon/lonsart) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:lonsart |
| native | https://schema.fintlabs.no/administrasjon/:lonsart |




## LinkML Source

<details>
```yaml
name: lonsart
description: Lønnsart.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:lonsart
domain_of:
- Fravaerstype
- Fastlonn
- Fasttillegg
- Variabellonn
range: Lonsart

```
</details>