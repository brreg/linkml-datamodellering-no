

# Slot: type_concept 


_Type ressurs frå eit kontrollert vokabular (dct:type)._





URI: [dct:type](http://purl.org/dc/terms/type)
Alias: type_concept

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Aktor](Aktor.md) | Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs |  no  |
| [Datasett](Datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |
| [RegulativRessurs](RegulativRessurs.md) | Ein regulativ ressurs (lov, forskrift o |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Begrep](Begrep.md) |
| Domain Of | [Aktor](Aktor.md), [RegulativRessurs](RegulativRessurs.md), [Datasett](Datasett.md) |
| Slot URI | [dct:type](http://purl.org/dc/terms/type) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:type |
| native | https://data.norge.no/linkml/dcat-ap-no/type_concept |




## LinkML Source

<details>
```yaml
name: type_concept
description: Type ressurs frå eit kontrollert vokabular (dct:type).
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dct:type
alias: type_concept
domain_of:
- Aktor
- RegulativRessurs
- Datasett
range: Begrep

```
</details>