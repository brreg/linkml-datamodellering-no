

# Slot: arbeidslokasjon 


_Fysisk lokasjon der den tilsette har sitt arbeidsstad._





URI: [adm:arbeidslokasjon](https://schema.fintlabs.no/administrasjon/arbeidslokasjon)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Arbeidslokasjon](arbeidslokasjon.md) |
| Domain Of | [Arbeidsforhold](arbeidsforhold.md) |
| Slot URI | [adm:arbeidslokasjon](https://schema.fintlabs.no/administrasjon/arbeidslokasjon) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:arbeidslokasjon |
| native | https://schema.fintlabs.no/administrasjon/:arbeidslokasjon |




## LinkML Source

<details>
```yaml
name: arbeidslokasjon
description: Fysisk lokasjon der den tilsette har sitt arbeidsstad.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:arbeidslokasjon
domain_of:
- Arbeidsforhold
range: Arbeidslokasjon

```
</details>