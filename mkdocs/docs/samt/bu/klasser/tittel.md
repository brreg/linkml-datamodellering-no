

# Slot: tittel 


_Namn/tittel på ressursen (dct:title)._





URI: [dct:title](http://purl.org/dc/terms/title)
Alias: tittel

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RegulativRessurs](regulativressurs.md) | Ein regulativ ressurs (lov, forskrift o |  no  |
| [Standard](standard.md) | Ein standard som ein ressurs er i samsvar med |  yes  |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  yes  |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  yes  |
| [Katalogpost](katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen |  no  |
| [Datasettserie](datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](langstring.md) |
| Domain Of | [Standard](standard.md), [RegulativRessurs](regulativressurs.md), [Distribusjon](distribusjon.md), [Datasett](datasett.md), [Datasettserie](datasettserie.md), [Datatjeneste](datatjeneste.md), [Katalogpost](katalogpost.md), [Katalog](katalog.md) |
| Slot URI | [dct:title](http://purl.org/dc/terms/title) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:title |
| native | samtbuskole:tittel |




## LinkML Source

<details>
```yaml
name: tittel
description: Namn/tittel på ressursen (dct:title).
from_schema: https://example.no/ontology/samt-bu-skole
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