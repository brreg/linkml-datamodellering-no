

# Slot: frekvens 


_Oppdateringsfrekvens for datasettet._





URI: [dct:accrualPeriodicity](http://purl.org/dc/terms/accrualPeriodicity)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |
| [Datasettserie](datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Datasett](datasett.md), [Datasettserie](datasettserie.md) |
| Slot URI | [dct:accrualPeriodicity](http://purl.org/dc/terms/accrualPeriodicity) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| gyldige_verdier | dct:Frequency |




### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:accrualPeriodicity |
| native | https://data.norge.no/ap-no/dcat-ap-no/frekvens |




## LinkML Source

<details>
```yaml
name: frekvens
annotations:
  gyldige_verdier:
    tag: gyldige_verdier
    value: dct:Frequency
description: Oppdateringsfrekvens for datasettet.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
slot_uri: dct:accrualPeriodicity
domain_of:
- Datasett
- Datasettserie
range: string

```
</details>