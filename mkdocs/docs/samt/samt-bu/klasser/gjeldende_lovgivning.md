

# Slot: gjeldende_lovgivning 


_Lovgjeving som gjeld for ressursen._





URI: [dcatap:applicableLegislation](http://data.europa.eu/r5r/applicableLegislation)
Alias: gjeldende_lovgivning

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  no  |
| [Datasettserie](datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  yes  |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RegulativRessurs](regulativressurs.md) |
| Domain Of | [Distribusjon](distribusjon.md), [Datasett](datasett.md), [Datasettserie](datasettserie.md), [Datatjeneste](datatjeneste.md), [Katalog](katalog.md) |
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