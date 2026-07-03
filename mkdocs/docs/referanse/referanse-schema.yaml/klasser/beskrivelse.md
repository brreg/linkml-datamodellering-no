

# Slot: beskrivelse 


_Kortfatta skildring av ressursen._





URI: [dct:description](http://purl.org/dc/terms/description)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RegulativRessurs](regulativressurs.md) | Ein regulativ ressurs (lov, forskrift o |  no  |
| [Gebyr](gebyr.md) | Eit gebyr knytt til bruk av ein datatjeneste |  no  |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  yes  |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |
| [Datasettserie](datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  yes  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |
| [Katalogpost](katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen |  no  |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  yes  |
| [Ressurs](ressurs.md) | Ein generisk ressurs med tittel, skildring og utgjevar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](langstring.md) |
| Domain Of | [RegulativRessurs](regulativressurs.md), [Gebyr](gebyr.md), [Distribusjon](distribusjon.md), [Datasett](datasett.md), [Datasettserie](datasettserie.md), [Datatjeneste](datatjeneste.md), [Katalogpost](katalogpost.md), [Katalog](katalog.md), [Ressurs](ressurs.md) |
| Slot URI | [dct:description](http://purl.org/dc/terms/description) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.org/linkml/referanse




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:description |
| native | https://example.org/linkml/referanse/beskrivelse |




## LinkML Source

<details>
```yaml
name: beskrivelse
description: Kortfatta skildring av ressursen.
from_schema: https://example.org/linkml/referanse
rank: 1000
slot_uri: dct:description
domain_of:
- RegulativRessurs
- Gebyr
- Distribusjon
- Datasett
- Datasettserie
- Datatjeneste
- Katalogpost
- Katalog
- Ressurs
range: LangString

```
</details>