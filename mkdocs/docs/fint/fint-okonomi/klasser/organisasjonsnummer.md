

# Slot: organisasjonsnummer 


_Niisifra nummer som eintydleg identifiserer einingar i Einingsregisteret._





URI: [fint:organisasjonsnummer](https://schema.fintlabs.no/organisasjonsnummer)
Alias: organisasjonsnummer

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
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Enhet](enhet.md) |
| Slot URI | [fint:organisasjonsnummer](https://schema.fintlabs.no/organisasjonsnummer) |

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


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:organisasjonsnummer |
| native | https://schema.fintlabs.no/okonomi/:organisasjonsnummer |




## LinkML Source

<details>
```yaml
name: organisasjonsnummer
description: Niisifra nummer som eintydleg identifiserer einingar i Einingsregisteret.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
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