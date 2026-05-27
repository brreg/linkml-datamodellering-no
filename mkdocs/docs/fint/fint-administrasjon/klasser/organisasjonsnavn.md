

# Slot: organisasjonsnavn 


_Namn på eining registrert i Einingsregisteret._





URI: [fint:organisasjonsnavn](https://schema.fintlabs.no/organisasjonsnavn)
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
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Enhet](enhet.md), [Arbeidslokasjon](arbeidslokasjon.md), [Organisasjonselement](organisasjonselement.md) |
| Slot URI | [fint:organisasjonsnavn](https://schema.fintlabs.no/organisasjonsnavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:organisasjonsnavn |
| native | https://schema.fintlabs.no/:organisasjonsnavn |




## LinkML Source

<details>
```yaml
name: organisasjonsnavn
description: Namn på eining registrert i Einingsregisteret.
from_schema: https://data.norge.no/fint/fint-common
slot_uri: fint:organisasjonsnavn
domain_of:
- Enhet
- Arbeidslokasjon
- Organisasjonselement
range: string

```
</details>