

# Slot: sprak 


_Språk brukt i ressursen (dct:language)._





URI: [dct:language](http://purl.org/dc/terms/language)
Alias: sprak

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Katalogpost](Katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen |  no  |
| [Distribusjon](Distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |
| [Katalog](Katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  yes  |
| [Datasett](Datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |
| [RegulativRessurs](RegulativRessurs.md) | Ein regulativ ressurs (lov, forskrift o |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Spraak](Spraak.md) |
| Domain Of | [RegulativRessurs](RegulativRessurs.md), [Distribusjon](Distribusjon.md), [Datasett](Datasett.md), [Katalogpost](Katalogpost.md), [Katalog](Katalog.md) |
| Slot URI | [dct:language](http://purl.org/dc/terms/language) |

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
| self | dct:language |
| native | https://data.norge.no/linkml/dcat-ap-no/sprak |




## LinkML Source

<details>
```yaml
name: sprak
description: Språk brukt i ressursen (dct:language).
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dct:language
alias: sprak
domain_of:
- RegulativRessurs
- Distribusjon
- Datasett
- Katalogpost
- Katalog
range: Spraak
multivalued: true

```
</details>