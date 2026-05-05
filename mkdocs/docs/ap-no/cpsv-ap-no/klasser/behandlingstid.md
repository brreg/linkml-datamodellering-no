

# Slot: behandlingstid 


_Forventa behandlingstid for tenesta eller kanalen (ISO 8601)._





URI: [cv:processingTime](http://data.europa.eu/m8g/processingTime)
Alias: behandlingstid

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tjenestekanal](tjenestekanal.md) | Ein kanal for å få tilgang til ei teneste (t |  yes  |
| [OffentligTjeneste](offentligtjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |
| [Tjeneste](tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Duration](duration.md) |
| Domain Of | [OffentligTjeneste](offentligtjeneste.md), [Tjeneste](tjeneste.md), [Tjenestekanal](tjenestekanal.md) |
| Slot URI | [cv:processingTime](http://data.europa.eu/m8g/processingTime) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/cpsv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cv:processingTime |
| native | https://data.norge.no/linkml/cpsv-ap-no/behandlingstid |




## LinkML Source

<details>
```yaml
name: behandlingstid
description: Forventa behandlingstid for tenesta eller kanalen (ISO 8601).
from_schema: https://data.norge.no/linkml/cpsv-ap-no
rank: 1000
slot_uri: cv:processingTime
alias: behandlingstid
domain_of:
- OffentligTjeneste
- Tjeneste
- Tjenestekanal
range: Duration

```
</details>