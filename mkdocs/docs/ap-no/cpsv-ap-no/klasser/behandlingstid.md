

# Slot: behandlingstid 


_Forventa behandlingstid for tenesta eller kanalen (ISO 8601)._





URI: [cv:processingTime](http://data.europa.eu/m8g/processingTime)
Alias: behandlingstid

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tjenestekanal](Tjenestekanal.md) | Ein kanal for å få tilgang til ei teneste (t |  yes  |
| [OffentligTjeneste](OffentligTjeneste.md) | Ei konkret offentleg teneste levert av ein offentleg organisasjon |  yes  |
| [Tjeneste](Tjeneste.md) | Ei teneste levert av ein ikkje-offentleg aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Duration](Duration.md) |
| Domain Of | [OffentligTjeneste](OffentligTjeneste.md), [Tjeneste](Tjeneste.md), [Tjenestekanal](Tjenestekanal.md) |
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