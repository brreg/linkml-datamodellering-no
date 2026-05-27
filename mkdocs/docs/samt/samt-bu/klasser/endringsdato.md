

# Slot: endringsdato 


_Dato for siste endring av ressursen (dct:modified)._





URI: [dct:modified](http://purl.org/dc/terms/modified)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |
| [Datasettserie](datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  no  |
| [Katalogpost](katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen |  yes  |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  yes  |






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


* from schema: https://data.norge.no/ap-no/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:modified |
| native | https://data.norge.no/ap-no/common-ap-no/endringsdato |




## LinkML Source

<details>
```yaml
name: endringsdato
description: Dato for siste endring av ressursen (dct:modified).
from_schema: https://data.norge.no/ap-no/common-ap-no
slot_uri: dct:modified
domain_of:
- Distribusjon
- Datasett
- Datasettserie
- Katalogpost
- Katalog
range: date

```
</details>