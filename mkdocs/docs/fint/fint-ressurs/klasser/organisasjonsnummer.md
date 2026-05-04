

# Slot: organisasjonsnummer 


_Niisifra nummer som eintydleg identifiserer einingar i Einingsregisteret._





URI: [fint:organisasjonsnummer](https://schema.fintlabs.no/organisasjonsnummer)
Alias: organisasjonsnummer

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
| Range | [Identifikator](Identifikator.md) |
| Domain Of | [Enhet](Enhet.md) |
| Slot URI | [fint:organisasjonsnummer](https://schema.fintlabs.no/organisasjonsnummer) |

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
| self | fint:organisasjonsnummer |
| native | https://schema.fintlabs.no/ressurs/:organisasjonsnummer |




## LinkML Source

<details>
```yaml
name: organisasjonsnummer
description: Niisifra nummer som eintydleg identifiserer einingar i Einingsregisteret.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: fint:organisasjonsnummer
alias: organisasjonsnummer
owner: Enhet
domain_of:
- Enhet
range: Identifikator
inlined: true

```
</details>