

# Slot: fasttillegg 


_Faste tillegg for arbeidsforholdet._





URI: [adm:fasttillegg](https://schema.fintlabs.no/administrasjon/fasttillegg)
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
| Range | [Fasttillegg](fasttillegg.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md), [Arbeidsforhold](arbeidsforhold.md) |
| Slot URI | [adm:fasttillegg](https://schema.fintlabs.no/administrasjon/fasttillegg) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:fasttillegg |
| native | https://schema.fintlabs.no/administrasjon/:fasttillegg |




## LinkML Source

<details>
```yaml
name: fasttillegg
description: Faste tillegg for arbeidsforholdet.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:fasttillegg
domain_of:
- AdministrasjonContainer
- Arbeidsforhold
range: Fasttillegg

```
</details>