

# Slot: stillingstittel 


_Arbeidstakarens stillingstittel i gjeldande stilling._





URI: [adm:stillingstittel](https://schema.fintlabs.no/administrasjon/stillingstittel)
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
| Slot URI | [adm:stillingstittel](https://schema.fintlabs.no/administrasjon/stillingstittel) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:stillingstittel |
| native | https://schema.fintlabs.no/administrasjon/:stillingstittel |




## LinkML Source

<details>
```yaml
name: stillingstittel
description: Arbeidstakarens stillingstittel i gjeldande stilling.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:stillingstittel
domain_of:
- Arbeidsforhold
range: string

```
</details>