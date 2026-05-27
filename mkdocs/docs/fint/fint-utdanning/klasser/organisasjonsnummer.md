

# Slot: organisasjonsnummer 


_Niisifra nummer som eintydleg identifiserer einingar i Einingsregisteret._





URI: [fint:organisasjonsnummer](https://schema.fintlabs.no/organisasjonsnummer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  yes  |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  yes  |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Enhet](enhet.md), [Skole](skole.md) |
| Slot URI | [fint:organisasjonsnummer](https://schema.fintlabs.no/organisasjonsnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:organisasjonsnummer |
| native | https://schema.fintlabs.no/:organisasjonsnummer |




## LinkML Source

<details>
```yaml
name: organisasjonsnummer
description: Niisifra nummer som eintydleg identifiserer einingar i Einingsregisteret.
from_schema: https://data.norge.no/fint/fint-common
slot_uri: fint:organisasjonsnummer
domain_of:
- Enhet
- Skole
range: Identifikator
inlined: true

```
</details>