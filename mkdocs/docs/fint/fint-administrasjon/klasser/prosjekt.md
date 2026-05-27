

# Slot: prosjekt 


_Prosjekt ressursen er knytt til._





URI: [adm:prosjekt](https://schema.fintlabs.no/administrasjon/prosjekt)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontostreng](kontostreng.md) | Sammensetning av kontodimensjonar for bokføring |  yes  |
| [Prosjektart](prosjektart.md) | Element i ei prosjektnedbrytningsstruktur eller arbeidsnedbrytningsstruktur |  yes  |
| [Fullmakt](fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |  yes  |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  yes  |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Prosjekt](prosjekt.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md), [Kontostreng](kontostreng.md), [Prosjektart](prosjektart.md), [Fullmakt](fullmakt.md), [Arbeidsforhold](arbeidsforhold.md) |
| Slot URI | [adm:prosjekt](https://schema.fintlabs.no/administrasjon/prosjekt) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:prosjekt |
| native | https://schema.fintlabs.no/administrasjon/:prosjekt |




## LinkML Source

<details>
```yaml
name: prosjekt
description: Prosjekt ressursen er knytt til.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:prosjekt
domain_of:
- AdministrasjonContainer
- Kontostreng
- Prosjektart
- Fullmakt
- Arbeidsforhold
range: Prosjekt

```
</details>