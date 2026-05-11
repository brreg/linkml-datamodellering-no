

# Slot: i_samsvar_med 


_Standard ressursen er i samsvar med._





URI: [dct:conformsTo](http://purl.org/dc/terms/conformsTo)
Alias: i_samsvar_med

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  yes  |
| [Katalogpost](katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen |  yes  |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |






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


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:conformsTo |
| native | https://data.norge.no/linkml/dcat-ap-no/i_samsvar_med |




## LinkML Source

<details>
```yaml
name: i_samsvar_med
description: Standard ressursen er i samsvar med.
from_schema: https://data.norge.no/linkml/dcat-ap-no
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