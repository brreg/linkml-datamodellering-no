

# Slot: er_del_av 


_Tenesta er del av ei anna teneste._





URI: [dct:isPartOf](http://purl.org/dc/terms/isPartOf)
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
| Slot URI | [dct:isPartOf](http://purl.org/dc/terms/isPartOf) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:isPartOf |
| native | https://data.norge.no/linkml/cpsv-ap-no/er_del_av |




## LinkML Source

<details>
```yaml
name: er_del_av
description: Tenesta er del av ei anna teneste.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: dct:isPartOf
domain_of:
- OffentligTjeneste
- Tjeneste
range: uriorcurie

```
</details>