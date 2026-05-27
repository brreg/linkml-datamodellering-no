

# Slot: fravaer 


_Fråvær knytt til ressursen._





URI: [adm:fravaer](https://schema.fintlabs.no/administrasjon/fravaer)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  yes  |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fravaer](fravaer.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md), [Arbeidsforhold](arbeidsforhold.md) |
| Slot URI | [adm:fravaer](https://schema.fintlabs.no/administrasjon/fravaer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:fravaer |
| native | https://schema.fintlabs.no/administrasjon/:fravaer |




## LinkML Source

<details>
```yaml
name: fravaer
description: Fråvær knytt til ressursen.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:fravaer
domain_of:
- AdministrasjonContainer
- Arbeidsforhold
range: Fravaer

```
</details>