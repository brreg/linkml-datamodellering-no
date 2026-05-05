

# Slot: postadresse 


_Informasjon om postadresse til ein aktør._





URI: [fint:postadresse](https://schema.fintlabs.no/postadresse)
Alias: postadresse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  no  |
| [Aktoer](aktoer.md) | Abstrakt base for person eller eining vi samhandlar med |  no  |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Person](person.md) | Fysiske private personar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Adresse](adresse.md) |
| Domain Of | [Aktoer](aktoer.md) |
| Slot URI | [fint:postadresse](https://schema.fintlabs.no/postadresse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Aktoer](aktoer.md) |








## In Subsets


* [Valgfri](valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:postadresse |
| native | https://schema.fintlabs.no/okonomi/:postadresse |




## LinkML Source

<details>
```yaml
name: postadresse
description: Informasjon om postadresse til ein aktør.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: fint:postadresse
alias: postadresse
owner: Aktoer
domain_of:
- Aktoer
range: Adresse
inlined: true

```
</details>