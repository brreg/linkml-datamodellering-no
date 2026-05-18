

# Slot: forretningsadresse 


_Besøksadresse til ein organisasjonseining._





URI: [fint:forretningsadresse](https://schema.fintlabs.no/forretningsadresse)
Alias: forretningsadresse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  yes  |
| [Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  yes  |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Adresse](adresse.md) |
| Domain Of | [Enhet](enhet.md), [Skole](skole.md) |
| Slot URI | [fint:forretningsadresse](https://schema.fintlabs.no/forretningsadresse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:forretningsadresse |
| native | https://schema.fintlabs.no/:forretningsadresse |




## LinkML Source

<details>
```yaml
name: forretningsadresse
description: Besøksadresse til ein organisasjonseining.
from_schema: https://data.norge.no/linkml/fint-common
slot_uri: fint:forretningsadresse
alias: forretningsadresse
domain_of:
- Enhet
- Skole
range: Adresse
inlined: true

```
</details>