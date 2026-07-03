

# Slot: tilgangsrettigheter 


_Egenskapen brukes til å angi om det er allmenn tilgang, betinget tilgang eller ikke-allmenn tilgang til datasettet. Bruk EU Access Rights-vokabularet: PUBLIC (ope, ingen registrering), RESTRICTED (avgrensa), NON_PUBLIC (ikkje offentleg)._





URI: [dct:accessRights](http://purl.org/dc/terms/accessRights)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
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
| gyldige_verdier | http://publications.europa.eu/resource/authority/access-right/PUBLIC http://publications.europa.eu/resource/authority/access-right/RESTRICTED http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC |




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
    value: http://publications.europa.eu/resource/authority/access-right/PUBLIC http://publications.europa.eu/resource/authority/access-right/RESTRICTED
      http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC
description: 'Egenskapen brukes til å angi om det er allmenn tilgang, betinget tilgang
  eller ikke-allmenn tilgang til datasettet. Bruk EU Access Rights-vokabularet: PUBLIC
  (ope, ingen registrering), RESTRICTED (avgrensa), NON_PUBLIC (ikkje offentleg).'
from_schema: https://data.norge.no/ap-no/dcat-ap-no
slot_uri: dct:accessRights
domain_of:
- Datasett
- Datatjeneste
range: uri
multivalued: true

```
</details>