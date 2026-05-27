

# Slot: arbeidsforholdsperiode 


_Periode for ei gjeven stilling._





URI: [adm:arbeidsforholdsperiode](https://schema.fintlabs.no/administrasjon/arbeidsforholdsperiode)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Periode](periode.md) |
| Domain Of | [Arbeidsforhold](arbeidsforhold.md) |
| Slot URI | [adm:arbeidsforholdsperiode](https://schema.fintlabs.no/administrasjon/arbeidsforholdsperiode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:arbeidsforholdsperiode |
| native | https://schema.fintlabs.no/administrasjon/:arbeidsforholdsperiode |




## LinkML Source

<details>
```yaml
name: arbeidsforholdsperiode
description: Periode for ei gjeven stilling.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:arbeidsforholdsperiode
domain_of:
- Arbeidsforhold
range: Periode
inlined: true

```
</details>