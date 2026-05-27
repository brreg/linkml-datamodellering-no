

# Slot: ansvar 


_Ansvarleg for ei utgift eller inntekt._





URI: [adm:ansvar](https://schema.fintlabs.no/administrasjon/ansvar)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontostreng](kontostreng.md) | Sammensetning av kontodimensjonar for bokføring |  yes  |
| [Fullmakt](fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |  yes  |
| [Organisasjonselement](organisasjonselement.md) | Eit element i organisasjonsstrukturen |  yes  |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  yes  |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Ansvar](ansvar.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md), [Kontostreng](kontostreng.md), [Fullmakt](fullmakt.md), [Organisasjonselement](organisasjonselement.md), [Arbeidsforhold](arbeidsforhold.md) |
| Slot URI | [adm:ansvar](https://schema.fintlabs.no/administrasjon/ansvar) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:ansvar |
| native | https://schema.fintlabs.no/administrasjon/:ansvar |




## LinkML Source

<details>
```yaml
name: ansvar
description: Ansvarleg for ei utgift eller inntekt.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:ansvar
domain_of:
- AdministrasjonContainer
- Kontostreng
- Fullmakt
- Organisasjonselement
- Arbeidsforhold
range: Ansvar

```
</details>