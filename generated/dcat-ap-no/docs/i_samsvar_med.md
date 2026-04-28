

# Slot: i_samsvar_med 


_Standard ressursen er i samsvar med._





URI: [dct:conformsTo](http://purl.org/dc/terms/conformsTo)
Alias: i_samsvar_med

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](Datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  yes  |
| [Katalogpost](Katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen |  yes  |
| [Datasett](Datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |
| [Distribusjon](Distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Standard](Standard.md) |
| Domain Of | [Distribusjon](Distribusjon.md), [Datasett](Datasett.md), [Datatjeneste](Datatjeneste.md), [Katalogpost](Katalogpost.md) |
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