

# Slot: funksjon 


_Det som vert produsert eller tenesta som vert levert._





URI: [adm:funksjon](https://schema.fintlabs.no/administrasjon/funksjon)
Alias: funksjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fullmakt](fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |  yes  |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  yes  |
| [Kontostreng](kontostreng.md) | Sammensetning av kontodimensjonar for bokføring |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Funksjon](funksjon.md) |
| Domain Of | [Kontostreng](kontostreng.md), [Fullmakt](fullmakt.md), [Arbeidsforhold](arbeidsforhold.md) |
| Slot URI | [adm:funksjon](https://schema.fintlabs.no/administrasjon/funksjon) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:funksjon |
| native | https://schema.fintlabs.no/administrasjon/:funksjon |




## LinkML Source

<details>
```yaml
name: funksjon
description: Det som vert produsert eller tenesta som vert levert.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:funksjon
alias: funksjon
domain_of:
- Kontostreng
- Fullmakt
- Arbeidsforhold
range: Funksjon

```
</details>