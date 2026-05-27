

# Slot: aktivitet 


_Detaljering av funksjon._





URI: [adm:aktivitet](https://schema.fintlabs.no/administrasjon/aktivitet)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontostreng](kontostreng.md) | Sammensetning av kontodimensjonar for bokføring |  yes  |
| [Fullmakt](fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |  yes  |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Aktivitet](aktivitet.md) |
| Domain Of | [Kontostreng](kontostreng.md), [Fullmakt](fullmakt.md), [Arbeidsforhold](arbeidsforhold.md) |
| Slot URI | [adm:aktivitet](https://schema.fintlabs.no/administrasjon/aktivitet) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:aktivitet |
| native | https://schema.fintlabs.no/administrasjon/:aktivitet |




## LinkML Source

<details>
```yaml
name: aktivitet
description: Detaljering av funksjon.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:aktivitet
domain_of:
- Kontostreng
- Fullmakt
- Arbeidsforhold
range: Aktivitet

```
</details>