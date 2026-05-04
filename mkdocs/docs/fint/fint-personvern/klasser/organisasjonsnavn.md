

# Slot: organisasjonsnavn 


_Namn på eining registrert i Einingsregisteret._





URI: [fint:organisasjonsnavn](https://schema.fintlabs.no/organisasjonsnavn)
Alias: organisasjonsnavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Virksomhet](Virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Enhet](Enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Enhet](Enhet.md) |
| Slot URI | [fint:organisasjonsnavn](https://schema.fintlabs.no/organisasjonsnavn) |

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


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:organisasjonsnavn |
| native | https://schema.fintlabs.no/personvern/:organisasjonsnavn |




## LinkML Source

<details>
```yaml
name: organisasjonsnavn
description: Namn på eining registrert i Einingsregisteret.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: fint:organisasjonsnavn
alias: organisasjonsnavn
owner: Enhet
domain_of:
- Enhet
range: string

```
</details>