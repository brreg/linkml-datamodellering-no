

# Slot: forretningsadresse 


_Besøksadresse til ein organisasjonseining._





URI: [fint:forretningsadresse](https://schema.fintlabs.no/forretningsadresse)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  yes  |
| [Arbeidslokasjon](arbeidslokasjon.md) | Fysisk lokasjon der ein tilsett har sitt arbeidsstad |  yes  |
| [Organisasjonselement](organisasjonselement.md) | Eit element i organisasjonsstrukturen |  yes  |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Adresse](adresse.md) |
| Domain Of | [Enhet](enhet.md), [Arbeidslokasjon](arbeidslokasjon.md), [Organisasjonselement](organisasjonselement.md) |
| Slot URI | [fint:forretningsadresse](https://schema.fintlabs.no/forretningsadresse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




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
from_schema: https://data.norge.no/fint/fint-common
slot_uri: fint:forretningsadresse
domain_of:
- Enhet
- Arbeidslokasjon
- Organisasjonselement
range: Adresse
inlined: true

```
</details>