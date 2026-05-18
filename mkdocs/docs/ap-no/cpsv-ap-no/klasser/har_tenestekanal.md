

# Slot: har_tenestekanal 


_Kanal for tilgang til tenesta._





URI: [cv:hasChannel](http://data.europa.eu/m8g/hasChannel)
Alias: har_tenestekanal

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
| Range | [Tjenestekanal](tjenestekanal.md) |
| Domain Of | [OffentligTjeneste](offentligtjeneste.md), [Tjeneste](tjeneste.md) |
| Slot URI | [cv:hasChannel](http://data.europa.eu/m8g/hasChannel) |

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
| self | cv:hasChannel |
| native | https://data.norge.no/linkml/cpsv-ap-no/har_tenestekanal |




## LinkML Source

<details>
```yaml
name: har_tenestekanal
description: Kanal for tilgang til tenesta.
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: cv:hasChannel
alias: har_tenestekanal
domain_of:
- OffentligTjeneste
- Tjeneste
range: Tjenestekanal
multivalued: true

```
</details>