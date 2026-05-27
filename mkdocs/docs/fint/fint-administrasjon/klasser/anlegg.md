

# Slot: anlegg 


_Objekt som skal aktiverast eller avskrivast._





URI: [adm:anlegg](https://schema.fintlabs.no/administrasjon/anlegg)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontostreng](kontostreng.md) | Sammensetning av kontodimensjonar for bokføring |  yes  |
| [Fullmakt](fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |  yes  |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  yes  |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Anlegg](anlegg.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md), [Kontostreng](kontostreng.md), [Fullmakt](fullmakt.md), [Arbeidsforhold](arbeidsforhold.md) |
| Slot URI | [adm:anlegg](https://schema.fintlabs.no/administrasjon/anlegg) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/fint/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:anlegg |
| native | https://schema.fintlabs.no/administrasjon/:anlegg |




## LinkML Source

<details>
```yaml
name: anlegg
description: Objekt som skal aktiverast eller avskrivast.
from_schema: https://data.norge.no/fint/fint-administrasjon
rank: 1000
slot_uri: adm:anlegg
domain_of:
- AdministrasjonContainer
- Kontostreng
- Fullmakt
- Arbeidsforhold
range: Anlegg

```
</details>