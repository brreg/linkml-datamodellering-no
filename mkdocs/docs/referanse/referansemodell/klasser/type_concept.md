

# Slot: type_concept 


_Type ressurs frå eit kontrollert vokabular (dct:type)._





URI: [dct:type](http://purl.org/dc/terms/type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Lisensdokument](lisensdokument.md) | Eit lisensdokument (dct:LicenseDocument). |  yes  |
| [Aktoer](aktoer.md) | Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs. |  yes  |
| [RegulativRessurs](regulativressurs.md) | Ein regulativ ressurs (lov, forskrift o.l.) som gjeld for ein ressurs. |  yes  |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](konsept.md) |
| Domain Of | [Lisensdokument](lisensdokument.md), [Aktoer](aktoer.md), [RegulativRessurs](regulativressurs.md), [Datasett](datasett.md) |
| Slot URI | [dct:type](http://purl.org/dc/terms/type) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:type |
| native | https://data.norge.no/ap-no/common-ap-no/type_concept |




## LinkML Source

<details>
```yaml
name: type_concept
description: Type ressurs frå eit kontrollert vokabular (dct:type).
from_schema: https://data.norge.no/ap-no/common-ap-no
slot_uri: dct:type
domain_of:
- Lisensdokument
- Aktoer
- RegulativRessurs
- Datasett
range: Konsept

```
</details>