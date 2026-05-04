

# Slot: har_regulativ_ressurs 


_Regulativ ressurs (lov, forskrift) knytt til tenesta._





URI: [cv:hasLegalResource](http://data.europa.eu/m8g/hasLegalResource)
Alias: har_regulativ_ressurs

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LovpalagtTjeneste](LovpalagtTjeneste.md) | Ei lovpålagd teneste som offentlege organ er pålagde å utføre |  yes  |
| [OffentligTjeneste](OffentligTjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |
| [Tjeneste](Tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RegulativRessurs](RegulativRessurs.md) |
| Domain Of | [LovpalagtTjeneste](LovpalagtTjeneste.md), [OffentligTjeneste](OffentligTjeneste.md), [Tjeneste](Tjeneste.md) |
| Slot URI | [cv:hasLegalResource](http://data.europa.eu/m8g/hasLegalResource) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cv:hasLegalResource |
| native | https://data.norge.no/linkml/cpsv-ap-no/har_regulativ_ressurs |




## LinkML Source

<details>
```yaml
name: har_regulativ_ressurs
description: Regulativ ressurs (lov, forskrift) knytt til tenesta.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: cv:hasLegalResource
alias: har_regulativ_ressurs
domain_of:
- LovpalagtTjeneste
- OffentligTjeneste
- Tjeneste
range: RegulativRessurs
multivalued: true

```
</details>