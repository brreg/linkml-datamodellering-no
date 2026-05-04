

# Slot: forretningsadresse 


_Besøksadresse til ein organisasjonseining i einingsregisteret._





URI: [fint:forretningsadresse](https://schema.fintlabs.no/forretningsadresse)
Alias: forretningsadresse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Enhet](Enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  no  |
| [Virksomhet](Virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Adresse](Adresse.md) |
| Domain Of | [Enhet](Enhet.md) |
| Slot URI | [fint:forretningsadresse](https://schema.fintlabs.no/forretningsadresse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Enhet](Enhet.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:forretningsadresse |
| native | https://schema.fintlabs.no/ressurs/:forretningsadresse |




## LinkML Source

<details>
```yaml
name: forretningsadresse
description: Besøksadresse til ein organisasjonseining i einingsregisteret.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: fint:forretningsadresse
alias: forretningsadresse
owner: Enhet
domain_of:
- Enhet
range: Adresse
inlined: true

```
</details>