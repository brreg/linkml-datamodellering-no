

# Slot: sprak 


_Språk brukt i ressursen (dct:language)._





URI: [dct:language](http://purl.org/dc/terms/language)
Alias: sprak

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RegulativRessurs](regulativressurs.md) | Ein regulativ ressurs (lov, forskrift o |  no  |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  yes  |
| [Katalogpost](katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Spraak](spraak.md) |
| Domain Of | [RegulativRessurs](regulativressurs.md), [Distribusjon](distribusjon.md), [Datasett](datasett.md), [Katalogpost](katalogpost.md), [Katalog](katalog.md) |
| Slot URI | [dct:language](http://purl.org/dc/terms/language) |

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
| self | dct:language |
| native | samtbuskole:sprak |




## LinkML Source

<details>
```yaml
name: sprak
description: Språk brukt i ressursen (dct:language).
from_schema: https://example.no/ontology/samt-bu-skole
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