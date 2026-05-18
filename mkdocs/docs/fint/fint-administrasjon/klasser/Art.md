

# Slot: art 


_Type inntekt eller utgift._





URI: [adm:art](https://schema.fintlabs.no/administrasjon/art)
Alias: art

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fullmakt](fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |  yes  |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  yes  |
| [Lonsart](lonsart.md) | Type ytelse |  yes  |
| [Kontostreng](kontostreng.md) | Sammensetning av kontodimensjonar for bokføring |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Art](art.md) |
| Domain Of | [Kontostreng](kontostreng.md), [Lonsart](lonsart.md), [Fullmakt](fullmakt.md), [Arbeidsforhold](arbeidsforhold.md) |
| Slot URI | [adm:art](https://schema.fintlabs.no/administrasjon/art) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:art |
| native | https://schema.fintlabs.no/administrasjon/:art |




## LinkML Source

<details>
```yaml
name: art
description: Type inntekt eller utgift.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:art
alias: art
domain_of:
- Kontostreng
- Lonsart
- Fullmakt
- Arbeidsforhold
range: Art

```
</details>