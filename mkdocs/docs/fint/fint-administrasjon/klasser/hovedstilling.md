

# Slot: hovedstilling 


_Angir kva arbeidsforhold som er hovudarbeidsforhold._





URI: [adm:hovedstilling](https://schema.fintlabs.no/administrasjon/hovedstilling)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) |
| Domain Of | [Arbeidsforhold](arbeidsforhold.md) |
| Slot URI | [adm:hovedstilling](https://schema.fintlabs.no/administrasjon/hovedstilling) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:hovedstilling |
| native | https://schema.fintlabs.no/administrasjon/:hovedstilling |




## LinkML Source

<details>
```yaml
name: hovedstilling
description: Angir kva arbeidsforhold som er hovudarbeidsforhold.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:hovedstilling
domain_of:
- Arbeidsforhold
range: boolean

```
</details>