

# Slot: kontrakt 


_Kontrakt ressursen er knytt til._





URI: [adm:kontrakt](https://schema.fintlabs.no/administrasjon/kontrakt)
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
| Range | [Kontrakt](kontrakt.md) |
| Domain Of | [Kontostreng](kontostreng.md), [Fullmakt](fullmakt.md), [Arbeidsforhold](arbeidsforhold.md) |
| Slot URI | [adm:kontrakt](https://schema.fintlabs.no/administrasjon/kontrakt) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:kontrakt |
| native | https://schema.fintlabs.no/administrasjon/:kontrakt |




## LinkML Source

<details>
```yaml
name: kontrakt
description: Kontrakt ressursen er knytt til.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:kontrakt
domain_of:
- Kontostreng
- Fullmakt
- Arbeidsforhold
range: Kontrakt

```
</details>