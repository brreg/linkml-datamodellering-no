

# Slot: identifikator_literal 


_Tekstleg identifikator for ressursen (dct:identifier)._





URI: [dct:identifier](http://purl.org/dc/terms/identifier)
Alias: identifikator_literal

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Katalog](Katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  no  |
| [Aktor](Aktor.md) | Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs |  no  |
| [Datasett](Datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |
| [RegulativRessurs](RegulativRessurs.md) | Ein regulativ ressurs (lov, forskrift o |  no  |
| [Datatjeneste](Datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Aktor](Aktor.md), [RegulativRessurs](RegulativRessurs.md), [Datasett](Datasett.md), [Datatjeneste](Datatjeneste.md), [Katalog](Katalog.md) |
| Slot URI | [dct:identifier](http://purl.org/dc/terms/identifier) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:identifier |
| native | https://data.norge.no/linkml/dcat-ap-no/identifikator_literal |




## LinkML Source

<details>
```yaml
name: identifikator_literal
description: Tekstleg identifikator for ressursen (dct:identifier).
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dct:identifier
alias: identifikator_literal
domain_of:
- Aktor
- RegulativRessurs
- Datasett
- Datatjeneste
- Katalog
range: string

```
</details>