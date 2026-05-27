

# Slot: stillingsnummer 


_Løpenummer for stillinga._





URI: [adm:stillingsnummer](https://schema.fintlabs.no/administrasjon/stillingsnummer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Arbeidsforhold](arbeidsforhold.md) |
| Slot URI | [adm:stillingsnummer](https://schema.fintlabs.no/administrasjon/stillingsnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:stillingsnummer |
| native | https://schema.fintlabs.no/administrasjon/:stillingsnummer |




## LinkML Source

<details>
```yaml
name: stillingsnummer
description: Løpenummer for stillinga.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:stillingsnummer
domain_of:
- Arbeidsforhold
range: string

```
</details>