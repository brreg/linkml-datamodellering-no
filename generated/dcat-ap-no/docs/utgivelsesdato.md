

# Slot: utgivelsesdato 


_Dato ressursen vart første gong publisert (dct:issued)._





URI: [dct:issued](http://purl.org/dc/terms/issued)
Alias: utgivelsesdato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasettserie](Datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  no  |
| [Katalogpost](Katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen |  yes  |
| [Distribusjon](Distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |
| [Katalog](Katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  yes  |
| [Datasett](Datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [Distribusjon](Distribusjon.md), [Datasett](Datasett.md), [Datasettserie](Datasettserie.md), [Katalogpost](Katalogpost.md), [Katalog](Katalog.md) |
| Slot URI | [dct:issued](http://purl.org/dc/terms/issued) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:issued |
| native | https://data.norge.no/linkml/dcat-ap-no/utgivelsesdato |




## LinkML Source

<details>
```yaml
name: utgivelsesdato
description: Dato ressursen vart første gong publisert (dct:issued).
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dct:issued
alias: utgivelsesdato
domain_of:
- Distribusjon
- Datasett
- Datasettserie
- Katalogpost
- Katalog
range: date

```
</details>