

# Slot: tilgangstjeneste 


_Datatjeneste som gjev tilgang til distribusjonen._





URI: [dcat:accessService](http://www.w3.org/ns/dcat#accessService)
Alias: tilgangstjeneste

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datatjeneste](datatjeneste.md) |
| Domain Of | [Distribusjon](distribusjon.md) |
| Slot URI | [dcat:accessService](http://www.w3.org/ns/dcat#accessService) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:accessService |
| native | samtbuskole:tilgangstjeneste |




## LinkML Source

<details>
```yaml
name: tilgangstjeneste
description: Datatjeneste som gjev tilgang til distribusjonen.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dcat:accessService
alias: tilgangstjeneste
domain_of:
- Distribusjon
range: Datatjeneste
multivalued: true

```
</details>