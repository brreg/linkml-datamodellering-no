

# Slot: i_samsvar_med 


_Standard ressursen er i samsvar med._





URI: [dct:conformsTo](http://purl.org/dc/terms/conformsTo)
Alias: i_samsvar_med

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  yes  |
| [Katalogpost](katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Standard](standard.md) |
| Domain Of | [Distribusjon](distribusjon.md), [Datasett](datasett.md), [Datatjeneste](datatjeneste.md), [Katalogpost](katalogpost.md) |
| Slot URI | [dct:conformsTo](http://purl.org/dc/terms/conformsTo) |

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
| self | dct:conformsTo |
| native | samtbuskole:i_samsvar_med |




## LinkML Source

<details>
```yaml
name: i_samsvar_med
description: Standard ressursen er i samsvar med.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dct:conformsTo
alias: i_samsvar_med
domain_of:
- Distribusjon
- Datasett
- Datatjeneste
- Katalogpost
range: Standard
multivalued: true

```
</details>