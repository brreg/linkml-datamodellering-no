

# Slot: begrep 


_Fagomgrep som datasettet handlar om. Verdien BØR peike til omgrep i ein begrepskatalog, t.d. Felles begrepskatalog (https://concept-catalog.fellesdatakatalog.digdir.no/) eller organisasjonens eigen begrepskatalog._





URI: [dct:subject](http://purl.org/dc/terms/subject)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](konsept.md) |
| Domain Of | [Datasett](datasett.md) |
| Slot URI | [dct:subject](http://purl.org/dc/terms/subject) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| gyldige_verdier | https://concept-catalog.fellesdatakatalog.digdir.no/ |
| vokabular_krav | bør |




### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:subject |
| native | https://data.norge.no/ap-no/dcat-ap-no/begrep |




## LinkML Source

<details>
```yaml
name: begrep
annotations:
  gyldige_verdier:
    tag: gyldige_verdier
    value: https://concept-catalog.fellesdatakatalog.digdir.no/
  vokabular_krav:
    tag: vokabular_krav
    value: bør
description: Fagomgrep som datasettet handlar om. Verdien BØR peike til omgrep i ein
  begrepskatalog, t.d. Felles begrepskatalog (https://concept-catalog.fellesdatakatalog.digdir.no/)
  eller organisasjonens eigen begrepskatalog.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
slot_uri: dct:subject
domain_of:
- Datasett
range: Konsept
multivalued: true

```
</details>