

# Slot: status 


_Status for ressursen frå eit kontrollert vokabular (adms:status)._





URI: [adms:status](http://www.w3.org/ns/adms#status)
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
| Range | [Konsept](konsept.md) |
| Domain Of | [OffentligTjeneste](offentligtjeneste.md), [Tjeneste](tjeneste.md) |
| Slot URI | [adms:status](http://www.w3.org/ns/adms#status) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adms:status |
| native | https://data.norge.no/linkml/common-ap-no/status |




## LinkML Source

<details>
```yaml
name: status
description: Status for ressursen frå eit kontrollert vokabular (adms:status).
from_schema: https://data.norge.no/linkml/common-ap-no
slot_uri: adms:status
domain_of:
- OffentligTjeneste
- Tjeneste
range: Konsept

```
</details>