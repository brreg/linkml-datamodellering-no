

# Slot: fastlonn 


_Fastlønn for arbeidsforholdet._





URI: [adm:fastlonn](https://schema.fintlabs.no/administrasjon/fastlonn)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  yes  |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Fastlonn](fastlonn.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md), [Arbeidsforhold](arbeidsforhold.md) |
| Slot URI | [adm:fastlonn](https://schema.fintlabs.no/administrasjon/fastlonn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:fastlonn |
| native | https://schema.fintlabs.no/administrasjon/:fastlonn |




## LinkML Source

<details>
```yaml
name: fastlonn
description: Fastlønn for arbeidsforholdet.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:fastlonn
domain_of:
- AdministrasjonContainer
- Arbeidsforhold
range: Fastlonn

```
</details>