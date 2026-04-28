

# Slot: tilgangstjeneste 


_Datatjeneste som gjev tilgang til distribusjonen._





URI: [dcat:accessService](http://www.w3.org/ns/dcat#accessService)
Alias: tilgangstjeneste

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Distribusjon](Distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datatjeneste](Datatjeneste.md) |
| Domain Of | [Distribusjon](Distribusjon.md) |
| Slot URI | [dcat:accessService](http://www.w3.org/ns/dcat#accessService) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:accessService |
| native | https://data.norge.no/linkml/dcat-ap-no/tilgangstjeneste |




## LinkML Source

<details>
```yaml
name: tilgangstjeneste
description: Datatjeneste som gjev tilgang til distribusjonen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dcat:accessService
alias: tilgangstjeneste
domain_of:
- Distribusjon
range: Datatjeneste
multivalued: true

```
</details>