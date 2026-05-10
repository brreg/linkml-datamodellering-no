

# Slot: endringsdato 


_Dato for siste endring av ressursen (dct:modified)._





URI: [dct:modified](http://purl.org/dc/terms/modified)
Alias: endringsdato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Katalogpost](katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen |  yes  |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  yes  |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |
| [Datasettserie](datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  no  |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:date](http://www.w3.org/2001/XMLSchema#date) |
| Domain Of | [Distribusjon](distribusjon.md), [Datasett](datasett.md), [Datasettserie](datasettserie.md), [Katalogpost](katalogpost.md), [Katalog](katalog.md) |
| Slot URI | [dct:modified](http://purl.org/dc/terms/modified) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:modified |
| native | https://data.norge.no/linkml/common-ap-no/endringsdato |




## LinkML Source

<details>
```yaml
name: endringsdato
description: Dato for siste endring av ressursen (dct:modified).
from_schema: https://data.norge.no/linkml/common-ap-no
slot_uri: dct:modified
alias: endringsdato
domain_of:
- Distribusjon
- Datasett
- Datasettserie
- Katalogpost
- Katalog
range: date

```
</details>