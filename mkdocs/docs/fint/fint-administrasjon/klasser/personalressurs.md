

# Slot: personalressurs 


_Personalressurs til arbeidsforholdet._





URI: [adm:personalressurs](https://schema.fintlabs.no/administrasjon/personalressurs)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  yes  |
| [Person](person.md) | Fysiske private personar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personalressurs](personalressurs.md) |
| Domain Of | [Person](person.md), [Arbeidsforhold](arbeidsforhold.md) |
| Slot URI | [adm:personalressurs](https://schema.fintlabs.no/administrasjon/personalressurs) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:personalressurs |
| native | https://schema.fintlabs.no/administrasjon/:personalressurs |




## LinkML Source

<details>
```yaml
name: personalressurs
description: Personalressurs til arbeidsforholdet.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:personalressurs
domain_of:
- Person
- Arbeidsforhold
range: Personalressurs

```
</details>