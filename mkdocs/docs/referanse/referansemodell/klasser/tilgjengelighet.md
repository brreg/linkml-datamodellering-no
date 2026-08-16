

# Slot: tilgjengelighet 


_Planlagt tilgjengelegheit for ressursen. Verdien BØR veljast frå EUs kontrollerte vokabular Planned availability (http://publications.europa.eu/resource/authority/planned-availability/). Gyldige verdiar: AVAILABLE (tilgjengeleg), EXPERIMENTAL (eksperimentell), STABLE (stabil), TEMPORARY (mellombels)._





URI: [dcatap:availability](http://data.europa.eu/r5r/availability)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett. |  yes  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](konsept.md) |
| Domain Of | [Distribusjon](distribusjon.md), [Datatjeneste](datatjeneste.md) |
| Slot URI | [dcatap:availability](http://data.europa.eu/r5r/availability) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| gyldige_verdier | http://publications.europa.eu/resource/authority/planned-availability/ |
| vokabular_krav | bør |
| vokabular_pattern | `^http://publications\.europa\.eu/resource/authority/planned-availability/[A-Z_]+$` |




### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcatap:availability |
| native | https://data.norge.no/ap-no/dcat-ap-no/tilgjengelighet |




## LinkML Source

<details>
```yaml
name: tilgjengelighet
annotations:
  gyldige_verdier:
    tag: gyldige_verdier
    value: http://publications.europa.eu/resource/authority/planned-availability/
  vokabular_krav:
    tag: vokabular_krav
    value: bør
  vokabular_pattern:
    tag: vokabular_pattern
    value: ^http://publications\.europa\.eu/resource/authority/planned-availability/[A-Z_]+$
description: 'Planlagt tilgjengelegheit for ressursen. Verdien BØR veljast frå EUs
  kontrollerte vokabular Planned availability (http://publications.europa.eu/resource/authority/planned-availability/).
  Gyldige verdiar: AVAILABLE (tilgjengeleg), EXPERIMENTAL (eksperimentell), STABLE
  (stabil), TEMPORARY (mellombels).'
from_schema: https://data.norge.no/ap-no/dcat-ap-no
slot_uri: dcatap:availability
domain_of:
- Distribusjon
- Datatjeneste
range: Konsept

```
</details>