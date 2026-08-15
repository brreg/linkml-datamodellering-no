

# Slot: tema 


_Tema frå eit kontrollert vokabular. For norske offentlege datasett SKAL Los (https://psi.norge.no/los/) brukast som primærvokabular. Bruk hovudtema (https://psi.norge.no/los/tema/<namn>) og eventuelt undertema i tillegg. EuroVoc kan brukast som sekundærvokabular. Los har ~200 hovudtema og er for omfattande til å modellerast som enum. Bruk MCP-server mcp__linkml-begrep-utkast__list_los_tema for å søkje i Los-hierarkiet._





URI: [dcat:theme](http://www.w3.org/ns/dcat#theme)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør. |  yes  |
| [Datasettserie](datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata. |  yes  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt. |  yes  |






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
| vokabular_krav | skal |
| vokabular_pattern | ^https://psi\.norge\.no/los/(tema|ord|hendelse)/[a-z0-9-]+(/[a-z0-9-]+)*$ |
| sekundare_vokabular | http://publications.europa.eu/resource/authority/eurovoc/ |
| sekundare_vokabular_krav | kan |




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
  vokabular_krav:
    tag: vokabular_krav
    value: skal
  vokabular_pattern:
    tag: vokabular_pattern
    value: ^https://psi\.norge\.no/los/(tema|ord|hendelse)/[a-z0-9-]+(/[a-z0-9-]+)*$
  sekundare_vokabular:
    tag: sekundare_vokabular
    value: http://publications.europa.eu/resource/authority/eurovoc/
  sekundare_vokabular_krav:
    tag: sekundare_vokabular_krav
    value: kan
description: Tema frå eit kontrollert vokabular. For norske offentlege datasett SKAL
  Los (https://psi.norge.no/los/) brukast som primærvokabular. Bruk hovudtema (https://psi.norge.no/los/tema/<namn>)
  og eventuelt undertema i tillegg. EuroVoc kan brukast som sekundærvokabular. Los
  har ~200 hovudtema og er for omfattande til å modellerast som enum. Bruk MCP-server
  mcp__linkml-begrep-utkast__list_los_tema for å søkje i Los-hierarkiet.
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