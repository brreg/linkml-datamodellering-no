

# Slot: variabellonn 


_Variabel lønn for arbeidsforholdet._





URI: [adm:variabellonn](https://schema.fintlabs.no/administrasjon/variabellonn)
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
| Range | [Variabellonn](variabellonn.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md), [Arbeidsforhold](arbeidsforhold.md) |
| Slot URI | [adm:variabellonn](https://schema.fintlabs.no/administrasjon/variabellonn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:variabellonn |
| native | https://schema.fintlabs.no/administrasjon/:variabellonn |




## LinkML Source

<details>
```yaml
name: variabellonn
description: Variabel lønn for arbeidsforholdet.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:variabellonn
domain_of:
- AdministrasjonContainer
- Arbeidsforhold
range: Variabellonn

```
</details>