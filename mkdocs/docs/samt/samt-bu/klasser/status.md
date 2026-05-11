

# Slot: status 


_Status for ressursen frå eit kontrollert vokabular (adms:status)._





URI: [adms:status](http://www.w3.org/ns/adms#status)
Alias: status

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  yes  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |
| [Katalogpost](katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](konsept.md) |
| Domain Of | [Distribusjon](distribusjon.md), [Datatjeneste](datatjeneste.md), [Katalogpost](katalogpost.md) |
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
alias: status
domain_of:
- Distribusjon
- Datatjeneste
- Katalogpost
range: Konsept

```
</details>