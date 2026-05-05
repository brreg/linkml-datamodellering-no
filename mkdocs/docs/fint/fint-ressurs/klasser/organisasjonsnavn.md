

# Slot: organisasjonsnavn 


_Namn på eining registrert i Einingsregisteret._





URI: [fint:organisasjonsnavn](https://schema.fintlabs.no/organisasjonsnavn)
Alias: organisasjonsnavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  no  |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Enhet](enhet.md) |
| Slot URI | [fint:organisasjonsnavn](https://schema.fintlabs.no/organisasjonsnavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Enhet](enhet.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:organisasjonsnavn |
| native | https://schema.fintlabs.no/ressurs/:organisasjonsnavn |




## LinkML Source

<details>
```yaml
name: organisasjonsnavn
description: Namn på eining registrert i Einingsregisteret.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: fint:organisasjonsnavn
alias: organisasjonsnavn
owner: Enhet
domain_of:
- Enhet
range: string

```
</details>