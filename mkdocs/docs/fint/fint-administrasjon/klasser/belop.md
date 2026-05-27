

# Slot: belop 


_Beløp i øre._





URI: [adm:belop](https://schema.fintlabs.no/administrasjon/belop)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fasttillegg](fasttillegg.md) | Faste tillegg til utbetaling |  yes  |
| [Variabellonn](variabellonn.md) | Informasjon om variabel lønn |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:integer](http://www.w3.org/2001/XMLSchema#integer) |
| Domain Of | [Fasttillegg](fasttillegg.md), [Variabellonn](variabellonn.md) |
| Slot URI | [adm:belop](https://schema.fintlabs.no/administrasjon/belop) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:belop |
| native | https://schema.fintlabs.no/administrasjon/:belop |




## LinkML Source

<details>
```yaml
name: belop
description: Beløp i øre.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:belop
domain_of:
- Fasttillegg
- Variabellonn
range: integer

```
</details>