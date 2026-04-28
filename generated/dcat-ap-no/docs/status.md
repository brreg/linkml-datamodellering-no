

# Slot: status 


_Status for ressursen frå eit kontrollert vokabular._





URI: [adms:status](http://www.w3.org/ns/adms#status)
Alias: status

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](Datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |
| [Katalogpost](Katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen |  yes  |
| [Distribusjon](Distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Begrep](Begrep.md) |
| Domain Of | [Distribusjon](Distribusjon.md), [Datatjeneste](Datatjeneste.md), [Katalogpost](Katalogpost.md) |
| Slot URI | [adms:status](http://www.w3.org/ns/adms#status) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adms:status |
| native | https://data.norge.no/linkml/dcat-ap-no/status |




## LinkML Source

<details>
```yaml
name: status
description: Status for ressursen frå eit kontrollert vokabular.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: adms:status
alias: status
domain_of:
- Distribusjon
- Datatjeneste
- Katalogpost
range: Begrep

```
</details>