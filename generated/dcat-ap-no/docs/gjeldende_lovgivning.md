

# Slot: gjeldende_lovgivning 


_Lovgjeving som gjeld for ressursen._





URI: [dcatap:applicableLegislation](http://data.europa.eu/r5r/applicableLegislation)
Alias: gjeldende_lovgivning

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasettserie](Datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  yes  |
| [Distribusjon](Distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |
| [Katalog](Katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  no  |
| [Datasett](Datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |
| [Datatjeneste](Datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RegulativRessurs](RegulativRessurs.md) |
| Domain Of | [Distribusjon](Distribusjon.md), [Datasett](Datasett.md), [Datasettserie](Datasettserie.md), [Datatjeneste](Datatjeneste.md), [Katalog](Katalog.md) |
| Slot URI | [dcatap:applicableLegislation](http://data.europa.eu/r5r/applicableLegislation) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcatap:applicableLegislation |
| native | https://data.norge.no/linkml/dcat-ap-no/gjeldende_lovgivning |




## LinkML Source

<details>
```yaml
name: gjeldende_lovgivning
description: Lovgjeving som gjeld for ressursen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dcatap:applicableLegislation
alias: gjeldende_lovgivning
domain_of:
- Distribusjon
- Datasett
- Datasettserie
- Datatjeneste
- Katalog
range: RegulativRessurs
multivalued: true

```
</details>