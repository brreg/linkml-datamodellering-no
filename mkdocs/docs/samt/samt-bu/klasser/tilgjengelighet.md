

# Slot: tilgjengelighet 


_Planlagt tilgjengelegheit for ressursen._





URI: [dcatap:availability](http://data.europa.eu/r5r/availability)
Alias: tilgjengelighet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  yes  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Distribusjon](distribusjon.md), [Datatjeneste](datatjeneste.md) |
| Slot URI | [dcatap:availability](http://data.europa.eu/r5r/availability) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcatap:availability |
| native | https://data.norge.no/linkml/dcat-ap-no/tilgjengelighet |




## LinkML Source

<details>
```yaml
name: tilgjengelighet
description: Planlagt tilgjengelegheit for ressursen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
slot_uri: dcatap:availability
alias: tilgjengelighet
domain_of:
- Distribusjon
- Datatjeneste
range: string

```
</details>