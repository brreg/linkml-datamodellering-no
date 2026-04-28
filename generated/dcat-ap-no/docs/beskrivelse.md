

# Slot: beskrivelse 


_Fritekstbeskrivelse av ressursen (dct:description)._





URI: [dct:description](http://purl.org/dc/terms/description)
Alias: beskrivelse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasettserie](Datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  yes  |
| [Katalogpost](Katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen |  no  |
| [Distribusjon](Distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  yes  |
| [Gebyr](Gebyr.md) | Eit gebyr knytt til bruk av ein datatjeneste |  no  |
| [Katalog](Katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  yes  |
| [Datasett](Datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |
| [RegulativRessurs](RegulativRessurs.md) | Ein regulativ ressurs (lov, forskrift o |  no  |
| [Datatjeneste](Datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](LangString.md) |
| Domain Of | [RegulativRessurs](RegulativRessurs.md), [Gebyr](Gebyr.md), [Distribusjon](Distribusjon.md), [Datasett](Datasett.md), [Datasettserie](Datasettserie.md), [Datatjeneste](Datatjeneste.md), [Katalogpost](Katalogpost.md), [Katalog](Katalog.md) |
| Slot URI | [dct:description](http://purl.org/dc/terms/description) |

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
| self | dct:description |
| native | https://data.norge.no/linkml/dcat-ap-no/beskrivelse |




## LinkML Source

<details>
```yaml
name: beskrivelse
description: Fritekstbeskrivelse av ressursen (dct:description).
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dct:description
alias: beskrivelse
domain_of:
- RegulativRessurs
- Gebyr
- Distribusjon
- Datasett
- Datasettserie
- Datatjeneste
- Katalogpost
- Katalog
range: LangString
multivalued: true

```
</details>