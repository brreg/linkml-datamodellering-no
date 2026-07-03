

# Slot: tema 


_Tema frå eit kontrollert vokabular. For norske offentlege datasett skal Los (https://psi.norge.no/los/) brukast som primærvokabular. Bruk hovudtema (https://psi.norge.no/los/tema/<namn>) og eventuelt undertema i tillegg. EuroVoc kan brukast som sekundærvokabular._





URI: [dcat:theme](http://www.w3.org/ns/dcat#theme)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |
| [Datasettserie](datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  yes  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](konsept.md) |
| Domain Of | [Datasett](datasett.md), [Datasettserie](datasettserie.md), [Datatjeneste](datatjeneste.md) |
| Slot URI | [dcat:theme](http://www.w3.org/ns/dcat#theme) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| gyldige_verdier | https://psi.norge.no/los/ |




### Schema Source


* from schema: https://data.norge.no/ap-no/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:theme |
| native | https://data.norge.no/ap-no/dcat-ap-no/tema |




## LinkML Source

<details>
```yaml
name: tema
annotations:
  gyldige_verdier:
    tag: gyldige_verdier
    value: https://psi.norge.no/los/
description: Tema frå eit kontrollert vokabular. For norske offentlege datasett skal
  Los (https://psi.norge.no/los/) brukast som primærvokabular. Bruk hovudtema (https://psi.norge.no/los/tema/<namn>)
  og eventuelt undertema i tillegg. EuroVoc kan brukast som sekundærvokabular.
from_schema: https://data.norge.no/ap-no/dcat-ap-no
slot_uri: dcat:theme
domain_of:
- Datasett
- Datasettserie
- Datatjeneste
range: Konsept
multivalued: true

```
</details>