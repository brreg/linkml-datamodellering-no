

# Slot: postadresse 


_Informasjon om postadresse til ein aktør._





URI: [fint:postadresse](https://schema.fintlabs.no/postadresse)
Alias: postadresse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Enhet](Enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  no  |
| [Aktoer](Aktoer.md) | Abstrakt base for person eller eining vi samhandlar med |  no  |
| [Virksomhet](Virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Person](Person.md) | Fysiske private personar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Adresse](Adresse.md) |
| Domain Of | [Aktoer](Aktoer.md) |
| Slot URI | [fint:postadresse](https://schema.fintlabs.no/postadresse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Aktoer](Aktoer.md) |








## In Subsets


* [Valgfri](Valgfri.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:postadresse |
| native | https://schema.fintlabs.no/ressurs/:postadresse |




## LinkML Source

<details>
```yaml
name: postadresse
description: Informasjon om postadresse til ein aktør.
in_subset:
- Valgfri
from_schema: https://data.norge.no/linkml/fint-ressurs
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