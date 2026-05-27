

# Slot: har_del 


_Deltenester som inngår i denne tenesta._





URI: [dct:hasPart](http://purl.org/dc/terms/hasPart)
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
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [OffentligTjeneste](offentligtjeneste.md), [Tjeneste](tjeneste.md) |
| Slot URI | [dct:hasPart](http://purl.org/dc/terms/hasPart) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/ap-no/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:hasPart |
| native | https://data.norge.no/ap-no/cpsv-ap-no/har_del |




## LinkML Source

<details>
```yaml
name: har_del
description: Deltenester som inngår i denne tenesta.
from_schema: https://data.norge.no/ap-no/cpsv-ap-no
rank: 1000
slot_uri: dct:hasPart
domain_of:
- OffentligTjeneste
- Tjeneste
range: uriorcurie
multivalued: true

```
</details>