

# Slot: har_regulativ_ressurs 


_Regulativ ressurs (lov, forskrift) knytt til tenesta._





URI: [cv:hasLegalResource](http://data.europa.eu/m8g/hasLegalResource)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OffentligTjeneste](offentligtjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |
| [Tjeneste](tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RegulativRessurs](regulativressurs.md) |
| Domain Of | [OffentligTjeneste](offentligtjeneste.md), [Tjeneste](tjeneste.md) |
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
domain_of:
- OffentligTjeneste
- Tjeneste
range: RegulativRessurs
multivalued: true

```
</details>