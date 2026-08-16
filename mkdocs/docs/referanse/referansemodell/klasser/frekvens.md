

# Slot: frekvens 


_Oppdateringsfrekvens for datasettet. Verdien SKAL veljast frå EUs kontrollerte vokabular Frequency (http://publications.europa.eu/resource/authority/frequency/). Sjå enumerasjonen DCTFrequency i common-ap-no for alle tilgjengelege verdiar (DAILY, WEEKLY, MONTHLY, ANNUAL, CONTINUOUS, osv.)._





URI: [dct:accrualPeriodicity](http://purl.org/dc/terms/accrualPeriodicity)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør. |  yes  |
| [Datasettserie](datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](konsept.md) |
| Domain Of | [Datasett](datasett.md), [Datasettserie](datasettserie.md) |
| Slot URI | [dct:accrualPeriodicity](http://purl.org/dc/terms/accrualPeriodicity) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| gyldige_verdier | http://publications.europa.eu/resource/authority/frequency/ |
| vokabular_krav | skal |
| vokabular_pattern | `^http://publications\.europa\.eu/resource/authority/frequency/[A-Z_0-9]+$` |
| enum_referanse | DCTFrequency |
| enum_dekning | full |




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
    value: http://publications.europa.eu/resource/authority/frequency/
  vokabular_krav:
    tag: vokabular_krav
    value: skal
  vokabular_pattern:
    tag: vokabular_pattern
    value: ^http://publications\.europa\.eu/resource/authority/frequency/[A-Z_0-9]+$
  enum_referanse:
    tag: enum_referanse
    value: DCTFrequency
  enum_dekning:
    tag: enum_dekning
    value: full
description: Oppdateringsfrekvens for datasettet. Verdien SKAL veljast frå EUs kontrollerte
  vokabular Frequency (http://publications.europa.eu/resource/authority/frequency/).
  Sjå enumerasjonen DCTFrequency i common-ap-no for alle tilgjengelege verdiar (DAILY,
  WEEKLY, MONTHLY, ANNUAL, CONTINUOUS, osv.).
from_schema: https://data.norge.no/ap-no/dcat-ap-no
slot_uri: dct:accrualPeriodicity
domain_of:
- Datasett
- Datasettserie
range: Konsept

```
</details>