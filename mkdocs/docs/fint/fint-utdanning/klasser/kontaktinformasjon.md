

# Slot: kontaktinformasjon 


_Den føretrekte måten å kome i kontakt med ein aktør._





URI: [fint:kontaktinformasjon](https://schema.fintlabs.no/kontaktinformasjon)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Aktoer](aktoer.md) | Abstrakt base for person eller eining vi samhandlar med |  yes  |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  yes  |
| [Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  no  |
| [Person](person.md) | Fysiske private personar |  no  |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kontaktinformasjon](kontaktinformasjon.md) |
| Domain Of | [Aktoer](aktoer.md), [Kontaktperson](kontaktperson.md) |
| Slot URI | [fint:kontaktinformasjon](https://schema.fintlabs.no/kontaktinformasjon) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:kontaktinformasjon |
| native | https://schema.fintlabs.no/:kontaktinformasjon |




## LinkML Source

<details>
```yaml
name: kontaktinformasjon
description: Den føretrekte måten å kome i kontakt med ein aktør.
from_schema: https://data.norge.no/fint/fint-common
slot_uri: fint:kontaktinformasjon
domain_of:
- Aktoer
- Kontaktperson
range: Kontaktinformasjon
inlined: true

```
</details>