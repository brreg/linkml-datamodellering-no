

# Slot: tittel 


_Namn/tittel på ressursen (dct:title)._





URI: [dct:title](http://purl.org/dc/terms/title)
Alias: tittel

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasettserie](Datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  yes  |
| [Katalogpost](Katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen |  no  |
| [Distribusjon](Distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |
| [Katalog](Katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  yes  |
| [Datasett](Datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |
| [Standard](Standard.md) | Ein standard som ein ressurs er i samsvar med |  yes  |
| [RegulativRessurs](RegulativRessurs.md) | Ein regulativ ressurs (lov, forskrift o |  no  |
| [Datatjeneste](Datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](LangString.md) |
| Domain Of | [Standard](Standard.md), [RegulativRessurs](RegulativRessurs.md), [Distribusjon](Distribusjon.md), [Datasett](Datasett.md), [Datasettserie](Datasettserie.md), [Datatjeneste](Datatjeneste.md), [Katalogpost](Katalogpost.md), [Katalog](Katalog.md) |
| Slot URI | [dct:title](http://purl.org/dc/terms/title) |

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
| self | dct:title |
| native | https://data.norge.no/linkml/dcat-ap-no/tittel |




## LinkML Source

<details>
```yaml
name: tittel
description: Namn/tittel på ressursen (dct:title).
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dct:title
alias: tittel
domain_of:
- Standard
- RegulativRessurs
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