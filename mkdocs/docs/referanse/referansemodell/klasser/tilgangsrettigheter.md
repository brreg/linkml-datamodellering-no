

# Slot: tilgangsrettigheter 


_Tilgangsrettar til datasettet. Verdien SKAL veljast frå EUs kontrollerte vokabular Access Right (http://publications.europa.eu/resource/authority/access-right/). Gyldige verdiar: PUBLIC (ope, ingen registrering), RESTRICTED (avgrensa tilgang), NON_PUBLIC (ikkje offentleg). Sjå enumerasjonen EUAccessRight i common-ap-no._





URI: [dct:accessRights](http://purl.org/dc/terms/accessRights)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør. |  yes  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](konsept.md) |
| Domain Of | [Datasett](datasett.md), [Datatjeneste](datatjeneste.md) |
| Slot URI | [dct:accessRights](http://purl.org/dc/terms/accessRights) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| gyldige_verdier | http://publications.europa.eu/resource/authority/access-right/ |
| vokabular_krav | skal |
| vokabular_pattern | `^http://publications\.europa\.eu/resource/authority/access-right/(PUBLIC|RESTRICTED|NON_PUBLIC)$` |
| enum_referanse | EUAccessRight |
| enum_dekning | full |




### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:accessRights |
| native | https://data.norge.no/ap-no/dcat-ap-no/tilgangsrettigheter |




## LinkML Source

<details>
```yaml
name: tilgangsrettigheter
annotations:
  gyldige_verdier:
    tag: gyldige_verdier
    value: http://publications.europa.eu/resource/authority/access-right/
  vokabular_krav:
    tag: vokabular_krav
    value: skal
  vokabular_pattern:
    tag: vokabular_pattern
    value: ^http://publications\.europa\.eu/resource/authority/access-right/(PUBLIC|RESTRICTED|NON_PUBLIC)$
  enum_referanse:
    tag: enum_referanse
    value: EUAccessRight
  enum_dekning:
    tag: enum_dekning
    value: full
description: 'Tilgangsrettar til datasettet. Verdien SKAL veljast frå EUs kontrollerte
  vokabular Access Right (http://publications.europa.eu/resource/authority/access-right/).
  Gyldige verdiar: PUBLIC (ope, ingen registrering), RESTRICTED (avgrensa tilgang),
  NON_PUBLIC (ikkje offentleg). Sjå enumerasjonen EUAccessRight i common-ap-no.'
from_schema: https://data.norge.no/ap-no/dcat-ap-no
slot_uri: dct:accessRights
domain_of:
- Datasett
- Datatjeneste
range: Konsept
multivalued: true

```
</details>