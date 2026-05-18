

# Slot: organisasjonsnavn 


_Namn på eining registrert i Einingsregisteret._





URI: [fint:organisasjonsnavn](https://schema.fintlabs.no/organisasjonsnavn)
Alias: organisasjonsnavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  yes  |
| [SoeknadDrosjeloeyve](soeknaddrosjeloeyve.md) | Sak om søknad om løyve til å køyre drosje |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Enhet](enhet.md), [SoeknadDrosjeloeyve](soeknaddrosjeloeyve.md) |
| Slot URI | [fint:organisasjonsnavn](https://schema.fintlabs.no/organisasjonsnavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-common




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
from_schema: https://data.norge.no/linkml/fint-common
slot_uri: fint:organisasjonsnavn
alias: organisasjonsnavn
domain_of:
- Enhet
- SoeknadDrosjeloeyve
range: string

```
</details>