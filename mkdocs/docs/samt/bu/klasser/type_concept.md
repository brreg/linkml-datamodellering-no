

# Slot: type_concept 


_Type ressurs frå eit kontrollert vokabular (dct:type)._





URI: [dct:type](http://purl.org/dc/terms/type)
Alias: type_concept

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RegulativRessurs](regulativressurs.md) | Ein regulativ ressurs (lov, forskrift o |  no  |
| [Aktor](aktor.md) | Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs |  no  |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](konsept.md) |
| Domain Of | [Aktor](aktor.md), [RegulativRessurs](regulativressurs.md), [Datasett](datasett.md) |
| Slot URI | [dct:type](http://purl.org/dc/terms/type) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:type |
| native | samtbuskole:type_concept |




## LinkML Source

<details>
```yaml
name: type_concept
description: Type ressurs frå eit kontrollert vokabular (dct:type).
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dct:type
alias: type_concept
domain_of:
- Aktor
- RegulativRessurs
- Datasett
range: Konsept

```
</details>