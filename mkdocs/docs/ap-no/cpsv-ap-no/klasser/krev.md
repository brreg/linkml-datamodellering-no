

# Slot: krev 


_Teneste eller ressurs denne tenesta krev._





URI: [dct:requires](http://purl.org/dc/terms/requires)
Alias: krev

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tjeneste](tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |
| [OffentligTjeneste](offentligtjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [OffentligTjeneste](offentligtjeneste.md), [Tjeneste](tjeneste.md) |
| Slot URI | [dct:requires](http://purl.org/dc/terms/requires) |

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
| self | dct:requires |
| native | https://data.norge.no/linkml/cpsv-ap-no/krev |




## LinkML Source

<details>
```yaml
name: krev
description: Teneste eller ressurs denne tenesta krev.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: dct:requires
alias: krev
domain_of:
- OffentligTjeneste
- Tjeneste
range: uriorcurie
multivalued: true

```
</details>